# Othello, copyright 2019 Christian Walther

import pew
try:
	import random
except ImportError:
	import urandom as random

import os
if 'PewPew 10.' in os.uname().machine:
	screen2 = pew.Pix()
	def show(p):
		for i in range(len(p.buffer)):
			c = p.buffer[i]
			screen2.buffer[i] = c ^ (c >> 1)
		pew.show(screen2)
else:
	show = pew.show

def lookup(board, x, y):
	return 0 if x < 0 or y < 0 or x >= 8 or y >= 8 else board[y*8 + x]

def move(board, x, y, color):
	if lookup(board, x, y) != 0:
		return None
	turned = False
	newboard = bytearray(board)
	newboard[8*y + x] = color
	for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
		nx = x
		ny = y
		while True:
			nx += dx
			ny += dy
			v = lookup(board, nx, ny)
			if v == 0:
				break
			elif v == color:
				while True:
					nx -= dx
					ny -= dy
					if nx == x and ny == y:
						break
					newboard[8*ny + nx] = color
					turned = True
				break
	return newboard if turned else None

weight = ((50, (0, 7, 56, 63)), (5, (3, 4, 24, 31, 32, 39, 59, 60)), (1, (2, 5, 16, 19, 20, 23, 26, 29, 34, 37, 40, 43, 44, 47, 58, 61)))
def count(board):
	c = [0, 0, 0]
	for w, ii in weight:
		for i in ii:
			c[board[i]] += w
	s = c[1] + c[2]
	return c[2]/s if s != 0 else 0.5

def evaluate(board, color, depth):
	max = -1.0
	maxx = -1
	maxy = -1
	for y in range(8):
		for x in range(8):
			newboard = move(board, x, y, color)
			if newboard:
				if depth == 0:
					c = count(newboard)
					if color == 1:
						c = 1.0 - c
				else:
					othermax = evaluate(newboard, color^3, depth - 1)[0]
					if othermax != -1.0:
						c = 1.0 - othermax
					else:
						c = count(newboard)
						if color == 1:
							c = 1.0 - c
				if c > max or (c == max and random.getrandbits(1) == 0):
					max = c
					maxx = x
					maxy = y
	return max, maxx, maxy

def checkwin(board, passcount):
	c = [0, 0, 0]
	for y in range(8):
		for x in range(8):
			c[board[y*8+x]] += 1
	if c[0] == 0 or c[1] == 0 or c[2] == 0 or passcount >= 2:
		winner = 0
		if c[1] >= c[2]:
			winner |= 1
		if c[2] >= c[1]:
			winner |= 2
		while pew.keys():
			pew.tick(0.1)
		while not pew.keys():
			for y in range(8):
				for x in range(8):
					p = lookup(board, x, y)
					if p & winner:
						r = random.getrandbits(3)
						if y == 7 or lookup(board, x, y+1) != p:
							if r & 3 == 0:
								p = 3
						else:
							if r & 6:
								p = screen.pixel(x, y+1)
							elif r & 1:
								p = 3
					screen.pixel(x, y, p)
			show(screen)
			pew.tick(0.06)
		raise pew.GameOver()

keyhistory = 0
def keyevents():
	global keyhistory
	keys = pew.keys()
	events = keys & (~keyhistory | (keyhistory & (keyhistory >> 8) & (keyhistory >> 16) & (keyhistory >> 24)))
	keyhistory = ((keyhistory & 0x3FFFFF) << 8) | keys
	return events

pew.init()
screen = pew.Pix()
board = bytearray(64)
board[27] = 1
board[28] = 2
board[35] = 2
board[36] = 1
cursorx = 1
cursory = 1

blink = 0
error = 0
turn = 1
difficulty = 2 #0..2
passcount = 0
while True:
	if turn == 2:
		_, x, y = evaluate(board, turn, difficulty)
		if x >= 0 and y >= 0:
			board = move(board, x, y, turn)
			passcount = 0
		else:
			passcount += 1
		turn = 1
		checkwin(board, passcount)
	
	keys = keyevents()
	if keys & pew.K_O:
		newboard = move(board, cursorx, cursory, turn)
		if newboard:
			board = newboard
			turn = turn ^ 3
			passcount = 0
		else:
			error = 4
	if keys & pew.K_X:
		turn = turn ^ 3
		passcount += 1
	if keys & pew.K_RIGHT:
		cursorx = (cursorx + 1) & 7
		error = 0
	if keys & pew.K_LEFT:
		cursorx = (cursorx - 1) & 7
		error = 0
	if keys & pew.K_UP:
		cursory = (cursory - 1) & 7
		error = 0
	if keys & pew.K_DOWN:
		cursory = (cursory + 1) & 7
		error = 0
	checkwin(board, passcount)
	blink = 0 if keys != 0 else (blink + 1) % 6
	
	screen.blit(pew.Pix(8, 8, board))
	if blink < 2 and turn == 1:
		screen.pixel(cursorx, cursory, turn if lookup(board, cursorx, cursory) == 0 and error == 0 else 3)
	if error != 0:
		error -= 1
	show(screen)
	pew.tick(0.06)
