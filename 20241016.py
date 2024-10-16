import requests
url='https://2023ntcu.ntcu.edu.tw/'
html= requests.get(url)
html.encoding="utf-8"

htmllist = html.text.splitlines()

n=0
keyword = "臺中"
for row in htmllist:
    if keyword in row: n+=1
print("找到{}次!".format(n))
