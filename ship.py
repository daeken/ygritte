from asset import Asset

class Ship(object):
	def __init__(self, game, id, twoStage=False):
		self.game = game
		if twoStage:
			self.low = Asset.load('ship%i_low' % id)
			self.high = Asset.load('ship%i_high' % id)
		else:
			self.low = self.high = Asset.load('ship%i')
		self.fixedPos = None
		self.pos = (0, 0)
		self.rot = 0
		self.enginesOn = False
	
	@property
	def state(self):
		return self.high if self.enginesOn else self.low

	def draw(self, surface):
		self.state.draw(surface, self.pos if self.fixedPos == None else self.fixedPos, rotation=self.rot)
	
	@property
	def rect(self):
		return self.state.rect(self.pos if self.fixedPos == None else self.fixedPos, self.rot)
