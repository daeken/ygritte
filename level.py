from asset import Asset

grid = Asset.load('layer0')
stars = Asset.load('layer1')

class Level(object):
	levels = {}

	def __init__(self, game):
		self.game = game
		self.bg = Asset.load('layer2_outline', mask='layer2_mask')# % self.levelNumber)
		stars.maskOff(self.bg)
		self.i = 0

	@staticmethod
	def spawn(game, number, *args, **kwargs):
		return Level.levels[number](game, *args, **kwargs)

	@staticmethod
	def register(level):
		Level.levels[level.levelNumber] = level
	
	def draw(self, surface):
		grid.draw(surface, (0, 0), center=False)
		stars.draw(surface, self.game.worldOff, center=True)
		self.bg.draw(surface, self.game.worldOff, center=True)
		self.i += 1

@Level.register
class LevelZero(Level):
	levelNumber = 0

	def __init__(self, game):
		Level.__init__(self, game)
