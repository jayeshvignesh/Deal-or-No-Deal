import replit
import random
import time
#TODO from main1 import
# https://www.101soundboards.com/boards/35203-deal-or-no-deal/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
caseNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26]
caseVal = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
    10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000,
    1000000]
caseValcopy = caseVal
cases = []
cases2 = []  #we can delete all instances of this if its bugging
removal = []
#round_cases_actual = 6
round_cases = [6, 5, 4, 3, 2, 1, 1, 1, 1]
avg = 0
roundNum = 0
percent = 0  #(DEAL PERCENTAGE)
dealNum = 0  #(DEAL NUMBER)
decision = " "
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# Choosing the case


def heading():
  print(r""" _______                       __         ______                   __    __                  _______                       __ 
|       \                     |  \       /      \                 |  \  |  \                |       \                     |  \
| $$$$$$$\  ______    ______  | $$      |  $$$$$$\  ______        | $$\ | $$  ______        | $$$$$$$\  ______    ______  | $$
| $$  | $$ /      \  |      \ | $$      | $$  | $$ /      \       | $$$\| $$ /      \       | $$  | $$ /      \  |      \ | $$
| $$  | $$|  $$$$$$\  \$$$$$$\| $$      | $$  | $$|  $$$$$$\      | $$$$\ $$|  $$$$$$\      | $$  | $$|  $$$$$$\  \$$$$$$\| $$
| $$  | $$| $$    $$ /      $$| $$      | $$  | $$| $$   \$$      | $$\$$ $$| $$  | $$      | $$  | $$| $$    $$ /      $$| $$
| $$__/ $$| $$$$$$$$|  $$$$$$$| $$      | $$__/ $$| $$            | $$ \$$$$| $$__/ $$      | $$__/ $$| $$$$$$$$|  $$$$$$$| $$
| $$    $$ \$$     \ \$$    $$| $$       \$$    $$| $$            | $$  \$$$ \$$    $$      | $$    $$ \$$     \ \$$    $$| $$
 \$$$$$$$   \$$$$$$$  \$$$$$$$ \$$        \$$$$$$  \$$             \$$   \$$  \$$$$$$        \$$$$$$$   \$$$$$$$  \$$$$$$$ \$$
                                                                                                                              
                                                                                                                              
                                                                                                                              """)


def reset():
  replit.clear()
  heading()
  print("Round", roundNum)
  print(f"Your case: {playercase['case_num']}")
  remaining_vals = sorted([case['case_val'] for case in cases2])
  print("Values remaining: ", end="")
  print(", ".join(f"${v}" for v in remaining_vals))


def exVal():
  case_val = [case['case_val'] for case in cases2]
  avg = int(round(sum(case_val) / len(case_val), 0))
  # print(f"Psst. The average value of the remaining cases is ${avg}")
  return avg
  


def deal():
  ex_val = exVal()
  percent = 0
  # for case in cases2:
  #   ex_val += case['case_val']
  # ex_val /= len(cases2)
  
  if roundNum == 1:  #1
    if ex_val >= 2500000:
      percent = random.uniform(0.26, 0.376)
    elif ex_val <= 2500000:
      percent = random.uniform(0.085, 0.201)
  elif roundNum == 2:  #2
    if ex_val >= 1900000:
      percent = random.uniform(0.344, 0.451)
    elif ex_val <= 1900000:
      percent = random.uniform(0.184, 0.291)
  elif roundNum == 3:  #3
    if ex_val >= 1400000:
      percent = random.uniform(0.447, 0.551)
    elif ex_val <= 1400000:
      percent = random.uniform(0.292, 0.396)
  elif roundNum == 4:  #4
    if ex_val >= 1000000:
      percent = random.uniform(0.54, 0.63)
    elif ex_val <= 1000000:
      percent = random.uniform(0.404, 0.494)
  elif roundNum == 5:  #5
    if ex_val >= 750000:
      percent = random.uniform(0.624, 0.71)
    if ex_val <= 750000:
      percent = random.uniform(0.494, 0.58)
  elif roundNum == 6:  #6
    if ex_val >= 550000:
      percent = random.uniform(0.714, 0.788)
    elif ex_val <= 550000:
      percent = random.uniform(0.602, 0.677)
  elif roundNum == 7:  #7
    if ex_val >= 450000:
      percent = random.uniform(0.824, 0.84)
    elif ex_val <= 450000:
      percent = random.uniform(0.8, 0.816)
  elif roundNum == 8:  #8
    if ex_val >= 350000:
      percent = random.uniform(0.93, 0.95)
    elif ex_val <= 350000:
      percent = random.uniform(0.9, 0.92)
  elif roundNum == 9:  #9
    if ex_val >= 250000:
      percent = random.uniform(0.93, 0.95)
    elif ex_val <= 250000:
      percent = random.uniform(0.9, 0.92)
  dealNum = int(round(ex_val * percent))
  print(f"The banker has offered you ${dealNum}")
  decision = str(input("Deal or No Deal? (Deal/No Deal) ")).strip().lower()
  if decision == "deal":
    print(f"You won ${dealNum}")
    exit()
  elif decision == "no deal":
    print("Round Over")
    time.sleep(3)  # CHANGE TO 3 SECONDS
  elif decision != "deal" or "no deal":
    while True:
      print("Invalid input. Please enter 'Deal' or 'No Deal'.")
      decision = str(input("Deal or No Deal? (Deal/No Deal) ")).strip().lower()
      if decision == "deal":
        print(f"You won ${dealNum}")
        exit()
      elif decision == "no deal":
        print("Round Over")
        time.sleep(1.5)
        break


def print_cases():
  for case in cases:
    print(f"{case['case_num']}", end=", ")
  print("")


heading()

for case in caseNum:
  caseval = random.choice(caseVal)
  cases.append({"case_num": case, "case_val": caseval})
  caseVal.remove(caseval)

playercase = random.choice(cases)
print(f"Your case: {playercase['case_num']}")

cases2 = cases.copy()

def function_1():
  reroll_player_case = input(
      "Do you want to reroll your case? (y/n) ").strip().lower()
  return reroll_player_case


reroll_player_case = function_1()

if reroll_player_case == "y":
  playercase = random.choice(cases)
  print(f"Your new case is case number {playercase['case_num']}")
  cases.remove(playercase)
elif reroll_player_case == "n":
  cases.remove(playercase)
else:
  while reroll_player_case != "y" or "n":
    print("Invalid input. Please enter 'y' or 'n'.")
    reroll_player_case = function_1()
    if reroll_player_case == "y":
      playercase = random.choice(cases)
      print(f"Your new case is case number {playercase['case_num']}")
    elif reroll_player_case == "n":
      cases.remove(playercase)
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

for num_cases in round_cases:
  roundNum += 1
  reset()
  print_cases()
  # if num_cases != 6:
  #   exVal()
  for num in range(1, (num_cases + 1)):
    print(f"Which {num_cases} case(s) would you like to open?")
    num_cases -= 1
    while True:
      user_choice = input("Enter the case number you want to remove: ").strip()
      if user_choice.isdigit():
        chosen_num = int(user_choice)
        case_to_remove = next(
            (c for c in cases if c['case_num'] == chosen_num), None)
        if case_to_remove is not None:
          removal.append(chosen_num)
          break
      print("Invalid case number or case already opened. Please try again.")
    print(f"Case {case_to_remove['case_num']}   ${case_to_remove['case_val']}")
    time.sleep(3)  #CHANGE TO 3 SECONDS
    cases.remove(case_to_remove)
    cases2.remove(case_to_remove)
    if num_cases == 0:
      break
    reset()
    print_cases()
  exVal()
  deal()

#BUGGY
reset()
print_cases()
print(
    f"Which case would you like to open and keep? ({playercase['case_num']}/{cases[0]['case_num']})"
)
openCase = (int(input("Enter the case number you want to open: ").strip()))

if openCase == playercase['case_num']:
  print(f"You won ${playercase['case_val']}")
  exit()
elif openCase == cases[0]['case_num']:
  print(f"You won ${cases[0]['case_val']}")
  exit()
elif openCase != playercase['case_num'] or cases[0]['case_num']:
  while True:
    openCase = int(input(f"Invalid input. Enter the case number you want to open ({playercase['case_num']}/{cases[0]['case_num']}): "))
    if openCase == playercase['case_num']:
      print(f"You won ${playercase['case_val']}")
      exit()
    elif openCase == cases[0]['case_num']:
      print(f"You won ${cases[0]['case_val']}")
      exit()
    

# """Round # of Cases to
# Round 1: 6 cases to open
# Round 2: 5 cases to open
# Round 3: 4 cases to open
# Round 4: 3 cases to open
# Round 5: 2 cases to open
# Round 6: 1 case to open
# Round 7: 1 case to open
# Round 8: 1 case to open
# Round 9: 1 case to open """
