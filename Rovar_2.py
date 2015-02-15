#!/usr/bin/python

from array import array
import time, math, os, sys, inspect

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

pwm.setPWMFreq(60)  # Set frequency to 60 Hz

# sorszam, kozep, lent, fent, pihen, sorszam, kozep, elol, hatul, pihen
B1  = array ("h", [ 0, 350, +100, +150, 1, 450, -150, -250])
B2  = array ("h", [ 3, 350, +100, +150, 2, 450, -150, -250])
B3  = array ("h", [ 5, 350, +100, +150, 4, 515, -150, -250]) 
J1  = array ("h", [ 7, 480, -100, -150, 6, 360, +150, +230])  
J2  = array ("h", [ 9, 480, -100, -150, 8, 380, +150, +230]) 
J3  = array ("h", [11, 480, -100, -150,10, 300, +150, +230]) 

Sebesseg = 0.004

for q in range (1,5):
  for i in range (0,101):
    #Vizszintes mozgas hatra:
    xv=i/float(100)
    pwm.setPWM(B1[4], 0, B1[5]+ int(B1[6]*xv))
    pwm.setPWM(J2[4], 0, J2[5]+ int(J2[6]*xv))
    pwm.setPWM(B3[4], 0, B1[5]+ int(B3[6]*xv))
    #Vizszintes mozgas elore:
    pwm.setPWM(J1[4], 0, J1[5]+ int(J1[6]*(1-xv)))
    pwm.setPWM(B2[4], 0, B2[5]+ int(B2[6]*(1-xv)))
    pwm.setPWM(J3[4], 0, J3[5]+ int(J3[6]*(1-xv)))
    # fuggoleges mozgas elore
    xf = (i-50)/float(50)
    yf = math.sqrt(1-pow(xf,2))
    pwm.setPWM(J1[0], 0, J1[1]+ int(J1[2]*yf))
    pwm.setPWM(B2[0], 0, B2[1]+ int(B2[2]*yf))
    pwm.setPWM(J3[0], 0, J3[1]+ int(J3[2]*yf))
    time.sleep(Sebesseg)
  for i in range (0,101):
    xv=1-i/float(100)
    #Vizszintes mozgas hatra:
    pwm.setPWM(B1[4], 0, B1[5]+ int(B1[6]*xv))
    pwm.setPWM(J2[4], 0, J2[5]+ int(J2[6]*xv))
    pwm.setPWM(B3[4], 0, B1[5]+ int(B3[6]*xv))
    #Vizszintes mozgas elore:
    pwm.setPWM(J1[4], 0, J1[5]+ int(J1[6]*(1-xv)))
    pwm.setPWM(B2[4], 0, B2[5]+ int(B2[6]*(1-xv)))
    pwm.setPWM(J3[4], 0, J3[5]+ int(J3[6]*(1-xv)))
    xf = (i-50)/float(50)
    yf = math.sqrt(1-pow(xf,2))
    pwm.setPWM(B1[0], 0, B1[1]+ int(B1[2]*yf))
    pwm.setPWM(J2[0], 0, J2[1]+ int(J2[2]*yf))
    pwm.setPWM(B3[0], 0, B3[1]+ int(B3[2]*yf))
    time.sleep(Sebesseg)
