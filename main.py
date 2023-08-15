import time
def timeDown(time_sec):
   while time_sec:
        mins, secs = divmod(time_sec, 60)
        result = "{:02d}: {:02d}".format(mins, secs)
        print(result)
        time.sleep(1)
        time_sec -=1
   print("stop")

time_sec = input("enter min: ")
timeDown(int(time_sec))





