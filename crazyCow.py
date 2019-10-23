#!/usr/bin/env python
import time

state = 0
timer = None

def initialize():
	# TODO: switch to hour:minutes format when 60 minutes are reached
	global state
	global timer
	state = 0
	timer = 3
	while state == 0:
		user_input = input(timer)
		if user_input == "+":
			timer += 1
		elif user_input == "-":
			if timer >= 2:
				timer -= 1
			else:
				print("Your timer value has to be one minute or more.")
		else:
			state = 1
	print("Your timer is set to %d minutes." % timer)

def run(timer):
	global state
	while state == 1:
		print("Drink again in %d minutes." % timer)
		timer -= 1
		if timer == 0:
			state = 2
			print("Drink!")
		time.sleep(6)

def alarm():
	global state
	runsound = "sound.py"
	while state == 2:
		exec(open("sound.py").read())
		alarmInput = input("Did you drink?")
		if alarmInput == "y":
			state = 1


def main():
	while True:
		if state == 0:
			initialize()
		elif state == 1:
			run(timer)
		elif state == 2:
			alarm()
main()
