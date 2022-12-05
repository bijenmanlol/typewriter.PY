#Typewriter.PY
#By drooler (https://drooler.tk/)

#imports

import time, random, sys, os

#project definition standard

Pdefine = False

#color functions

def fg(r,g,b):
  return f'\033[38;2;{r};{g};{b}m'

def bg(r,g,b):
  return f"\033[48;2;{r};{g};{b}m"

#color codes

color_red = fg(242,78,78)
color_orange = fg(255,168,5)
color_yellow = fg(249,255,89)
color_lightgreen = '\033[92m'
color_green = fg(54,200,99)
color_lightblue = '\033[94m'
color_blue = '\033[34m'
color_purple = fg(151,71,255)
color_brown = fg(190,140,100)
color_black = fg(0,0,0)
color_silver = fg(191,191,191)

bcolor_red = bg(255,0,69)
bcolor_orange = bg(255,100,0)
bcolor_yellow = bg(255,255,0)
bcolor_lightgreen = '\033[102m'
bcolor_green = bg(54,150,50)
bcolor_lightblue = '\033[104m'
bcolor_blue = '\033[44m'
bcolor_purple = bg(151,50,250)
bcolor_brown = bg(190,100,77)
bcolor_silver = bg(163,163,163)

#text markup

bold = '\033[1m'
dim = '\033[2m'
italic = '\033[3m'
underline = '\033[4m'
reverse = '\033[7m'
invisible = '\033[8m'
crossover = '\033[9m'
reset = '\033[0m'

#warning print function

def warn_print(error: str):
    print(color_red + error + reset)

#clear console

def clear():
    os.system('cls')

#define project settings

def define(smooth: bool, speed: int = None):
    global Pdefine
    Pdefine = True
    if smooth:
        if speed is None:
            speed = 0.05
        global Psmooth
        Psmooth = True
        global Pspeed
        Pspeed = speed
    else:
        if speed is not None:
            warn_print('|Typewriter ERROR| Speed can not be defined while the smooth argument is False')
            sys.exit()
        Psmooth = False

#main type function

def type(input: str, smooth: bool = None, speed: int = None):
    if Pdefine and smooth is None and speed is None:
        if Psmooth:
            for i in range(len(input)):
                sys.stdout.write(input[i])
                sys.stdout.flush()
                time.sleep(Pspeed)
        else:
            for i in range(len(input)):
                sys.stdout.write(input[i])
                sys.stdout.flush()
                time.sleep(random.randint(1, 2)/20)
        print('')
    else:
        if smooth:
            if speed is None:
                speed = 0.05
            for i in range(len(input)):
                sys.stdout.write(input[i])
                sys.stdout.flush()
                time.sleep(speed)
        elif smooth is None:
                warn_print('|Typewriter ERROR| Smooth argument can not be left empty if project settings are not defined')
                sys.exit()
        else:
            if speed is not None:
                warn_print('|Typewriter ERROR| Speed can not be defined while the smooth argument is False')
                sys.exit()
            for i in range(len(input)):
                sys.stdout.write(input[i])
                sys.stdout.flush()
                time.sleep(random.uniform(1, 2)/20)
        print('')
