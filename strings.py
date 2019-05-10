myStr = "Hello World, car"


#METHODS
#per vedere tutti metodi disponibili
#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())

print(myStr.replace('hello','bye'))
print(myStr.count('l'))
#metodo encadenados
#print(myStr.replace('hello','bye').upper)
print(myStr.startswith('hola')) #false
print(myStr.startswith('Hello')) #True
print(myStr.startswith('H')) #True
print(myStr.endswith('World')) #True

print(myStr.split(','))
print(myStr.split('o'))
print(myStr.find('o'))
print(myStr.index('e'))

#print(myStr.isnumeric())
#print(myStr.isalpha())


print(len(myStr))

print(myStr[4])
print(myStr[-1])

#concatenacion
print ("ciao " + myStr)

name = "Lea"
print ("My name is " + name)
#print (f"My name is {name}")#con f indico que entre el texto hay una variable
print ("My name is {0}".format(name))