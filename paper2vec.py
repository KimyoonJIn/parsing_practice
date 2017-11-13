
import nltk
import numpy as np
import tensorflow as tf
from tensorflow.python.client import timeline
import networkx as nx
from collections import defaultdict,namedtuple,Counter
from glob import glob
import sys
import os
import math
import random
from six.moves import xrange
if sys.version_info[0] >= 3:
    unicode = str

import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV,train_test_split
from gensim.models.word2vec import Word2Vec
from gensim.models.doc2vec import Doc2Vec


random.seed(0)
np.random.seed(0)

CORA = namedtuple('CORA', 'words tags')

datasets = []
labels = defaultdict(list)
with open("cora_content.txt") as f:
    for line in f:
        line = line.split()
        ID = line[0]
        labels[line[-1]].append(ID)
        words = []
        for i,w in enumerate(line[1:-1]):
            if w == "1":
                words.append(str(i))
        datasets.append(
            CORA(
                words,
                [ID]
            )
        )

logging.info("done... %s papers loaded" % (len(datasets)))
logging.info("%s labels" % (len(labels)))




model = Doc2Vec(alpha=0.025, window=10, min_count=10, min_alpha=0.025, size=100)
model.build_vocab(datasets)

# decrease alpha
for i in range(10):
    random.shuffle(datasets)
    model.alpha = 0.025-0.002*i
    model.min_alpha = model.alpha
    model.train(datasets,total_examples=model.corpus_count,epochs=model.iter)




X = []
Y = []
with open('doc2vec.embd','w') as f:
    f.write("%s %s\n"%(len(datasets),100))
    for y,key in enumerate(labels.keys()):
        for index,paper in enumerate(labels[key]):
            f.write(paper+" "+" ".join([str(x) for x in model.docvecs[paper]])+"\n")
            X.append(model.docvecs[paper])
            Y.append(y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=0)
clf = SVC(kernel='rbf',C=1.5).fit(X_train,y_train)
print(clf.score(X_test, y_test))

# classify with 10-fold
parameters = {
    "kernel":["rbf"],
    "C" :[1.5]
             }
tunedclf = GridSearchCV(clf,parameters,cv=10,n_jobs=24)
tunedclf.fit(X,Y)
print("scores %s" % tunedclf.best_score_)


G = defaultdict(dict)

for data in datasets:
    for n in model.docvecs.most_similar(data.tags,topn=2):
        G[data.tags[0]][n[0]] = None
        G[n[0]][data.tags[0]] = None

with open('cora_cites.txt') as f:
    for line in f:
        line = line.rstrip().split("\t")
        try:
            G[line[0]][line[1]] = None
            G[line[1]][line[0]] = None
        except:
            print(line)

neighbors = []

for i in range(10):
    for node in G:
        path = [node]
        while len(path) < 40:
            cur = path[-1]
            path.append(random.choice(list(G[cur].keys())))
        neighbors.append(path)
print(len(neighbors))





p2v = Word2Vec(size=100, window=5, min_count=0)
p2v.build_vocab(neighbors)
p2v.intersect_word2vec_format('doc2vec.embd',lockf=1.0)
p2v.train(neighbors,total_examples=p2v.corpus_count,epochs=p2v.iter)


# predict


X = []
Y = []
for y,key in enumerate(labels.keys()):
    for index,paper in enumerate(labels[key]):
        X.append(p2v[paper])
        Y.append(y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
clf = SVC(kernel='rbf',C=1.5).fit(X_train,y_train)
print(clf.score(X_test, y_test))
clf = SVC()
parameters = {
    "kernel":["rbf"],
    "C" :[1,10,100]
             }
tunedclf = GridSearchCV(clf,parameters,cv=10,n_jobs=24)
tunedclf.fit(X,Y)
logging.info("scores %s" % tunedclf.best_score_)



G = defaultdict(dict)

for data in datasets:
    for n in model.docvecs.most_similar(data.tags,topn=2):
        G[data.tags[0]][n[0]] = None
        G[n[0]][data.tags[0]] = None

with open('cora_cites.txt') as f:
    for line in f:
        line = line.rstrip().split("\t")
        try:
            G[line[0]][line[1]] = None
            G[line[1]][line[0]] = None
        except:
            print(line)


update_neighbors = []

for node in G:
    for neighbor in node:
        update_neighbors.append([node,neighbor])
print(len(update_neighbors))




update_p2v = Word2Vec(size=100, window=5, min_count=0)
update_p2v.build_vocab(update_neighbors)
update_p2v.intersect_word2vec_format('doc2vec.embd')
update_p2v.train(update_neighbors,total_examples=update_p2v.corpus_count,epochs=update_p2v.iter)


X_M = []
Y_M = []
for y,key in enumerate(labels.keys()):
    for index,paper in enumerate(labels[key]):
        X_M.append(update_p2v[paper])
        Y_M.append(y)

X_train, X_test, y_train, y_test = train_test_split(X_M, Y_M, test_size=0.5, random_state=42)
clf = SVC(kernel='rbf',C=1.5).fit(X_train,y_train)
print(clf.score(X_test, y_test))

clf = SVC()
parameters = {
    "kernel":["rbf"],
    "C" :[1,10,100]
             }
tunedclf = GridSearchCV(clf,parameters,cv=10,n_jobs=24)
tunedclf.fit(X_M,Y_M)
print("scores %s" % tunedclf.best_score_)
