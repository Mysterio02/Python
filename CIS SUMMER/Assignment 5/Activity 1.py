def calculateAnnually(weekly):
    annually = 52 * weekly
    
    return annually

def calculateMonthly(weekly):
    monthly = 4 * weekly
    
    return monthly

def calculateWeekly(hours, rate):
    weekly = hours * rate
    
    return weekly

def displayResult(weekly, monthly, annually):
    print("weekly: " + str(weekly))
    print("monthly: " + str(monthly))
    print("annually: " + str(annually))

def getHours():
    print("Enter the number of hours")
    hours = int(input())
    
    return hours

def getRate():
    print("Enter rate per hour")
    rate = int(input())
    
    return rate

# Main
# Seperate functions for output, processing, and input
hours = getHours()
rate = getRate()
weekly = calculateWeekly(hours, rate)
monthly = calculateMonthly(weekly)
annually = calculateAnnually(weekly)
displayResult(weekly, monthly, annually)
