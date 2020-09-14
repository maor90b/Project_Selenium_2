from datetime import datetime

today = datetime.today().month
print(today)

mydate = datetime.now()
month = mydate.strftime("%B")

print(month[0:3])