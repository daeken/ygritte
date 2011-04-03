from asset import Asset

class Level(object):
	levels = {}

	def __init__(self, game):
		self.game = game
		self.bg = Asset('bg_level%i' % self.levelNumber)
		self.i = 0
		self.pos = 0, 0

	@staticmethod
	def spawn(game, number, *args, **kwargs):
		return Level.levels[number](game, *args, **kwargs)

	@staticmethod
	def register(level):
		Level.levels[level.levelNumber] = level
	
	def move(self, off):
		self.pos = (self.pos[0]+off[0], self.pos[1]+off[1])

	def draw(self, surface):
		self.bg.draw(surface, self.pos, center=True)
		self.i += 1

@Level.register
class LevelZero(Level):
	levelNumber = 0

	def __init__(self, game):
		Level.__init__(self, game)
