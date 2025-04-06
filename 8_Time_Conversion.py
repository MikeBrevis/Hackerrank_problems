s= "12:00:00PM"

hour = s[0:2]
min = s[3:5]
seg = s[6:8]
day_time = s[8:]

if day_time == "PM" and hour != str(12):
    new_hour = int(hour) + 12
    hour = new_hour

elif day_time == "AM" and hour == str(12):
    new_hour = int(hour) - 12
    hour = str(new_hour).zfill(2)
    
military_time = f"{hour}:{min}:{seg}"
print(military_time)
    
