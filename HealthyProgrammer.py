#Healthy Pragrammer
#9am - 5am.
#drinking water 3.5 liter during his duty.
#eye exercise every 30 minutes.
#physical activity every every 40 minutes.
# water mp3 file will be play every 40 minutes.
#Rules
#import mixer from pygame
#import time from time
#import datetime from datetime
from time import time
from pygame import mixer # pip install pygame
from datetime import datetime
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user =  input()
        if input_of_user  == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with  open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_secs = 40*60
    eye_secs = 30*60
    exercise_secs = 45*60
    while True:
        if time() -init_water >water_secs:
            print("Water Drinking Time.Enter 'stop' to stop the alarm")
            musiconloop("water.mp3","stop")
            init_water = time()
            log_now("Drank Water at")
        if time() -init_eyes >eye_secs:
            print("Eye exercise Time.Enter 'doneeyes' to stop the alarm")
            musiconloop("eyes.mp3","doneeyes")
            init_eyes = time()
            log_now("Eyes Relaxed at")
        if time() -init_exercise > exercise_secs:
            print("Physical Activity Time.Enter 'donephy' to stop the alarm")
            musiconloop("physical.mp3","donephy")
            init_eyes = time()
            log_now("Physical Activity Done at")




