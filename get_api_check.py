import requests
import chime
import datetime
from whatsapp import send_message

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                  AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/56.0.2924.76 Safari/537.36'}


def find_availability(URL, pin, wa_number):
    result = requests.get(URL, headers=header)
    response_json = result.json()
    try:
        data = response_json["centers"]
    except:
        print(f"Invalid Pincode {pin}")
        exit(0)
    if not data:
        print(f"No centers available at {pin} pincode")

    a = []
    for each in data:
        for every in each["sessions"]:
            if (every["available_capacity"] > 0) and (every["min_age_limit"] == 18):
                a.append(each["name"])
                a.append(each["pincode"])
                a.append(every["vaccine"])
                a.append(every["available_capacity"])
                day = datetime.datetime.now()
                send_message(a, day.hour, day.minute, wa_number)
                chime.success()

    print(f"No Available Slots at {data[0]['pincode']}")
