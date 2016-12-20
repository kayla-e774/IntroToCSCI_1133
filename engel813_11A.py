# CSci 1133 HW 11
# Kayla Engelstad
# HW Problem 11A
# Lab Section 22

# PASTRY DATABASE CODE
# This code will be able to store pastries in a database. The possible types of pastries (cookies, cakes, and
# pastries) will each have their own class that inherits from the Item class. The user will be able to create and
# view their entries for this database through use of a Display method, and the list of items will be maintained
# by a Database class. The database object will be displayed once the user is done entering values.

# define base class

class Item(object):
    def __init__(self, Name='', Description='', Price=0, Cost=0, NumberStock=0):
        self.Name = Name
        self.Description = Description
        self.Price = Price
        self.Cost = Cost
        self.NumberStock = NumberStock

    # getters/setters (TESTED)

    def getName(self):
        return(self.Name)

    def setName(self, string):
        self.Name = string
        return(self.Name)

    def getDescription(self):
        return(self.Description)

    def setDescription(self, string):
        self.Description = string
        return(self.Description)

    def getPrice(self):
        return(self.Price)

    def setPrice(self, num):
        self.Price = num
        return(self.Price)

    def getCost(self):
        return(self.Cost)

    def setCost(self, num):
        self.Cost = num
        return(self.Cost)

    def getNumberStock(self):
        return(self.NumberStock)

    def setNumberStock(self, intnum):
        self.NumberStock = intnum
        return(self.NumberStock)

    # Display Method (Works, but formatting needs work)

    def Display(self):
        print('{0:30} {1}'.format("Item Name: ", self.Name))
        print('{0:30} {1}'.format("Description: ", self.Description))
        print('{0:30} {1}'.format("Selling Price: ", self.Price))
        print('{0:30} {1}'.format("Cost to Bake: ", self.Cost))
        print('{0:30} {1}'.format("Number in Stock: ", self.NumberStock))

# define sub-classes of item

class Cookies(Item):
    def __init__(self, Name, Description, Price, Cost, NumberStock, Dough=''):
        Item.__init__(self, Name, Description, Price, Cost, NumberStock)
        self.Dough = Dough

    def getDough(self):
        return(self.Dough)

    def setDough(self, string):
        self.Dough = string
        return(self.Dough)

    def Display(self):
        Item.Display(self)
        print('{0:30} {1}'.format('Dough:', self.Dough))


class Cake(Item):
    def __init__(self, Name, Description, Price, Cost, NumberStock, Frosted=False):
        Item.__init__(self, Name, Description, Price, Cost, NumberStock)
        self.Frosted = Frosted

    def getFrosted(self):
        return(self.Frosted)

    def setFrosted(self, bval):
        self.Frosted = bval
        return(self.Frosted)

    def Display(self):
        Item.Display(self)
        print('{0:30} {1}'.format(('Frosted:'), str(self.Frosted)))

class Pastries(Item):
    def __init__(self, Name, Description, Price, Cost, NumberStock, Filling=''):
        Item.__init__(self, Name, Description, Price, Cost, NumberStock)
        self.Filling = Filling

    def getFilling(self):
        return(self.Filling)

    def setFilling(self, string):
        self.Filling = string
        return(self.Filling)

    def Display(self):
        Item.Display(self)
        print('{0:30} {1}'.format('Filling: ', self.Filling))

# define Database class

class Database(object):
    def __init__(self, ilist=[]):
        self.ilist = ilist

    def addItem(self, theItem):
        list1 = list(self.ilist)
        list1.append(theItem)
        self.ilist = list1
        return(self.ilist)

    def Display(self):
        list1 = list(self.ilist)
        print("\nDatabase:\n")

        for i in range(len(list1)):
            item = list1[i]
            item.Display()
            print('\n')
        

    def TotalEarn(self):
        list1 = list(self.ilist)
        total = 0

        for i in range(len(list1)):
            item = list1[i]
            val = (float(item.Price) - float(item.Cost)) * int(item.NumberStock)
            total += val

        return total


# --main

items = Database()
running = True
while running:
    try:
        Type = str(input('Please enter "Cookies", "Cake", or "Pastries": ').lower())
        name = str(input('Enter item name: '))
        description = str(input('Enter description: '))
        price = float(input('Enter selling price in dollars: '))
        cost = float(input('Enter cost of baking in dollars: '))
        stock = int(input('Enter number of items in stock: '))

        if Type == 'cookies':
            dough = str(input("Enter type of dough: "))
            item = Cookies(name, description, price, cost, stock, dough)

        elif Type == 'cake':
            valid_in = False
            while not valid_in:

                frosted = input("Is the cake frosted? (Y/N): ").lower()

                if frosted in ('y', 't', 'true', 'yes'):
                    frosted = True
                    valid_in = True

                elif frosted in ('n', 'f', 'false', 'no'):
                    frosted = False
                    valid_in = True

                else:
                    print("input not recognized, please try again")
                    valid_in = False

            item = Cake(name, description, price, cost, stock, frosted)

        elif Type == 'pastries':
            filling = str(input("Enter the type of filling: "))
            item = Pastries(name, descrption, price, cost, stock, filling)

    except:
        print("Input not compatible, please try again.")

    items.addItem(item)

    again = str(input('Add another item? (Y/N): ').lower())

    if again in ('n', 'no'):
        running = False

items.Display()
total = items.TotalEarn()
print('{0:30} {1}'.format("Total projected Earnings:", str(total)))
