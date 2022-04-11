from playsound import playsound
import time
import dbus
import audioread

snoozeTimes=5 #amount of times to snooze (including initial run)
snoozeSleep=2 #stored in seconds (time between runs)

notificationName='bean'
notificationDefinition='cheese'
alarmName='beep.mp3'

def durationDetector(length):
    seconds = length
    return seconds
with audioread.audio_open(alarmName) as f:
    totalsec = f.duration
    notificationTime=int((totalsec*snoozeTimes)+(snoozeSleep*(snoozeTimes-1))*1000)
    print(notificationTime)

item = "org.freedesktop.Notifications"
notfy_intf = dbus.Interface(
    dbus.SessionBus().get_object(item, "/"+item.replace(".", "/")), item)

def notification():
    notfy_intf.Notify(
        "", 0, "", notificationName, notificationDefinition,
        [], {"urgency": 1}, notificationTime)

def alarmRing():
    try:
        notification()
        for i in range(snoozeTimes):
            playsound('beep.mp3')
            time.sleep(snoozeSleep)
    except:
        print('')

alarmRing()
