from datetime import datetime

date = "2003-04-09 12:00:00"
converted_datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
print(converted_datetime)