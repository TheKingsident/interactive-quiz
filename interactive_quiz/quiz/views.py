from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    startDevDate = datetime(2024, 8, 22)
    todaysDate = datetime.now()
    daysDeveloped = (todaysDate - startDevDate).days
    days = "days"
    
    if daysDeveloped <= 1:
        days = "day"

    return render(request, 'quiz/home.html', {
        "daysDeveloped": daysDeveloped,
        "days": days
    })
