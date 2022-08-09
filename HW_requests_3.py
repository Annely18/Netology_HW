from datetime import datetime
import time
import datetime

import requests


    # Задача 3

def two_day_questions():
    todate = int(time.time())
    fromdate = todate - 172800
    params = {'site' : 'stackoverflow', 'tagged' : 'Python', 'fromdate' : fromdate, 'todate' : todate, 'sort' : 'creation'}
    url = 'https://api.stackexchange.com/2.3/questions'
    response = requests.get(url=url, params=params)
    for data in response.json()['items']:
        print(data['question_id'], datetime.datetime.fromtimestamp(data['creation_date']), data['title'], data['tags'])


two_day_questions()
