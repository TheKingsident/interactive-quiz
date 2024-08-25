from datetime import datetime

def days_developed(request):
    startDevDate = datetime(2024, 8, 22)
    todaysDate = datetime.now()
    daysDeveloped = (todaysDate - startDevDate).days
    days = "days"
    
    if daysDeveloped <= 1:
        days = "day"

    return {
        "daysDeveloped": daysDeveloped,
        "days": days,
    }
