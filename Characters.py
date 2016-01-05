import random
#Each enemy can be a level by itself, no need for locations

class Character(object): #Template for main character and all 7 bosses. 

	def __init__(self,name,health,attack,ability):
		self.name = name
		self.health = health
		self.attack = attack
		self.ability = ability
			
	
	def is_alive(self):#function to check on main character, should probably use this
		print "%s, %d"%(self.name, self.health)
		return self.health > 0
		
	def abilities(ability):
		pass
		
class Player(Character):
	def __init__(self):
		Character.__init__(self,'Player',100,0,None)
	
	def battle(self,enemy): # Main battle sequence
		healing_usage = 5 #set healing number
		lightning_usage = 3 #set lightning number
		while enemy.health > 0 and self.health >0:
			print "\n\tPress the 'Enter' key to attack, and the number keys to use your special ability"
			power = raw_input(">")
			if power == '1':
				water = random.randint(1,2) #Causes the ability used to only be effective 50% of the time
				if water == 2: #enemy attack is deflected
					print "You successfully deflected the attack"
					enemy.health -= enemy.attack
					print "Your health is %d.\n%s has %d health" %(self.health,enemy.name,enemy.health)
				else:#enemy manages to deal damage, but you don't do any on it
					print "Failed to deflect attack.\n%s attacked you!" %enemy.name
					self.health -= enemy.attack
					print "Your health is %d.\n%s has %d health" %(self.health,enemy.name,enemy.health)
			
			elif power == '2':#use healing ability
				
				if healing_usage>0:
					print "You have healed yourself by %d"%self.attack
					self.health += self.attack
					print "Your health is now %d" %self.health
					healing_usage -= 1
					print "\nYou may only heal %d more times in this battle" %healing_usage
					
				else:
					print "You have used up your heals in this battle"
			
			elif power == '3':#use lightning ability
				
				if lightning_usage>0:
					print "You have dealt 30 damage to %s"%enemy.name
					enemy.health -= 30
					print "His health is now %d" %enemy.health
					lightning_usage -= 1
					print "\nYou may only use this attack %d more times in this battle" %lightning_usage
					
				else:
					print "You have used up your lightning attacks in this battle"
					
			else:#attack with (standard attack)
				print "You attacked with %s.\n%s attacks you" %(self.ability,enemy.name)
				enemy.health -= self.attack
				self.health -= enemy.attack
				print "Your health is %d.\n%s has %d health" %(self.health,enemy.name,enemy.health)
		return self, enemy
		
		
#Main enemies and their stats.
		
class Pride(Character):
	def __init__(self):
		Character.__init__(self,'Pride',30,4,"unknown")
		
class Gluttony(Character):
	def __init__(self):
		Character.__init__(self,'Gluttony',80,10,None)
		
		
		
class Lust(Character):
	def __init__(self):
		Character.__init__(self,'Lust',50,10,None)
	
		
class Greed(Character):
	def __init__(self):
		Character.__init__(self,'Greed',50,10,None)
		
class Sloth(Character):
	def __init__(self):
		Character.__init__(self,'Sloth',200,1,None)#Make the attack a probability. Mostly 0 because he's asleep, but 20 when he attacks

class Wrath(Character):
	def __init__(self):
		Character.__init__(self,'Wrath',50,10,None)

class Envy(Character):
	def __init__(self):
		Character.__init__(self,'Envy',250,14,None)
