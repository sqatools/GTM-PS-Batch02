#import self as self


class  Engineer:
    def __init__(self, proj_manager, team_lead, total_resource):
        self.proj_manager = proj_manager
        self.team_lead = team_lead
        self.total_resource = total_resource

    def show_Engineer_details(self):
        print(f"proj_manager name : {self.proj_manager}")
        print(f"team_lead name : {self.team_lead}")
        print(f"total_resource name : {self.total_resource}")

class QA:
    def __init__(self, QA_Head, QA_Lead, QA_Engineer):
        self.QA_Head = QA_Head
        self.QA_Lead = QA_Lead
        self.QA_Engineer = QA_Engineer

    def show_QA_details(self):
        print(f"QA_Head name : {self.QA_Head}")
        print(f"QA_Lead name : {self.QA_Lead}")
        print(f"QA_Engineer name : {self.QA_Engineer}")


# MRO : Method Resolution Order
class Company(Engineer, QA):
    def __init__(self, comp_name, comp_address, comp_worth, proj_manager, team_lead, total_resource,QA_Head, QA_Lead, QA_Engineer ):
        super().__init__(comp_name, comp_address, comp_worth)
        #super().__init__(m_name, m_business)
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.comp_worth = comp_worth

    def show_Company_details(self):
        print(f"comp_name : {self.comp_name}")
        print(f"comp_address : {self.comp_address}")
        print(f"comp_worth : {self.comp_worth}")

    def show_QA_details(self):
        self.show_Engineer_details()
        #self.show_QA_details()



if __name__ == '__main__':
    obj = Company("TCS", "Bangalore", "1000000cr", "Phani", "kiran", "5", "pk","pk2","pk3")

    obj.show_Engineer_details()
    obj.show_QA_details()
