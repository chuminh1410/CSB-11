from datetime import datetime

now = datetime.now()
date_string = now.strftime('%d/%m/%Y')
time_string = now.strftime('%H:%M:%S')

print("Today is", date_string)
print("Time right now:", time_string)
