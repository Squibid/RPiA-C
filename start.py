import pygame
import time
import dbus
import audioread 

snoozeTimes=5 #amount of times to snooze (including initial run)
snoozeSleep=2 #stored in seconds (time between runs)
alarmVolume=0.9 #alarm volume
pygame.init() #start pygame
pygame.mixer.init() 
alarmName = pygame.mixer.Sound('beep.mp3') #sets alarm name
alarmName.set_volume(alarmVolume) #sets the volume based on the above variable

def durationDetector(length):
    seconds = length
    return seconds
with audioread.audio_open(alarmName) as f:
    totalsec = f.duration

#alarm clock notification variables
notificationName='bean'
notificationDefinition='cheese'
notificationTime=((round(totalsec)*snoozeTimes)+(snoozeSleep*(snoozeTimes-1)))*1000

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
            alarmName.play()
            time.sleep(snoozeSleep)
    except:
        print('')
