import pywhatkit


def send_message(a, h, m, wa_number):
    pywhatkit.sendwhatmsg(wa_number, text(a), h, m + 1, wait_time=15)


def text(a):
    message = f"Vaccine available at: {a[0]}\nPincode: {a[1]}\n" \
              f"Vaccine name: {a[2]}\nAvailable doses: {a[3]}\n" \
              f"Book at : https://www.cowin.gov.in/home"
    return message
