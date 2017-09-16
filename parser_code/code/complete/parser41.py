
# coding: utf-8

#2005.08.25~2006.07.26 ok
#2006.07.26~2006.08.23
#20060117 ok
#20060725 ok
#20060801 ok
#20060822(end) assistant examiners ok
#correct applicant address, added postcode and street
#correct citation, added category, classification country and main classification

class parserVer41(Parser):
    def __init__(self,xml):
        super().__init__(xml)

        #botantic
        self.ubdg_us_botantic_latin_name = None
        self.ubdg_us_botantic_variety = None

        #add assistant examiners
        #만약 assistant examiners가 없으면 어떡하지?(option) :NULL처리해줘야함
        #수정해야됨
        self.ubdg_examiners_assistant_examiner_last_name = None
        self.ubdg_examiners_assistant_examiner_first_name = None

        #add us-claim-statement
        self.upg_us_claim_statement = doc['us-patent-grant']['us-claim-statement']
        #address_street
        self.ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
        #assignee
        self.ubdg_assignees_assignee_address_orgname =None
        self.ubdg_assignees_assignee_address_role=None
        self.ubdg_assignees_assignee_address_address_city=None
        self.ubdg_assignees_assignee_address_address_state=None
        self.ubdg_assignees_assignee_address_address_country=None
                #agents #null
        self.ubdg_parties_agents_agent_rep_type=None
        self.ubdg_parties_agents_agent_addressbook_orgname=None
        self.ubdg_parties_agents_agent_addressbook_address_country=None
        #further 추가

        self.further=None
        self.further_classification=None
        self.further_class=None

        self.patcit = None
        self.patcit_num =None
        self.patcit_country = None
        self.patcit_doc_number = None
        self.patcit_kind=None
        self.patcit_name=None
        self.patcit_date=None

        self.nplcit_num=None
        self.nplcit_othercit=None
        self.npl_category = None


        self.patcit_category= doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation']['category']
        self.patcit_classification_country=None
        self.patcit_classification_main=None

        #classification
        self.classification_national= None
        self.classification_country= None
        self.classification_main= None
        self.us_classifications_ipcr = None
        #applicant
        self.ubdg_parties_applicants_applicant_sequence =None
        self.ubdg_parties_applicants_applicant_app_type=None
        self.ubdg_parties_applicants_applicant_designation=None
        self.ubdg_parties_applicants_applicant_addressbook_last_name=None
        self.ubdg_parties_applicants_applicant_addressbook_first_name=None
        self.ubdg_parties_applicants_applicant_addressbook_address_city=None
        self.ubdg_parties_applicants_applicant_addressbook_address_country=None
        self.ubdg_parties_applicants_applicant_nationality_country=None
        self.ubdg_parties_applicants_applicant_residence_country=None
        self.applicant=None
        self.applicant_sequence=None
        self.pplicant_designation=None
        self.applicant_app_type=None
        self.applicant_address_last_name=None
        self.applicant_address_first_name=None
        self.applicant_address_city=None
        self.applicant_address_state=None
        self.applicant_address_country=None
        self.applicant_nationality_country=None
        self.applicant_residence_country=None
        #null
        self.applicant_address_street=None
        self.applicant_address_postcode=None


        #relation
        self.us_related_documents=None
        self.different_tags=None
        self.get_relation=None
        self.ubdg_relateddoc_relation_parentdoc_di_country=None
        self.ubdg_relateddoc_relation_parentdoc_di_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_di_kind=None
        self.ubdg_relateddoc_relation_parentdoc_di_date=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_country=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_parent_status=None
        self.ubdg_relateddoc_relation_parentdoc_di_country=None
        self.ubdg_relateddoc_relation_parentdoc_di_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_di_kind=None
        self.ubdg_relateddoc_relation_parentdoc_di_date=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_country=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=None
        self.realtion_parent_grant_doc_country=None
        self.realtion_parent_grant_doc_number=None
        self.realtion_parent_grant_doc_kind=None
        self.realtion_parent_grant_doc_date=None
        self.relation_parent_status=None

        #megaTable
        self.ubdg_mega_table = None

        #abstract
        self.ubdg_abstract = None
        #drawing
        self.ubdg_drawing= None
        #sequence list
        self.ubdg_us_sequence_list_doc= None
        #table external
        self.ubdg_table_external_doc= None
        #chemistry
        self.ubdg_us_chemistry= None
        #math
        self.ubdg_us_math= None



         try:
            null_variables = []
            null_variables.append(ubdg_examiners_assistant_examiner_last_name)
            null_variables.append(ubdg_examiners_assistant_examiner_first_name)

            null_tag = []
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

            for v,t in zip(null_variables, null_tag):
                    if v == t:
                        v =  t

        except:
            pass

    def drawing(self,xml):
        ubdg_drawing = doc['us-patent-grant']['us-bibliographic-data-grant']['drawings']

    def sequenceListDoc(self,xml):
        ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-bibliographic-data-grant']['us-sequence-list-doc']

    def tableExternalDoc(self,xml):
        ubdg_table_external_doc = doc['us-patent-grant']['us-bibliographic-data-grant']['table-external-doc']
    def usChemistry(self,xml):
        ubdg_us_chemistry = doc['us-patent-grant']['us-bibliographic-data-grant']['us-chemistry']

    def usMath(self,xml):
        ubdg_us_math = doc['us-patent-grant']['us-bibliographic-data-grant']['us-math']

    def abstract(self,xml):
        ubdg_abstract = doc['us-patent-grant']['us-bibliographic-data-grant']['abstract']
    def megaTable(self,xml):
        ubdg_mega_table =doc['us-patent-grant']['us-bibliographic-data-grant']['us-megatable-doc']

            #NULL
    def usBotantic(self, xml):
        ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
        ubdg_us_botantic_variety=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']

        #NULL
    def agent(self,xml):

        ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
        ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
        ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
        ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']

        #NULL
    def assignee(self,xml):

        ubdg_assignees_assignee_address_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
        ubdg_assignees_assignee_address_role = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']
        ubdg_assignees_assignee_address_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
        ubdg_assignees_assignee_address_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['state']
        ubdg_assignees_assignee_address_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['country']



        #citation에 classification natiojnal이랑 main 있음 확인 수정필요
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
        patcit_category = []
        patcit_classification_country =[]
        patcit_classification_main =[]
        nplcit_num =[]
        nplcit_othercit=[]


        for j in patcit:
            patcit_number = j['patcit']['@num']
            patcit_doc_country = j['patcit']['document-id']['country']
            patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
            patcit_doc_kind = j['patcit']['document-id']['kind']
            patcit_doc_name = j['patcit']['document-id']['name']
            patcit_doc_date = j['patcit']['document-id']['date']
            patcit_c_category =j['patcit']['category']
            patcit_c_classification_country =j['patcit']['classification-national']['country']
            patcit_c_classification_main = j['patcit']['classification-national']['main-classification']
            patcit_num.append(patcit_number)
            patcit_country.append(patcit_doc_country)
            patcit_doc_number.append(patcit_doc_docnumber)
            patcit_kind.append(patcit_doc_kind)
            patcit_name.append(patcit_doc_name)
            patcit_date.append(patcit_doc_date)
            patcit_classification_country.append(patcit_c_classification_country)
            patcit_category.appen(patcit_c_category)
            patcit_classification_main.append(patcit_c_classification_main)
            nplcit_number = j['nplcit']['@num']
            nplcit_othercitation = j['nplcit']['othercit']

            nplcit_num.append(nplcit_number)
            nplcit_othercit.append(nplcit_othercitation)



    def classification(self,xml):
        try:
            us_classifications_ipcr = doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['us-classifications-ipcr']
        except:
            pass

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


    #함수전체를 null..optional
    def furtherClassification(self,xml):
        further = []
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification'])):
            further.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification']))

        further_classification = []

        for i in further:
            further_class = i
            further_classification.append(further_class)


    def classificationIpcr:

        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])) ==0:

            ubdg_csipcr_cipcr_ipc_ver_indicator_date = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-ipcr']['ipc-version-indicator']['date']
            ubdg_csipcr_cipcr_classification_level = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-level']
            ubdg_csipcr_cipcr_section = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['section']
            ubdg_csipcr_cipcr_class= doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['class']
            ubdg_csipcr_cipcr_subclass =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subclass']
            ubdg_csipcr_cipcr_main_group =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['main-group']
            ubdg_csipcr_cipcr_subgroup = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subgroup']
            ubdg_csipcr_cipcr_symbol_position = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['symbol-position']
            ubdg_csipcr_cipcr_classification_value = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-value']
            ubdg_csipcr_cipcr_action_date =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['action-date']['date']
            ubdg_csipcr_cipcr_generating_office_country =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['generating-office']['country']
            ubdg_csipcr_cipcr_classification_status =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-status']
            ubdg_csipcr_cipcr_classification_data_source = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-data-source']

        else:
            classifications_ipcr = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])):
                classifications_ipcr.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])[i])

            classification_ipc_version_indicator_date = []
            classification_level = []
            classification_section = []
            classification_class = []
            classification_subclass =[]
            classification_main_group =[]
            classification_subgroup =[]
            classification_symbol_position =[]
            classification_value = []
            classification_action_date = []
            classification_generating_office_country = []
            classification_status = []
            classification_data_source = []

            for i in classifications_ipcr:
                ubdg_csipcr_cipcr_ipc_ver_indicator_date = i['ipc-version-indicator']['date']
                ubdg_csipcr_cipcr_classification_level = i['classification-level']
                ubdg_csipcr_cipcr_section = i['section']
                ubdg_csipcr_cipcr_class = i['class']
                ubdg_csipcr_cipcr_subclass = i['subclass']
                ubdg_csipcr_cipcr_main_group = i['main-group']
                ubdg_csipcr_cipcr_subgroup = i['subgroup']
                ubdg_csipcr_cipcr_symbol_position = i['symbol-position']
                ubdg_csipcr_cipcr_classification_value = i['classification-value']
                ubdg_csipcr_cipcr_action_date = i['action-date']['date']
                ubdg_csipcr_cipcr_generating_office_country = i['generating-office']['country']
                ubdg_csipcr_cipcr_classification_status = i['classification-status']
                ubdg_csipcr_cipcr_classification_data_source = i['classification-data-source']
                classification_ipc_version_indicator_date.append(ubdg_csipcr_cipcr_ipc_ver_indicator_date)
                classification_level.append(ubdg_csipcr_cipcr_classification_level)
                classification_section.append(ubdg_csipcr_cipcr_section)
                classification_class.append(ubdg_csipcr_cipcr_class)
                classification_subclass.append(ubdg_csipcr_cipcr_subclass)
                classification_main_group.append(ubdg_csipcr_cipcr_main_group)
                classification_subgroup.append(ubdg_csipcr_cipcr_subgroup)
                classification_symbol_position.append(ubdg_csipcr_cipcr_symbol_position)
                classification_value.append(ubdg_csipcr_cipcr_classification_value)
                classification_action_date.append(ubdg_csipcr_cipcr_action_date)
                classification_generating_office_country.append(ubdg_csipcr_cipcr_generating_office_country)
                classification_status.append(ubdg_csipcr_cipcr_classification_status)
                classification_data_source.append(ubdg_csipcr_cipcr_classification_data_source)


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
                applicant_address_first_name.append(ubdg_parties_appli cants_applicant_addressbook_first_name)
                applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                applicant_nationality_country.append(ubdg_parties_applicants_applicant_nationality_country)
                applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)

    def beforeRelation(relation):
        us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

        different_tags = []
        for i in us_related_documents.keys():
            different_tags.append(i)

        relation_list =[]
        for i in different_tags:
            get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
            if isinstance(get_relation, type(list)) is True:
                for j in range(len(get_relation)-1):
                    for k in get_relation:
                        relation_list.append(k)
            else:
                relation_list.append(get_relation)
        relation(relation_list)

    def relation(has_relation):

        ubdg_relateddoc_relation_parentdoc_di_country= []
        ubdg_relateddoc_relation_parentdoc_di_doc_number =[]
        ubdg_relateddoc_relation_parentdoc_di_kind=[]
        ubdg_relateddoc_relation_parentdoc_di_date=[]
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=[]
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=[]
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=[]
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=[]
        ubdg_relateddoc_relation_parentdoc_childdoc_country=[]
        ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=[]
        ubdg_relateddoc_relation_parentdoc_parent_status=[]

        for relation_element in has_relation:

            ubdg_relateddoc_relation_parentdoc_di_country.append(relation_element['relation']['parent-doc']['document-id']['country'])
            ubdg_relateddoc_relation_parentdoc_di_doc_number.append(relation_element['relation']['parent-doc']['document-id']['doc-number'])
            ubdg_relateddoc_relation_parentdoc_di_kind.append(relation_element['relation']['parent-doc']['document-id']['kind'])
            ubdg_relateddoc_relation_parentdoc_di_date.append(relation_element['relation']['parent-doc']['document-id']['date'])

            ubdg_relateddoc_relation_parentdoc_childdoc_country.append(relation_element['relation']['child-doc']['document-id']['country'])
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(relation_element['relation']['child-doc']['document-id']['doc-number'])

            #null
            try:
                realtion_parent_grant_doc_country = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['country']
                realtion_parent_grant_doc_number = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']
                realtion_parent_grant_doc_kind = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']
                realtion_parent_grant_doc_date = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(realtion_parent_grant_doc_country)
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(realtion_parent_grant_doc_number)
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(realtion_parent_grant_doc_kind)
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(realtion_parent_grant_doc_date)
            except:
                pass

            try:
                relation_parent_status = relation_element['relation']['parent-doc']['parent_status']
                ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
            except:
                pass



    def usProvisionalApplication(self,xml):
        ubdg_provisional_appl_doc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
        ubdg_provisional_appl_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['doc-number']
        ubdg_provisional_appl_doc_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['kind']
        ubdg_provisional_appl_doc_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']

    def relatedPublication(self,xml):
        ubdg_related_publ_doc_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['country']
        ubdg_related_publ_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['doc-number']
        ubdg_related_publ_doc_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['kind']
        ubdg_related_publ_doc_country_date = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['date']




# In[ ]:
