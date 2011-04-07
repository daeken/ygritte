from util import *
from asset import Asset

class Bullet(object):
	def __init__(self, game, type, pos, rot, accel, friendly):
		self.game = game
		self.pos = (pos[0]-game.worldOff[0])/2, (pos[1]-game.worldOff[1])/2
		self.rot = rot
		x, y = rotatePoint(self.rot, 10)
		self.accel = (-accel[0]-x, -accel[1]-y)
		self.friendly = friendly
		self.im = Asset.load('bullet%i' % type)
	
	def draw(self, surface):
		self.im.draw(surface, (self.game.worldOff[0]+self.pos[0], self.game.worldOff[1]+self.pos[1]), rotation=self.rot)
	
	def update(self):
		self.pos = self.pos[0]+self.accel[0], self.pos[1]+self.accel[1]
	
	@property
	def rect(self):
		return self.im.rect(self.pos, self.rot)
