import datetime

#store the value in a variable called currentDate
currentDate = datetime.date.today()
print(currentDate)
print(currentDate.month)
print(currentDate.year)

#strftime allows you to specify  the date format
print(currentDate.strftime("%d %b, %Y"))
print(currentDate.strftime("%d %b, %y"))

#strptime
userInput = input("Please enter your birthdaty (mm/dd/yyyy) ")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)

days = birthday - currentDate
print(days.days)

#time
currentDate = datetime.datetime.now()
print(currentDate.minute)