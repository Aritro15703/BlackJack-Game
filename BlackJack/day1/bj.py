import random


def dealcard():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card


def calc_score(cards):
   

   if 11 in cards and 10 in cards and len(cards)==2:
      return 0 #blackjack 
   
   if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1) #ace choosing 1 or 11
   
   # if sum(cards)>21 and 11 in cards and 10 in cards:
   #    gameover=True

   return sum(cards)




   # sum_user=sum(usercard)
   # sum_comp=sum(compcard)

   # # print(sum_user)
   # # print(sum_comp)
   # if sum_user==21 and len(usercard)==2:
   #    sum_user==0
   # elif sum_comp==21 and len(compcard)==2:
   #    sum_comp==0
   
   # print(sum_user)
   # print(sum_comp)

def compare(user_score,comp_score):
   if user_score>comp_score:
      print(f"You Won! Congratulations")
   elif comp_score>user_score:
      print(f"Dealer Won :( Try again.")
   elif user_score==comp_score:
      print('Its a Draw!')

gameover= False

usercard=[]
compcard=[]

for i in range(2):
   usercard.append(dealcard())
   compcard.append(dealcard())

# print(usercard)
# print(compcard[0])
user_score= calc_score(usercard)
comp_score=calc_score(compcard)

if user_score==0 or comp_score==0 or user_score>21 or comp_score>21:
   gameover= True

print(f"Your cards are:{usercard}, Your current score is: {user_score}.")
print(f"Dealer's First Card is: {compcard[0]}")

while gameover is not True:
   newcard=input("Do you want to draw another card? Type y for yes and n for no: ").lower()
   if newcard=='y':
      usercard.append(dealcard())
      user_score=calc_score(usercard)
      print(usercard, user_score)

      if user_score>21 or (11 in usercard and 10 in usercard):
         print(f"You Bust! Your cards: {usercard}, Your score: {user_score}.")
         
   elif newcard=='n':
       gameover=True

print(f'Dealer Cards: {compcard}.\n') 
if comp_score>=17:
   compare(user_score,comp_score)   
while comp_score<17:
   compcard.append(dealcard())
   comp_score=calc_score(compcard)
   print(f"Dealer's cards:{compcard},Dealer's new score:{comp_score}.")

if comp_score>21 or (11 in compcard and 10 in compcard):
      print(f"Your final hand: {usercard}.Your Score: {user_score},\nDealer's final hand: {compcard}, Dealer's score: {comp_score}\n")
      print('Dealer Bust, Congrats you won!') 

# compare(user_score,comp_score)
# compare(user_score,comp_score)
     


