class XYZ:
     def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2

     def show_addition(self):
           print("addition:", self.n1+self.n2)

#obj= XYZ (20,30)
#obj.show_addition()
###################class###########
class xyz:


   def __init__(self,num1,num2):
     self.n1=num1
     self.n2=num2

   def addition(self):
    print("addition",self.n1+self.n2)

   def multiplication(self):
    print("multiplication", self.n1*self.n2)

#obj=xyz(20,30)
#obj.addition()
#obj.multiplication()
################class method#################
class new:

    name="class name is xyz"
    def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2

    def addition(self):
        print("addition:",self.n1+self.n2)

    def multiplication(self):
        print("multipliaction:",self.n1*self.n2)

    @classmethod
    def class_method(cls):
        print(cls.name)

#obj=new(20,30)
#obj.addition()
#obj.multiplication()
#obj.class_method()
####################static method################
class xyz:

    name="class name is xyz"
    def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2
    def addition(self):
        print("adddition",self.n1+self.n2)

    def multiplication(self):
        print("multipliacation",self.n1*self.n2)

    @classmethod
    def show_class_name(cls):
        print(cls.name)

    @staticmethod
    def factorials(num):
        fact=1
        for i in range(num,0,-1):
            fact=fact*i
        return fact
#obj=xyz(20,30)
#obj.addition()
#obj.multiplication()
#j.show_class_name()
#print(xyz.factorials(7))


#################self***********************

class car:
   def __init__(self,car_name,car_company):
        self.car_name=car_name
        self.car_company=car_company

   def show_car_name(self):
    print("car name:",self.car_name)

   def show_car_company(self):
    print("car company:",self.car_company)

#obj=car("nexon","tata")
#obj.show_car_name()
#car.show_car_company(obj)

############Inner class#############

class school:
    def __init__(self,school_name,admin_head,account_head):
        self.school_name=school_name
        self.admin_head=self.administrator(admin_head)
        self.account_head=self.account(account_head)


    def show_school_name(self):
        print("school_name",self.school_name)

    class administrator:
        def __init__(self,admin_head):
            self.admin_head=admin_head
        def show_administration(self):
            print("admini_head:",self.admin_head)

    class account:

        def __init__(self,acc_head):
            self.acc_head=acc_head
        def show_account(self):
            print("acc_head:",self.acc_head)

# if __name__ == "__main__":
#    obj=school("jpehs","vijay","ajay")
#    obj.admin_head.show_administration()
#    obj.account_head.show_account()
#    obj.show_school_name()

#####################Inheritance concept######################
class Father:
    def __init__(self,fname,fjob,fhouse):
      self.fname=fname
      self.fjob=fjob
      self.fhouse=fhouse

    def father_name(self):
        print("fname:",self.fname)

    def father_job(self):
       print("fjob:",self.fjob)

    def father_house(self):
        print("fhouse:",self.fhouse)

class son(Father):
    def __init__(self,sname,sjob,fname,fjob,fhouse):
        self.sname=sname
        self.sjob=sjob
        super().__init__(fname, fjob, fhouse)

    def show_sname(self):
        print("sname:",self.sname)

    def show_sjob(self):
        print("sjob:",self.sjob)

# if __name__== "__main__":
#     obj=son("mohan","engineer","ravi","constructor","4bhk")
#     obj.father_name()
#     obj.father_job()
#     obj.father_house()
#     obj.show_sname()
#     obj.show_sjob()

##################multi level ######################
class Grandfather:
     def __init__(self,Gname,Gproperty):
         self.Gname=Gname
         self.Gproperty=Gproperty

     def Gfather_name(self):
         print("Gname:", self.Gname)

     def Gfather_property(self):
         print("Gproperty:", self.Gproperty)

class Father(Grandfather):
    def __init__(self,fname,fjob,fhouse,Gname,Gproperty):
        super().__init__(Gname,Gproperty)
        self.fname=fname
        self.fjob=fjob
        self.fhouse=fhouse

    def father_name(self):
        print("fname:",self.fname)

    def father_job(self):
       print("fjob:",self.fjob)

    def father_house(self):
        print("fhouse:",self.fhouse)

class son(Father):
    def __init__(self,sname,sjob,fname,fjob,fhouse,Gname,Gproperty):
        self.sname=sname
        self.sjob=sjob
        super().__init__(fname, fjob, fhouse,Gname,Gproperty)

    def show_sname(self):
        print("sname:",self.sname)

    def show_sjob(self):
        print("sjob:",self.sjob)

if __name__== "__main__":
    obj=son("mohan","engineer","ravi","constructor","4bhk","moorty","100acr")
    obj.father_name()
    obj.father_job()
    obj.father_house()
    obj.show_sname()
    obj.show_sjob()
    obj.Gfather_name()
    obj.Gfather_property()

#########################Assignment#####################

# Home Work
# Create a class structure with multi level inheritance
# class1 -> Engineer (project_manager, team_lead, total_resource)
# class2(class1) -> QA (QA_Head, QA_Lead, QA_Engineer)
# Class3(class2) -> company(comp_name, comp_address, comp_worth)

class Engineer:
    def __init__(self, project_manager, team_lead, total_resource):
        self.project_manager = project_manager
        self.team_lead = team_lead
        self.total_resource = total_resource

    def projcet_manager(self):
        print("project_manager:", self.project_manager)

    def team_lead(self):
        print("team_lead:",self.team_lead)

    def total_resource(self):
        print("total_resource:",self.total_resource)

class QA(Engineer):
    def __init__(self,QA_head,QA_lead,QA_manager,project_manager, team_lead, total_resource):
        self.QA_head=QA_head
        self.QA_lead=QA_lead
        self.QA_manager=QA_manager
        super().__init__(project_manager, team_lead, total_resource)

    def QA_head(self):
        print("QA_head:",self.QA_head)

    def QA_lead(self):
        print("QA_lead",self.QA_lead)

    def QA_manager(self):
        print("QA_Manager",self.QA_manager)

class company(QA):
     def __init__(self,comp_name,comp_address,comp_worth,QA_head,QA_lead,QA_manager):
        self.comp_name=comp_name
        self.comp_address=comp_address
        self.comp.worth=comp_worth
        super().__init__(project_manager, team_lead, total_resource,QA_head,QA_lead,QA_manager)

        def comp_name(self):
            print("comp_name:",comp_name)

        def comp_address(self):
            print("comp_address:",comp_address)

        def comp_worth(self):
            print("comp_worth:",comp_worth)