import requests, threading

url = "http://127.0.0.1:8000"
count = 0
interval_flag = True

def change_flag():
    global interval_flag, count
    count = 0
    interval_flag = True
    print("completed 60 sec interval")
    print("ok")
    

class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def check_interval():
    timer = RepeatTimer(60, change_flag)
    timer.start()


def get_request():
    global count, interval_flag

    if count >= 6:
        interval_flag = False
    while not interval_flag:
        continue
    count += 1
    print("request_sent", count)
    r = requests.get(url = url)
    return r


