from datetime import datetime
from quiz.models import Score

def days_developed(request):
    startDevDate = datetime(2024, 9, 4)
    todaysDate = datetime.now()
    daysDeveloped = (todaysDate - startDevDate).days
    days = "days"
    
    if daysDeveloped <= 1:
        days = "day"

    return {
        "daysDeveloped": daysDeveloped,
        "days": days,
    }

def top_five_scores(request):
    score_list = Score.objects.all().order_by('-score')[:5]
    return {
        "score_list": score_list
    }
