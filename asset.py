import pygame

class Asset(object):
	def __init__(self, name):
		self.image = pygame.image.load('assets/%s.png' % name)
		self.size = self.image.get_size()
		self.hsize = self.size[0]/2, self.size[1]/2
		self.cacheRot = {0: (self.image, self.hsize)}
		self.doubleImage = pygame.transform.scale2x(self.image)
	
	def draw(self, surface, pos, rotation=0, center=True):
		rotation %= 360
		if rotation not in self.cacheRot:
			im = pygame.transform.rotate(self.doubleImage, rotation)
			size = im.get_size()
			hsize = size[0]/2, size[1]/2
			im = pygame.transform.scale(im, hsize)
			size = im.get_size()
			hsize = size[0]/2, size[1]/2
			self.cacheRot[rotation] = (im, hsize)
		else:
			im, hsize = self.cacheRot[rotation]
		
		if center:
			pos = pos[0]-hsize[0], pos[1]-hsize[1]
		
		surface.blit(im, pos)

explosions = (
		Asset('explosion0'), 
		Asset('explosion1'), 
		Asset('explosion2'), 
		Asset('explosion3'), 
		Asset('explosion4'), 
	)
