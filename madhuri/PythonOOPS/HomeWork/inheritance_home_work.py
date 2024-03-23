# Home Work
# Create a class structure with multi level inheritance
# class1 -> Engineer (project_manager, team_lead, total_resource)
# class2(class1) -> QA (QA_Head, QA_Lead, QA_Engineer)
# Class3(class2) -> company(comp_name, comp_address, comp_worth)

# multilevel inheritance  (A -> B -> C)
class Engineer:
    def __init__(self, project_manager, team_lead, total_resource):
        self.project_manager = project_manager
        self.team_lead = team_lead
        self.total_resource = total_resource

    def project_manager_details(self):
        print("\t", "_"*20, "Project Manager Details: ", "_"*20)
        print("\n 1. Name: ", self.project_manager)
        print("\n 2. Team Lead: ", self.team_lead)
        print("\n 3. Total Resources: ", self.total_resource)


class QA(Engineer):
    def __init__(self, project_manager, team_lead, total_resource, qa_head, qa_lead, qa_engineer):
        super().__init__(project_manager, team_lead, total_resource)
        self.qa_head = qa_head
        self.qa_lead = qa_lead
        self.qa_engineer = qa_engineer


    def qa_details(self):
        print("\t", "_"*20, "QA Details: ", "_"*20)


class Company(QA):
    def __init__(self, project_manager, team_lead, total_resource,
                 qa_head, qa_lead, qa_engineer,
                 comp_name, comp_address,
                 comp_worth, **kwargs):
        super().__init__(project_manager, team_lead, total_resource,
                         qa_head, qa_lead, qa_engineer)
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.comp_worth = comp_worth
        self.comp_details = kwargs
        #
        # for key, val in kwargs.items():
        #     print("args val: ", key, '=', val)
    def company_details(self):
        print("\n 1. QA Name: ", self.project_manager)
        print("\n 2. Team Lead: ", self.team_lead)
        print("\n 3. Total Resources: ", self.total_resource)

        print("\t", "_"*20, "Company Details: ", "_"*20)
        print("\n 1. Company Name : ", self.comp_name)
        print("\n 2. Company Address: ", self.comp_address)
        print("\n 3. Company Worth: ", self.comp_worth)

    def show_kwargs_values(self):
        print(self.comp_details)


if __name__ == '__main__':
    dict_company = {
        'Employee':
        [
            {
                'employee_id': 120,
                'employee_name': 'madhuri',
                'employee_phone': 9860138618,
                'employee_status': True,
                'employee_aadhar': "C:\\Users\\madhu\\Pictures\\Profile_Pic.webp"
            },
            {
                'employee_id': 121,
                'employee_name': 'Ridhaa',
                'employee_phone': 8609138618,
                'employee_status': True,
                'employee_aadhar': "C:\\Users\\madhu\\Pictures\\Profile_Pic.webp"
            }
        ]
    }
    obj = Company("Rahul Sharma", "Asif", 10, "Aishwarya",
                  "Sarika Jain", "jr. Abhishek", "TCS",
                  "Pune", "100Cr", cmp_details=dict_company)
    # obj.project_manager_details()
    # obj.qa_details()
    # obj.company_details()
    obj.show_kwargs_values()
