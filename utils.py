def setFilterOptions(args):
    minimum_rating = int(args[0])
    rating = True if args[1].upper()=="HIGHEST" else False
    text = True if args[2].upper()=="YES" else False
    date = True if args[3].upper()=="NEWEST" else False

    return minimum_rating, rating, text, date

