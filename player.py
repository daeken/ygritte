from math import cos, sin, pi

from ship import Ship

epsilon = 0.001
shootSpeed = 10
gravity = 0

class Player(Ship):
	def __init__(self, game):
		Ship.__init__(self, game, 0, twoStage=True)
		self.pos = (400, 300)
		self.accel = (0, 0)
		self.accelFactor = 0.4
		self.turning = 0
		self.shooting = False
		self.shootCounter = 0
	
	def update(self):
		self.accel = (self.accel[0]/1.06, self.accel[1]/1.06)
		if self.enginesOn:
			a = self.rot*pi/180
			x = self.accelFactor * sin(a)
			y = self.accelFactor * cos(a)
			self.accel = (self.accel[0]+x, self.accel[1]+y)
		
		if self.turning:
			self.rot = (self.rot + 10*self.turning) % 360

		self.game.level.move((self.accel[0], self.accel[1]-gravity))

		if self.shooting:
			if self.shootCounter == 0:
				pass#self.game.addBullet(self.rot, self.accel, )
			self.shootCounter = (self.shootCounter + 1) % shootSpeed
