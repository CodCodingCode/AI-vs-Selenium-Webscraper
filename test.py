from datetime import datetime

day = str(datetime.now())
important, not_important = day.split(" ")
year, month, day = important.split("-")
print(year, month, day)

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month = months[month]