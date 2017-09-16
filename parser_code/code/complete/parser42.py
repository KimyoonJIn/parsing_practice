
# coding: utf-8

# In[ ]:

#2006.08.23~2012.12.04
#20060829(1)ok
#20070130 ok
#20080916 ok
#20120207 error -> it has not a 'agent'
#20121127(end _> it has 'agent' ok.
#agent는 들어갈수도 있고 아닐수도 있는 태그

class parserVer42(Parser):
    def __init__(self,xml):
        super().__init__(xml)
        
        #us-claim-statement(new tag)
        self.ubdg_us_claim_statement = self.doc['us-patent-grant']['us-claim-statement']
        #address_street
        self.ubdg_parties_applicants_applicant_addressbook_address_state = self.doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
        #agents
        self.ubdg_parties_assignees_assignee_address_country=ubdg_parties_assignees_assignee_address_country
        self.ubdg_parties_agents_agent_rep_type=ubdg_parties_agents_agent_rep_type
        self.ubdg_parties_agents_agent_addressbook_orgname=ubdg_parties_agents_agent_addressbook_orgname
        self.ubdg_parties_agents_agent_addressbook_address_country=ubdg_parties_agents_agent_addressbook_address_country
        #description
        self.p = p
        self.p_id = p_id
        self.p_num = p_num
        self.p_text = p_text
        #citation
        self.patcit = patcit
        self.patcit_num = patcit_num
        self.patcit_country = patcit_country
        self.patcit_doc_country = patcit_doc_country
        self.patcit_kind=patcit_kind
        self.patcit_name=patcit_name
        self.patcit_date=patcit_date
        self.nplcit_num=nplcit_num
        self.nplcit_othercit=nplcit_othercit
        self.npl_category=npl_category
        #classification
        self.classification_national=classification_national
        self.classification_country=classification_country
        self.classification_main=classification_main
        #applicant
        self.ubdg_parties_applicants_applicant_sequence =self.ubdg_parties_applicants_applicant_sequence
        self.ubdg_parties_applicants_applicant_app_type=self.ubdg_parties_applicants_applicant_app_type
        self.ubdg_parties_applicants_applicant_designation=self.ubdg_parties_applicants_applicant_designation
        self.ubdg_parties_applicants_applicant_addressbook_last_name=self.ubdg_parties_applicants_applicant_addressbook_last_name
        self.ubdg_parties_applicants_applicant_addressbook_first_name=self.ubdg_parties_applicants_applicant_addressbook_first_name
        self.ubdg_parties_applicants_applicant_addressbook_address_city=self.ubdg_parties_applicants_applicant_addressbook_address_city
        self.ubdg_parties_applicants_applicant_addressbook_address_country=self.ubdg_parties_applicants_applicant_addressbook_address_country
        self.ubdg_parties_applicants_applicant_nationality_country=self.ubdg_parties_applicants_applicant_nationality_country
        self.ubdg_parties_applicants_applicant_residence_country=self.ubdg_parties_applicants_applicant_residence_country
        self.applicant=self.applicant
        self.applicant_sequence=self.applicant_sequence
        self.pplicant_designation=self.applicant_designation
        self.applicant_app_type=self.applicant_app_type
        self.applicant_address_last_name=self.applicant_address_last_name
        self.applicant_address_first_name=self.applicant_address_first_name
        self.applicant_address_city=self.applicant_address_city
        self.applicant_address_state=self.applicant_address_state
        self.applicant_address_country=self.applicant_address_country
        self.applicant_nationality_country=self.applicant_nationality_country
        self.applicant_residence_country=self.applicant_residence_country

        
    def agent(self,xml):
        
        ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
        ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
        ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
        ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']

    def patcit(self,xml):
        patcit=[]
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])):
                patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])[i])
        
        
        patcit_num = []
        patcit_country = []
        patcit_doc_number = []
        patcit_kind = []
        patcit_name = []
        patcit_date = []
        nplcit_num =[]
        nplcit_othercit=[]
        npl_category=[]
        
        for j in patcit:
            patcit_number = j['patcit']['@num']
            patcit_doc_country = j['patcit']['document-id']['country']
            patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
            patcit_doc_kind = j['patcit']['document-id']['kind']
            patcit_doc_name = j['patcit']['document-id']['name']
            patcit_doc_date = j['patcit']['document-id']['date']
            patcit_num.append(patcit_number)
            patcit_country.append(patcit_doc_country)
            patcit_doc_number.append(patcit_doc_docnumber)
            patcit_kind.append(patcit_doc_kind)
            patcit_name.append(patcit_doc_name)
            patcit_date.append(patcit_doc_date)
            nplcit_number = j['nplcit']['@num']
            nplcit_othercitation = j['nplcit']['othercit']
            category_in_npl = j['category']
            nplcit_num.append(nplcit_number)
            nplcit_othercit.append(nplcit_othercitation)
            npl_category.append(category_in_npl)    
            
    def classification(self,xml):
        classification_national = []
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])):
            classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])[i])

        classification_country = []
        classification_main = []

        for i in classification_national:
            classificiation_c = i['country']
            classificiation_m = i['main-classification']
            classification_country.append(classificiation_c)
            classification_main.append(classificiation_m)


            
    def applicant(self,xml):
        self.ubdg_parties_applicants_applicant_sequence =self.ubdg_parties_applicants_applicant_sequence
        self.ubdg_parties_applicants_applicant_app_type=self.ubdg_parties_applicants_applicant_app_type
        self.ubdg_parties_applicants_applicant_designation=self.ubdg_parties_applicants_applicant_designation
        self.ubdg_parties_applicants_applicant_addressbook_last_name=self.ubdg_parties_applicants_applicant_addressbook_last_name
        self.ubdg_parties_applicants_applicant_addressbook_first_name=self.ubdg_parties_applicants_applicant_addressbook_first_name
        self.ubdg_parties_applicants_applicant_addressbook_address_city=self.ubdg_parties_applicants_applicant_addressbook_address_city
        self.ubdg_parties_applicants_applicant_addressbook_address_country=self.ubdg_parties_applicants_applicant_addressbook_address_country
        self.ubdg_parties_applicants_applicant_nationality_country=self.ubdg_parties_applicants_applicant_nationality_country
        self.ubdg_parties_applicants_applicant_residence_country=self.ubdg_parties_applicants_applicant_residence_country
        self.applicant=self.applicant
        self.applicant_sequence=self.applicant_sequence
        self.pplicant_designation=self.applicant_designation
        self.applicant_app_type=self.applicant_app_type
        self.applicant_address_last_name=self.applicant_address_last_name
        self.applicant_address_first_name=self.applicant_address_first_name
        self.applicant_address_city=self.applicant_address_city
        self.applicant_address_state=self.applicant_address_state
        self.applicant_address_country=self.applicant_address_country
        self.applicant_nationality_country=self.applicant_nationality_country
        self.applicant_residence_country=self.applicant_residence_country
        
        #applicant가 1개일 경우
        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])) == 0:

            ubdg_parties_applicants_applicant_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@sequence']
            ubdg_parties_applicants_applicant_app_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@app-type']
            ubdg_parties_applicants_applicant_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@designation']
            ubdg_parties_applicants_applicant_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['last-name']
            ubdg_parties_applicants_applicant_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['first-name']
            ubdg_parties_applicants_applicant_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['city']
            ubdg_parties_applicants_applicant_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['country']
            ubdg_parties_applicants_applicant_nationality_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['nationality']['country']
            ubdg_parties_applicants_applicant_residence_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['residence']['country']
        
        #applicant가 2개이상일   경우
        else:                        
            applicant = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])):
                applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])[i])

            applicant_sequence =[]
            applicant_app_type =
            applicant_designation =[]
            applicant_address_last_name =[]
            applicant_address_first_name =[]
            applicant_address_city =[]
            applicant_address_state =[]
            applicant_address_country =[]
            applicant_nationality_country =[]
            applicant_residence_country =[]
            
            for i in applicant:
                ubdg_parties_applicants_applicant_sequence = i['@sequence']
                ubdg_parties_applicants_applicant_app_type = i['@app-type']
                ubdg_parties_applicants_applicant_designation = i['@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                applicant_address_first_name.append(ubdg_parties_applicants_applicant_addressbook_first_name)
                applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                applicant_nationality_country.append(ubdg_parties_applicants_applicant_nationality_country)
                applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)

    def showElement(self):
#         print("Claims sequence:"+self.ubdg_priority_claims_sequence+" country:"+self.ubdg_priority_claims_countr+" Kind:"+self.ubdg_priority_claims_kind+" Doc Number:"+self.ubdg_priority_claims_doc_number+" Date:"+self.ubdg_priority_claims_date)

        

