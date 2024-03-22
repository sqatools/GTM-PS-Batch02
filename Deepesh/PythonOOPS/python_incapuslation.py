"""
Encapsulation/Data Hiding: data hiding is to avoid the data access outside of the class, then it
is known as Encapsulation.
we can achieve the data hiding with single '_' and double '__' underscore as prefix in the variable and
method name.
- If any method defined with single underscore as prefix, then the method will not show in suggestion
  list, but  if user wants to access it, then can access directly.

- If any method/variable defined with double underscore as prefix, then the method name will not
  show in suggestion list, and direct access is not possible, user has to follow below pattern
  _<classname>__method/variable name.



"""

class Car:
    def __init__(self, comp, car_name, car_price):
        self.company = comp
        self._car_name = car_name
        self.__car_price = car_price

    def show_company_name(self):
        print(f"Company name : {self.company}")

    def _show_car_name(self):
        print(f"Car name : {self._car_name}")
        self.__show_car_price()

    def __show_car_price(self):
        print(f"Car price : {self.__car_price}")


if __name__ == "__main__":
    obj = Car("TATA", "Nexon", "10 Lac")
    obj.show_company_name()
    obj._show_car_name()
    obj._Car__show_car_price()
