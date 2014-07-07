import pygame, sys, players, math, random, check
from pygame.locals import *

pygame.init()

def main():
	FPS = 30
	fpsClock = pygame.time.Clock()

	# set up the window
	DISPLAYSURF = pygame.display.set_mode((600, 350), 0, 32)

	myfont = pygame.font.SysFont("gothic", 30, bold=True)
	healthLabel = myfont.render("HEALTH", 1, (0,0,0))
	goldLabel = myfont.render("GOLD:", 1, (0,0,0))
	
	deathFont = pygame.font.SysFont("gothic", 60, bold=True)
	deathMsg = deathFont.render("U DIED", 1, (0,0,0))

	pygame.display.set_caption('Dungeon Arena')
	background_image = pygame.image.load("background.png").convert()
	goldImg = pygame.image.load("gold.png").convert()
	goldImg.set_colorkey((0,0,0))
	#the sprite sheet
	enemySS= players.SpriteSheet("enemyset.png")

	player = players.hero()
	player.setImage(enemySS.get_image(96,64,32,32))

	level = 1
	goldLevel = 0
	#def levelGold(level):
		#total = 0
		#while level > 0 :
			#total += level
			#level -= 1
		#print total
		#return total
	
	def spawnCharacters(level):
		loop = 0
		enemies = []
		gold = []
		while loop < level:
			enemies.append(players.enemy())
			gold.append(players.gold(goldImg))
			loop +=1
		for someEnemy in enemies:
			someEnemy.setImage(enemySS.get_image(0,64,32,32))
		actors = pygame.sprite.Group(player)
		actors.add(enemies)
		actors.add(gold)
		goldGroup = pygame.sprite.Group(gold)
		return (enemies, actors, gold)	
		#firstSkeleton = players.enemy()
		#secondSkeleton = players.enemy()

		#firstSkeleton.setImage(enemySS.get_image(0,64,32,32))
		#secondSkeleton.setImage(enemySS.get_image(0,64,32,32))


		

	#enemies = [firstSkeleton, secondSkeleton]
	#actors = pygame.sprite.Group((player, firstSkeleton, secondSkeleton))






			
	def heroMove(direction):
		if direction == "right":
			if spriteCount == 1:
				player.setImage(enemySS.get_image(96,64,32,32))
			elif spriteCount == 2:
				player.setImage(enemySS.get_image(128,64,32,32))
			elif spriteCount == 3:
				player.setImage(enemySS.get_image(160,64,32,32))
		elif direction == 'left':
			if spriteCount == 1:
				player.setImage(enemySS.get_image(96,32,32,32))
			elif spriteCount == 2:
				player.setImage(enemySS.get_image(128,32,32,32))
			elif spriteCount == 3:
				player.setImage(enemySS.get_image(160,32,32,32))
		elif direction == 'down':
			if spriteCount == 1:
				player.setImage(enemySS.get_image(96,0,32,32))
			elif spriteCount == 2:
				player.setImage(enemySS.get_image(128,0,32,32))
			elif spriteCount == 3:
				player.setImage(enemySS.get_image(160,0,32,32))
		elif direction == 'up':
			if spriteCount == 1:
				player.setImage(enemySS.get_image(96,96,32,32))
			elif spriteCount == 2:
				player.setImage(enemySS.get_image(128,96,32,32))
			elif spriteCount == 3:
				player.setImage(enemySS.get_image(160,96,32,32))
			

	roundStart = True		
	spriteCount = 1
	while True: # the main game loop
		
		DISPLAYSURF.blit(background_image,[0,0])
		DISPLAYSURF.blit(healthLabel, (10, 0))
		DISPLAYSURF.blit(goldLabel, (250, 0))
		DISPLAYSURF.blit(myfont.render(str(player.getGold()), 1, (0,0,0)), (310, 0))
		pygame.draw.rect(DISPLAYSURF, (255,0,0), (100,5,player.getHealth()-4, 10))
		if roundStart == True:
			goldLevel += level
			enemies, actors, gold = spawnCharacters(level)
			roundStart = False
		
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
		
		check.combatRange(player, enemies, enemySS, spriteCount)
		
		check.collisionCheck (player, enemies)
		
		check.goldPickup(player, gold, actors)
		
		

		if player.getHealth() <= 0:
			DISPLAYSURF.blit(deathMsg, (160, 200 ))
			pygame.display.flip()
			while roundStart == False:
				for event in pygame.event.get():
					if event.type == KEYDOWN and event.key == K_n:
						pygame.quit()
						sys.exit()
					elif event.type == KEYDOWN and event.key == K_y:
						main()
						
		if player.getGold() == goldLevel:
			player.resetPos()
			roundStart = True
			level +=1
			
		
		actors.clear(DISPLAYSURF, background_image)
		actors.update()
		actors.draw(DISPLAYSURF)
		
		#DISPLAYSURF.blit(heroImg,(player.getX(),player.getY()))
		#DISPLAYSURF.blit(enemyImg,(enemy.getX(),enemy.getY()))
		
		pygame.display.flip()
		#pygame.display.update()
		fpsClock.tick(FPS)
		
		if spriteCount == 3:
			spriteCount = 0
		spriteCount +=1
		
		for enemy in enemies:
			tempcount = enemy.getLoiterTime()
			tempcount +=1
			enemy.setLoiterTime(tempcount)
		
if __name__ == "__main__":
    main()
