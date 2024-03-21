#create Inner class

class IRIS:
    def __init__(self, Enterprise, admin_head, Location_head):
        self.ent_obj = Enterprise
        self.Company_obj = self.Company(admin_head)
        # self.Company_obj1 = self.Company(account_head)
        self.Location_obj = self.Location(Location_head)

    def show_enterprise_name(self):
        print("Enterprise Name:", self.ent_obj)

    class Company:
        def __init__(self, admin_department_head):
            self.ad_dep = admin_department_head
            #self.ac_dep = account_department_head

        def show_admin_depart_head(self):
            print("Admin Department Head name :", self.ad_dep)

        # def show_account_depart_head(self):
        #     print("Account Department Head name :", self.ac_dep)

    class Location:
        def __init__(self, Location_department_head):
            self.Loc_head = Location_department_head

        def show_location_head(self):
            print("Admin Department Head name :", self.Loc_head)


if __name__ == "__main__":
    obj = IRIS("Reliance" , "Kanchan Rai" , "Jyoti Pandey")
    obj.show_enterprise_name()
    obj.Company_obj.show_admin_depart_head()
    # obj.Company_obj1.show_account_depart_head()
    obj.Location_obj.show_location_head()

