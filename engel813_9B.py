# CSci 1133 HW 9
# Kayla Engelstad
# HW Problem 9B
# Lab Section 22

# WATCH CLASS PROGRAM
# This program defines and imports a Watch class that will report the current local time in military time format.
# It will also function as a simple start-stop timer.This class will utilize the time module. It will also have the
# private instance variables startTime and endTime which may be accessed by getStartTime and getEndTime methods. It
# will also be able to report the current local time useing a getTimeNow function. Mutator methods will include
# start (to reset startTime) and stop (to reset endtime). The accessor function elapsedTime will return the time
# passed for the stopwatch. A test program will be written to test the Watch class.

# import modules
from time import time, localtime
import random

# define class

class Watch(object):

    def __init__(self):
        self.__startTime = time()
        self.__endTime = time()
    
    def __repr__(self):
        string = "Start Time: " + str(self.__startTime) + "\n" + "End Time: " + str(self.__endTime) + "\n"
        return string
    
    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def getTimeNow(self):
        lst = localtime()

        seconds = str(lst[5])
        if len(seconds) == 1:
            seconds = '0' + seconds

        minutes = str(lst[4])
        if len(minutes) == 1:
            minutes = '0' + minutes

        hours = str(lst[3])
        if len(hours) == 1:
            hours = '0' + hours

        time = hours + ':' + minutes + ':' + seconds
        return time

    def start(self):
        self.__startTime = time()
        return self.__startTime

    def stop(self):
        self.__endTime = time()
        return self.__endTime

    def elapsedTime(self):
        time_diff = float(self.__endTime - self.__startTime)
        return time_diff




# Test Program

test = Watch()

# print local time 1
print(test.getTimeNow())

# time the sorting of a 5,000 int list
longList = []

for i in range(0, 5000):
    longList.append(random.randint(0, 1000))

#print(longList) #--for testing

test.start()
longList.sort()
test.stop()

print('It takes ', test.elapsedTime(), ' seconds to sort a 5,000 integer list.\n')

# print local time 2
print(test.getTimeNow())

# time the sorting of a 10,000 int list
longerList = []

for i in range(0, 10000):
    longerList.append(random.randint(0, 1000))

#print(longerList) #--for testing

test.start()
longerList.sort()
test.stop()

print('It takes ', test.elapsedTime(), ' seconds to sort a 10,000 integer list.\n')

# print local time 3
print(test.getTimeNow())
