daysOfTheMonth = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def findDay (thisYear, thisMonth, thisDate, thisDay, bdayYear, bdayMonth, bdayDate):
    dienu_nosaukumi = ["nekas", "pirmdiena", "otrdiena", "trešdiena", "ceturtdiena", "piektdiena", "sestdiena", "svētdiena"]
    
    daysGoneBy = 0
    yearsPassed = thisYear-bdayYear

    if hasBdayPassed(thisMonth, thisDate, bdayMonth, bdayDate) == False:
        yearsPassed -=1

    daysGoneBy += 365*yearsPassed

    leapYear = 0
    startYear = bdayYear
    if hasBdayPassed(bdayMonth, bdayDate, 2, 29):
        startYear +=1

    endYear = thisYear

    if hasBdayPassed(thisMonth, thisDate, 2, 29) == False:
        endYear -=1

    for gads in range(startYear, endYear+1):
        if gads % 4 == 0:
            leapYear +=1
        if gads % 100 == 0 and gads % 400 != 0:
            leapYear -=1

    daysGoneBy += leapYear

    if thisMonth>=bdayMonth:
        fullMonths = thisMonth-bdayMonth
    else:
        fullMonths = thisMonth+12-bdayMonth

    if hasBdayPassed(1, thisDate, 1, bdayDate) == False:
        fullMonths = fullMonths - 1

    daysinMonth = 0
    month = bdayMonth
    while month != thisMonth:
        daysinMonth += daysOfTheMonth[month]
        month +=1
        if month == 13:
            month=1
    daysGoneBy += daysinMonth
    if thisDate>=bdayDate:
        extraDays = thisDate-bdayDate
    else:
        extraDays = thisDate + daysOfTheMonth[thisMonth-1] - bdayDate
    daysGoneBy += extraDays
    print("Kopš dzimšanas ir pagājušas: ", daysGoneBy, " dienas.")
    daysLeft = daysGoneBy % 7
    bdayDay = thisDay-daysLeft
    if bdayDay <=0:
        bdayDay +=7
    print("Jums ir ", yearsPassed, " gadi, ", fullMonths, " mēneši un ", extraDays, " dienas")
    return dienu_nosaukumi[bdayDay]


def hasBdayPassed(monthNow, dateNow, monthCompare, dateCompare):
    if monthNow>monthCompare:
        return True
    if monthNow<monthCompare:
        return False
    if dateNow>dateCompare:
        return True
    return False
    
def dataCheck(bdayYear, bdayMonth, bdayDate, thisYear, thisMonth, thisDate, thisDay):
    correctData = True

    if bdayYear > thisYear:
        correctData = False
    elif bdayYear == thisYear and bdayMonth > thisMonth:
        correctData = False
    elif bdayYear == thisYear and bdayMonth == thisMonth and bdayDate > thisDate:
        correctData = False
    elif bdayYear == thisYear and bdayMonth == thisMonth and bdayDate == thisDate:
        correctData = False


    if bdayYear<=0 or bdayMonth<=0 or bdayDate<=0 or thisYear<=0 or thisMonth<=0 or thisDate<=0 or thisDay<=0:
        correctData = False

    if bdayMonth > 12 or thisMonth > 12:
        correctData = False
    else:
        if (bdayYear % 4) == 0 or (thisYear % 4) == 0:
            if bdayYear == 2 or bdayYear == 2:
                if bdayDate > (daysOfTheMonth
            [bdayMonth]+1) or thisMonth > (daysOfTheMonth
            [thisMonth]+1):
                    correctData = False
        if bdayDate > daysOfTheMonth[bdayMonth] or thisMonth > daysOfTheMonth[thisMonth]:
            correctData = False
    
    if not correctData:
        print("Nepareizi ievades dati!")
    return correctData

    


answer = "y"
while answer == "y":
    bdayDate = input('Lūdzu ievadi savu dzimšanas datumu YYYY-MM-DD: ').split('-')
    thisDate = input('Lūdzu ievadi pašreizējo datumu YYYY-MM-DD: ').split('-')
    thisDayOfTheWeek = int(input("Lūdzu ievadiet pašreizējo nedēļas dienu (skaitlī):"))
    flag = False
    amountDate = False
    if len(bdayDate) != 3 or len(thisDate) != 3:
        amountDate = True
    if not amountDate:
        for i in range(len(bdayDate)):
            try:
                int(bdayDate[i])
                int(thisDate[i])
                int(thisDayOfTheWeek)
            except ValueError:
                flag = True
    if not flag and not amountDate:
        if dataCheck(int(bdayDate[0]), int(bdayDate[1]), int(bdayDate[2]), int(thisDate[0]), int(thisDate[1]), int(thisDate[2]), thisDayOfTheWeek):

            print(findDay(int(thisDate[0]), int(thisDate[1]), int(thisDate[2]), thisDayOfTheWeek, int(bdayDate[0]), int(bdayDate[1]), int(bdayDate[2])))
    else:
        print("Nepareizi ievades dati!")
    answer = input("Vai mēģināt vēlreiz? ('y'/'n')")