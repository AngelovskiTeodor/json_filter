import json

if __name__=="__main__":
    json_file = open('reviews.json', "r", encoding='utf-8-sig')
    json_data = json.load(json_file)

    
