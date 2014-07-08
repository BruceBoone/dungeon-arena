import players, math, random, pygame, time


FPS = 30 # frames per second setting


def distanceCheck(pX, pY, eX, eY):
    a = pX - eX
    b = pY - eY
    c = a**2 + b**2
    distance = math.sqrt(c)
    return distance

def enemyLoiter(loiterTime, loiterDirection, someEnemy, someSS, count):
	if loiterTime < FPS:	
		#print enemy.getLoiterDirection()
		#print enemy.getIsLoiter()
		if loiterDirection == 1:
			someEnemy.moveUp()
			enemySprit(someEnemy,'1',someSS, count)
		elif loiterDirection == 2:
			someEnemy.moveDown()
			enemySprit(someEnemy,'2',someSS, count)
		elif loiterDirection == 3:
			someEnemy.moveLeft()
			enemySprit(someEnemy,'3',someSS, count)
		elif loiterDirection == 4:
			someEnemy.moveRight()
			enemySprit(someEnemy,'4',someSS, count)
	elif loiterTime >= FPS:
		#print enemy.getLoiterTime()
		#print enemy.getLoiterDirection()
		someEnemy.setLoiterDirection(random.randint(1,4))
		someEnemy.setLoiterTime(0)
	

def combatRange(someHero, someEnemyList, someSS, count):
	for someEnemy in someEnemyList:
		gap = distanceCheck(someHero.getX(), someHero.getY(), someEnemy.getX(), someEnemy.getY())
		if gap <= 100:
			someEnemy.setIsLoiter(False)
			#print "False"
			if someEnemy.getX() - someHero.getX() < 0:
				enemySprit(someEnemy,'4',someSS, count)
				someEnemy.moveRight()
			if someEnemy.getX() - someHero.getX() > 0:
				enemySprit(someEnemy,'3',someSS, count)
				someEnemy.moveLeft()
			if someEnemy.getY() - someHero.getY() < 0:
				enemySprit(someEnemy,'2',someSS, count)
				someEnemy.moveDown()
			if someEnemy.getY() - someHero.getY() > 0:
				enemySprit(someEnemy,'1',someSS,  count)
				someEnemy.moveUp()
		else:
			someEnemy.setIsLoiter(True)
			#print "True"
			enemyLoiter(someEnemy.getLoiterTime(), someEnemy.getLoiterDirection(), someEnemy, someSS, count)

def enemySprit(someEnemy, direction, someSS, count):
	if direction == '4':#right
		if count == 1:
			someEnemy.setImage(someSS.get_image(0,64,32,32))
		elif count == 2:
			someEnemy.setImage(someSS.get_image(32,64,32,32))
		elif count == 3:
			someEnemy.setImage(someSS.get_image(64,64,32,32))
	if direction == '3':#left
		if count == 1:
			someEnemy.setImage(someSS.get_image(0,32,32,32))
		elif count == 2:
			someEnemy.setImage(someSS.get_image(32,32,32,32))
		elif count == 3:
			someEnemy.setImage(someSS.get_image(64,32,32,32))
	if direction == '2':#down
		if count == 1:
			someEnemy.setImage(someSS.get_image(0,0,32,32))
		elif count == 2:
			someEnemy.setImage(someSS.get_image(32,0,32,32))
		elif count == 3:
			someEnemy.setImage(someSS.get_image(64,0,32,32))
	if direction == '1':#up
		if count == 1:
			someEnemy.setImage(someSS.get_image(0,96,32,32))
		elif count == 2:
			someEnemy.setImage(someSS.get_image(32,96,32,32))
		elif count == 3:
			someEnemy.setImage(someSS.get_image(64,96,32,32))

def collisionCheck(somePlayer, enemyList):
	playerRect = pygame.Rect(somePlayer.getX(),somePlayer.getY(),32,32)
	for someEnemy in enemyList:
		enemyRect = pygame.Rect(someEnemy.getX(),someEnemy.getY(),16,16)
		if playerRect.colliderect(enemyRect):
		#if playerRect.contains(enemyRect):
			somePlayer.takeHit()
			print somePlayer.getHealth()

def goldPickup(somePlayer, goldList, actors):
	playerRect = pygame.Rect(somePlayer.getX(),somePlayer.getY(),32,32)
	for someGold in goldList.getList():
		goldRect = pygame.Rect(someGold.getX(),someGold.getY(),8,8)
		if playerRect.colliderect(goldRect) == False:
		#if somePlayer.rect.colliderect(someGold.rect) == False:
			continue
		else:			
			print 'COLLIDED'
			#time.sleep(3)
			goldList.remove(someGold)
			actors.remove(someGold)
			
			somePlayer.takeGold()
			#someGold.kill()
			#goldRect = ""
