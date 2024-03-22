# Home Work
# Create a class structure with multi level inheritance
# class1 -> Engineer (project_manager, team_lead, total_resource)
# class2(class1) -> QA (QA_Head, QA_Lead, QA_Engineer)
# Class3(class2) -> company(comp_name, comp_address, comp_worth)

class Engineer:
    def __init__(self,project_manager,team_lead,total_resource):
        self.Eng_P_M=project_manager
        self.Eng_T_L=team_lead
        self.Eng_T_R=total_resource

    def show_Eng_Detail(self):
        print(f"Eng-Project Manager name: {self.Eng_P_M}\n"
               f"Eng-Team Lead name: {self.Eng_T_L}\n"
               f"Eng-Total_resource name: {self.Eng_T_R}")

class QA(Engineer):
    def __init__(self,QA_Head,QA_Lead, QA_Engineer,Eng_P_M,Eng_T_L,Eng_T_R):
        super().__init__(Eng_P_M,Eng_T_L,Eng_T_R)
        self.QA_H=QA_Head
        self.QA_L=QA_Lead
        self.QA_E=QA_Engineer

    def show_QA_Details(self):
        print(f"QA head Name: {self.QA_H}\n"
               f"QA Lead Name: {self.QA_L}\n"
               f"QA Engineer Name: {self.QA_E}")

class Company(QA):
    def __init__(self,comp_name, comp_address, comp_worth,QA_H,QA_L,QA_E,Eng_P_M,Eng_T_L,Eng_T_R):
        super().__init__(QA_H,QA_L,QA_E,Eng_P_M,Eng_T_L,Eng_T_R)
        self.co_N=comp_name
        self.co_A=comp_address
        self.co_W=comp_worth
    def show_company_details(self):
        print(f"comp_name: {self.co_N}\n"
              f"comp_address: {self.co_A}\n"
              f"comp_worth: {self.co_W}")

    def show_all_details(self):
        self.show_Eng_Detail()
        self.show_QA_Details()
        self.show_company_details()

"""if __name__ == '__main__':
    obj = Company("IT Company", "Pune", 5000000, "Rahul", "Ram", "Sham", "radhika", "radha", "ramya")
    obj.show_all_details()"""

obj = Company("IT Company", "Pune", 5000000, "Rahul",
              "Ram", "Sham", "radhika", "radha", "ramya")
obj.show_all_details()



