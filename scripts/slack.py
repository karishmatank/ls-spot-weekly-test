import config
import requests
from w2m import generate_slack_thread_content
import time

PREFIX_LEN = 2

def post_to_slack(additional_data):
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

def get_assessment_course_num(course_num):
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
    posts = {}

    for course in config.courses:
        prefix = course[:PREFIX_LEN]
        number = course[PREFIX_LEN:]

        assessment_number = get_assessment_course_num(number)
        icon = config.icons[prefix]

        posts[course] = f"Reminder: {icon} {prefix} {number}-{assessment_number} Study Session: Sign Up Here!"
    
    return posts

def posts_all_courses():
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