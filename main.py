from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

while True:
  print(art.logo)
  name = input("Please enter your full name: ")
  price = input("Please enter bid price: ")
  bid = {}
  for a in ["name", "price"]:
    bid[a] = eval(a)

  while True:
    answer = str(input('Run again? (y/n)?: '))
    if answer in ('y', 'n'):
      break
    print("invalid input.")
  if answer == 'y':
    clear()
    continue
  else: 
    print("Goodbye.")
    break
    

