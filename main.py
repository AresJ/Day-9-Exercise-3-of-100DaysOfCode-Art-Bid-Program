from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

bid = {}

def GetBid():
  name = input("Please enter your full name: ")
  price = input("Please enter bid price: ")
  for a in ["name", "price"]:
    bid[a] = eval(a)

def SeeIfThereAreOtherBidders():
  question = input("Are there any other bidders?")
    if question in ('y', 'n'):
      break
  print("invalid input.")
  if answer == 'y':
    GetBid()
    continue
  else: 
    FindHighestBidder()
    break

def FindHighestBidder():
    highestBid = max(bid, key=bid.get)
    print("The highest bidder is:", highestBid)
  


while True:
  print(art.logo)
  GetBid()

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
    

