from asset import Asset

class Level(object):
	levels = {}

	def __init__(self, game):
		self.game = game
		self.bg = Asset.load('bg_level%i' % self.levelNumber)
		self.i = 0

	@staticmethod
	def spawn(game, number, *args, **kwargs):
		return Level.levels[number](game, *args, **kwargs)

	@staticmethod
	def register(level):
		Level.levels[level.levelNumber] = level
	
	def draw(self, surface):
		self.bg.draw(surface, self.game.worldOff, center=True)
		self.i += 1

@Level.register
class LevelZero(Level):
	levelNumber = 0

	def __init__(self, game):
		Level.__init__(self, game)
