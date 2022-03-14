1
import os
import time
print ("""
Launching OOBE.
""")

time.sleep(1)
print ("""
Launching "epycsoftware-pyset."
""")

time.sleep(1.5)
print ("""
Launching epycsoftware-code.exe-Accessibility.
""")

time.sleep (3)
print ("""

██████████████████████████████████████████████████████████████████████
█▄─▄▄─█▄─██─▄█─▄─▄─█▄─▄▄▀█─▄▄─█─▄▄▄▄███─▄▄▄▄█▄─▄▄─█─▄─▄─█▄─██─▄█▄─▄▄─█
██─▄████─██─████─████─▄─▄█─██─█▄▄▄▄─███▄▄▄▄─██─▄█▀███─████─██─███─▄▄▄█
▀▄▄▄▀▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀
                      
                █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
                ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄

                     [1] Start Setup
""")

setup = input ("[?]:")
if setup == '1':
        name = input(str("Please create your username to be displayed:"))
        pas  = input(str("Please create a Password to login after setup:"))
print ("""
Your username and password were created succesfully.
""")
name = input (str("Please enter your First Name."))
name = input(str("Please enter your Last Name."))

time.sleep (2)
print (""""
Okay. Your Name has been registered.
""")
time.sleep(1)
print ("""
We're setting up your beta license, this will take a few seconds.
""")

time.sleep(5)
print ("""
Your beta license has been activated succesfully
""")

time.sleep(2)
print ("""
Would You Like To Activate Special Features (Special Features allow you to get access to selected unstable apps or features)?
                                                         [Y/N]
""")

setup = input ("[?]:")
if setup == 'Y':
    print ("""
Okay, special features have been activated, Click Enter to go to Optimization.
""")

setup = input ("[?]:")
if setup == 'N':
    print ("""
Okay, special features have been disabled, Click Enter to go to Optimization.
""")

time.sleep(2)
print ("""
Hi
""")

time.sleep(2)
print ("""
We're optimizing FutrOS for you.
""")

time.sleep(3)
print ("""
Hold on tight!
""")

time.sleep(2)
print ("""
FutrOS After-Installation Setup is nearly ready!
""")

