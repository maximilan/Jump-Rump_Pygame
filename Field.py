import sys, pygame
class Field():

	def __init__(self, x, y, toBePlaced):
		self.x = x
		self.y = y
		self.design = None
		if toBePlaced == True:
			return x, y


class Block(Field):

	def __init__(self, screen, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		self.design = pygame.image.load("blockdesign.png").convert_alpha()
		self.rect = self.design.get_rect()
		self.rect = self.rect.move([x,y-5])
		self.screen.blit(self.design, self.rect)

	def show(self):
		self.rect = self.design.get_rect()
		self.rect = self.rect.move([self.x,self.y-5])
		self.screen.blit(self.design, self.rect)


class Movement_Unit():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.movable = True
	def setMovementStatus(self, movementStatus):
		self.movable = movementStatus
