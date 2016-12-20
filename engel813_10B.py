# CSci 1133 HW 10
# Kayla Engelstad
# HW Problem 10B
# Lab Section 22

# VEHICLE INHERITANCE PROGRAM
# This program will include a base class (Vehicle) and three subclasses (Car, Truck, SUV). The user will be able to
# set the number of doors and the color of the car through getter and setter methods. However, the subclasses will
# have a default setting for number of doors that corresponds with the type.


# base class

class Vehicle(object):

    def __init__(self, color=''):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, string):
        self.color = string
        return self.color


# Subclasses

class Car(Vehicle):

    def __init__(self, color='', numDoors=4):
        Vehicle.__init__(self, color)
        self.numDoors = numDoors

    def getNumDoors(self):
        return self.numDoors

    def setNumDoors(self, num):
        self.numDoors = num
        return self.numDoors

class Truck(Vehicle):

    def __init__(self, color='', numDoors=2):
        Vehicle.__init__(self, color)
        self.numDoors = numDoors

    def getNumDoors(self):
        return self.numDoors

    def setNumDoors(self, num):
        self.numDoors = num
        return self.numDoors
        
class SUV(Vehicle):

    def __init__(self, color='', numDoors=4):
        Vehicle.__init__(self, color)
        self.numDoors = numDoors

    def getNumDoors(self):
        return self.numDoors

    def setNumDoors(self, num):
        self.numDoors = num
        return self.numDoors


# test

vehicle_1 = Car("Black")
print(vehicle_1.getColor())
print(vehicle_1.getNumDoors())
vehicle_1.setColor("Yellow")
print(vehicle_1.getColor())
vehicle_1.setNumDoors(6)
print(vehicle_1.getNumDoors())
