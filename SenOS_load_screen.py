#load screen for SenOS

from pyfiglet import *
from time import sleep
import sys
from modules import clrsc



def SenOS_load_screen():
	clrsc()
	scr = figlet_format("   = SenOS. = ")
	print(scr)
	sleep(2)
	ind1 = 0
	print("Loading...")
	sleep(3)
	print("Checking system peripherals...")
	sleep(1)
	print("Checking CPU...")
	sleep(0.5)
	print("Checking RAM...")
	sleep(0.5)
	print("Checking storage...")
	sleep(3)
	print("Finished the checking process.")
	sleep(2)
	print("Initializing the system...")
	sleep(3)
	clrsc()
	sleep(3)





SenOS_load_screen()