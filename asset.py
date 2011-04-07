import pygame

class Asset(object):
	cache = {}

	@staticmethod
	def load(name):
		if name in Asset.cache:
			return Asset.cache[name]
		Asset.cache[name] = ret = Asset(name)
		return ret

	def __init__(self, name):
		self.image = pygame.image.load('assets/%s.png' % name)
		self.size = self.image.get_size()
		self.hsize = self.size[0]/2, self.size[1]/2
		self.cacheRot = {0: (self.image, self.hsize)}
		self.doubleImage = pygame.transform.scale2x(self.image)
	
	def ensureCached(self, rotation):
		rotation %= 360
		if rotation in self.cacheRot:
			return self.cacheRot[rotation]
		else:
			im = pygame.transform.rotate(self.doubleImage, rotation)
			size = im.get_size()
			hsize = size[0]/2, size[1]/2
			im = pygame.transform.scale(im, hsize)
			size = im.get_size()
			hsize = size[0]/2, size[1]/2
			self.cacheRot[rotation] = (im, hsize)
			return im, hsize
	
	def draw(self, surface, pos, rotation=0, center=True):
		im, hsize = self.ensureCached(rotation)
		
		if center:
			pos = pos[0]-hsize[0], pos[1]-hsize[1]
		
		surface.blit(im, pos)
	
	def rect(self, pos, rot=0, center=True):
		hsize = self.ensureCached(rot)[1]
		if center:
			return pygame.Rect(pos[0]-hsize[0], pos[1]-hsize[1], pos[0]+hsize[0], pos[1]+hsize[1])
		else:
			return pygame.Rect(pos[0], pos[1], pos[0]+hsize[0]*2, pos[1]+hsize[1]*2)

explosions = (
		Asset('explosion0'), 
		Asset('explosion1'), 
		Asset('explosion2'), 
		Asset('explosion3'), 
		Asset('explosion4'), 
	)
