import re
import requests
from datetime import datetime, date, timedelta
import time
import config

def get_form_dates(start_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    date_range = [start + timedelta(days=x) for x in range(0, 7)]

    return "|".join([d.strftime("%Y-%m-%d")for d in date_range])

def post_form(title, dates_str):
    data = {
        'NewEventName': title,
        'DateTypes': 'SpecificDates',
        'PossibleDates': dates_str,
        'NoEarlierThan': '4',
        'NoLaterThan': '0',
        'TimeZone': 'America/New_York',
    }

    # response = requests.post(config.new_event_endpoint, cookies=cookies, headers=headers, data=data)
    response = requests.post(config.new_event_endpoint, headers=config.headers, data=data)
    
    try:
        # Tag looks like this in response: <body onload="window.location='./?34071889-83eWy'">, ID is 34071889-83eWy
        w2m_id = re.search(r'window\.location=\'\.\/\?([a-zA-Z0-9-]+)', response.text).group(1) # Get parenthesized subgroup
    except Exception as e:
        print(response.text)
        raise e

    return w2m_id

def format_and_log(links):
    *bulk_course_keys, last_course_key = config.courses

    for title in bulk_course_keys:
        links[title] = config.bulk_desc + links[title]
    links[last_course_key] = config.last_desc + links[last_course_key]

    for key, value in links.items():
        print(key)
        print(value)

    return links

def create_events(start_date):
    links = {}
    dates_str = get_form_dates(start_date)

    for title in config.courses:
        w2m_id = post_form(title, dates_str)
        links[title] = f"{title}: https://www.when2meet.com/?{w2m_id}"
        time.sleep(2)

    return links

def get_next_sunday():
    today = date.today()

    # Sunday is 6 in weekday(): Monday is 0, Sunday is 6
    days_ahead = 6 - today.weekday()
    next_sunday = today + timedelta(days=days_ahead)
    return next_sunday.strftime("%Y-%m-%d")

def generate_slack_thread_content():
    sunday = get_next_sunday()
    links = create_events(sunday)
    return format_and_log(links)
    
if __name__ == '__main__':
    generate_slack_thread_content()
