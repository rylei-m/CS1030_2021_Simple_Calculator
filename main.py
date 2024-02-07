#Rylei Mindrum
#Computer Science Principles OL
#Harrison

#Calculator
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x,y):
  return x / y

def exponent(x,y):
  return x ** y

def greater_than(x,y):
  return x > y

def less_than(x,y):
  return x < y

#def gtoet(x,y):
  #return x >= y

#def ltoet(x,y):
  #return x <= y



while True:
  choice = input("Choose(add/subtract/multiply/divide/exponent/greater than/less than) ")
  if choice in ('add' , 'subtract' , 'multiply' , 'divide' , 'exponent' , 'greater than', 'less than' ):
    value1 = float(input("enter first number: "))
    value2 = float(input("enter second number: "))
  if choice == 'add':
    print(value1, "+", value2, "=", add(value1, value2))
  elif choice == 'subtract':
    print(value1, "-", value2, "=", subtract(value1, value2))
  elif choice == 'multiply':
    print(value1, "*", value2, "=", multiply(value1, value2))
  elif choice == 'divide':
    print(value1, "/", value2, "=", divide(value1, value2))
  elif choice == 'exponent':
    print(value1, "**", value2, "=", exponent(value1, value2))
  elif choice == 'greater than':
    print(value1, ">", value2, "=", greater_than(value1, value2))
  elif choice == 'less than':
    print(value1, "<", value2, "=", less_than(value1, value2))
  #elif choice == 'gtoet':
    #print(value1, ">=", value2, "=", gtoet(value1, value2))
  #elif choice == 'ltoet':
    #print(value1, "<=", value2, "=", ltoet(value1, value2))
  #elif choice == 'dgtoet':
    #print(value1, "2*<=", value2, "=", dgtoet(value1, value2))
  #elif choice == 'hgtoet':
    #print(value1, ">=/2", value2, "=", hgtoet(value1, value2))
  #elif choice == 'dltoret':
    #print(value1, "2*<=", value2, "=", dltoret(value1, value2))
  #elif choice == 'hgtoet':
    #print(value1, ">=/2", value2, "=", hgtoet(value1, value2))
  