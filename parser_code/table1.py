


from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, VARCHAR, DATE, TEXT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy import create_engine
# import hashlib
import uuid





#매핑선언
Base = declarative_base()



#patent table
class patent(Base):
    __tablename__ = 'patent'
    lang = Column(VARCHAR(20))
    dtd_version = Column(VARCHAR(20))
    file = Column(VARCHAR(30), primary_key=True)
    status = Column(VARCHAR(20))
    id  =Column(VARCHAR(20))
    country = Column(VARCHAR(20))
    date_produced = Column(VARCHAR(8))
    date_publ = Column(VARCHAR(8))
    def __init__(self, lang, dtd_version, file, status, id, country, date_produced, date_publ):
        self.lang = lang
        self.dtd_version = dtd_version
        self.file = file
        self.status = status
        self.id = id
        self.country = country
        self.date_produced = date_produced
        self.date_publ = date_publ
    def __repr__(self):
        return "<Patent('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.lang, self.dtd_version, self.file, self.status, self.id, self.country, self.date_produced, self.date_publ)

#reference table이다. but it's included publication and application.
class reference(Base):
    __tablename__ = 'reference'
    file = Column(VARCHAR(30), primary_key=True)
    publ_country = Column(VARCHAR(10))
    publ_docnumber = Column(VARCHAR(10))
    publ_kind = Column(VARCHAR(10))
    publ_date = Column(Integer())
    appl_type = Column(VARCHAR(20))
    appl_country = Column(VARCHAR(10))
    appl_docnumber = Column(VARCHAR(10))
    appl_date = Column(Integer())

    def __init__(self, file, publ_country, publ_docnumber, publ_kind, publ_date, appl_type, appl_country, appl_docnumber,appl_date):
        self.file = file
        self.publ_country = publ_country
        self.publ_docnumber = publ_docnumber
        self.publ_kind = publ_kind
        self.publ_date = publ_date
        self.appl_type = appl_type
        self.appl_country = appl_country
        self.appl_docnumber = appl_docnumber
        self.appl_date = appl_date

    def __repr__(self):
        return "<Reference('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
        self.file, self.publ_country, self.publ_docnumber, self.publ_kind,self.publ_date, self.appl_type, self.appl_country, self.appl_docnumber,
        self.appl_date)


class priorityClaim(Base):
    __tablename__ = 'priorityclaim'
    file = Column(VARCHAR(30), primary_key=True)
    sequence = Column(VARCHAR(10))
    kind = Column(VARCHAR(10))
    country = Column(VARCHAR(10))
    doc_number = Column(VARCHAR(10))
    date = Column(VARCHAR(20))

    def __init__(self, file, sequence, kind, country, doc_number, date):
        self.file = file
        self.sequence = sequence
        self.kind = kind
        self.country = country
        self.doc_number = doc_number
        self.date = date

    def __repr__(self):
        return "<PriorityClaim('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.file, self.sequence, self.kind, self.country, self.doc_number, self.date)

class claasification(Base):
    __tablename__ = 'classification'
    file = Column(VARCHAR(30), primary_key=True)
    locarno_edition = Column(VARCHAR(10))
    locarno_main = Column(VARCHAR(10))
    national_country = Column(VARCHAR(10))
    national_main = Column(VARCHAR(10))

    def __init__(self, file, locarno_edition, locarno_main, national_country, national_main):
        self.file = file
        self.locarno_edition = locarno_edition
        self.locarno_main = locarno_main
        self.national_country = national_country
        self.national_main = national_main

    def __repr__(self):
        return "<Classification('%s', '%s', '%s', '%s', '%s')>" % (
            self.file, self.locarno_edition, self.locarno_main, self.national_country, self.national_main)

class citation(Base):
    __tablename__ = 'citation'
    file = Column(VARCHAR(30), primary_key=True)
    pacit_num = Column(VARCHAR(10))
    pacit_country = Column(VARCHAR(10))
    pacit_kind = Column(VARCHAR(10))
    pacit_name = Column(VARCHAR(10))
    pacit_date = Column(VARCHAR(10))
    category = Column(VARCHAR(10))

    def __init__(self, file, pacit_num, pacit_country, pacit_kind, pacit_name,pacit_date,category):
        self.file = file
        self.pacit_num = pacit_num
        self.pacit_country = pacit_country
        self.pacit_kind = pacit_kind
        self.pacit_name = pacit_name
        self.pacit_date = pacit_date
        self.category = category

    def __repr__(self):
        return "<Citation('%s', '%s', '%s', '%s', '%s')>" % (
            self.file, self.pacit_num, self.pacit_country, self.pacit_kind, self.pacit_name,self.pacit_date,self.category)

class classificationNational(Base):
    __tablename__ = 'classificationnational'
    file = Column(VARCHAR(30), primary_key=True)
    country = Column(VARCHAR(10))
    main = Column(VARCHAR(10))

    def __init__(self, file, country, main):
        self.file = file
        self.country = country
        self.main = main

    def __repr__(self):
        return "<classificationNational('%s', '%s', '%s')>" % (
            self.file, self.country, self.main)

#applicant
class applicant(Base):
    __tablename__ = 'applicant'
    file = Column(VARCHAR(30), primary_key=True)
    sequence = Column(INTEGER())
    app_type = Column(VARCHAR(64))
    nationality = Column(VARCHAR(64))
    residence = Column(VARCHAR(64))
    designation = Column(VARCHAR(64))


    def __init__(self, id, sequence, app_type , designation, residence, nationality):
        self.id = id
        self.sequence = sequence
        self.app_type = app_type
        self.designation = designation
        self.residence = residence
        self.nationality = nationality

    def __repr__(self):
        return "<applicant('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.sequence, self.app_type, self.designation, self.residence, self.nationality)

#address
class applAddress(Base):
    __tablename__ = 'appl_address'

    file = Column(VARCHAR(30), primary_key=True)
    street = Column(VARCHAR(256))
    city= Column(VARCHAR(128))
    country = Column(VARCHAR(10))

    def __init__(self, file, street, city, country):
        self.file = file
        self.street = street
        self.city = city
        self.country = country

    def __repr__(self):
        return "<applAddress('%s', '%s', '%s',  '%s')>" % (self.file, self.street, self.city, self.country)

#agent
class agent(Base):
    __tablename__ = 'agent'
    file = Column(VARCHAR(30), primary_key=True)
    sequence = Column(INTEGER())
    rep_type = Column(VARCHAR(64))

    def __init__(self, file, sequence, rep_type):
        self.file = file
        self.sequence = sequence
        self.rep_type = rep_type

    def __repr__(self):
        return "<agent('%s', '%s', '%s')>" % (self.file, self.sequence, self.rep_type)


#address
class agentAddress(Base):
    __tablename__ = 'agent_address'
    file = Column(VARCHAR(30), primary_key=True)
    org_name= Column(VARCHAR(128))
    country = Column(VARCHAR(10))

    def __init__(self, file, org_name, country):
        self.file = file
        self.country = country
        self.org_name = org_name

    def __repr__(self):
        return "<agentAddress('%s', '%s', '%s')>" % (self.file, self.country, self.org_name)


#examiner
class examiner(Base):
    __tablename__ = 'examiner'
    file = Column(VARCHAR(30), primary_key=True)
    primary_last_name = Column(VARCHAR(36))
    primary_first_name = Column(VARCHAR(36))
    primary_department = Column(VARCHAR(36))
    assistant_last_name = Column(VARCHAR(36))
    assistant_first_name = Column(VARCHAR(36))
    assistant_department = Column(VARCHAR(36))

    def __init__(self, file, primary_last_name,  primary_first_name, primary_department, assistant_last_name,assistant_first_name,assistant_department):
        self.file = file
        self.primary_last_name= primary_last_name
        self.primary_first_name= primary_first_name
        self.primary_department = app_type
        self.assistant_last_name = assistant_last_name
        self.assistant_first_name = assistant_first_name
        self.assistant_department = assistant_department

    def __repr__(self):
        return "<examiner('%s', '%s', '%s', '%s','%s', '%s', '%s')>" % (self.file, self.primary_first_name, self.primary_department, self.primary_last_name, self.assistant_department, self.assistant_first_name, self.assistant_last_name)


#lengthofgrant
class lengthOfGrant(Base):
    __tablename__ = 'lengthofgrant'
    file = Column(VARCHAR(30), primary_key=True)
    length = Column(VARCHAR(100))


    def __init__(self, file, length):
        self.file = file
        self.length= length

    def __repr__(self):
        return "<lengthOfGrant('%s', '%s')>" % (self.file, self.length)

#drawing figure
class drawingFigure(Base):
    __tablename__ = 'drawingfigure'
    file = Column(VARCHAR(30), primary_key=True)
    figure_id = Column(VARCHAR(20))
    figure_num = Column(VARCHAR(10))
    img_id = Column(VARCHAR(10))
    img_he = Column(VARCHAR(15))
    img_wi = Column(VARCHAR(10))
    img_file = Column(VARCHAR(100))
    img_content = Column(VARCHAR(40))
    img_alt = Column(VARCHAR(40))

    def __init__(self, figure_id, figure_num,img_id,img_he,img_wi,img_file,img_content,img_alt):
        self.file = file
        self.figure_id = figure_id
        self.figure_num = figure_num
        self.img_id = img_id
        self.img_he = img_he
        self.img_content = img_content
        self.img_wi = img_wi
        self.img_file = img_file
        self.img_alt = img_alt



    def __repr__(self):
        return "<drawingFigure('%s', '%s','%s', '%s','%s', '%s','%s', '%s','%s')>" % (self.file, self.figure_id, self.figure_num, self.img_file, self.img_wi, self.img_content, self.img_he, self.img_alt, self.img_id)


#lengthofgrant
class descriptionOfDrawings(Base):
    __tablename__ = 'description'
    file = Column(VARCHAR(30), primary_key=True)
    id = Column(VARCHAR(256))
    num = Column(VARCHAR(100))


    def __init__(self, file, length):
        self.file = file
        self.id = id
        self.num = num

    def __repr__(self):
        return "<descriptionOfDrawings('%s', '%s', '%s')>" % (self.file, self.id, self.num)

#lengthofgrant
class claims(Base):
    __tablename__ = 'claim'
    file = Column(VARCHAR(30), primary_key=True)
    id = Column(VARCHAR(50))
    num = Column(VARCHAR(10))
    claim_text = Column(VARCHAR(256))

    def __init__(self, file, length):
        self.file = file
        self.length= length

    def __repr__(self):
        return "<claims('%s', '%s')>" % (self.file, self.length)


#lengthofgrant
class usApplicationSeriesCode(Base):
    __tablename__ = 'usapplicationseriescode'
    file = Column(VARCHAR(30), primary_key=True)
    us_application_series_code = Column(VARCHAR(10))

    def __init__(self, file, us_application_series_code):
        self.file = file
        self.us_application_series_code= us_application_series_code


    def __repr__(self):
        return "<usApplicationSeriesCode('%s', '%s')>" % (self.file, self.us_application_series_code)

#lengthofgrant
class inventionTitle(Base):
    __tablename__ = 'inventiontitle'
    file = Column(VARCHAR(30), primary_key=True)
    inventionTitle = Column(VARCHAR(10))
    inventionTitle_id = Column(VARCHAR(10))


    def __init__(self, file, inventionTitle, inventionTitle_id):
        self.file = file
        self.inventionTitle= inventionTitle
        self.inventionTitle_id = inventionTitle_id


    def __repr__(self):
        return "<inventionTitle('%s', '%s', '%s')>" % (self.file, self.inventionTitle, self.inventionTitle_id)


class numberOfClaims(Base):
    __tablename__ = 'numberofclaims'
    file = Column(VARCHAR(30), primary_key=True)
    number_of_claims = Column(VARCHAR(10))

    def __init__(self, file, number_of_claims):
        self.file = file
        self.number_of_claims= number_of_claims


    def __repr__(self):
        return "<numberOfClaims('%s', '%s')>" % (self.file, self.number_of_claims)


class usExemplaryClaims(Base):
    __tablename__ = 'us_exemplary_claims'
    file = Column(VARCHAR(30), primary_key=True)
    us_exemplary_claims =Column(VARCHAR(10))

    def __init__(self, file, us_exemplary_claims):
        self.file = file
        self.us_exemplary_claims= us_exemplary_claims


    def __repr__(self):
        return "usExemplaryClaims<('%s', '%s')>" % (self.file, self.us_exemplary_claims)


Base.metadata.create_all(engine)






class Main():
    def __init__(self):
        pass

    def __del__(self):
        pass
1
    def run(self):
        if not sesion.quert(exists().where(Patent.file  == )).scalar():
            u1 = Patent()









if __name == '__main__' or __name__ == 'Test':


    engine = create_engine('sqlite:///:memory:', echo=True)
    connection = engine.connet()

    Session = sessionmaker(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    Main().run()
    connection.close()


