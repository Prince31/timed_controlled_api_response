import requests, threading

url = "http://127.0.0.1:5000"


def send_request(count):
    print("client request sent")
    r = requests.get(url = url)
    count += 1
    print(r.text)
    print(f"client receive count {count}")

for i in range(10):
    t = threading.Timer(0.0, send_request, (i,))
    t.start()
    # send_request(i)