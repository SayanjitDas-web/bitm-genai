#lambda functions

# def add(num1, num2):
#     print(num1+num2)

# add = lambda num1, num2 : print(num1 + num2)
# sutdent = lambda num1, num2 : num1 - num2

# add(10,12)
# result = sutdent(10,12)

# square = lambda num: print(num * num)

# square(3)
# print(result)

#Object Oriented Programming(OOP)

# - class  - circuit design
# - object - circuit

# class - constructor , methods, attributes

# class Circuit:
#     def __init__(self,colour):
#         self.colour = colour
#         print("pink light is truned on")

    
    
# c1 = Circuit("red")
# c2 = Circuit("green")
# c3 = Circuit("blue")

# print(c1.colour)
# print(c2.colour)
# print(c3.colour)

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def add(self):
#         return self.num1 + self.num2
    
#     def sub(self):
#         return self.num1 - self.num2
    
#     def div(self):
#         return self.num1 / self.num2
    
#     def mul(self):
#         return self.num1 * self.num2
    


# cal = Calculator(10, 2)

# print(cal.add())
# print(cal.sub())
# print(cal.div())
# print(cal.mul())

# class Chat:
#     def __init__(self,message):
#         self.message = message

#     def send(self):
#         return f"message send: {self.message}"
    
#     def delete(self):
#         return f"message deleted: {self.message}"
    
# chat = Chat("hello bitm")

# print(chat.send())
# print(chat.delete())

# inheretance
# class Vehichle:
#     def __init__(self,name):
#             self.name = name

#     def move(self):
#           print(self.name + " is moving")

#     def showColour(self):
#           print(self.name + "'s colour is red")

# class TwoWheeler(Vehichle):
#       def __init__(self, name):
#             super().__init__(name)

#       def countWheel(self):
#             print("I have two wheels")

# class FourWheeler(Vehichle):
#       def __init__(self, name):
#             super().__init__(name)

#       def countWheel(self):
#             print(self.name +" have four wheels")

# pulser = TwoWheeler("pulser")
# nano = FourWheeler("nano")

# pulser.move()
# pulser.showColour()
# pulser.countWheel()


# nano.move()
# nano.showColour()
# nano.countWheel()

# ploymorphism

class Vehichle:
    def __init__(self,name):
            self.name = name

    def showColour(self):
          print(self.name + "'s colour is red")

class TwoWheeler(Vehichle):
      def __init__(self, name):
            super().__init__(name)

      def countWheel(self):
            print("I have two wheels")

      def move(self):
            print(self.name + " is moving 100km/h")

class FourWheeler(Vehichle):
      def __init__(self, name):
            super().__init__(name)

      def countWheel(self):
            print(self.name +" have four wheels")

      def move(self):
            print(self.name + " is moving 150km/h")

# def add(num1,num2):
#       print(num1+num2)

# def add(num1,num2):
#       print(num1 - num2)

# add(1,2)

bike1 = TwoWheeler("Pulser")
car1 = FourWheeler("Thar")

bike1.move()
car1.move()