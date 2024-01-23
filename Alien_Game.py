#Alien_Game


#greets the user
print("Welcome to Alien Game")


#this sets the karmic scale's points to 0
good_Karma = 0
bad_Karma = 0


#this sets the user's health
health = 3


#this makes sure you will always have to enter a valid answer
attempts = True


#this loop keeps asking the user if they would like to play, and displays the appropriate message based on the user's response
while attempts == True:
    play = input("Would you like to play? click 1 if yes, click 2 if no: ")
    if play == "1":
        print("Let's get started ")
        #prints a blank line so wording can be spaced out
        print()
        break
    elif play == "2":
        print("I'll be here until you're ready")
        print()
    else:
        print("invalid option, please try again")
        print()


#this entire block until the comment that indicates the end, asks the user for the information to personalize the game to their liking
print("Before we start, we're gonna need some information from you, to personalize the experience, please answer the following questions: ")
name = input("What would you like your name to be? ")
print()
print("Now choose the class you would like to play as, here are your options: ")
print("1. Guardian | Legendary defenders of Earth that specialize in the protection of their people. Grants 2 extra HP")
print("2. Champion | Noble warriors of earth who specialize in taking out anything that threatens Earth. Grants 1 extra damage")
print("3. Citizen | A regular Ol' civilian who lives in the city. Meant for experienced players, hard mode")
print()


#this block changes the class based on the number chosen by the player, also returns the value if the value chosen was invalid until it's chosen
while attempts == True:
    pClass = input("Now, which one would you like to be? (Guardian, Champion, or Citizen):  ")
    if pClass == "Guardian":
        pClass == "Guardian"
        health = health + 2
        print()
        break
    elif pClass == "Champion":
        pClass == "Champion"
        print()
        break
    elif pClass == "Citizen":
        pClass == "Citizen"
        print()
        break
    else:
        print("Invalid option, try again")
        print()


city = input("Please enter the name of the city you're defending: ")
print()
#the code above is the last in the entire block for the personalization section


#this is the introduction    
print(f"Your name is {name}, you're 28 years old, and you have the honor of being a {pClass} for the last city left on earth {city}. As a {pClass} you're one of the last lines of defense on Earth against attacks from extraterrestrial threats. The most recent threats have come from an alien race known as the Legion, a group of aliens bent on destroying what's left of planet Earth. Knowing this threat, you’re alert 24/7, ready to strike back at any given moment. However, unfortunately, the Legion decided to strike while you were sound asleep. Welcome, to Alien Game")
print("your choices will now begin, based on certain choices, they'll add points to your karmic scale. The karmic scale will have 2 sides, Good or Bad, it will function based on the amount of karmic points you have towards either side, which will in turn, decide the ending you will achieve. ")
print()
print("1. You wake up to the sounds of explosions, and distant screams, curious, you open your blinds to see that the legion is wreaking havoc across your hometown. Unfortunately for you, the armory is shut down due to the damages from the Legion, so you rush around to find a weapon, managing to spot a few possible options. Which one will you take?")
print("A) slingshot")
print("B) kitchen knife")
print("C) dinner plate")


while attempts == True:
    choice1 = input("(Slingshot, Knife, or Plate: Your choice: ")
    if choice1 == "Slingshot":
        print("You pick up the slingshot, unfortunately for you, there is no ammo, so your weapon is useless.")
        break
    elif choice1 =="Knife":
        print("You pick up the kitchen knife, which is a little dull, but works as a last-minute choice for a weapon.")
        break
    elif choice1 == "Plate":
        print("You pick up the dinner plate, which works as a somewhat good defense against attacks.")
        break
    else:
        print("Invalid option, please pick again")
#This will be repeated throughout the rest of the code, which if the health variable ever reaches 0, the game will be over
if health == 0:
    print("Game over, you died")
    exit()


print()
print("2. A flying alien swoops into your kitchen, spraying glass from broken windows all over your floor. The alien is about 3 times your size, with large jaws filled with sharp teeth, and large eyes that stare through your soul. How do you wish to fight?")
print("A) Attack it head-on")
print("B) Run away into the streets")
print("C) Curl into a ball and cry")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice2 = input("(A, B or C) Your choice: ")
    if choice2 == "A" and pClass == "Champion":
        print(f"You fight the alien head-on, swinging your {choice1} at it, doing minimal damage. Luckily, this alien was not as strong as it looked and got scared and ran away. You walk out your front door to see the apocalyptic scene the legion created. There is fire spreading all around the city, collapsed buildings, and people scrambling to find loved ones.")
        break
    elif choice2 == "A" and pClass == "Guardian":
        print("You defeat the alien, but you took serious damage in the process (-1 hp) You walk out your front door to see the apocalyptic scene that the legion has created. There is fire spreading all around the city, collapsed buildings, and people scrambling to find loved ones.")
        health = health - 1
        break
    elif choice2 == "A" and pClass == "Citizen":
        print("You defeat the alien, but you took serious damage in the process (-1 hp) You walk out your front door to see the apocalyptic scene that the legion has created. There is fire spreading all around the city, collapsed buildings, and people scrambling to find loved ones.")
        health = health - 1
        break
    elif choice2 == "B":
        print("You flee out the back door into the streets, luckily, the alien behind you stumbles on your furniture, giving you time to escape. You walk out to see the apocalyptic scene that the legion has created. There is fire spreading all around the city, collapsed buildings, and people scrambling to find loved ones.")
        break
    elif choice2 == "C":
        print("The alien decides you are too weak even to bother fighting, and promptly exits to find new prey. You follow it out the door to see the apocalyptic scene the legion created. There is fire spreading all around the city, collapsed buildings, and people scrambling to find loved ones.")
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()


print()
print("3. You hear a young man's voice, begging for help at what is left of the house next to yours. You rush over to find a teenager around 16 years old trapped under a beam of the destroyed house. What do you do?:")
print("A) Attempt to help him out of the rubble")
print("B) Leave him to die")
print("C) Call out for help")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice3 = input("(A, B or C) Your choice: ")
    if choice3 == "A":
        print(f"You attempt to lift the beam that the boy is trapped under, barely moving it enough for him to wiggle out. He thanks you and leaves immediately, saying that he needs to find his mom.")
        good_Karma = good_Karma + 1
        break
    elif choice3 == "B":
        print("You choose to ignore the boy's desperate cry for help, leaving him to either be found by an alien or bleed out.")
        bad_Karma = bad_Karma + 1
        break
    elif choice3 == "C":
        print("You call out desperately for help, but nobody answers. Leaving you with no choice but to try and move the beam. You attempt to lift the beam that the boy is trapped under, barely moving it enough for him to wiggle out. He thanks you and leaves immediately, saying that he needs to find his mom.")
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()


print()
print("4. After parting ways with the boy, you decide to roam the streets to find more people to help. You stumble upon another guardian of the city, who tells you that all of the guardians are meeting at the town hall, which is at the center of the city. What would you like to do:")
print("A) Go to the town hall")
print("B) Refuse")
print("C) Punch the Guardian in the face")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice4 = input("(A, B or C) Your choice: ")
    if choice4 == "A":
        print("You decide to make the journey to the town hall, however, a thick line of aliens block your path. Leaving you with no choice but to find another way")
        break
    elif choice4 == "B":
        print("You decide to refuse to go to the town hall, and attempt to find more people to help. Unfortunately, a thick line of aliens surrounds the city, leaving you with no choice but to follow the path to the town hall")
        break
    elif choice4 == "C":
        print("You swing your fist at the guardian, but miss completely and fall to the ground. The guardian then stomps on your skull, killing you.")
        health = 0
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()


print()
print("5. As you go down the different path, a small alien the size of a rat approaches you and starts to run circles around you. He doesn’t seem to pose a threat.")
print("A) Kick the rat alien as far as you can")
print("B) Attack the rat alien with your weapon")
print("C) Ignore the rat alien")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice5 = input("(A, B or C) Your choice: ")
    if choice5 == "A":
        print("You kick the alien like a soccer ball, sending it 40 yards away from you.")
        break
    elif choice5 == "B":
        print(f"You swing your {choice1} at the alien, but it's like trying to spear a fish in the water. It continues to run circles around you, and eventually, you get dizzy trying to follow it and fall over. You hit the rat with your {choice1}, right as it takes a bite out of your leg. (-1 hp)")
        break
    elif choice5 == "C":
        print("The alien continues to run circles around you, and after about 30 seconds of this, 20 more rat-like aliens start to surround you. They all pounce towards you at once, ending your life slowly and painfully.")
        health = 0
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()


print()
print("6. After killing the alien rat, all the attention is drawn onto you, and a thick wall of aliens slowly move towards you. You have 0 chance of winning against that many enemies, what do you do?")
print("A) Nah, I'd win")
print("B) Run in the opposite direction")
print("C) Pretend to be an alien")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice6 = input("(A, B or C) Your choice: ")
    if choice6 == "A":
        print("You run head-on at the wall of aliens, which is suicide, and you die.")
        health = 0
        break
    elif choice6 == "A" and pClass == "Citizen":
        print("You run head-on at the wall of aliens, which is suicide, but somehow, you defy all laws of nature, jumping 20 feet into the sky and taking out every alien one by one with your bare fists. (ACHIEVEMENT UNLOCKED: I’m him.)")
    elif choice6 == "B":
        print("You run away as fast as you can, and manage to duck behind a destroyed phone booth without being seen.")
        break
    elif choice6 == "C":
        print("You start growling aggressively towards the wall of aliens, which they do not seem to like very much, and you get incinerated by a beam of light shot by one of them.")
        health = 0
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()


print()
print(f"7. After trekking through the wreckage of {city} for hours on end, you eventually find yourself at the doors to the town hall. Miraculously, the town hall looks to be in good shape, so you knock on the front door, waiting in anticipation to see if anyone lets you in. Lucky for you, most of the townspeople are alive and well within the town hall. Upon entering, The mayor greets you and explains that most of the defense force is unfortunately dead. He also fills you in on why the aliens are attacking this time. He explains that they’re after a great power hidden within the timelost vault of {city}. Knowing this information you come up with a few options:")
print("A) Kick back and relax while the apocalypse happens. ")
print("B) Go to the vault and obtain the power right now")
print("C) Find the Weaponsmith in the town hall and speak with him before going out.")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice7 = input("(A, B or C) Your choice: ")
    if choice7 == "A":
        print("You walk around the town hall, find a seat, kick back, and crack open a soda. You sit here for a few hours and eventually get obliterated by the Legion’s superweapon they planned on using from the power they obtained from the timelost vault.")
        print("(ACHIEVEMENT UNLOCKED: Taking it Easy)")
        health = 0
        break
    elif choice7 == "B":
        print(f"You burst out the front door of the town hall, ready for action. You run down the block and round the corner to see a large portion of the Legion’s army. They immediately charge you and overwhelm you in an instant. Your {choice1} was useless against them.")
        health = 0
        break
    elif choice7 == "C":
        print(f"You walk around the town hall and eventually stumble upon the weaponsmith. He greets you and says “What can I do for you today my friend?”, “I’m in desperate need of an upgrade”, you responded, “I couldn’t have guessed”, he responded sarcastically. You hand over your {choice1} and he turns it into:")
        if choice1 == "Plate":
            print("The Sentinel’s Shield a circular shield similar to that of Captain America’s, fueled by the void, an energy-like power coloured purple.")
        elif choice1 == "Knife":
            print("The Hammer of Sol, a hammer fueled by fire")
        elif choice1 == "Slingshot":
            print("The Zahlo supercell, a gun fueled by electricity")
        break
    else:
        print("Invalid option, please pick again")


print()
print("8. Upon the gunsmith upgrading your weapon, you thank him and run outside around the corner, coming within the view of the legion’s champion: Vaugrul. What do you do next?")
print("A) Run away")
print("B) Fight them head-on")
print("C) Point them in the direction of the town hall, to distract them from you")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice8 = input("(A, B or C) Your choice: ")
    if choice8 == "A":
        print("You run away from them, however their speed is drastically faster compared to you. The champion catches up to you almost immediately, jumps on you, and squashes you like a bug.")
        health = 0
        break
    elif choice8 == "B" and choice1 == "Plate":
        print("You run towards them, throwing the shield into the crowd of combatants. The shield bounces off one, then another, and another, and so on, taking out all of the peons, leaving just you and the champion. The champion attempts to incinerate you with his fire, however, you stand your ground and absorb the damage with the shield, which charges it, glowing purple. You run as fast as you can toward the champion, leaping upwards with all your strength, and slamming the shield onto its heading, creating an energy shockwave of purple that kills the legion’s champion. The void energy stole the lifeforce of the champion, giving it to you (+ 1 health)")
        health = health + 1
        good_Karma = good_Karma + 2
        break
    elif choice8 == "B" and choice1 == "Knife":
        print("The peons charge you, and you take them out with ease just after a few swings of your hammer, charging it with solar energy. The champion then looks towards you, with fury in its eyes. As it charges you, you slam the hammer down onto the ground with a force that matches an earthquake's, creating a wave of solar energy that explodes in contact with the champion, incinerating it.")
        good_karma = good_Karma + 2
        break
    elif choice8 == "B" and choice1 == "Slingshot":
        print("You immediately take fire upon the peons killing a few of them with just a few magazines of it. Doing this charged it with electricity that can be discharged. The champion then begins charging you. As it's doing this, you press a button that discharges the the electrical charge. After you did this, you opened fire on the champion, with your magazine seamlessly refusing to run out of ammo, and your bullets electrifying the champion, killing it.")
        good_karma = good_Karma + 2
        break
    elif choice8 == "C":
        print("You point the aliens towards the town hall, upon them seeing this, they immediately start towards the town hall, demolishing it in an instant, allowing you to escape.")
        bad_Karma = bad_Karma + 3
        health = 0
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()


print()
print("9. After your victory with the champion, you keep moving through the city towards the timelost vault. On your journey, you spot a lady hiding in some rubble, as an alien from the Legion hovers above trying to find her. What do you do?")
print("A) Stay quiet and wait for the alien to find her, allowing you to run")
print("B) Yell out to draw the attention of the alien")
print("C) Run for it")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice9 = input("(A, B or C) Your choice: ")
    if choice9 == "A":
        print("You allow the alien the time to find the lady hiding in the rubble, which gives you time to sneak by and run past.")
        bad_Karma = bad_Karma + 1
        break
    elif choice9 == "B":
        print("You yell and successfully gain the aliens attention, drawing him towards you and allowing the lady to escape. However, the alien pounces towards you, knocking you over before you kill it with your weapon. (-1 hp)")
        good_Karma = good_Karma + 1
        health = health - 1
        break
    elif choice9 == "C":
        print("You run as fast as you can, but you make too much noise and the alien sees you. It then swoops in and picks you up before swallowing you whole.")
        health = 0
        break
    else:
        print("Invalid option, please pick again")


if health == 0:
    print("Game over, you died")
    exit()

print()
print("10. You finally made your way to the timelost vault, where surprisingly, there are no aliens around. You open up the vault to see the massive superweapon in all of its glory. What would you like to do with it?:")
print("A) Use it to kill off the aliens")
print("B) Destroy it")
print("C) Leave it there")
print()
print(f"Your health is: {health}")


while attempts == True:
    choice10 = input("(A, B or C) Your choice: ")
    if choice10 == "A":
        print("You pick up the superweapon, and walk out into the city, using it like a railgun to completely eradicate every alien in sight.")
        good_Karma = good_Karma + 100
        break
    elif choice10 == "B":
        print("You use your weapon to fully destroy the superweapon, leaving no more opportunity for the aliens to use it on humans. However, aliens still stay on earth hunting humans, and everyone who survives will forever live in terror and fear.")
        break
    elif choice10 == "C":
        print("You choose to leave the superweapon, allowing the aliens free access to eradicate all of humankind. Which they do, killing you in the process.")
        health = 0
        bad_Karma = bad_Karma + 100
        break
    else:
        print("Invalid option, please pick again")

print()
if good_Karma > bad_Karma:
    print("Good ending: Despite the hard times experienced throughout the war between humans and aliens, you are seen as a hero, and the savior of earth.")
elif bad_Karma > good_Karma:
    print("Bad ending: Despite the hard times experienced throughout the the war between humans and aliens, you are seen as the newest champion of the aliens, and one of the destroyers of earth.")

if health == 0:
    print("Game over, you died")
    exit()