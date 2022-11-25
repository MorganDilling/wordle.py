# imports
import random
import time
import os


# dict list
print('Compiling dictionary...')

dictFile = open("wordlist.txt", "r")

dictArr = dictFile.read().split('\n')

dictFile.close()

# functions

# generates a random 5 letter word
def randWord():
  word = dictArr[random.randint(0, len(dictArr))]
  if len(word) != 5:
    word = randWord()
  return word

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    else:
      os.system(command)

# colours
class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m' # used for correct
    WARNING = '\033[93m' # used for correct but wrong place
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# variables
guessing = True
guesses = 6 # default
defGuesses = guesses
word = randWord()

consoleMessage = f"{clr.BOLD}{clr.HEADER}Good luck!{clr.ENDC}"


def main ():
  # globalise
  global guessing
  global guesses
  global consoleMessage
  global word

  # reinit
  guessing = True
  guesses = defGuesses
  word = randWord()
  
  # main
  clearConsole()
  
  print(f'{clr.HEADER}{clr.BOLD}Welcome to Wordle.Py!{clr.ENDC}\nYou have a total of {guesses} guesses.')

  time.sleep(3)

  clearConsole()

  while guessing:
    clearConsole()
    if len(consoleMessage) > 0:
      print(consoleMessage)
    
    inp = input('')
    msg = ""

    if len(inp) > 5:
      print(f'{clr.FAIL}Input cannot exceed 5 letters.{clr.ENDC}')
      time.sleep(3)
      continue

    if len(inp) < 5:
      print(f'{clr.FAIL}Input cannot be less than 5 letters.{clr.ENDC}')
      time.sleep(3)
      continue

    if not inp in dictArr:
      print(f"{clr.FAIL}Not a real word!{clr.ENDC}")
      time.sleep(3)
      continue

    for i in range(5):
      if inp[i] == word[i]:
        msg += f"{clr.OKGREEN}{inp[i]}{clr.ENDC}"
      elif inp[i] in word:
        msg += f"{clr.WARNING}{inp[i]}{clr.ENDC}"
      else:
        msg += f"{inp[i]}"

    # only add newline if console message is 0
    if len(consoleMessage) > 0:
      msg = '\n' + msg

    consoleMessage += msg

    if inp == word:
      guessing = False

      clearConsole()

      print(consoleMessage)
      
      print(f"\n{clr.HEADER}Congrats! You guessed it with {guesses} guess(es) left. {clr.ENDC}")
      break
    else:
      guesses -= 1

    if guesses == 0:
      guessing = False

      clearConsole()

      print(consoleMessage)
      
      print(f"\n{clr.FAIL}You didn't guess the word. The word was {clr.BOLD + clr.UNDERLINE}{word}{clr.ENDC}.")

# init
if __name__ == '__main__':
  main()


# TODO add word definitions at the end