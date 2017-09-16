
# coding: utf-8

# In[1]:

#NULL처리만 해주면 끝..이라고 생각함.
#검토 필요.

#2005.01.01~2005.08.25
#050104 ok
#050524 ok
#added parentdoc and childdoc
#050823
class parserVer40(Parser):
    def __init__(self,xml):
        super().__init__(xml)
        
        #address_street
        self.ubdg_parties_applicants_applicant_addressbook_address_street = self.doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['street']
        
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
        self.nplcit_num= None
        self.nplcit_othercit=None
        self.npl_category=None
        
        #classification
        self.classification_national=classification_national
        self.classification_country=classification_country
        self.classification_main=classification_main
        
        #applicant
        #postcode is option
        self.ubdg_parties_applicants_applicant_sequence =self.ubdg_parties_applicants_applicant_sequence
        self.ubdg_parties_applicants_applicant_app_type=self.ubdg_parties_applicants_applicant_app_type
        self.ubdg_parties_applicants_applicant_designation=self.ubdg_parties_applicants_applicant_designation
        self.ubdg_parties_applicants_applicant_addressbook_last_name=self.ubdg_parties_applicants_applicant_addressbook_last_name
        self.ubdg_parties_applicants_applicant_addressbook_first_name=self.ubdg_parties_applicants_applicant_addressbook_first_name
        self.ubdg_parties_applicants_applicant_addressbook_address_state=self.ubdg_parties_applicants_applicant_addressbook_address_state
        self.ubdg_parties_applicants_applicant_addressbook_address_postcode=self.ubdg_parties_applicants_applicant_addressbook_address_postcode
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
        self.applicant_address_street=self.applicant_address_street
        self.applicant_address_postcode=None
        
        #claim
        self.ubdg_priority_claims_sequence =self.ubdg_priority_claims_sequence
        self.ubdg_priority_claims_kind = self.ubdg_priority_claims_kind
        self.ubdg_priority_claims_country =self.ubdg_priority_claims_country
        self.ubdg_priority_claims_doc_number= self.ubdg_priority_claims_doc_number
        self.ubdg_priority_claims_date =self.ubdg_priority_claims_date
        
        #figure
        self.figure = self.figure
        self.figure_id = self.figure_id
        self.figure_num=self.figure_num
        self.figure_img_id=self.figure_img_id
        self.figure_img_he=self.figure_img_he
        self.figure_img_wi=self.figure_img_wi
        self.figure_img_file=self.figure_img_file
        self.figure_img_alt=self.figure_img_alt
        self.figure_img_content=self.figure_img_content
        self.figure_img_format=self.figure_img_format
        
        #relation
        #check that other parsers have a 'relation'
        self.ubdg_relateddoc_cip_relation_parentdoc_di_country=None
        self.ubdg_relateddoc_cip_relation_parentdoc_di_doc_number=None
        self.ubdg_relateddoc_cip_relation_parentdoc_di_kind=None
        self.ubdg_relateddoc_cip_relation_parentdoc_di_date=None
        #parent_status is option.
        self.ubdg_relateddoc_cip_relation_parentdoc_parent_status= None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_country=None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_doc_number=None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_kind=None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_date=None
        self.ubdg_relateddoc_cip_relation_parentdoc_childdoc_country=None
        self.ubdg_relateddoc_cip_relation_parentdoc_childdoc_doc_number=None
        self.relation = None
        self.parentdoc_di_country=None
        self.parentdoc_di_country =None
        self.parentdoc_di_doc_number =None
        self.parentdoc_di_kind =None
        self.parentdoc_di_date =None
        self.parentgrantdoc_di_country =None
        self.parentgrantdoc_di_doc_number =None
        self.parentgrantdoc_di_kind =None
        self.parentgrantdoc_di_date =None
        self.childdoc_country =None
        self.childdoc_doc_number =None
        self.parent_status =None
        
        #assistant examiner(option) be NULL
        self.ubdg_examiners_assistant_examiner_last_name = None
        self.ubdg_examiners_assistant_examiner_first_name = None
       
        #agent
        self.ubdg_parties_agents_agent_sequence=self.ubdg_parties_agents_agent_sequence
        self.ubdg_parties_agents_agent_rep_type=self.ubdg_parties_agents_agent_rep_type
        self.ubdg_parties_agents_agent_addressbook_orgname=self.ubdg_parties_agents_agent_addressbook_orgname
        self.ubdg_parties_agents_agent_addressbook_address_country=self.ubdg_parties_agents_agent_addressbook_address_country
        self.agents= self.agents
        self.agent_sequence =self.agent_sequence
        self.agent_rep_type=self.agent_rep_type
        self.agent_orgname=self.agent_orgname
        self.agent_country=self.agent_country
            
        #additional_info
        self.classification_add_info=None
        self.classification_add=None
        
    

    def figure(self):

        figure = []
        for i in range(len(doc['us-patent-grant']['drawings']['figure'])):
            figure.append((doc['us-patent-grant']['drawings']['figure'])[i])

        figure_id = []
        figure_num = []
        figure_img_id = []
        figure_img_he =[]
        figure_img_wi = []
        figure_img_file = []
        figure_img_alt = []
        figure_img_content =[]
        figure_img_format = []

        for i in figure:
            figure_id.append(i['@id'])
            figure_num.append(i['@num'])
            figure_img_id.append(i['img']['@id'])
            figure_img_he.append(i['img']['@he'])
            figure_img_wi.append(i['img']['@wi'])
            figure_img_file.append(i['img']['@file'])
            figure_img_alt.append(i['img']['@alt'])
            figure_img_content.append(i['img']['@img-content'])
            figure_img_format.append(i['img']['@img-format'])


    def description(self):

        p =[]
        for i in range(len(doc['us-patent-grant']['description']['description-of-drawings']['p'])):
             p.append((doc['us-patent-grant']['description']['description-of-drawings']['p'])[i])

        p_id = []
        p_num =[]
        p_text=[]

        for i in p:
            p_id.append(i['@id'])
            p_num.append(i['@num'])
            p_text.append(i['#text'])


        
    def agent(self,xml):
        #1개인 경우
        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent'])) == 0:
            ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
            ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
            ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
            ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']
     
        else:                        
            agents = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent'])):
                applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent'])[i])

            agent_sequence =[]
            agent_rep_type =[]
            agent_orgname =[]
            agent_country =[]

            for i in agents:
                ubdg_parties_agents_agent_sequence=i['@sequence']
                ubdg_parties_agents_agent_rep_type=i['@rep_type']
                ubdg_parties_agents_agent_addressbook_orgname=i['addressbook']['orgname']
                ubdg_parties_agents_agent_addressbook_address_country=i['addressbook']['address']['country']
                agent_sequence.append(ubdg_parties_agents_agent_sequence)
                agent_rep_type.append(ubdg_parties_agents_agent_rep_type)
                agent_orgname.append(ubdg_parties_agents_agent_addressbook_orgname)
                agent_country.append(ubdg_parties_agents_agent_addressbook_address_country)
                
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
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['field-of-search']['classification-national'])):
            classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant']['field-of-search']['classification-national'])[i])

        classification_country = []
        classification_main = []
        classification_add_info =[]
        for i in classification_national:
            classification_add = i['additional-info']
            classificiation_c = i['country']
            classificiation_m = i['main-classification']
            classification_country.append(classificiation_c)
            classification_main.append(classificiation_m)
            classification_add_info.append(classification_add)
            
    def applicant(self,xml):

        #applicant가 1개일 경우
        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])) == 0:

            ubdg_parties_applicants_applicant_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@sequence']
            ubdg_parties_applicants_applicant_app_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@app-type']
            ubdg_parties_applicants_applicant_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@designation']
            ubdg_parties_applicants_applicant_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['last-name']
            ubdg_parties_applicants_applicant_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['first-name']
            ubdg_parties_applicants_applicant_addressbook_address_street = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['street']
            ubdg_parties_applicants_applicant_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['city']
            ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
            ubdg_parties_applicants_applicant_addressbook_address_postcode = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['postcode']
            ubdg_parties_applicants_applicant_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['country']
            ubdg_parties_applicants_applicant_nationality_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['nationality']['country']
            ubdg_parties_applicants_applicant_residence_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['residence']['country']
        
        #applicant가 2개이상일   경우
        else:                        
            applicant = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])):
                applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])[i])

            applicant_sequence =[]
            applicant_app_type =[]
            applicant_designation =[]
            applicant_address_last_name =[]
            applicant_address_first_name =[]
            applicant_address_city =[]
            applicant_address_state =[]
            applicant_address_country =[]
            applicant_nationality_country =[]
            applicant_residence_country =[]
            applicant_address_street = []
            applicant_address_postcode=[]
            
            
            for i in applicant:
                ubdg_parties_applicants_applicant_sequence = i['@sequence']
                ubdg_parties_applicants_applicant_app_type = i['@app-type']
                ubdg_parties_applicants_applicant_designation = i['@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']
                ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address']['postcode']
                ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                applicant_address_first_name.append(ubdg_parties_applicants_applicant_addressbook_first_name)
                applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                applicant_nationality_country.append(ubdg_parties_applicants_applicant_nationality_country)
                applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)

    def claim(self):
        ubdg_priority_claims_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@sequence']
        ubdg_priority_claims_kind['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@kind']
        ubdg_priority_claims_country = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['country']
        ubdg_priority_claims_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['doc-number']
        ubdg_priority_claims_date = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['date']
    
    #이거 자체가 option.
    def relation(self):
        
                   
                #relation
        #check that other parsers have a 'relation'
        self.ubdg_relateddoc_cip_relation_parentdoc_di_country=None
        self.ubdg_relateddoc_cip_relation_parentdoc_di_doc_number=None
        self.ubdg_relateddoc_cip_relation_parentdoc_di_kind=None
        self.ubdg_relateddoc_cip_relation_parentdoc_di_date=None
        #parentgrant is option.
        self.ubdg_relateddoc_cip_relation_parentdoc_parent_status= None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_country=None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_doc_number=None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_kind=None
        self.ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_date=None
        
        self.ubdg_relateddoc_cip_relation_parentdoc_childdoc_country=None
        self.ubdg_relateddoc_cip_relation_parentdoc_childdoc_doc_number=None
        self.relation = None
        self.parentdoc_di_country=None
        self.parentdoc_di_country =None
        self.parentdoc_di_doc_number =None
        self.parentdoc_di_kind =None
        self.parentdoc_di_date =None
        self.parentgrantdoc_di_country =None
        self.parentgrantdoc_di_doc_number =None
        self.parentgrantdoc_di_kind =None
        self.parentgrantdoc_di_date =None
        self.childdoc_country =None
        self.childdoc_doc_number =None
        self.parent_status =None
        
        
        
        #relation이 1개 일 경우
        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation'])) == 0:

            ubdg_relateddoc_cip_relation_parentdoc_di_country = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['document-id']['country']
            ubdg_relateddoc_cip_relation_parentdoc_di_doc_number = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['document-id']['doc-number']
            ubdg_relateddoc_cip_relation_parentdoc_di_kind = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['document-id']['kind']
            ubdg_relateddoc_cip_relation_parentdoc_di_date = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['document-id']['date']
            ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_country=['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['parent-grant-document']['document-id']['country']
            ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_doc_number=['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']
            ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_kind=['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['parent-grant-document']['document-id']['kind']
            ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_date=['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['parent-grant-document']['document-id']['date']
            ubdg_relateddoc_cip_relation_parentdoc_childdoc_country = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['child-doc']['document-id']['country']
            ubdg_relateddoc_cip_relation_parentdoc_childdoc_doc_number = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['child-doc']['document-id']['doc-number']
            ubdg_relateddoc_cip_relation_parentdoc_parent_status = ['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation']['parent-doc']['parent_status']

        #relation이 2개이상일 경우
        else:                        
            relation = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation'])):
                applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['continuation-in-part']['relation'])[i])

            parentdoc_di_country =[]
            parentdoc_di_doc_number =[]
            parentdoc_di_kind =[]
            parentdoc_di_date =[]
            parentgrantdoc_di_country =[]
            parentgrantdoc_di_doc_number =[]
            parentgrantdoc_di_kind =[]
            parentgrantdoc_di_date =[]
            childdoc_country =[]
            childdoc_doc_number =[]
            parent_status = []
            
            
            for i in relation:
                
                ubdg_relateddoc_cip_relation_parentdoc_di_country = i['parent-doc']['document-id']['country']
                ubdg_relateddoc_cip_relation_parentdoc_di_doc_number = i['parent-doc']['document-id']['doc-number']
                ubdg_relateddoc_cip_relation_parentdoc_di_kind = i['parent-doc']['document-id']['kind']
                ubdg_relateddoc_cip_relation_parentdoc_di_date = i['parent-doc']['document-id']['date']
                ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_country = i['parent-doc']['parent-grant-document']['document-id']['country']
                ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_doc_number = i['parent-doc']['parent-grant-document']['document-id']['doc-number']
                ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_kind = i['parent-doc']['parent-grant-document']['document-id']['kind']
                ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_date = i['parent-doc']['parent-grant-document']['document-id']['date']
                ubdg_relateddoc_cip_relation_parentdoc_childdoc_country = i['child-doc']['document-id']['country']
                ubdg_relateddoc_cip_relation_parentdoc_childdoc_doc_number = i['child-doc']['document-id']['doc-number']
                ubdg_relateddoc_cip_relation_parentdoc_parent_status = i['parent-doc']['parent_status']
                parentdoc_di_country.append(ubdg_relateddoc_cip_relation_parentdoc_di_country)
                parentdoc_di_doc_number.append(ubdg_relateddoc_cip_relation_parentdoc_di_doc_number)
                parentdoc_di_kind.append(ubdg_relateddoc_cip_relation_parentdoc_di_kind)
                parentdoc_di_date.append(ubdg_relateddoc_cip_relation_parentdoc_di_date)
                parentgrantdoc_di_country.append(ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_country)
                parentgrantdoc_di_doc_number.append(ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_doc_number)
                parentgrantdoc_di_kind.append(ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_kind)
                parentgrantdoc_di_date.append(ubdg_relateddoc_cip_relation_parentdoc_parentgrantdoc_di_date)
                childdoc_country.append(ubdg_relateddoc_cip_relation_parentdoc_childdoc_country)
                childdoc_doc_number.append(ubdg_relateddoc_cip_relation_parentdoc_childdoc_doc_number)
                parent_status.append(ubdg_relateddoc_cip_relation_parentdoc_parent_status)



#     def showElement(self):
# #         print("Claims sequence:"+self.ubdg_priority_claims_sequence+" country:"+self.ubdg_priority_claims_countr+" Kind:"+self.ubdg_priority_claims_kind+" Doc Number:"+self.ubdg_priority_claims_doc_number+" Date:"+self.ubdg_priority_claims_date)

        


# In[ ]:



