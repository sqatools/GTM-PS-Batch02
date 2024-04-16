from datetime import datetime
from datetime import date

var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
print(var)


var1 = date.today()
print(var1, var1.year, var1.month, var1.day)
