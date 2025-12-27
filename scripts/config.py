import os
from dotenv import load_dotenv

load_dotenv() # Load .env file

# Courses
# courses = [
#     'RB101',
#     'RB110',
#     'RB120',
#     'RB130',
#     'JS101',
#     'JS110',
#     'JS120',
#     'JS130',
#     'PY101',
#     'PY110',
#     'PY120',
#     'PY130',
#     'LS170',
#     'RB175',
#     'JS175',
#     'PY175',
#     'LS180',
#     'JS210',
#     'LS215',
#     'JS225',
#     'JS230',
#     'TS240',
#     'LS250'
# ]

courses = [
    'RB101',
    'RB110',
    'LS250'
]

# Post content
bulk_desc = "If interested in attending a session, please provide your availability and let us know by commenting here so that a spot lead can take this session. If a lead isn't available by mid-week, it is advised that everyone pair up. Students must follow the LS code of conduct.\n\n"
last_desc = "Congrats! You made it! Since this is the last course, we don't have any qualified leads to host sessions. But feel free to use this When2Meet to coordinate with other students in the course!\n\n"

# W2M
new_event_endpoint = 'https://www.when2meet.com/SaveNewEvent.php'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.when2meet.com',
    'priority': 'u=0, i',
    'referer': 'https://www.when2meet.com/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1497556288.1766671381; _gcl_au=1.1.560636778.1766671381; PHPSESSID=dvr66hr4pon7h1ncv7vsa8b2kd; __gads=ID=ba1e5d0a76b6534e:T=1766671381:RT=1766780225:S=ALNI_MYs0NDa_7bJYs21jZB44OXGGKE--Q; __gpi=UID=0000131fc4426a71:T=1766671381:RT=1766780225:S=ALNI_Ma88Wzvi2EepaM0QqPYSY9JWs9clA; __eoi=ID=4e2651b1bfff0455:T=1766671381:RT=1766780225:S=AA-AfjZeSt8-kfsgsyxqIhc9dq3p; _fbp=fb.1.1766780268967.631677324912250444; _ga_3L5STP8FEF=GS2.1.s1766780225$o2$g1$t1766780455$j58$l0$h0; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22a3898237-0151-444a-b959-33f21c035f01%5C%22%2C%5B1766671381%2C605000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol9ZiUI5xHI66CuLJvZqVmsORZWxQZ9iX3lLrYW96IgYEDAJKdBQDJmpvog37y1PCi8VMVVwtz6DhXKYIpc-deHawR-FbmH7AldA2tSxxYLznFd_Cnvtdkl4RAa9X1UjU9MWRh8cif7SSfWqGgHW7pogzWnBeQ%3D%3D%22%5D%5D',
}

# Slack
post_message_endpoint = "https://slack.com/api/chat.postMessage"
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
channel_id = os.environ["SLACK_CHANNEL_ID"]
icons = {
    'RB': ':ruby:',
    'JS': ':js:',
    'PY': ':py:',
    'LS': ':ls:',
    'TS': ':typescript:',
}

