# import time 
# import datetime
# # You can also get the current date and time using datetime.now() or datetime.today().
# # x=datetime.datetime.now()
# # x=datetime.datetime.today()
# # x=datetime.datetime(2025,1,4,14,30,0)#year,month,day,hour,minute,second
# # print(x)

# x=datetime.date(2025,1,4)#year,month,day

# import datetime
# dt1 = datetime.datetime(2025, 1, 4, 14, 30)
# dt2 = datetime.datetime(2025, 1, 5, 16, 30)
# delta = dt2 - dt1  # Difference between the two dates
# print(delta)

from datetime import date
from datetime import timedelta
today=date.today()
print("Today's date is =",today)    
after_5_days=timedelta(days=5)# only days modification is allowed no month and year modification is possible
new_date=today+after_5_days
print("After 5 days date is =",new_date)



