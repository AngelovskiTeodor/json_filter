import json
import sys
from utils import setFilterOptions

if __name__=="__main__":
    json_file = open('reviews.json', "r", encoding='utf-8-sig')
    json_data = json.load(json_file)

    args = sys.argv[1:]
    if len(args)==4:
        minimum_rating, rating, text, date = setFilterOptions(args)

