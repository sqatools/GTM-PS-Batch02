class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"Father name : {self.fname}")

    def show_father_business(self):
        print(f"Father Business : {self.fbusiness}")

    def show_father_house(self):
        print(f"Father owns : {self.fhouse}")


class Son(father):
    def __init__(self, sname, sjob, fname, fbusiness, fhouse):
        self.sname = sname
        self.sjob = sjob
        super().__init__(fname, fbusiness, fhouse)

    def show_son_details(self):
        print(f"Son name : {self.sname}")
        print(f"Son job : {self.sjob}")



obj = Son("Mohit", "Engineer", "Mohan", "Construction", "4 BHK")

obj.show_father_business()
obj.show_son_details()
obj.show_father_house()