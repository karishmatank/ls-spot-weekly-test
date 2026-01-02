import config
from datetime import datetime, date
import requests
from w2m import generate_slack_thread_content
import time

PREFIX_LEN = 2

def post_to_slack(additional_data):
    """Trigger the actual post to Slack"""
    data = {
        "token": config.slack_bot_token,
        "channel": config.channel_id
    }
    data.update(additional_data)

    response = requests.post(config.post_message_endpoint, data=data)
    response_json = response.json()

    if not response_json.get('ok'):
        raise RuntimeError(f"Failed: {response_json}")

    return response_json

def get_conversation_history():
    """Get messages sent today in the channel."""
    t = date.today()
    dt = datetime(t.year, t.month, t.day)

    headers = {
        "Authorization": f"Bearer {config.slack_bot_token}"
    }

    data = {
        "channel": config.channel_id,
        "oldest": dt.timestamp()
    }

    response = requests.get(config.get_history_endpoint, headers=headers, params=data)
    response_json = response.json()

    if not response_json.get('ok'):
        raise RuntimeError(f"Failed: {response_json}")
    
    return response_json['messages']

def get_assessment_course_num(course_num):
    """Generate assessment course number"""
    if course_num in ['101', '110', '120', '130', '225', '230', '240', '250']:
        # Assessment number ends in 9
        return course_num[:-1] + '9'
    elif course_num in ['170', '180', '210']:
        return course_num[:-1] + '1'
    elif course_num == '215':
        return '216'
    else:
        return ""

def generate_slack_parent_content():
    """Generate content for parent posts on Slack"""
    posts = {}

    for course in config.courses:
        prefix = course[:PREFIX_LEN]
        number = course[PREFIX_LEN:]

        assessment_number = get_assessment_course_num(number)
        icon = config.icons[prefix]

        posts[course] = f"Reminder: {icon} {prefix} {number}-{assessment_number} Study Session: Sign Up Here!"
    
    return posts

def has_manually_posted():
    """Check to see if the app has already posted today, likely due to someone triggering a manual posting"""
    messages_today = get_conversation_history()

    for message in messages_today:
        if message.get('app_id') == config.slack_app_id:
            return True
    return False

def posts_all_courses():
    """Post all Slack content if there has not been a manual or scheduled posting yet today."""
    if has_manually_posted():
        return

    parent_content = generate_slack_parent_content()
    thread_content = generate_slack_thread_content()

    for course in config.courses:
        parent = post_to_slack({
            "text": parent_content[course]
        })

        thread_ts = parent['ts']

        post_to_slack({
            "text": thread_content[course],
            "thread_ts": thread_ts
        })

        time.sleep(2)

if __name__ == '__main__':
    posts_all_courses()