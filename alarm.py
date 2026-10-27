
import time
from datetime import datetime
import winsound

# Set alarm time in 24-hour format (HH:MM:SS)
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ Wake up! Your alarm is ringing!")

        # Play alarm sound 10 times
        for i in range(10):
            winsound.Beep(1000, 1000)  # Frequency, duration in milliseconds
            time.sleep(0.5)

        break

    time.sleep(1)
```
