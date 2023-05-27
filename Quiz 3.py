# დავაიმპორტე საჭირო მოდულები
import requests
import random
import json
import sqlite3
from win10toast import ToastNotifier

# 1 requests მოდულის 3 ფუნქცია/ატრიბუტი
resp = requests.get("https://api.tvmaze.com/shows")
status_code = resp.status_code
header = resp.headers

print(resp)
print(status_code)
print(header)

# 2 json ფორმატის მონაცემის სტრუქტურული სახით წარმოდგენა
result_json = resp.text
shows = json.loads(result_json)
shows_structured = json.dumps(shows, indent=4)

print(shows_structured)

# 3 შემთხვევითი სატელევიზიო შოუს არჩევა და მონაცემების გამოტანა (ID, ფილმის სახელი, პრემიერის თარიღი, მიმოხილვა)
random_show = random.choice(shows)
show_id = random_show["id"]
show_name = random_show["name"]
premiered = random_show["premiered"]
summary = random_show["summary"]

print(f"ფილმის სახელი: {show_name}")
print(f"პრემიერის თარიღი: {premiered}")
print(f"მიმოხილვა: {summary}")

# 4 ბაზაში "tvshows.db" ინფორმაციის შეტანა
conn = sqlite3.connect("tvshows.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS shows (name TEXT, premiered TEXT, summary TEXT)")
cur.execute("INSERT INTO shows VALUES (?, ?, ?)", (show_name, premiered, summary))

conn.commit()
conn.close()

# Windows notification
toaster = ToastNotifier()
toaster.show_toast("TV Show Information", f"ფილმის სახელი: {show_name}\nპრემიერის თარიღი: {premiered}\nმიმოხილვა: {summary}")