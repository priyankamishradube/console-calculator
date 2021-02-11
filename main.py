from replit import clear
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
should_continue = True
num1 = int(input("Enter the first number "))
for i in operations:
  print(i)

while should_continue:
  user_operator = input("Pick an operation ")
  num2 = int(input("Enter the next number "))

  calculation_function = operations[user_operator]
  answer = calculation_function(num1,num2)
  print(f"{num1} {user_operator} {num2} = {answer}")

  response = input("Would you like to continue? Y or N").lower()
  if response == "y":
    num1= answer
  else:
    should_continue = False
    clear()



