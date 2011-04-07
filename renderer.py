import pygame

class Renderer(object):
	def __init__(self, game):
		self.game = game
		self.setup()
	
	def setup(self):
		self.screen = pygame.display.set_mode((800, 600), pygame.HWSURFACE|pygame.DOUBLEBUF)
		self.size = self.screen.get_size()
		self.hsize = self.size[0]/2, self.size[1]/2
		pygame.display.set_caption('Ygritte')
	
	def run(self):
		self.running = True
		clock = pygame.time.Clock()
		while self.running:
			clock.tick(60)
			self.tick()
			#self.sprites.update()
			self.draw()
	
	def quit(self):
		self.running = False
	
	def tick(self):
		self.handleInput()
		self.game.tick()
	
	def handleInput(self):
		while True:
			event = pygame.event.poll()
			if event:
				self.game.handleInput(event)
			else:
				break
	
	def draw(self):
		self.screen.fill((0, 0, 0))
		self.game.level.draw(self.screen)
		self.game.player.draw(self.screen)
		for bullet in self.game.bullets:
			bullet.draw(self.screen)

		pygame.display.flip()
