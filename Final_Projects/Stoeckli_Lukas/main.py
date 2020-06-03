import pew
from microqiskit import QuantumCircuit, simulate


# init pew
pew.init()
screen = pew.Pix()


# --- QUANTUM STUFF ---

# NOT gate
def X():
  global food, foodB
  if foodB == 3: # food
    foodB = 0
    food = False
  elif foodB == 0: # not food
    foodB = 3
    food = True
  elif foodB == 1: # hadamarded food
    food = not food

# Hadamard gate
def H():
  global food, foodB
  if foodB == 3: # food
    foodB = 1
  elif foodB == 0: # not food
    foodB = 1
  elif foodB == 1: # hadamarded food
    if food == True: # |->
      foodB = 3
    else: # |+>
      foodB = 0

# get random number with 'bits' bits
# use hadamard gate to create random number
# microqiskit can have circuits with 1 or 2 qubits, so we need
# to repeat the below cirquit for each bit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
def randBits(bits):
  number = 0
  for i in range (bits):
    bit = simulate(qc, shots=1, get='memory')
    if bit[0][0] == '1':
      number += 2**i
  return number






# --- GAME ---

# init variables 
up, down, left, right = 0, 0, 0, 0
snek = []
speed = 0
food = True
foodX, foodY, foodB = 0, 0, 0

def placeFood():
  global food, foodX, foodY, foodB
  global snek
  global screen
  # get new food
  foodX, foodY = snek[0]
  while (foodX, foodY) in snek:
    foodX = randBits(3)
    foodY = randBits(3)
  foodS = randBits(2)
  if foodS == 0: # |0>
    foodB = 0
    food = False
  elif foodS == 1: # |+>
    foodB = 1
    food = False
  elif foodS == 2: # |->
    foodB = 1
    food = True
  elif foodS == 3: # |1>
    foodB = 3
    food = True

# init/reset game state
def initGame():
  # init direction
  global up, down, left, right
  up, down, left, right = 0, 0, 0, 0
  direction = randBits(2)
  if direction == 0:
    up = 1
  elif direction == 1:
    down = 1
  elif direction == 2:
    left = 1
  elif direction == 3:
    right = 1
  # init position of snake
  global snek
  snek = [(randBits(3), randBits(3))]
  # init speed
  global speed
  speed = 2.7
  # place food
  placeFood()

# game over, print message
def gameOver():
  for i in range(8):
    for j in range(8):
      screen.pixel(i, j, 0)
  message = pew.Pix.from_text("Gameover!")
  for i in range(-8, message.width):
    screen.blit(message, -i, 1)
    pew.show(screen)
    pew.tick(1/10)
  initGame()

# get pushed buttons
def getUserInput():
  global up, down, left, right
  keys = pew.keys()
  if keys & pew.K_UP:
    up, down, left, right = 1, 0, 0, 0
  elif keys & pew.K_DOWN:
    up, down, left, right = 0, 1, 0, 0
  elif keys & pew.K_LEFT:
    up, down, left, right = 0, 0, 1, 0
  elif keys & pew.K_RIGHT:
    up, down, left, right = 0, 0, 0, 1
  elif keys & pew.K_X:
    X()
  elif keys & pew.K_O:
    H()




# --- MAIN ---

initGame()
while 1:
  # print head of snek
  x, y = snek[-1]
  screen.pixel(x, y, 3)
  pew.show(screen)
  pew.tick(1 / speed)

  # draw food
  screen.pixel(foodX, foodY, foodB)

  # get user input
  getUserInput()

  # update coords
  x = (x - left + right) % 8
  y = (y - up + down) % 8 # 0, 0 is in the top left corner

  # game over
  if (x, y) in snek:
    gameOver()
    continue

  # append current position to snek
  snek.append((x, y))

  # eat
  if x == foodX and y == foodY:
    if foodB == 1:
      # hadamarded food
      foodBit = randBits(1)
      if foodBit == 0:
        foodB = 0
        food = False
    if foodB == 0:
      # not food
      if len(snek) == 2:
        gameOver()
        continue
      for i in range(2):
        snekTailX, snekTailY = snek.pop(0)
        screen.pixel(snekTailX, snekTailY, 0)
    # get new food
    placeFood()
    # increase speed
    speed += 0.2
  else:
    # remove tail
    snekTailX, snekTailY = snek.pop(0)
    screen.pixel(snekTailX, snekTailY, 0)
