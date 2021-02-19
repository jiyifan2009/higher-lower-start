from art import logo
from art import vs
from game_data import data
import random

print(logo)
index_a=random.randint(0,len(data)-1)
print(f"Compare A: {data[index_a]['name']}, {data[index_a]['description']}, from {data[index_a]['country']}")

new_data=data
data.remove(data[index_a])
new_data=data
#print(new_data)
index_b=random.randint(0,len(new_data)-1)
print(vs)
print(f"Compare B: {data[index_b]['name']}, {data[index_b]['description']}, from {data[index_b]['country']},")

guess=input("Who has more follower? Type 'A' or 'B':")

if guess=="A":
  if data[index_a]['follower_count']>data[index_b]['follower_count']:
    print("You win!")
  else:
    print("You lose!")
elif guess=="B":
  if data[index_a]['follower_count']<data[index_b]['follower_count']:
    print("You win!")
  else:
    print("You lose!")

    
#def higherlower_game():

