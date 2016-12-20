# CSci 1133 HW 10
# Kayla Engelstad
# HW Problem 10A
# Lab Section 22

# FOOTMEASURE CLASS
# This program contains the FootMeasure class which will include special methods __init__, __repr__, __add__,
# __sub__, __lt__, __gt__, and __eq__. A non-pure function, testMeasure, will test the FootMeasure class by checking
# each special method and the value it returns.

# define class
class FootMeasure(object):
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches

    def __repr__(self):
        if self.inches == 0 and self.feet != 0:
            return(str(self.feet) + ' ft.')

        elif self.inches >= 12:
            inches = self.inches
            feet = self.feet

            new_feet = feet + (inches // 12)
            new_inches = inches % 12

            return(str(new_feet) + ' ft.   ' + str(new_inches) + ' in.')

        else:
            return(str(self.feet) + ' ft.   ' + str(self.inches) + ' in.')

    def __str__(self):
        return(self.__repr__())

    def __add__(self, other):
        in1 = self.inches + (self.feet * 12)
        in2 = other.inches + (other.feet * 12)
        return(FootMeasure(inches = (in1 + in2)))

    def __sub__(self, right):
        in1 = self.inches + (self.feet * 12)
        in2 = (right.inches + (right.feet * 12))
        val = in1 - in2

        if val < 0:
            print("Error: subtraction results in a negative value of " + str(val) + " inches")

        else:
            return(FootMeasure(inches = val))

    def __lt__(self, right):
        in1 = self.inches + (self.feet * 12)
        in2 = (right.inches + (right.feet * 12))

        if in1 < in2:
            return True
        else:
            return False

    def __eq__(self, right):
        in1 = self.inches + (self.feet * 12)
        in2 = (right.inches + (right.feet * 12))

        if in1 == in2:
            return True
        else:
            return False

    def __gt__(self, right):
        in1 = self.inches + (self.feet * 12)
        in2 = (right.inches + (right.feet * 12))

        if in1 > in2:
            return True
        else:
            return False
        
        
        
        

# define test
def testMeasure():
    meas1 = FootMeasure()
    meas2 = FootMeasure(feet = 5)
    meas3 = FootMeasure(5, 8)
    meas4 = FootMeasure(inches = 68)

    print("Representation Test:\n")
    print(meas1)
    print(meas2)
    print(meas3)
    print(meas4)

    print("\nAddition Test:\n")
    meas5 = meas2 + meas3
    print(str(meas2) + " and " + str(meas3) + " added:")
    print(meas5)
    meas5 = meas3 + meas4
    print("\n" + str(meas3) + " and " + str(meas4) + " added:")
    print(meas5)

    print("\nSubtraction Test:\n")
    meas6 = meas3 - meas4
    print(str(meas3) + " subtracted from " + str(meas4) + ':')
    print(meas6)
    print(str(meas2) + " subtracted from " + str(meas3) + ':')
    meas6 = meas2 - meas3

    print("\nRelational Operators Test:\n")
    print(str(meas3) + " less than " + str(meas2))
    print(meas3 < meas2)
    print(str(meas2) + " less than " + str(meas3))
    print(meas2 < meas3)
    print(str(meas4) + " less than " + str(meas3))
    print(meas4 < meas3)
    print(str(meas1) + " equal to " + str(meas4))
    print(meas1 == meas4)
    print(str(meas3) + " equal to " + str(meas4))
    print(meas3 == meas4)
    print(str(meas2) + " greater than " + str(meas4))
    print(meas2 > meas4)
    print(str(meas4) + " greater than " + str(meas2))
    print(meas4 > meas2)
    print(str(meas4) + " greater than " + str(meas3))
    print(meas4 > meas3)
    
