#import datetime

#x = datetime.datetime.now()

#(x.strftime("%x"))

from datetime import date    
age = date.today() - date(2002,10,8)
print ("Number of days old:")
print(age.days)

# days= (age.days)  
# years= days / 365  
# print("Number of years old: ");  
# print(years);  
