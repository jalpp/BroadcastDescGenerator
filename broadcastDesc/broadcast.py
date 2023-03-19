
import datetime
import pytz


def main():
    print("------ Lichess Description Generator -------- \n\n")
    print("    ----")
    print("   /  .\_")
    print("   |   ___)")
    print("   |   \|")
    print("   |  =  |")
    print("   /_____\|")
    print("   [_______]")
    print("\n ----------------------------------")
    name = input('Enter Tournament Name \n')
    playercount = input('Enter Tournament Player count \n ')
    location = input("Enter Tournament Location \n")
    rounds = input("Enter Tournament Rounds \n")
    format = input("Enter Tournament format(swiss-round robin) \n")
    timecontrol = input(
        "Enter Tournament time control(Rapid,Blitz,Classical,etc) \n")
    monthStart = input("Enter Tournament Start Month [Feb/Mar/Jan etc] \n")
    startDate = input("Enter Tournament start Date [1,2,20 etc] \n")
    monthEnd = input("Enter Tournament end Month [Feb/Mar/Jan etc] \n")
    endDate = input("Enter Tournament end Date [1,2,20 etc] \n")
    isOneDay = input("Is Tournament one day duration? [Y/N] \n")
    extra = input("Enter extra info: time per move, markdowns etc \n\n")
    target_timezone = input(
        f"Enter the Tournament time zone (e.g. 'Europe/London'): ")
    user_timezone = input("Enter your current time zone (e.g. 'US/Pacific'): ")

    if (isOneDay == "Y" or (monthStart == monthEnd and startDate == endDate)):
        print("--------Your short Description:---------- \n")
        print(broadcastStylingShort(rounds, format, timecontrol,
              monthStart, startDate, monthEnd, endDate, True))
        print("\n --------Your long description:----------")
        print(broadcastStylingLong(name, playercount, location, extra, rounds, format,
              timecontrol, monthStart, startDate, monthEnd, endDate, True))
    else:
        print("---------Your short Description:------------- \n")
        print(broadcastStylingShort(rounds, format, timecontrol,
              monthStart, startDate, monthEnd, endDate, False))
        print("\n-------- Your long description--------------")
        print(broadcastStylingLong(name, playercount, location, extra, rounds, format,
              timecontrol, monthStart, startDate, monthEnd, endDate, False))

    print('\n\n ------Rounds Time to your Time zone converter-----')
    calculatetz(user_timezone, target_timezone, rounds)


def dateMapping(date):

    val = int(date)

    if (val == 1 or val == 21 or val == 31):
        return '{}{}'.format(val, 'st')
    elif (val == 2 or val == 22):
        return '{}{}'.format(date, 'nd')
    elif (val == 3 or val == 23):
        return '{}{}'.format(date, 'rd')
    else:
        return '{}{}'.format(date, 'th')


def broadcastStylingShort(round, format, timecontrol,  startMonth, startDate, endMonth, endDate, isOneDay):
    if (isOneDay == True):

        return '{} {} | {}-round {} | {} time control'.format(startMonth, dateMapping(startDate), round, format, timecontrol)
    elif (startMonth == endMonth and startDate != endDate):

        return '{} {} - {} | {}-round {} | {} time control'.format(startMonth, dateMapping(startDate), dateMapping(endDate), round, format, timecontrol)
    else:
        return '{} {} - {} {} | {}-round {} | {} time control'.format(startMonth, dateMapping(startDate), endMonth, dateMapping(endDate), round, format, timecontrol)

# def broadcastStylingLong(name, rounds, startDate, )


def broadcastStylingLong(name, playercount, location, extra, round, format, timecontrol,  startMonth, startDate, endMonth, endDate, isOneDay):
    if (format == "SWISS" or format == "Swiss" or format == "swiss"):
        if (isOneDay == True):
            return 'The {} is a {}-round {} tournament held on the {} of {} in {} \n\n {} \n [Offical Website]() | [Results]()'.format(name, round, format, startDate, startMonth, location, extra)
        elif (startMonth == endMonth and startDate != endDate):
            return 'The {} is a {}-round {} tournament held from the {} to the {} of {} in {} \n\n {} \n [Offical Website]() | [Results]()'.format(name, round, format, startDate, endDate, startMonth, location, extra)
        else:
            return 'The {} is a {}-round {} tournament held from the {} {} to the {} {} in {} \n\n {} \n [Offical Website]() | [Results]()'.format(name, round, format, startDate, startMonth, endDate, endMonth, location, extra)
    else:
        if (isOneDay == True):
            return 'The {} is a {}-player {} tournament held on the {} of {} in {} \n\n {} \n [Offical Website]() | [Results]()'.format(name, playercount, format, startDate, startMonth, location, extra)
        elif (startMonth == endMonth and startDate != endDate):
            return 'The {} is a {}-player {} tournament held from the {} to the {} of {} in {} \n\n {} \n [Offical Website]() | [Results]()'.format(name, playercount, format, startDate, endDate, startMonth, location, extra)
        else:
            return 'The {} is a {}-player {} tournament held from the {} {} to the {} {} in {} \n\n {} \n [Offical Website]() | [Results]()'.format(name, playercount, format, startDate, startMonth, endDate, endMonth, location, extra)


def calculatetz(user_timezone, target_timezone, rounds):

    for i in range(int(rounds)):

        target_date = input(
            f"Enter the Round {i + 1} date in the Tournament time zone (e.g. '2023-03-19'): ")
        target_time = input(
            f"Enter the Round {i + 1} time in the Tournament time zone (e.g. '12:00 PM'): ")

        target_datetime_str = f"{target_date} {target_time}"
        target_datetime = datetime.datetime.strptime(
            target_datetime_str, "%Y-%m-%d %I:%M %p")

        target_timezone_obj = pytz.timezone(target_timezone)

        target_datetime_tz = target_timezone_obj.localize(target_datetime)

        user_timezone_obj = pytz.timezone(user_timezone)
        user_datetime_tz = target_datetime_tz.astimezone(user_timezone_obj)

        user_date_str = user_datetime_tz.strftime("%Y-%m-%d")
        user_time_str = user_datetime_tz.strftime("%I:%M %p")
        print(
            f"The target date and time in your time zone is: {user_date_str} {user_time_str}")


main()
