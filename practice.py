def increment(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
 
    if time.minute >= 60:
        time.minute -=60
        time.hour += 1
        
 def time_to_int(time):
     minutes = time.hour * 60 + time.minutes
     seconds = minutes * 60 + time.second
     return seconds
