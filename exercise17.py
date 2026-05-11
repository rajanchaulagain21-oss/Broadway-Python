#countdown timer 

import time


user_input = int(input("enter time in second for timer to start: "))

for x in range(user_input,-1,-1):
    hour = x // 3600
    minute = (x %3600) // 60
    second = x % 60
    print(f"Countdown timer : {hour:02}::{minute:02}::{second:02}",end="\r", flush=True)
    time.sleep(1)

print("\n Ding! Time's up \a")