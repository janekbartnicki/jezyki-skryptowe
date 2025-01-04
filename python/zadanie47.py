import datetime


def get_first_monday_of_week(year, week_number):
    return datetime.datetime.strptime(f"{year}-W{week_number}-1", "%Y-W%W-%w").date()


first_monday = get_first_monday_of_week(2023, 2)

print(first_monday.strftime("Mon %b %d %H:%M:%S %Y"))