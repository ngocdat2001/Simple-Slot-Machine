#Load library
from random import randint

#Constants:
MENUS_OPTIONS = "Choose one of the following menus options:\n1) Play the slot machine.\n2) Save game.\n3) Cash out."
OPTIONS = ['1', '2', '3']

#Define function read_money_data
def read_money_data():
  # read money from players saved
  try :
    file = open("money_data.txt",'r')
    money_data = file.read()
    file.close()
    money_data = float(money_data)
    return money_data
  # if no data saved returns 10$
  except:
    return 10

#Define function ask_player
def ask_player(money):
  #Check input of Player
  while True:
    print("You have $"+ str(money))
    print(MENUS_OPTIONS)
    player_option = input()
    if player_option in OPTIONS:
      break
  return player_option

#Define function play_game
def play_game(money):
  money = money - 0.25
  machine_number = randint(0,999)
  print("The slot machine shows " + str(machine_number).zfill(3) + ".")
  a = machine_number // 100
  b = (machine_number // 10) % 10
  c = machine_number % 10
  if a != b and a != c and b != c:
    print("Sorry you don't won anything.")
  elif a == b == c:
    money = money + 10
    print("You won the big prize, $10.00!")
  else:
    money = money + 0.5
    print("You win 50 cent!")
  #End if-elif-else
  return money

#Define function save_game
def save_game(money):
  file = open("money_data.txt","w")
  file.write(str(money))
  file.close
  print("save game successfull. Thanks for playing game ")

#Define function cash_out
def cash_out(money):
  print("Cash out " + str(money) + " $ successfull. Thanks for playing game")
  file = open("money_data.txt", 'w')
  file.write("10")

#Main
def main():
  money = read_money_data()
  while True:
    
    player_option = ask_player(money)

    if player_option == '1':
      money = play_game(money)
      if money == 0 :
        print("You have no money left. Thanks for playing game")
        break

    if player_option == '2':
      save_game(money)
      break

    if player_option == '3':
      cash_out(money)
      break

#Call main function
main()

