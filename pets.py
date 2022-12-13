#Ch 13 Programming Assignment
#Jared Adamson
#Part A
# Demonstrates inheritance of a class.  

'''
Directions
Create a program called pets.py that that defines a pet class with at least three general attributes (fields) for all pets (for example, name, age, etc) 
and at least two functions/behaviors for all pets (for example, eating). The functions can simply print something.

Next, create two derived classes from the base class that represent specific types of pets. For example, one derived class might be a dog. 
Add at least one attribute/field and at least two functions/behaviors specific to that kind of pet.

Finally, demonstrate that both derived classes work by creating at least one instance of each and showing off their fields and functions.

Note: In preparation for the Final Project, this assignment leaves room for you to make more decisions about the code than previous assignments. 
Just be sure that your submission demonstrates the key concepts from the chapter, as indicated in these directions.
'''



class Pet:
   def __init__(self):
       self.name = ''
       self.age = 0
       self.animalClass = ''

   def setName(self, nme):
        self.name = nme

   def setAge(self, age):
       self.age = age
       
   def setClass(self, cls):
       self.animalClass = cls
 
   def petEats(self):
       print('The pet eats.')
   
   def petSleep(self):
       print('The pet sleeps.')

   def petPrint(self):
       print(self.name, self.age, self.animalClass)

# Derived class one.

class Dog(Pet):  
   def __init__(self):
        Pet.__init__(self)
        self.breed = ''
        self.animalClass = 'Mammal'

   def setBreed(self, breed):
       self.breed = breed
 
   def petFetch(self):
       print('The Dog collected the item.')

   def petRollover(self):
       print('The Dog rolls on the floor.')

   def petPrint(self):
       print(self.name, self.age, self.breed, self.animalClass)

# Derived class Two.

class Frog(Pet):  
   def __init__(self):
       Pet.__init__(self)  
       self.animalClass = 'Amphibian'
       self.color = ''

   def setColor(self, colr):
       self.color = colr
 
   def petHop(self):
       print('The Frog hops.')

   def petCroak(self):
       print('The Frog croaks.')
  
   def petPrint(self):
       print(self.name, self.age, self.color, self.animalClass)

kermit = Frog()

lassy = Dog()

x = input('What is your pet dogs name?')
lassy.setName(x)
x = input('What is your pet dogs breed?')
lassy.setBreed(x)
x = int(input('What is your pet dogs age?'))
lassy.setAge(x)

lassy.petPrint()
lassy.petFetch()
lassy.petRollover()
lassy.petEats()
lassy.petSleep()

x = input('What is your pet frogs name?')
kermit.setName(x)
x = input('What is your pet frogs color?')
kermit.setColor(x)
x = int(input('What is your pet frogs age?'))
kermit.setAge(x)

kermit.petPrint()
kermit.petHop()
kermit.petCroak()
kermit.petEats()
kermit.petSleep()