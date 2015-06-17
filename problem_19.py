import datetime

__author__ = 'Tiger'

start_date = datetime.date(1901, 1, 1)
current_date = start_date
end_date = datetime.date(2000, 12, 31)
counter = 0
while current_date < end_date:
    if current_date.weekday() == 6 and current_date.day == 1:
        counter += 1
        print(current_date)
    current_date = current_date + datetime.timedelta(days=1)

print(counter)