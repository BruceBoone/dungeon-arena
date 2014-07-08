import pygame


class goldList:
	def __init__(self,inList):
		self.gold = inList
	def getList(self):
		return self.gold
	def remove(self,someGold):
		self.gold.remove(someGold)

