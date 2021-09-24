#create a program that will print a countdown timer in a given time using the .sleep() and divmode function

#this is for the time import module

import time

timesec = int(input("Enter time here for the countdown in seconds: ")) #this should be in int because we are inserting an integer

def countdown(timesec): #this is for defining the countdown in time
    while timesec:
        min, secs = divmod(timesec, 60) #the divmod method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder
        format = '{:02d}:{:02d}'.format(min, secs) #the '{:02d}:{:02d}' is used for the format of the time
        print("time is set for: " + str(format))
        time.sleep(1) #the .sleep() is used for the countdown delay
        timesec -= 1
    print("ALARMING!!!!!!")
countdown(timesec) #this should call the function of the def this is import for the function to start














