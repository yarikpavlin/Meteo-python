from Whether import Whether
from datetime import datetime as dt
import time
import os
import threading
from mail import Gmail


station = Whether()


def discover(interval=10):
    while True:
        currentHour = dt.now().strftime("%H:%M")
        f = open('statistics.txt', 'a')
        station.get_data()
        data = station.get_string()
        f.write('{} -> {};\n'.format(dt.now().strftime("%b %d %Y %H:%M:%S"), data))
        print("Notes create: {}".format(dt.now().strftime("%H:%M:%S")))
        f.close()
        send_email(currentHour)
        time.sleep(60 * interval)


def send_email(currentHour):
    g = Gmail("email", "password")
    if currentHour.split(":")[1] == "00" or currentHour.split(":")[1] == "30":
        last_result = os.popen('cat statistics.txt | tail -6').read()
        g.send_message('MeteoInfo', str(last_result))
    else:
        print("It's early for sending report")


if __name__ == '__main__':
    while True:
        currentHour = dt.now().strftime("%H:%M")
        if currentHour.split(":")[1].endswith("0"):
            print('Start app..')
            discover(10)
            break
        else:
            print('Waiting for start..')
            time.sleep(60)
