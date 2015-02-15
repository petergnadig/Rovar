#!/usr/bin/python

from array import array
import time, math
import os, sys, inspect

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"./Adafruit_PWM_Servo_Driver")))
if cmd_subfolder not in sys.path:
   sys.path.insert(0, cmd_subfolder)

from Adafruit_PWM_Servo_Driver import PWM

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

lent = 2
fent = 3
pihen = 4
elol = 2
hatul = 3

#Labak:
# sorszam, kozep, lent, fent, pihen
Bal1Talp  = array ("h", [ 0,360, -10, +60, +140])
Bal2Talp  = array ("h", [ 3,360, -10, +60, +140])
Bal3Talp  = array ("h", [ 5,360, -10, +60, +140])

Jobb1Talp = array ("h", [ 7,300, 180, 110, +40])
Jobb2Talp = array ("h", [ 9,300, 180, 110, +40])
Jobb3Talp = array ("h", [11,300, 180, 110, +40])

# sorszam, kozep, elol, hatul, pihen
Bal1Lab   = array ("h", [ 1,380, 70, -80, -180]) #kozep: 380
Bal2Lab   = array ("h", [ 2,360, 70, -80, -180]) #kozep: 360
Bal3Lab   = array ("h", [ 4,385, 70, -80, -180]) #kozep: 385

Jobb1Lab =  array ("h", [ 6,420, -60, 90, 170])
Jobb2Lab =  array ("h", [ 8,440, -60, 90, 170])
Jobb3Lab =  array ("h", [10,420, -60, 90, 170])


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)  # Set frequency to 60 Hz

def AFelLe(pozicio):
  pwm.setPWM(Bal1Talp[0], 0, Bal1Talp[1]+ Bal1Talp[pozicio])
  pwm.setPWM(Jobb2Talp[0], 0, Jobb2Talp[1]+ Jobb2Talp[pozicio])
  pwm.setPWM(Bal3Talp[0], 0, Bal3Talp[1]+ Bal3Talp[pozicio])
  time.sleep(1)
def BFelLe(pozicio):
  pwm.setPWM(Jobb1Talp[0], 0, Jobb1Talp[1]+ Jobb1Talp[pozicio])
  pwm.setPWM(Bal2Talp[0], 0, Bal2Talp[1]+ Bal2Talp[pozicio])
  pwm.setPWM(Jobb3Talp[0], 0, Jobb3Talp[1]+ Jobb3Talp[pozicio])
  time.sleep(1)
def AElolHatul(pozicio):
  pwm.setPWM(Bal1Lab[0], 0, Bal1Lab[1]+ Bal1Lab[pozicio])
  pwm.setPWM(Jobb2Lab[0], 0, Jobb2Lab[1]+ Jobb2Lab[pozicio])
  pwm.setPWM(Bal3Lab[0], 0, Bal3Lab[1]+ Bal3Lab[pozicio])
  time.sleep(1)
def BElolHatul(pozicio):
  pwm.setPWM(Jobb1Lab[0], 0, Jobb1Lab[1]+ Jobb1Lab[pozicio])
  pwm.setPWM(Bal2Lab[0], 0, Bal2Lab[1]+ Bal2Lab[pozicio])
  pwm.setPWM(Jobb3Lab[0], 0, Jobb3Lab[1]+ Jobb3Lab[pozicio])
  time.sleep(1)
def Alszik():
  BFelLe(fent)
  BElolHatul(hatul) 
  BFelLe(lent)
  AFelLe(fent)
  AElolHatul(pihen)
  AFelLe(lent)
  BFelLe(fent)
  BElolHatul(pihen) 
  BFelLe(pihen)
  AFelLe(pihen)
def Indul():
  AFelLe(fent)
  BFelLe(lent)
  AElolHatul(hatul)
  AFelLe(lent)
  BFelLe(fent)
  BElolHatul(hatul)
  BFelLe(lent)

Indul()
time.sleep(3)
BFelLe(lent)
AFelLe(fent)

for i in range (0,4):
  AElolHatul(elol)
  BElolHatul(hatul)
  AFelLe(lent)
  BFelLe(fent)
  AElolHatul(hatul)
  BElolHatul(elol)
  BFelLe(lent)
  AFelLe(fent)

time.sleep(3)
Alszik()
