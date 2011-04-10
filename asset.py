import pygame

class Asset(object):
	cache = {}

	@staticmethod
	def load(name, mask=None):
		if name in Asset.cache:
			return Asset.cache[name]
		Asset.cache[name] = ret = Asset(name, mask=mask)
		return ret

	def __init__(self, name, mask=None):
		self.orig = self.image = pygame.image.load('assets/%s.png' % name)
		self.mask = None
		if mask:
			self.mask = pygame.image.load('assets/%s.png' % mask)
		self.size = self.image.get_size()
		self.hsize = self.size[0]/2, self.size[1]/2
		self.cacheRot = {0: (self.image, self.hsize)}
		self.doubleImage = pygame.transform.scale2x(self.image)
	
	def maskOff(self, asset):
		assert asset.mask != None
		mask = asset.mask
		self.image = self.orig.copy()
		isize = self.size
		msize = mask.get_size()
		size = (min(isize[0], msize[0]), min(isize[1], msize[1]))
		self.image.lock()
		mask.lock()
		print 'Masking'
		for x in xrange(isize[0]):
			for y in xrange(isize[1]):
				if x >= size[0] or y >= size[1] or mask.get_at((x, y))[3] == 0:
					self.image.set_at((x, y), (0, 0, 0, 0))
		print 'Done'
		self.image.unlock()
		mask.unlock()
		self.cacheRot = {0: (self.image, self.hsize)}
	
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

#explosions = (
#		Asset('explosion0'), 
#		Asset('explosion1'), 
#		Asset('explosion2'), 
#		Asset('explosion3'), 
#		Asset('explosion4'), 
#	)
