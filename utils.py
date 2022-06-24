from datetime import datetime

def setFilterOptions(args):
    minimum_rating = int(args[0])
    rating = True if args[1].upper()=="HIGHEST" else False
    text = True if args[2].upper()=="YES" else False
    date = True if args[3].upper()=="NEWEST" else False

    return minimum_rating, rating, text, date

def text_prioritize(prioritize, value):
    if prioritize:
        return not value
    else:
        return value

def prioritize_highest_rating(prioritize, value):
    if prioritize:
        return -value
    else:
        return value
    
def prioritize_newest(prioritize, value):
    if prioritize:
        return datetime.utcnow()-value
    else:
        return value
