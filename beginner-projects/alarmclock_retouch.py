from datetime import datetime
from playsound import playsound
alarm_time = str(input('Enter the time of the alarm to be set:- HH:MM:SS:AM/PM\n')).upper()
setted_alarm = alarm_time.split(':')
print('setted alart: ', setted_alarm)
while True:
    now = datetime.now()
    current_time_format = now.strftime("%I:%M:%S:%p")
    current_time = current_time_format.split(':')
    print(current_time_format)
    if(alarm_time == current_time_format):
        print('wake up')
        playsound('audio.mp3')
        break

