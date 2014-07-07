import pygame, sys, players, math, random, check
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 350), 0, 32)
	
pygame.display.set_caption('Dungeon Arena')
background_image = pygame.image.load("background.png").convert()
heroStartX= 150
heroStartY= 160
firstSkeletonStartX= 450
firstSkeletonStartY= 160
secondSkeletonStartX= 450
secondSkeletonStartY= 200


heroImg = pygame.image.load('hero.png')
player = players.hero(heroStartX,heroStartY)


enemyImg = pygame.image.load('enemy.png')
firstSkeleton = players.enemy(firstSkeletonStartX, firstSkeletonStartY)
secondSkeleton = players.enemy(secondSkeletonStartX, secondSkeletonStartY)
enemySS= players.SpriteSheet("enemyset.png")
firstSkeleton.setImage(enemySS.get_image(0,64,32,32))
secondSkeleton.setImage(enemySS.get_image(0,64,32,32))

player.setImage(enemySS.get_image(96,64,32,32))

actors = pygame.sprite.RenderPlain((player, firstSkeleton, secondSkeleton))

enemies = [firstSkeleton, secondSkeleton]

countLoiter = 0
randomDirection = random.randint(1,4)


		
def heroMove(direction):
	if direction == "right":
		if count == 1:
			player.setImage(enemySS.get_image(96,64,32,32))
		elif count == 2:
			player.setImage(enemySS.get_image(128,64,32,32))
		elif count == 3:
			player.setImage(enemySS.get_image(160,64,32,32))
	elif direction == 'left':
		if count == 1:
			player.setImage(enemySS.get_image(96,32,32,32))
		elif count == 2:
			player.setImage(enemySS.get_image(128,32,32,32))
		elif count == 3:
			player.setImage(enemySS.get_image(160,32,32,32))
	elif direction == 'down':
		if count == 1:
			player.setImage(enemySS.get_image(96,0,32,32))
		elif count == 2:
			player.setImage(enemySS.get_image(128,0,32,32))
		elif count == 3:
			player.setImage(enemySS.get_image(160,0,32,32))
	elif direction == 'up':
		if count == 1:
			player.setImage(enemySS.get_image(96,96,32,32))
		elif count == 2:
			player.setImage(enemySS.get_image(128,96,32,32))
		elif count == 3:
			player.setImage(enemySS.get_image(160,96,32,32))
		
		
		
count = 1
while True: # the main game loop
	
	DISPLAYSURF.blit(background_image,[0,0])
	
	#check held keys
	state = pygame.key.get_pressed()
	if state[K_LEFT]==True:
		player.moveLeft()	
		heroMove('left')
	if state[K_RIGHT]==True:
		player.moveRight()
		heroMove('right')
	if state[K_UP]==True:
		player.moveUp()
		heroMove('up')
	if state[K_DOWN]==True:
		player.moveDown()
		heroMove('down')
		
	for event in pygame.event.get():
		#check for newly pressed keys
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.moveLeft()
				heroMove('left')
			if event.key == pygame.K_RIGHT:
				player.moveRight()
				heroMove('right')
			if event.key == pygame.K_UP:
				player.moveUp()
				heroMove('up')
			if event.key == pygame.K_DOWN:
				player.moveDown()
				heroMove('down')

				
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	
	check.combatRange(player, enemies, enemySS, count)
	
	#playerRect = pygame.Rect(player.getX(),player.getY(),50,50)
	#enemyRect = pygame.Rect(enemy.getX(),enemy.getY(),50,50)
	
	#if playerRect.contains(enemyRect):
		#print True
	
	#print combatGap
	#print player.getX()
	#print player.getY()
	
	
	actors.clear(DISPLAYSURF, background_image)
	actors.update()
	actors.draw(DISPLAYSURF)
	
	#DISPLAYSURF.blit(heroImg,(player.getX(),player.getY()))
	#DISPLAYSURF.blit(enemyImg,(enemy.getX(),enemy.getY()))
	
	pygame.display.flip()
	#pygame.display.update()
	fpsClock.tick(FPS)
	
	if count == 3:
		count = 0
	count +=1
	
	
	#if enemy.getIsLoiter() == True:
		#tempcount = enemy.getLoiterTime() +1
		#enemy.setLoiterTimer(tempcount)
	for enemy in enemies:
		tempcount = enemy.getLoiterTime()
		tempcount +=1
		enemy.setLoiterTime(tempcount)
		
