import json
import sys
from utils import setFilterOptions

if __name__=="__main__":
    json_file = open('reviews.json', "r", encoding='utf-8-sig')
    json_data = json.load(json_file)

    prioritize_by_text = True
    HIGHEST_FIRST = True
    LOWEST_FIRST = False
    rating = HIGHEST_FIRST
    NEWEST_FIRST = True
    OLDEST_FIRST = False
    date = OLDEST_FIRST
    minimum_rating = 3

    args = sys.argv[1:]
    if len(args)==4:
        minimum_rating, rating, text, date = setFilterOptions(args)

