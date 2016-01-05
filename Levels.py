import Characters as chr
import random
#ADD COMMENTS THROUGHOUT THE GAME! It's gonna get confusing

def level_one(main_character):#main_character is an input to add the player class, so the stats get updated
	Pride = chr.Pride() #Defining the first enemy class (Located in Characters.py file)
	
	#Intro to level one
	print """
  _________                           ________                     .___.__            _________.__               
 /   _____/ _______  __ ____   ____   \______ \   ____ _____     __| _/|  | ___.__.  /   _____/|__| ____   ______
 \_____  \_/ __ \  \/ // __ \ /    \   |    |  \_/ __ \\\\__  \   / __ | |  |<   |  |  \_____  \ |  |/    \ /  ___/
 /        \  ___/\   /\  ___/|   |  \  |    `   \  ___/ / __ \_/ /_/ | |  |_\___  |  /        \|  |   |  \\___ \ 
/_______  /\___  >\_/  \___  >___|  / /_______  /\___  >____  /\____ | |____/ ____| /_______  /|__|___|  /____  >
        \/     \/          \/     \/          \/     \/     \/      \/      \/              \/         \/     \/ 
	"""
	raw_input(">")
	print """ 
	LEVEL 1 \n\n
	It's hard to tell where you are, but you just appeared in an unknown land. It's bare, 
	rocky, and dessert-like. You see a small man standing in front of you. 
	He has an annoying smirk on his face as he admires his reflection on his broadsword.
	It's FAR larger than any broadsword should be, almost the size of his body, in both
	length AND width. But he doesn't seem to notice.
	\n\n"""
	raw_input(">")
	print"\tYou don't want to fight, but you know his type. You can't rationalize with him."
	print "\tThe little man throws you a sword and an odd dodecahedrom shaped pill to get you started\n\n"
	raw_input(">")
	print """
	You swallow the pill and feel a rush of energy in your veins.\n\n
	You have acquired the 'water bubble' ability. Press '1' to use it in battle.
	The water bubble is a defensive move that has a 50% chance to reflect an attack.\n
	Your sword grants you an attack power of 5.\n
	The man introduces himself to you, 'Pride...That's what they call me' he says.
	'No need to thank me for the battle aids, my friend. It will only prolong your suffering.'\n
	Pride tries to lunge at you, but is weighed down by his broadsword. So he slowly walks
	to you instead, draging the beast of a weapon behind him.\n\n
	THE BATTLE COMMENCES!!"""
	main_character.ability = 'Sword' #add new ability
	main_character.attack += 5 #add new attack damage
	
	main_character.battle(Pride)#begin battle sequence
	return main_character.health
	
def level_two(main_character):#Second level of the game, fight against gluttony
	Gluttony = chr.Gluttony()#Getting the enemy, gluttony from the Characters.py file
	print """
	LEVEL 2\n\n
	After your unexpected victory against Pride, you notice that the hilt of his sword held
	a pill, similar to the one he gave you. You take the pill. What could go wrong"""
	raw_input(">")
	print """
	You swallow the pill, and start to feel an unbelievable amount of confidence. You also
	feel a surge of power in your veins. It feels almost instinctive to use this magic, and
	you can tell that your sword would just get in the way, so you drop it. You don't really
	know how to use it anyway.\n \tYou have attained the powers of fire and healing! Your attack power is now
	8. You can also heal yourself by the same amount by pressing '2' during battle.
	You may only heal 5 times during any battle\n"""
	main_character.ability ='Fire'#Remove sword to replace with fire
	main_character.attack += 3 #increase attack damage
	raw_input(">")
	print "\tThe rush of power knocks you out, and you wake up in a HUGE KFC!"
	raw_input(">")
	print """
	Beside a 4 storey tall mountain of chicken bones, there is a really fat bear wearing a bib.
	This is the first time you've seen a bear with greater width than height. It's quite impressive.
	The bear snarls at you, as it thinks you're gonna eat it's food. He doesn't understand human
	speak. So talking to him is useless.\n"""
	raw_input(">")
	print """
	Unfortunately, due to his severe cholesterol problems, the bear needs to rest quite often. He wants to end this quick!
	\n\n
	THE BATTLE BEGINS!"""
	
	
	main_character.battle(Gluttony)
	return main_character.health
	
def level_three(main_character): # Make this the final level for now
	Envy = chr.Envy()
	print """
	LEVEL 3\n\n
	After defeating Gluttony, you ate some of his KFC, replenishing your health!\n
	While eating, you accidentally drank a magic potion that you thought was soda. Fortunately, you didn't die.
	Instead, you could feel your strength growing, your attack and healing increases by 5. You also gained the 
	power of lightning.\n
	By pressing '3' during battle, you deal 30 damage. You can only use this ability 3 times during a battle.\n\n"""
	main_character.attack += 5
	main_character.health = 100
	raw_input(">")
	print "\tYour health is now %d\n" %main_character.health
	raw_input(">")
	print"""
	You decide to leave the comfort of the KFC and try to find an exit from this place.\n
	After a long walk towards what looked like a lone tree in the middle of the random city you found yourself in,
	You found what seemed to be a portal to your world. But before you could step in, you are attacked from behind!\n\n"""
	raw_input(">")
	print """
	You see a girl without a face, in front of you. 
	'AH, how great it would be to get through that portal. But alas, with the way I am now, I will be shunned 
	by your kind!
	All I need is your face, kid. So don't mind me, I'll just take a second'
	She says as she lunges at you!"""
	raw_input(">")
	print "\t Envy has %d attack and %d health. She's gonna be tough" %(Envy.attack,Envy.health)
	main_character.battle(Envy)
