from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict,Counter,namedtuple
from sklearn import neighbors
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

CORA = namedtuple('CORA', 'words tags')

datasets=[]
word_dataset = []
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
        word_dataset.append(words)
        datasets.append(
            CORA(
                words,
                [ID]
            )
        )

all_words =[' '.join(k) for k in word_dataset]

vectorizer=TfidfVectorizer()
new_model= vectorizer.fit_transform(all_words).toarray()

print(Counter(new_model[100]))
#Counter({0.0: 1397, 0.14732297916530482: 2, 0.20695867199751719: 2, 0.1779974979048525: 1, 0.16893395481183937: 1, 0.14749558278595248: 1, 0.1418262090979738: 1, 0.2006973001515098: 1, 0.20563266260941088: 1, 0.17185203330833002: 1, 0.26564168494282547: 1, 0.16489216378338889: 1, 0.28088183079928947: 1, 0.10442837161347646: 1, 0.25055320288151606: 1, 0.26077501160592897: 1, 0.1790518853366535: 1, 0.18315109004752353: 1, 0.16362381523529063: 1, 0.28468901021420068: 1, 0.21270527365793346: 1, 0.22820204758784843: 1, 0.20629064434843181: 1, 0.15844245098055179: 1})

print('tf-idf matrix shape :', new_model.shape)
#tf-idf matrix shape : (2708, 1422)





Y=[]
for y,key in enumerate(labels.keys()):
    for index,paper in enumerate(labels[key]):
        Y.append(y)
X=[]
for i in range(len(new_model)):
        X.append(new_model[i])
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=0)
for i in range(6):
    k_value= i+1
    knn=neighbors.KNeighborsClassifier(n_neighbors=k_value)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    print( "Accuracy is ", accuracy_score(y_test,y_pred)*100,"% for K-Value:",k_value)




 




