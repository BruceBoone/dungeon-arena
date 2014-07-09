import pygame, random

class SpriteSheet(object):
	""" Class used to grab images out of a sprite sheet. """
	# This points to our sprite sheet image
	sprite_sheet = None
	def __init__(self, file_name):
		""" Constructor. Pass in the file name of the sprite sheet. """
		# Load the sprite sheet.
		self.sprite_sheet = pygame.image.load(file_name).convert()
	def get_image(self, x, y, width, height):
		""" Grab a single image out of a larger spritesheet
		Pass in the x, y location of the sprite
		and the width and height of the sprite. """
		# Create a new blank image
		image = pygame.Surface([width, height]).convert()
		# Copy the sprite from the large sheet onto the smaller image
		image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
		# Assuming black works as the transparent color
		#image.set_colorkey(constants.BLACK)
		image.set_colorkey((0,0,0))
		# Return the image
		return image

class gold(pygame.sprite.Sprite):
	def __init__(self, inImg):
		pygame.sprite.Sprite.__init__(self)
		self.rect = (32,32)
		self.x = random.randint(133,537)
		self.y = random.randint(33,286)
		self.image = inImg
	def update(self):
		self.rect = (self.x, self.y)
	def setImage(self, inImage):
		self.image = inImage
	def getX(self):
		return self.x
	def getY(self):
		return self.y
		
class hero(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = 33
		self.y = 160
		self.rect = pygame.Rect(32, 32, 16, 16)
		#self.rect = (32,32)
		self.health = 100
		self.gold = 0
	def update(self):
		self.rect = (self.x, self.y)
	def takeGold(self):
		self.gold += 1
	def getGold(self):
		return self.gold
	def resetHealth(self):
		self.health = 100
	def getHealth(self):
		return self.health
	def takeHit(self):
		if self.health <= 0:
			return
		self.health -= 2
	def setImage(self, inImage):
		self.image = inImage
	def moveRight(self):
		if self.x > 537:
			return
		self.x +=5
		
	def moveLeft(self):
		if self.x < 33:
			return
		self.x-=5
		
	def moveUp(self):
		if self.y < 33:
			return
		self.y-=5
		
	def moveDown(self):
		if self.y > 286:
			return
		self.y+=5
	def resetPos(self):
		self.x = 33
		self.y = 160
	def getX(self):
		return self.x
	def getY(self):
		return self.y

class enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = random.randint(133,537)
		self.y = random.randint(33,286)
		self.isLoiter = True
		self.rect = (32,32)
		self.loiterTime = 0
		self.loiterDirection = random.randint(1,4)
	def setIsLoiter(self, switch):
		self.isLoiter = switch
	def getIsLoiter(self):
		return self.isLoiter
	def setImage(self, inImage):
		self.image = inImage
	def setLoiterTime(self, inLoiterTime):
		self.loiterTime = inLoiterTime
	def getLoiterTime(self):
		return self.loiterTime
	def setLoiterDirection(self, inLoiterDirection):
		self.loiterDirection = inLoiterDirection
	def getLoiterDirection(self):
		return self.loiterDirection
	def update(self):
		self.rect = (self.x, self.y)
	def moveRight(self):
		if self.x > 537:
			self.loiterDirection = random.randint(1,4)
			return
		self.x +=3
		
	def moveLeft(self):
		if self.x < 33:
			self.loiterDirection = random.randint(1,4)
			return
		self.x-=3
		
	def moveUp(self):
		if self.y < 33:
			self.loiterDirection = random.randint(1,4)
			return
		self.y-=3
		
	def moveDown(self):
		if self.y > 286:
			self.loiterDirection = random.randint(1,4)
			return
		self.y+=3
		
	def getX(self):
		return self.x
	def getY(self):
		return self.y
