import requests
import datetime

def find_questions(from_date, tag):
    headers = {'Content-Type': 'application/json'}
    params = {
        'page': 1, 'pagesize': 100, 'fromdate': from_date, 'tagged': tag,
        'order': 'asc', 'sort': 'creation', 'site':'stackoverflow'
     }
    url = "https://api.stackexchange.com/2.3/search"
    len_list = 100
    while len_list == 100:
        r = requests.get(url, headers=headers, params=params)
        for inem in r.json()['items']:    
            print(inem['title'])
        params['page'] += 1
        len_list = len(r.json()['items'])

if __name__ == '__main__':
    days_before = 1
    tag = 'python'
    from_date = (datetime.datetime.today() - datetime.timedelta(days=days_before)).strftime("%Y-%m-%d")
    find_questions(from_date, tag)