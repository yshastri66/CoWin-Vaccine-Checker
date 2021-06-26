import time
import datetime
from get_api_check import find_availability


def main():
    pincodes = list(map(str, input("Enter the pincodes with space separation: ").split()))

    t = int(input("Enter the frequency with which the code should check in the website: (>=15 seconds) "))
    t = 15 if t < 15 else t

    wa_number = "+91" + input("Enter the whatsapp number to which you want to send notification: ")
    if len(wa_number)!=13:
        print("Invalid mobile number. Try Again")
        exit(0)

    n = int(input("Enter number of times you want to check: "))
    if n<1:
        print("Enter valid repetition number")
        exit(0)

    while n:
        day = datetime.datetime.now()
        print(f"\nChecking at : {day.hour % 12}:{day.minute}:{day.second}s")
        date = str(day.day + 1) + "-" + str(day.month) + "-" + str(day.year)
        for pin in pincodes:
            URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin}&date={date}'
            find_availability(URL, pin, wa_number)

        time.sleep(t)
        n -= 1


if __name__ == '__main__':
    main()
