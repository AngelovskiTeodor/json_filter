import json
import sys
from utils import setFilterOptions, text_prioritize, prioritize_highest_rating, prioritize_newest
from review import ReviewFactory, ReviewDTO, DescriptiveReviewDTO
import cgi, cgitb

if __name__=="__main__":
    json_file = open('reviews.json', "r", encoding='utf-8-sig')
    json_data = json.load(json_file)

    HIGHEST_FIRST = True
    LOWEST_FIRST = False
    NEWEST_FIRST = True
    OLDEST_FIRST = False

    minimum_rating = 3
    rating = HIGHEST_FIRST
    prioritize_by_text = True
    date = OLDEST_FIRST

    args = sys.argv[1:]
    if len(args)==4:
        minimum_rating, rating, text, date = setFilterOptions(args)

    cgitb.enable()
    parameters = cgi.FieldStorage()
    if len(parameters)==4:
        minimum_rating = parameters.getvalue('minimum_rating', minimum_rating.__str__())
        minimum_rating = int(minimum_rating)
        rating = HIGHEST_FIRST if parameters.getvalue('rating_order').upper()=="HIGHEST" else LOWEST_FIRST
        prioritize_by_text = True if parameters.getvalue('prioritize_text').upper()=="YES" else False
        date = OLDEST_FIRST if parameters.getvalue('date_order').upper()=="OLDEST" else NEWEST_FIRST

    reviews = []
    for o in json_data:
        new_review = ReviewFactory(**o)
        reviews.append(new_review)

    reviews = filter(lambda r: (r.getRating() >= minimum_rating), reviews)
    reviews = list(reviews)
    reviews.sort(key=lambda r: (text_prioritize(prioritize_by_text ,isinstance(r, DescriptiveReviewDTO)),
                                prioritize_highest_rating(rating, r.getRating()),
                                prioritize_newest(date, r.getReviewCreatedOnDate())))

    print("Content-Type: text/html")
    print()
    for r in reviews:
        print(r)