# Home Work
# Create a class structure with multi level inheritance
# class1 -> Engineer (project_manager, team_lead, total_resource)
# class2(class1) -> QA (QA_Head, QA_Lead, QA_Engineer)
# Class3(class2) -> company(comp_name, comp_address, comp_worth)

class engineer:
    def __init__(self, project_manager, team_lead, total_resource):
        self.project_manager = project_manager
        self.team_lead = team_lead
        self.total_resource = total_resource

    def show_engineer_team_detail(self):
        print("Project Manager Name : ", self.project_manager)
        print("Team Lead Name : ", self.team_lead)
        print("Team Total Resource : ", self.total_resource)

class QA(engineer):
    def __init__(self, QA_head, QA_Lead, QA_Engineer,project_manager, team_lead, total_resource):
        super().__init__(project_manager, team_lead, total_resource)
        self.QA_head = QA_head
        self.QA_Lead = QA_Lead
        self.QA_Engineer = QA_Engineer

    def show_QA_team_detail(self):
        print("QA head Name : ", self.QA_head)
        print("QA Lead Name : ", self.QA_Lead)
        print("QA Engineer Name : ", self.QA_Engineer)

class company(QA):
    def __init__(self, Com_Name,Com_Address,Com_worth,QA_head, QA_Lead, QA_Engineer,project_manager, team_lead, total_resource):
        super().__init__(QA_head, QA_Lead, QA_Engineer,project_manager, team_lead, total_resource)
        self.Company_Name = Com_Name
        self.Company_Add = Com_Address
        self.Company_Worth = Com_worth

    def show_company_detail(self):
        print("Company Name : ", self.Company_Name)
        print("Company Address : ", self.Company_Add)
        print("Company Worth : ", self.Company_Worth)

if __name__ == '__main__':
     obj = company("XYZ limited","Plot No.2 Vasant kunj,New Delhi","970 Cr","Nakul Singh", "Asmita Sharma", "Chinmayi","Shalini Sinha","Rakesh Nayak",10)
     obj.show_engineer_team_detail()
     obj.show_QA_team_detail()
     obj.show_company_detail()

