import Levels as lvl
import Characters as chr
import sys
import time

def main():#Run entire game
	player = chr.Player()
	lvl.level_one(player)
	
	if player.health>0:#run the next level if the player isn't dead
		print "Holy shizzle, your health is still %d\n" %player.health
		lvl.level_two(player)
		
		if player.health >0:#run the next level if the player isn't dead
			print "Holy shizzle, your health is still %d\n" %player.health
			lvl.level_three(player)
			
			if player.health >0:
				print """
				You have won the game!! You have defeated your greatest sins!\n
				You make your way through the portal, back to sanity. """
				time.sleep(60)#wait one minute
				
			else:
				print "You have lost. You is dead! You lost to Envy, the most unforgiving sin.\n"
				print "Restart game? (y/n)"
				restart = raw_input(">")
				if restart == 'y':
					main()
				else:
					sys.exit()
			
		
		else:
			print "You have lost. You is dead! You lost to Gluttony, the grossest sin\n"
			print "Restart game? (y/n)"
			restart = raw_input(">")
			if restart == 'y':
				main()
			else:
				sys.exit()
	else:
		print "You have lost. You is dead! You lost to Pride, the most abundant sin\n"
		print "Restart game? (y/n)"
		restart = raw_input(">")
		if restart == 'y':
			main()
		else:
			sys.exit()
main()
