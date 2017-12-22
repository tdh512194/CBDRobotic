class Bicycle:
    "Bicycle class"

    bikelist = {} # dict with key is the model and value is list of weight and cost
    costlist = {}  # dict with key is the model and the value is the cost

    def __init__(self, model, wheel, frame):
        "constructor"
        self.model = model
        self.weight = wheel.weight * 2 + frame.weight
        self.cost = wheel.cost * 2 + frame.cost

        l = [self.weight, self.cost]
        Bicycle.bikelist[self.model] = l
        Bicycle.costlist[self.model] = self.cost

class Wheel:
    "Wheel class"
    wheellist = {} # dict with key is the model and value is list of weight and cost
    def __init__(self, model, weight, cost):
        "constructor"
        self.model = model
        self.weight = weight
        self.cost = cost

        l = [weight, cost]
        Wheel.wheellist[model] = l

class Frame:
    "Frame class"

    framelist = {} # dict with key is the material and value is list of weight and cost

    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

        l = [weight, cost] #dung dict
        Frame.framelist[material] = l

class Bikeshop:
    "Bike shop class"

    shoplist = {}  # dict with key is the shop name and value is the object

    def __init__(self, name, inventory):
        "constructor"
        self.name = name
        self.bikelist = []
        self.inventory = inventory  # a dict with key is the model and value is the stock number
        for model in inventory:  # create a list of available bike models
            self.bikelist.append(model)
        self.pricelist = {}  # a dict with key is the model and value is the price
        self.profit = 0
        self.pricing()
        self.printInventory()  # print initial inventory
        Bikeshop.shoplist[name] = self

    def printAffordableBikeList(self, customer):
        "print the bike list that the customer can purchase with his budget"
        print("Customer has :", customer.budget)
        for model in (model for model in self.bikelist if self.pricelist[model] <= customer.budget):
            # only print the model with affordable price
            print(model + " ", self.pricelist[model])

    def printInventory(self):
        "print the inventory dictionary  ofthe models and the respective stocks"
        for model in self.inventory:
            print("The " + model + " bike has ", self.inventory[model], "left in stock")

    def pricing(self):
        "determine the price of the bike belongs to the bike list of shop"
        for model in self.bikelist:
            self.pricelist[model] = Bicycle.costlist[model] * 1.2

    def isInStock(self, model):
        "check if the bike of the model is in stock"
        if self.inventory[model] == 0:
            return False
        else:
            return True

    def sellBike(self, model):
        "sell the bike that decreases the stock and gains the profit"
        if self.isInStock(model):
            self.inventory[model] = self.inventory[model] - 1
            self.profit = self.profit + Bicycle.costlist[model] * 0.2
            return True
        else:
            print ("No bike left for that model")
            return False

    def printSaleReport(self):
        "print sale report after the customers have finished buying"
        self.printInventory()
        print("Total profit: ", self.profit)


class Customer:
    "Customer class"
    budgetlist = {}  # dict with key is the name and value is his budget
    bicyclelist = {}  # dict with key is the name and value is the own bicycle model

    def __init__(self, name, budget):
        "constructor"
        self.name = name
        self.budget = budget
        self.bike = 'none'
        Customer.budgetlist[self.name] = budget
        Customer.bicyclelist[self.name] = self.bike

    def goToShop(self, shop):
        "ask shop for the list of affordable bike models"
        print("Name: " + self.name)
        shop.printAffordableBikeList(self)

    def buyBike(self, model, shop):
        "attempt to buy the bike of the model at the shop"
        if shop.pricelist[model] > self.budget:
            print("Not enough money")
        else:
            if shop.sellBike(model):
                self.bike = model
                Customer.bicyclelist[self.name] = model
                self.budget = self.budget - shop.pricelist[model]
                self.printReceipt(model, shop)

    def printReceipt(self, model, shop):
        "print customer name, bike name, purchased bike cost, shop name, remaining budget"
        print("Customer " + self.name +
              " has purchased the " + model +
              " bike that costs ", shop.pricelist[model],
              " at shop " + shop.name +
              ". The remaining budget is ", self.budget)

    def printCustomerInfo(self):
        "print customer name, bike, and budget"
        print("Name: " + self.name)
        print("Bike: " + self.bike)
        print("Budget: ", self.budget)


w1 = Wheel("W1", 1, 30)
w2 = Wheel("W2", 2, 50)
w3 = Wheel("W3",3, 100)

print(Wheel.wheellist)

f1 = Frame("Aluminum", 5, 100)
f2 = Frame("Carbon", 4, 320)
f3 = Frame("Steel", 9, 6)

print(Frame.framelist)

b1 = Bicycle("B1", w1, f1)
b2 = Bicycle("B2", w1, f2)
b3 = Bicycle("B3", w2, f1)
b4 = Bicycle("B4", w3, f3)
b5 = Bicycle("B5", w2, f3)
b6 = Bicycle("B6", w3, f2)

print(Bicycle.bikelist)

i1 = {'B1': 2, 'B2': 3, 'B3': 4, 'B4':1, 'B6': 3, 'B5': 1}
s1 = Bikeshop("SHOP1", i1)

print(Bikeshop.shoplist)
print(s1.pricelist)

c1 = Customer("C1", 200)
c2 = Customer("C2", 500)
c3 = Customer("C3", 1000)
print(Customer.budgetlist)
print(Customer.bicyclelist)

c1.goToShop(s1)
c2.goToShop(s1)
c3.goToShop(s1)

c1.buyBike('B5',s1)
c1.printCustomerInfo()
c2.buyBike('B1', s1)
c2.printCustomerInfo()
c3.buyBike('B6',s1)
c3.printCustomerInfo()
s1.printSaleReport()