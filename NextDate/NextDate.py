def nextdate( year, month, day):
    days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1900 or year > 2025 or month < 1 or month > 12:
        return "Out of range value"
    if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0):
        days[2] += 1
    if day < 1 or day > 31:
        return "Out of range value"
    elif day > days[month]:
        return "Invalid date"
    if month == 12 and day == 31:
        return str(year+1)+"/1/1"
    elif day == days[month]:
        return str(year)+"/"+str(month+1)+"/1"
    else:
        return str(year)+"/"+str(month)+"/"+str(day+1)
