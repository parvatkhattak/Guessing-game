import random
computer=random.randint(1,6)
prompt="what is your guessing? "
message="are you sure to exit?(y/n)"
quit_text="q"
quit_program=-1
def quit():
  quit=input(message)
  if quit=="n":
    return False
  else:
    return True
def guess():
  computer=random.randint(1,6)
  no_of_guesses=0
  while True:
    no_of_guesses+=1
    player=input(prompt)
    if player==quit_text:
      if quit():
        return quit_program
      else:
        continue
    if computer==int(player):
      print("correct")
      return no_of_guesses
    elif player<computer:
      print("too low")
    else:
      print("too high")
total_rounds=0
total_guesses=0
while True:
  total_rounds+=1
  print("starting round no: ",total_rounds)
  this_round=guess()
  if this_round==quit_program:
    total_rounds= total_rounds-1
    if total_rounds==0:
      print("you played no rounds. try again")
    else:
      avg=float(total_guesses/total_rounds)
      print("you played",total_rounds-1,"rounds with guessing average of",avg)
    break
  total_guesses+=this_round
  print("you took",this_round,"guesses")
  avg=float(total_guesses/total_rounds)
  print("your guessing average is",avg)
  print("")
