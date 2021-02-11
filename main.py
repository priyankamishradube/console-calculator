from replit import clear
from art import logo
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  if n1 > n2:
    return n1-n2
  return n2-n1

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  if n1>n2:
    return n1/n2
  return n2/n1

operations ={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  should_continue = True
  num1 = float(input("Enter the first number "))
  for i in operations:
    print(i)

  while should_continue:
    user_operator = input("Pick an operation ")
    num2 = float(input("Enter the next number "))

    calculation_function = operations[user_operator]
    answer = calculation_function(num1,num2)
    print(f"The answer is : {answer}")

    response = input("Would you like to continue? Y or N").lower()
    if response == "y":
      num1= answer
    else:
      should_continue = False
      calculator()

calculator()



