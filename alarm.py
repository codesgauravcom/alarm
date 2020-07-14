import time
import winsound

def timer(minutes):
    print(f'alarm will go off in {minutes} minutes.')
    time.sleep(minutes * 60)
    frequency=  2500
    duration = 1000
    winsound.Beep(frequency,duration)
if __name__ =="__main__":
    minutes = int(input('mins to alarm'))
    timer(minutes)    