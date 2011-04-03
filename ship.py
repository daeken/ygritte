from asset import Asset

class Ship(object):
	def __init__(self, game, id, twoStage=False):
		self.game = game
		if twoStage:
			self.low = Asset('ship%i_low' % id)
			self.high = Asset('ship%i_high' % id)
		else:
			self.low = self.high = Asset('ship%i')
		self.pos = (0, 0)
		self.rot = 0
		self.enginesOn = False
	
	def draw(self, surface):
		state = self.high if self.enginesOn else self.low
		state.draw(surface, self.pos, rotation=self.rot)
