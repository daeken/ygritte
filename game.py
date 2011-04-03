from pygame import *

import types
from level import Level
from player import Player
from renderer import Renderer

inputHandlers = {}

class Game(object):
	def __init__(self):
		global inputHandlers
		inputHandlers = dict((k, types.MethodType(v, self, Game)) for k, v in inputHandlers.items())

		self.renderer = Renderer(self)
		self.level = Level.spawn(self, 0)
		self.player = Player(self)
		self.level.move(self.player.pos)
		self.enemies = []
		self.keys = {}
	
	def run(self):
		self.renderer.run()
	
	def tick(self):
		self.player.update()
	
	def handleInput(self, event):
		if event.type in inputHandlers:
			inputHandlers[event.type](event)
	
	def handle(type):
		def sub(func):
			inputHandlers[type] = func
			return func
		return sub

	@handle(QUIT)
	def quit(self, event):
		self.renderer.quit()
	
	@handle(KEYDOWN)
	def keydown(self, event):
		self.keys[event.key] = True
		if event.key == K_UP:
			self.player.enginesOn = True
		elif event.key == K_RIGHT:
			self.player.turning = -1 if K_LEFT not in self.keys or not self.keys[K_LEFT] else 0
		elif event.key == K_LEFT:
			self.player.turning = 1 if K_RIGHT not in self.keys or not self.keys[K_RIGHT] else 0
		elif event.key == K_ESCAPE:
			self.renderer.quit()
		elif event.key == K_SPACE:
			self.player.shooting = True
	
	@handle(KEYUP)
	def keyup(self, event):
		self.keys[event.key] = False
		if event.key == K_UP:
			self.player.enginesOn = False
		elif event.key == K_RIGHT:
			self.player.turning = 0 if K_LEFT not in self.keys or not self.keys[K_LEFT] else 1
		elif event.key == K_LEFT:
			self.player.turning = 0 if K_RIGHT not in self.keys or not self.keys[K_RIGHT] else -1
		elif event.key == K_SPACE:
			self.player.shooting = False
