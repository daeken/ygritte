from util import *
from ship import Ship

epsilon = 0.001
shootSpeed = 5
gravity = 0.075
decel = 1.06

class Player(Ship):
	def __init__(self, game):
		Ship.__init__(self, game, 0, twoStage=True)
		self.fixedPos = self.pos = (400, 300)
		self.accel = (0, 0)
		self.accelFactor = 0.4
		self.turning = 0
		self.shooting = False
		self.shootCounter = 0
	
	def update(self):
		self.accel = (self.accel[0]/decel, self.accel[1]/decel-gravity)
		if self.enginesOn:
			x, y = rotatePoint(self.rot, self.accelFactor)
			self.accel = (self.accel[0]+x, self.accel[1]+y)
		
		if self.turning:
			self.rot = (self.rot + 10*self.turning) % 360

		self.pos = (self.pos[0]-self.accel[0], self.pos[1]-self.accel[1])
		self.game.move((self.accel[0], self.accel[1]))

		if self.shooting:
			if self.shootCounter == 0:
				x, y = rotatePoint(self.rot, point=(0, self.state.hsize[1]))
				self.game.addBullet(1, (self.pos[0]+x, self.pos[1]-y), self.rot, self.accel, True)
			self.shootCounter = (self.shootCounter + 1) % shootSpeed
