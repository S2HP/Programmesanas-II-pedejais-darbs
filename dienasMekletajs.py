def find_day(this_year, this_month, this_day, this_date, bday_month, bday_year, bday_date):
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 30, 31]
    dayNames = ["nothing", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    # Skaita cik dienas ir pagājušas.
    daysGoneBy = 0
    yearsGoneBy = this_year-bday_year

    if bdayPassed(this_month, this_date, bday_month, bday_date) == False:
        yearsGoneBy -=1
    daysGoneBy += 365*yearsGoneBy

    leapYear = 0
    test_year_start = bday_year
    if bdayPassed(bday_month, bday_date, 2, 29):
        test_year_start +=1
    
    
    test_year_end = this_year
    if bdayPassed(bday_month, bday_date, 2, 29) == False:
        test_year_end = this_year-1


    for year in range(bday_year, this_year+1, 1):
        if year % 4 == 0:
            leapYear +=1
        if year % 100 == 0 and year % 400 != 0:
            leapYear -=1
    
    daysGoneBy += leapYear

    if this_month>bday_month:
        full_months = this_month-bday_month
    else:
        full_months = this_month+12-bday_month

    if bdayPassed(1, this_date, 1, bday_date) == False:
        full_months -= 1

    daysinMonth = 0

    if this_date>=bday_date:
        extra_days = this_date-bday_date
    else:
        extra_days = this_date + daysinMonth[this_month-1] - bday_date

    daysGoneBy += extra_days

    print("Kopš dzimšanas ir pagājušas: ", daysGoneBy, "dienas.")

    spareDays = daysGoneBy % 7

    bday_day = this_day-spareDays

    if bday_day <=0:
        bday_day +=7

    print("Jums ir ", yearsGoneBy, "gadi, ", full_months, "menesi un ", extra_days, " dienas")

    return dayNames[bday_day]

def bdayPassed(this_month, this_date, bday_month, bday_date):
    if this_month>bday_month:
        return True
    if this_month<bday_month:
        return True
    if this_date<bday_date:
        return False 
    return True


dz_g = int(input("Lūdzu ievadiet savu dzimšanas gadu!:"))
dz_m = int(input("Lūdzu ievadiet savu dzimšanas mēnesi!:"))
dz_d = int(input("Lūdzu ievadiet savu dzimšanas datumu!:"))
sis_g = int(input("Lūdzu ievadiet pašreizējo gadu!:"))
sis_m = int(input("Lūdzu ievadiet pašreizējo mēnesi!:"))
sis_d = int(input("Lūdzu ievadiet pašreizējo datumu!:"))
sis_n = int(input("Lūdzu ievadiet pašreizējo nedēļas dienu!:"))

print(find_day(sis_g, sis_m, sis_d, sis_n, dz_g, dz_m, dz_d))