""" # introduction to the littlebigplanetgenesisedition.py
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂


░██████╗░███████╗███╗░░██╗███████╗░██████╗██╗░██████╗░██████╗░██╗██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝██║██╔════╝██╔════╝░██║██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░██║╚█████╗░██║░░██╗░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗██║░╚═══██╗██║░░╚██╗██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██████╔╝██║██████╔╝╚██████╔╝██║██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝╚═════╝░░╚═════╝░╚═╝╚═╝░░╚═╝


█░░ █ ▀█▀ ▀█▀ █░░ █▀▀ █▄▄ █ █▀▀ █▀█ █░░ ▄▀█ █▄░█ █▀▀ ▀█▀
█▄▄ █ ░█░ ░█░ █▄▄ ██▄ █▄█ █ █▄█ █▀▀ █▄▄ █▀█ █░▀█ ██▄ ░█░

LittleBigPlanet is a puzzle-platformer game for the PlayStation 3, developed by Media Molecule and published by
Sony Computer Entertainment Europe, that allows players to create and share their own levels with other players 
using various objects. The game was released on October 27, 2008. Genesis Edition takes you on a remix version
of that with crafting items and so on! be creative and create your very own level and share it with the world
this program is based off the Littlebigplanet franchise and will rock your socks right off! So what are you waiting
for? Hop right into it sack fellow!


丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺

𝙡𝙞𝙩𝙩𝙡𝙚𝙗𝙞𝙜𝙥𝙡𝙖𝙣𝙚𝙩 𝙬𝙖𝙨 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮 𝙢𝙚𝙙𝙞𝙖 𝙢𝙤𝙡𝙚𝙘𝙪𝙡𝙚

 Github Link: https://github.com/GenesisGir
 Twitch Link: https://www.twitch.tv/genesisgir
 
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
"""

# importing modules/libraries
import os, time, random, sys, webbrowser, winsound
from playsound import playsound


# defining variables/constants

# player status variable
player = "new player"

# sackboy/sackgirl constants
SACKBOY = "Sackboy™" # a friendly creative lot!
SACKGIRL = "Sackgirl™" # sackboy's bestfriend!

# mode constants
CREATIVE = "Create mode"
STORY = "Story mode"

# trophie constants
_100_COMPLETE = "100% Complete trophie" # Earn all LittleBigPlanet™ trophies to unlock this platinum trophy.
THE_GARDENS = "The Gardens trophie" # Complete all levels in The Gardens.
THE_SAVANNAH = "The Savannah trophie" # Complete all levels in The Savannah.
THE_WEDDING = "The Wedding trophie" # Complete all levels in The Wedding.
THE_CANYONS = "The Canyons trophie" # Complete all levels in The Canyons.
THE_METROPOLIS = "The Metropolis trophie" # Complete all levels in The Metropolis 
THE_ISLANDS = "The Islands trophie" # Complete all levels in The Islands.
THE_TEMPLES = "The Temples trophie" # Complete all levels in The Temples.
EXPERT_CREATOR = "Expert Creator trophie" # Complete all levels in the Tutorials.
ARTIST = "Artist trophie" # Place a sticker.
HOMEMAKER = "Homemaker trophie" # Place 10 stickers or decorations in your pod.
FASHION_SENSE = "Fashion Sense trophie" # Choose a costume for your sackperson with at least one item on your head, at least one item on your body, and a material.
TRENDSETTER = "Trendsetter trophie" # Place a sticker or a decoration on another player's sackperson.
FORAGER = "Forager trophie" # Collect 25% of the prize bubbles on the story levels.
STICKY_FINGERS = "Sticky Fingers trophie" # Collect 50% of the prize bubbles on the story levels.
TREASURE_HUNTER = "Treasure Hunter trophie" # Collect 75% of the prize bubbles on the story levels.
_2X_MULTIPLIER = "2X Multiplier! trophie" # Get a 2X Multiplier.
_8X_MULTIPLIER = "8X Multiplier! trophie" # Get a 8X Multiplier.

# trophie progress variables
_100_complete_progress = "locked" 
the_gardens_trophie_progress = "locked"
the_savannah_trophie_progress = "locked"
the_wedding_trophie_progress = "locked"
the_canyons_trophie_progress = "locked"
the_metropolis_trophie_progress = "locked"
expert_creator_progress = "locked"
artist_progress = "locked"
homemaker_progress = "locked"
fashion_sense_progress = "locked"
trendsetter_progress = "locked"
forager_progress = "locked"
sticky_fingers_progress = "locked"
treasure_hunter_progress = "locked"
_2x_multiplier_progress = "locked"
_8x_multiplier_progress = "locked"






# tool constants
POPIT = "Popit"

# tool gadget constants
TOOLS_BAG = "Tools Bag"

""" Tool's bag info

▀█▀ █▀█ █▀█ █░░ █▀   █▄▄ ▄▀█ █▀▀
░█░ █▄█ █▄█ █▄▄ ▄█   █▄█ █▀█ █▄█

The Tools Bag will only appear in your Popit in Create Mode. It contains everything from connectors, logic,
power-ups, hazards, and creature parts to music and sounds. Below is a brief description of each tool and its 
function.

"""

GOODIES_BAG = "Goodies Bag"

""" Goodie's bag info

█▀▀ █▀█ █▀█ █▀▄ █ █▀▀ █▀   █▄▄ ▄▀█ █▀▀
█▄█ █▄█ █▄█ █▄▀ █ ██▄ ▄█   █▄█ █▀█ █▄█

Goodies Bag is an important menu that will only appear in the Create Mode. Goodies permit you to create the
landscape of your level and to add different objects to it. Goodies Bag in combination with Tools bag will let
you to also create your own functional objects and save them for posterior use.

"""

GLOBAL_STUFF = "Global Stuff"

""" Global Stuff info

█▀▀ █░░ █▀█ █▄▄ ▄▀█ █░░   █▀ ▀█▀ █░█ █▀▀ █▀▀
█▄█ █▄▄ █▄█ █▄█ █▀█ █▄▄   ▄█ ░█░ █▄█ █▀░ █▀░

Gameplay
Game Mode: 

Cooperative
Versus
Cut Scene
Manual jump down

Enable Sackpocket

Enable Organizertron

Recommended Players
Minimum Recommended Players

Maximum Recommended Players

Game End Conditions
Time Limit

Score Limit

Gravity
Gravity

Water
Water Level

Wave Height

Water Color

Water Bits

Light Patterns

Water Drain Sounds

Dynamic Thermometer
Dynamic Thermometer

Loading Zone Shape

Loading Zone Size

Global Controls
Lighting
Lighting

Darkness

Fogginess

Fog Color

Color Correction

Backgrounds
Choose Background

Background Left/Right Position

Background Up/Down Position

Background In/Out Position

Camera
Standard Zoom

Maximum Zoom

Depth of Field (Back)

Depth of Field (Front)

Focus on Players===Audio Volumes=== Choose Ambience

SFX Volume

Background Volume

Music Volume

Dialogue Volume

Audio Reverb
Reverb Setting

SFX Reverb Send

Music Reverb Send

Dialogue Reverb Send

Low-Pass Filter Settings
SFX Filter Amount

Music Filter Amount

Dialogue Filter Amount

High Pass Filter Settings
SFX Filter Amount

Music Filter Amount

Dialogue Filter Amount

"""

STICKERS_DECORATIONS = " Stickers & Decorations"

""" Stickers & Decoration info

█▀ ▀█▀ █ █▀▀ █▄▀ █▀▀ █▀█ █▀     █▀▄ █▀▀ █▀▀ █▀█ █▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█ █▀
▄█ ░█░ █ █▄▄ █░█ ██▄ █▀▄ ▄█     █▄▀ ██▄ █▄▄ █▄█ █▀▄ █▀█ ░█░ █ █▄█ █░▀█ ▄█

Stickers and decorations are collectable items within LittleBigPlanet that do not have any physical properties. 
They are accessible to the player in both Play and Create Mode, and may even be placed in a player's Pod.

"""

# character constants
GENESISGIR = "GenesisGir™"

STEPHEN_FRY = "Stephen Fry™"

""" Stephen Fry's biography

█▀ ▀█▀ █▀▀ █▀█ █░█ █▀▀ █▄░█   █▀▀ █▀█ █▄█
▄█ ░█░ ██▄ █▀▀ █▀█ ██▄ █░▀█   █▀░ █▀▄ ░█░

Stephen Fry is an English actor and the narrator for the LittleBigPlanet games. He is not only the narrator for the
LittleBigPlanet games, but also stars as a video game hero-villain Reaver in Fable 2 and 3. He is also the narrator
for the English version of the toddler show Pocoyo created by Guillermo García Carsí, Luis Gallego and David Cantolla. 
As one of the most literate, well educated people in the United Kingdom, Stephen Fry adapts well to connecting to
the older and younger generations to the LittleBigPlanet games. His charming way of twisting words instantly connects
the player to the LittleBigPlanet world.

'On LittleBigPlanet, you're a little sack person. This is you. Aww bless, you're quite a cute one.' 

Quote from Stephen Fry from LittleBigPlanet.

A truly wonderful game for all ages. And a truly wonderful man to help the gamer along their way.

"""

THE_KING = "The King™"

""" The King's biography

▀█▀ █░█ █▀▀   █▄▀ █ █▄░█ █▀▀
░█░ █▀█ ██▄   █░█ █ █░▀█ █▄█

“ You must love jumping just as much as I like animal-shaped cheese crackers! ”
— The King on OddSock's second visit.

The King is one of the Creator Curators who rule, rebuild and maintain the world of LittleBigPlanet.

He is, unsurprisingly married to The Queen and his domain is The Gardens, where the first series of 
levels in Story Mode take place. In these levels he tells the player different ways to play the level and helps 
them along their path.

"""

THE_QUEEN = "The Queen™"

""" The queen biography

▀█▀ █░█ █▀▀   █▀█ █░█ █▀▀ █▀▀ █▄░█
░█░ █▀█ ██▄   ▀▀█ █▄█ ██▄ ██▄ █░▀█

The Queen is the Creator Curator of the Tutorials rather than an actual game world. The Queen is married to The King,
and appears throughout The Gardens and the level creation tutorials. Her role is relative to Dumpty's, as an 
informative character for the player along the three first levels. The Queen also has one sound file which is
accessible through the Magic Mouth. 


"""

ZOLA = "Zola™"

""" Zola's biography

▀█ █▀█ █░░ ▄▀█
█▄ █▄█ █▄▄ █▀█

Zola is the second of the Creator Curators. He is the king of The Savannah, the second set of levels in the game, 
LittleBigPlanet. He is another character than can be obtained in the level The Collector's Lair.

"""

FRIDA_THE_BRIDE = "Frida The Bride™"

""" Frida The Bride's biography


█▀▀ █▀█ █ █▀▄ ▄▀█   ▀█▀ █░█ █▀▀   █▄▄ █▀█ █ █▀▄ █▀▀
█▀░ █▀▄ █ █▄▀ █▀█   ░█░ █▀█ ██▄   █▄█ █▀▄ █ █▄▀ ██▄

“ Oh, please find my beloved Don Lu! I heard he went underground into the dark crypts. Where IS he?! ”
— Frida, in The Wedding Reception

Frida the Bride is the third Creator Curator in LittleBigPlanet in charge of The Wedding. She uses the two sound
files Zombie Bride (crying) and Zombie Bride (happy), but in The Journey Home, she is voice acted.

"""

UNCLE_JALEPENO = "Uncle Jalepeno™"

""" Uncle Jalepeno's biography

█░█ █▄░█ █▀▀ █░░ █▀▀   ░░█ ▄▀█ █░░ █▀▀ █▀█ █▀▀ █▄░█ █▀█
█▄█ █░▀█ █▄▄ █▄▄ ██▄   █▄█ █▀█ █▄▄ ██▄ █▀▀ ██▄ █░▀█ █▄█

Uncle Jalapeño (pronounced Cala-peen-yo) is the Creator Curator of The Canyons. He teaches Sackboy how to use 
explosives, and helps chase Sheriff Zapata throughout The Canyons. He also drives Sackboy over to The Metropolis.


"""

MAGS_THE_MECHANIC = "Mags The Mechanic™"

""" Mags The Mechanic's biography

█▀▄▀█ ▄▀█ █▀▀ █▀   ▀█▀ █░█ █▀▀   █▀▄▀█ █▀▀ █▀▀ █░█ ▄▀█ █▄░█ █ █▀▀
█░▀░█ █▀█ █▄█ ▄█   ░█░ █▀█ ██▄   █░▀░█ ██▄ █▄▄ █▀█ █▀█ █░▀█ █ █▄▄

“ Jalapeño, my man! That's one ugly ride! go to my garage in the scrapyard and I'll give you a cooler one. ”
— Mags upon Sackboy's arrival.

Mags the Mechanic is the Creator Curator in charge of The Metropolis and a friend of Uncle Jalapeno. She seems to 
enjoy building cars and owns a construction site.

"""

GRAND_MASTER_SENSEI = " Grand Master Sensei™"

""" Grand Master Sensei's biography

█▀▀ █▀█ ▄▀█ █▄░█ █▀▄   █▀▄▀█ ▄▀█ █▀ ▀█▀ █▀▀ █▀█   █▀ █▀▀ █▄░█ █▀ █▀▀ █
█▄█ █▀▄ █▀█ █░▀█ █▄▀   █░▀░█ █▀█ ▄█ ░█░ ██▄ █▀▄   ▄█ ██▄ █░▀█ ▄█ ██▄ █

“ Planning to break into the castle? To get over the castle wall, try using the catapult. There should be some way
to reposition it. And beware the evil Sumo! ”
— Grandmaster Sensei, in Sensei's Lost Castle.

Grandmaster Sensei is the Creator Curator of The Islands levels and also Ze Dude's sensei, whom Ze Dude recommends
when Sackboy beats him at The Construction Site.

Later in the game, Grandmaster Sensei is locked away by the Collector, and freeing her earns you her character model
in Create Mode.

"""

THE_GREAT_MAGICIAN = "The Great Magician™"

""" The Great Magician's biography

▀█▀ █░█ █▀▀   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀   █▀▄▀█ ▄▀█ █▀▀ █ █▀▀ █ ▄▀█ █▄░█
░█░ █▀█ ██▄   █▄█ █▀▄ ██▄ █▀█ ░█░   █░▀░█ █▀█ █▄█ █ █▄▄ █ █▀█ █░▀█

“ LittleBigPlanet is in danger! The Collector is stealing all our creations and not sharing them with the world! 
Go to The Collector's Wilderness and find them. ” — The Great Magician, in Great Magician's Palace

The Great Magician is the Creator Curator of The Temples, and the master of the Emitters.

"""

THE_COLLECTOR = "The Collector™"

""" The Collector's biography

▀█▀ █░█ █▀▀   █▀▀ █▀█ █░░ █░░ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
░█░ █▀█ ██▄   █▄▄ █▄█ █▄▄ █▄▄ ██▄ █▄▄ ░█░ █▄█ █▀▄

The Collector is a Creator Curator who is the main antagonist in LittleBigPlanet. He is the Creator Curator of a
Siberian Tundra, or Soviet warbase-themed world known as The Wilderness. He speaks with the "Evil Pixie" voice and 
throughout his other appearances he triggers the "Evil Laugh" sound effect with the speed and pitch turned all the 
way up. He is the final boss and the 8th and last Creator Curator in LittleBigPlanet.

"""

# level constants
THE_GARDENS = "The gardens" # The Gardens is the first area in LittleBigPlanet that Sackboy travels to.
THE_SAVANNAH = "The Savannah" # The Savannah is the second area in LittleBigPlanet based on Africa.
THE_WEDDING = "The Wedding" # The Wedding is the third area in LittleBigPlanet based on The Day of the Dead.
THE_CANYONS = "The Canyons" # The Canyons is the fourth area in LittleBigPlanet based on the Aztec Empire and the Mexico in the 19th century.
THE_METROPOLIS = "The Metropolis" # The Metropolis is the fifth area in LittleBigPlanet based on USA.

#  story level completion variables
the_gardens_progress = "0%"
the_savannah_progress = "0%"
the_wedding_progress = "0%"
the_canyons_progress = "0%"
the_metropolis_progress = "0%"

# basic material constants
CARDBOARD = "Cardboard material" 
DARK_MATTER = "Dark Matter material"
DISSOLVE = "Dissolve material"
GLASS = " material"
METAL = " material"
PEACH_FLOATY = "Peach Floaty material"
POLYSTYRENE = "Polystyrene material"
RUBBER = "Rubber material"
SPONGE = "Sponge material"
STONE = "Stone material"
WOOD = "Wood material"

"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
"""

# program begins on line '391'
print("\n \n \n")

winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\leftbank.wav", winsound.SND_ASYNC)

print("                                               a                                   \n")

print("                     █▀▄▀█ █▀▀ █▀▄ █ ▄▀█   █▀▄▀█ █▀█ █░░ █▀▀ █▀▀ █░█ █░░ █▀▀")
print("                     █░▀░█ ██▄ █▄▀ █ █▀█   █░▀░█ █▄█ █▄▄ ██▄ █▄▄ █▄█ █▄▄ ██▄ \n \n")

time.sleep(5)

print("                                           𝙥𝙧𝙤𝙙𝙪𝙘𝙩𝙞𝙤𝙣                          \n \n")

time.sleep(5)


print("██╗░░░░░██╗████████╗████████╗██╗░░░░░███████╗██████╗░██╗░██████╗░██████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗████████╗")
print("██║░░░░░██║╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██╔══██╗██║██╔════╝░██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝╚══██╔══╝")
print("██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░██████╦╝██║██║░░██╗░██████╔╝██║░░░░░███████║██╔██╗██║█████╗░░░░░██║░░░")
print("██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░██╔══██╗██║██║░░╚██╗██╔═══╝░██║░░░░░██╔══██║██║╚████║██╔══╝░░░░░██║░░░")
print("███████╗██║░░░██║░░░░░░██║░░░███████╗███████╗██████╦╝██║╚██████╔╝██║░░░░░███████╗██║░░██║██║░╚███║███████╗░░░██║░░░")
print("╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░ \n \n \n \n \n")


time.sleep(5)

winsound.PlaySound(None, winsound.SND_PURGE)

# Story Dialog
print(f"- A {SACKBOY} can be seen running into frame and adjusts the view - \n \n \n \n \n")

playsound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\sackboy.wav")

# Pod menu U/I logic!
while True: # Main pod menu loop
    print()
    print()
    print("                 █░░ █ ▀█▀ ▀█▀ █░░ █▀▀ █▄▄ █ █▀▀ █▀█ █░░ ▄▀█ █▄░█ █▀▀ ▀█▀")
    print("                 █▄▄ █ ░█░ ░█░ █▄▄ ██▄ █▄█ █ █▄█ █▀▀ █▄▄ █▀█ █░▀█ ██▄ ░█░tm \n \n")


    print("     *                           ██████╗░░█████╗░██████╗░                                        ")
    print("                 +               ██╔══██╗██╔══██╗██╔══██╗                       *        *       ")
    print("                                 ██████╔╝██║░░██║██║░░██║           +                            ")
    print("           *                     ██╔═══╝░██║░░██║██║░░██║                                        ")
    print("                                 ██║░░░░░╚█████╔╝██████╔╝                                        ")
    print("                                 ╚═╝░░░░░░╚════╝░╚═════╝░                                        ")
    print("                        *                                                          +             ")
    print(" *                                 █▀▄▀█ █▀▀ █▄░█ █░█                                              ")
    print("                                   █░▀░█ ██▄ █░▀█ █▄█ \n \n                                        ")


    print("                      Welcome to Littlebigplanet:Genesis Edition! \n                          ")

    print("                        丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺                                \n")

    print("                    𝙨𝙩𝙤𝙧𝙮 𝙢𝙤𝙙𝙚 [s]    𝙢𝙮 𝙢𝙤𝙤𝙣 [m]     𝙢𝙮 𝙥𝙧𝙤𝙛𝙞𝙡𝙚 [p]                          \n")

    print("                                       𝙚𝙭𝙞𝙩 𝙥𝙤𝙙 [x]                                             ")
    print("       *                                                                                 +      ")
    print("                                                                                                ")
    print("             +                                                           +           *          ")
    print("                               *                  .--.                                          ")
    print("                                                 / /  `          +               +              ")
    print("      +                          +               | |                                            ")
    print("                                       '         \ \__,                                         ")
    print("               +                   *          +   '--'  *                 +                     ")
    print("                                       +   /\                    --*                   *        ")
    print("     *                     +             .'  '.   *           --                                ")
    print("            *                    *      /======\      +                                         ")
    print("                                       ;:.  _   ;                                               ")
    print("                                       |:. (_)  |                                *              ")
    print("                                       |:.  _   |                                               ")
    print("   +                         +         |:. (_)  |          *                                    ")
    print("                                       ;:.      ;                                               ")
    print("                                     .' \:.    / `.                                  *          ")
    print("                                    / .-'':._.'`-. \                                            ")
    print("                                    |/    /||\    \|                   *                        ")
    print("            *                     _..----````----.._                                            ")
    print("                            _.-'``        LBP        ``'-._                                    ")
    print("                          -'                                '-                                 \n \n")
    
    """ Learn about playsound & winsound intergrations here!


█▀█ █░░ ▄▀█ █▄█ █▀ █▀█ █░█ █▄░█ █▀▄   █▀▄▀█ █▀█ █▀▄ █░█ █░░ █▀▀
█▀▀ █▄▄ █▀█ ░█░ ▄█ █▄█ █▄█ █░▀█ █▄▀   █░▀░█ █▄█ █▄▀ █▄█ █▄▄ ██▄

░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
██▀▀▀██▀▀▀▀▀▀██▀▀▀██
█▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█  ~ ♫ ♩ ♬ ♪    
█▒▒▒▒▒█▒████▒█▒▒▒▒▒█
██▄▄▄██▄▄▄▄▄▄██▄▄▄██    𝙏𝙞𝙥: 𝙄𝙢𝙥𝙤𝙧𝙩 𝙥𝙡𝙖𝙮𝙨𝙤𝙪𝙣𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙖𝙪𝙙𝙞𝙤 𝙛𝙞𝙡𝙚𝙨 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙥𝙧𝙤𝙜𝙧𝙖𝙢

Pure Python, cross platform, single function module with no dependencies for playing sounds.

The playsound module must be imported to be used this module is responsible for playing audio files through the program
as you see through this .py file there are lots of playsound function calls being used these are responsible for outputting
the audio FX that you hear when you run the program or debug that's playsounds hefty work in cohesion with winsound
as well.

eg. import playsound, winsound

The playsound module contains only one thing - the function (also named) playsound.
It requires one argument - the path to the file with the sound you’d like to play. 
This may be a local file, or a URL.

There’s an optional second argument, block, which is set to True by default. 
Setting it to False makes the function run asynchronously.


█░█░█ █ █▄░█ █▀ █▀█ █░█ █▄░█ █▀▄   █▀▄▀█ █▀█ █▀▄ █░█ █░░ █▀▀
▀▄▀▄▀ █ █░▀█ ▄█ █▄█ █▄█ █░▀█ █▄▀   █░▀░█ █▄█ █▄▀ █▄█ █▄▄ ██▄

░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
██▀▀▀██▀▀▀▀▀▀██▀▀▀██
█▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█
█▒▒▒▒▒█▒████▒█▒▒▒▒▒█
██▄▄▄██▄▄▄▄▄▄██▄▄▄██   𝙏𝙞𝙥: 𝙐𝙨𝙚 𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙 𝙬𝙞𝙩𝙝 𝙥𝙡𝙖𝙮𝙨𝙤𝙪𝙣𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙨𝙤𝙪𝙣𝙙𝙨 𝙖𝙨𝙮𝙣𝙘𝙝𝙧𝙤𝙣𝙤𝙪𝙨𝙡𝙮


The winsound module provides access to the basic sound-playing machinery provided by Windows platforms. It includes functions
and several constants.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝘽𝙚𝙚𝙥(𝙛𝙧𝙚𝙦𝙪𝙚𝙣𝙘𝙮, 𝙙𝙪𝙧𝙖𝙩𝙞𝙤𝙣)

Beep the PC’s speaker. The frequency parameter specifies frequency, in hertz, of the sound, and must be in the range 37 through 32,767.
The duration parameter specifies the number of milliseconds the sound should last. If the system is not able to beep the speaker, RuntimeError is raised

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙋𝙡𝙖𝙮𝙎𝙤𝙪𝙣𝙙(𝙨𝙤𝙪𝙣𝙙, 𝙛𝙡𝙖𝙜𝙨)

Call the underlying PlaySound() function from the Platform API. The sound parameter may be a filename, a system sound alias, audio data as a bytes-like object,
or None. Its interpretation depends on the value of flags, which can be a bitwise ORed combination of the constants described below. If the sound parameter is None, 
any currently playing waveform sound is stopped. If the system indicates an error, RuntimeError is raised.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙈𝙚𝙨𝙨𝙖𝙜𝙚𝘽𝙚𝙚𝙥(𝙩𝙮𝙥𝙚=𝙈𝘽_𝙊𝙆)

Call the underlying MessageBeep() function from the Platform API. This plays a sound as specified in the registry. The type argument specifies which sound to play; 
possible values are -1, MB_ICONASTERISK, MB_ICONEXCLAMATION, MB_ICONHAND, MB_ICONQUESTION, and MB_OK, all described below. The value -1 produces a “simple beep”; 
this is the final fallback if a sound cannot be played otherwise. If the system indicates an error, RuntimeError is raised.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙁𝙄𝙇𝙀𝙉𝘼𝙈𝙀

The sound parameter is the name of a WAV file. Do not use with SND_ALIAS.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝘼𝙇𝙄𝘼𝙎

The sound parameter is a sound association name from the registry. If the registry contains no such name, play the system default sound unless SND_NODEFAULT is also specified.
If no default sound is registered, raise RuntimeError. Do not use with SND_FILENAME.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙇𝙊𝙊𝙋
Play the sound repeatedly. The SND_ASYNC flag must also be used to avoid blocking. Cannot be used with SND_MEMORY.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙈𝙀𝙈𝙊𝙍𝙔
The sound parameter to PlaySound() is a memory image of a WAV file, as a bytes-like object.

𝙣𝙤𝙩𝙚: This module does not support playing from a memory image asynchronously, so a combination of this flag and SND_ASYNC
will raise RuntimeError.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙋𝙐𝙍𝙂𝙀
Stop playing all instances of the specified sound.

𝙉𝙤𝙩𝙚: This flag is not supported on modern Windows platforms.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝘼𝙎𝙔𝙉𝘾
Return immediately, allowing sounds to play asynchronously.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙉𝙊𝘿𝙀𝙁𝘼𝙐𝙇𝙏
If the specified sound cannot be found, do not play the system default sound.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙉𝙊𝙎𝙏𝙊𝙋
Do not interrupt sounds currently playing.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙎𝙉𝘿_𝙉𝙊𝙒𝘼𝙄𝙏
Return immediately if the sound driver is busy.

𝙉𝙤𝙩𝙚: This flag is not supported on modern Windows platforms.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙈𝘽_𝙄𝘾𝙊𝙉𝘼𝙎𝙏𝙀𝙍𝙄𝙎𝙆
Play the SystemDefault sound.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙈𝘽_𝙄𝘾𝙊𝙉𝙀𝙓𝘾𝙇𝘼𝙈𝘼𝙏𝙄𝙊𝙉
Play the SystemExclamation sound.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙈𝘽_𝙄𝘾𝙊𝙉𝙃𝘼𝙉𝘿
Play the SystemHand sound.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙈𝘽_𝙄𝘾𝙊𝙉𝙌𝙐𝙀𝙎𝙏𝙄𝙊𝙉
Play the SystemQuestion sound.

𝙬𝙞𝙣𝙨𝙤𝙪𝙣𝙙.𝙈𝘽_𝙊𝙆
Play the SystemDefault sound.

"""
    
    # pod audio source
    playsound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\Pod.wav")
    
    if player == "player": # play pod theme if player passed introduction!
        
                # play pod theme
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\podtheme.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
           
    if player == "new player": # user is new to Littlebigplanet greet them like every sackfolk deserves!
        
        player = "player"
        
        # Introduction to the pod using playsound 
        #playsound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\MyPod.wav")
        
        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\tutorial.wav", winsound.SND_ASYNC)
        # In-game Dialog notifcation
        print("You have " + "(" + str(int(round(1.15))) + ")" + " Popit Notifcation!")
        print(f"{GENESISGIR}: Welcome to your pod! I see you met {STEPHEN_FRY}! You can now navigate through the menu! go ahead")
        print("give it a whirl why won't you?") 
    
    resp = input(">>>")
    
    if resp == "s": # user decides to play story mode!
        
        if player == "player": # play pod theme if player passed introduction!
        
                # play pod theme
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\podtheme.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        
        # story mode while loop menu U/I
        while True: # story loop menu!
            
            print("                     █▀ ▀█▀ █▀█ █▀█ █▄█   █▀▄▀█ █▀█ █▀▄ █▀▀")
            print("                     ▄█ ░█░ █▄█ █▀▄ ░█░   █░▀░█ █▄█ █▄▀ ██▄ \n \n")


            print("                                𝙥𝙡𝙖𝙮 The gardens [p]                 ")
            print("                                Exit to pod [x]")
            playsound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\story.wav")

            resp = input()
            
            # flow control if statement for story mode prompts
            if resp == "p": # user plays gardens!
                
                print("                         █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀")
                print("                         █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ \n")
                
                # loading screen audio source
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\advice.wav", winsound.SND_ASYNC)
                
                # buffer logic U/I
                for buff in range(0,101,10):
                    
                    time.sleep(random.randint(3,5)) # loading time
                    
                    # hint flow controls
                    if buff == 0: # release hint at 0%
                        print("Fun fact: Did you know you can unlock trophies in Littlebigplanet™? \n \n")
                        
                    elif buff == 20: # release hint at 20%
                        print("Fun fact: Littlebigplanet™ was crafted in 2008 by Media molecule! \n \n")
                        
                        time.sleep(abs(random.randint(1.5,1.4)))
                        
                        print("Fun fact: You are the coolest Sack person ever! \n \n")
                        
                    elif buff == 50: # release hint at 50%
                        print("Fun fact: Genesisgir has a Github where he posts all his work! \n \n")
                        
                    elif buff == 70: # release hint at 70%
                        print("Fun fact: This lesson was created for beginners and pro's like you! \n \n")
                
                    elif buff == 90: # release hint at 90%
                        print("Fun fact: You can watch Genesisgir craft programs from scratch on his twitch! \n \n")
                
                # loading has finished and user now enter's the gardens on line '720'!
                
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\garden.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
                
                
                print("                                                     ▀█▀ █░█ █▀▀   █▀▀ ▄▀█ █▀█ █▀▄ █▀▀ █▄░█ █▀")
                print("                                                     ░█░ █▀█ ██▄   █▄█ █▀█ █▀▄ █▄▀ ██▄ █░▀█ ▄█ \n \n")   
                
                                                                                                                                                                                                                        
                                                                                                                                                                                                
                                                                                                                                                                           
                print("                                 ▓▓                              ░░                                                                                            ")            
                print("                                 ▒▒▒▒                      ▓▓    ▓▓                                                    ▒▒                                      ")            
                print("                               ▓▓▒▒▒▒                    ▓▓▓▓░░▓▓▓▓                                                ░░  ░░▒▒                                    ")            
                print("                           ▒▒  ▓▓▒▒▓▓                    ▓▓▓▓▒▒▓▓▓▓░░                ░░  ░░▒▒░░                    ▒▒▒▒▒▒▓▓                                    ")            
                print("                         ░░░░░░░░▒▒░░░░░░▒▒            ▒▒░░░░░░░░░░░░              ▒▒░░░░░░▒▒░░▒▒░░            ░░░░░░▒▒░░░░▒▒▒▒                                ")            
                print("                       ░░    ░░▒▒░░░░░░░░▒▒          ▒▒░░░░░░░░░░▓▓░░░░          ▒▒░░▒▒▒▒░░░░░░░░░░▒▒        ▒▒░░░░░░░░░░▒▒▒▒░░▒▒                              ")            
                print("                       ▓▓██▒▒▒▒▒▒░░░░░░░░▒▒░░      ░░░░▒▒░░░░░░░░▒▒░░░░░░      ░░░░░░▓▓▒▒░░░░░░▒▒░░░░▒▒    ▒▒░░▒▒▓▓░░░░░░▒▒▒▒░░▒▒▒▒                            ")            
                print("                     ▓▓░░▒▒  ░░░░░░▒▒░░░░░░░░▓▓  ▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒  ░░░░░░░░░░░░░░░░░░▒▒░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░▒▒                            ")            
                print("                     ░░░░░░▒▒░░░░░░▒▒░░░░░░░░░░  ▒▒░░░░░░░░░░░░░░░░░░░░░░░░  ▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░                          ")            
                print("                     ▒▒▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░  ░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░▓▓░░▒▒░░░░░░░░░░░░▒▒▓▓░░░░  ▒▒░░▓▓▓▓░░░░░░░░░░▓▓▒▒░░░░░░                          ")            
                print("                     ░░▓▓▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓                          ")            
                print("                     ░░▓▓▓▓▓▓▒▒▓▓░░░░░░▓▓░░░░░░  ░░░░▓▓▒▒░░░░░░░░░░░░░░░░▓▓  ▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓                          ")            
                print("                     ▒▒▒▒▒▒░░▒▒▓▓░░░░░░░░░░░░▓▓  ▓▓░░▓▓▓▓░░░░░░▒▒▓▓░░░░░░▒▒    ░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒  ░░░░░░░░░░▒▒▓▓░░░░░░▒▒▒▒▒▒                            ")            
                print("                       ▓▓▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒      ░░░░░░░░░░░░░░░░░░░░▒▒      ▒▒░░░░░░░░░░░░░░░░░░░░▓▓    ▓▓░░░░░░░░░░░░░░░░░░▒▒▒▒                            ")            
                print("                           ▒▒░░░░▒▒░░▒▒░░░░▒▒          ░░▒▒░░▒▒▓▓▒▒▒▒░░▒▒                                                                                      ")
                print("                                   ▒▒                            ▒▒                        ▓▓                                ▒▒                  ")
                print("                                   ▒▒                            ▒▒                        ▓▓                              ▒▒▒▒░░                ")
                print("                                   ▒▒                            ▒▒            ▒▒▒▒▒▒      ▓▓                    ▓▓    ░░▓▓▓▓▓▓▓▓  ▓▓            ")
                print("                       ▒▒        ▒▒▓▓▓▓            ▒▒          ▓▓░░▓▓            ▒▒          ▓▓▒▒░░▒▒  ▒▒▒▒▓▓      ▓▓  ▒▒        ▒▒▒▒  ▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒        ")  
                print("                       ▒▒      ▒▒  ▒▒▒▒  ░░▒▒▒▒░░░░▒▒▒▒░░  ░░▒▒▒▒▓▓    ▒▒  ░░▒▒  ▒▒  ░░▒▒▒▒    ▒▒    ▒▒▒▒▒▒▓▓        ▒▒░░      ░░▒▒▒▒░░  ▓▓░░▒▒▓▓░░▒▒░░▓▓▓▓    ")  
                print("                       ▒▒      ██▒▒▓▓▒▒▓▓    ▒▒▓▓▓▓      ▒▒    ▒▒▒▒  ▓▓▒▒▒▒▒▒▒▒  ▓▓▒▒▒▒  ▒▒▒▒  ▓▓▒▒▓▓▓▓    ▓▓    ▓▓  ▓▓  ▓▓▓▓  ▒▒▒▒▓▓▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ")  
                print("                       ▓▓  ▒▒  ▒▒▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒██▒▒▓▓▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░▒▒▓▓  ▓▓▒▒▒▒░░▒▒  ░░▓▓      ░░▓▓░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒    ")  
                print("                       ▓▓  ▒▒▒▒██▓▓▓▓▒▒▒▒▓▓██▓▓▒▒▓▓  ▒▒▓▓▒▒▓▓██▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░▒▒▓▓▒▒▓▓▓▓▒▒░░▓▓▒▒▓▓▒▒  ▒▒▒▒▓▓▒▒▒▒▓▓▒▒░░░░░░░░▒▒▒▒  ▒▒▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓")  
                print("                       ▓▓▓▓▒▒▓▓  ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒░░▓▓▓▓▓▓▒▒▒▒▒▒  ░░▓▓▓▓▓▓▓▓░░░░▒▒ \n \n \n \n")
                
                time.sleep(5)
                
                # The king's voice audio src
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\King.wav", winsound.SND_ASYNC)
                
                # The King Dialog
                print(f"{THE_KING}: Hello there {SACKBOY} welcome to {THE_GARDENS} it's nice to have you!")
                input(">>> press enter \n")
                
                # The king's voice audio src
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\King.wav", winsound.SND_ASYNC)
                
                # The King Dialog
                print(f"{THE_KING}: This is The Gardens a beautiful place where you can trot and make new friends!")
                input(">>> press enter \n")
                    
                # The king's voice audio src
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\King.wav", winsound.SND_ASYNC)
                
                # The King Dialog
                print(f"{THE_KING}: But first you'll need to learn how to use your popit menu, This will help you complete this level and collect")
                print("prizes and even trophies and much more!")
                input(">>> press enter \n")
                
                # The king's voice audio src
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\King.wav", winsound.SND_ASYNC)
                
                # The King Dialog
                print(f"{THE_KING}: ")
                input(">>> press enter \n")
                
                
                
                
            elif resp == "x": # user returns back to pod!
                break
            else: # invalid return
                continue
        
    elif resp == "m": # user wants to  go to moon!
        print()
        
    elif resp == "p": # user wishes to look at their profile!
        
        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\profile.wav", winsound.SND_ASYNC)
        
        # my profile system
        while True: # profile menu loop
            
            print("\n \n")
            print("█▀▄▀█ █▄█   █▀█ █▀█ █▀█ █▀▀ █ █░░ █▀▀")
            print("█░▀░█ ░█░   █▀▀ █▀▄ █▄█ █▀░ █ █▄▄ ██▄ \n")

            print("𝙨𝙩𝙤𝙧𝙚 𝙢𝙤𝙙𝙚 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚 \n")
            print(f"{THE_GARDENS} {the_gardens_progress}")
            print(f"{THE_SAVANNAH} {the_savannah_progress}")
            print(f"{THE_WEDDING} {the_wedding_progress}")
            print(f"{THE_CANYONS} {the_canyons_progress}")
            print(f"{THE_METROPOLIS} {the_metropolis_progress} \n")

            print("𝙩𝙧𝙤𝙥𝙝𝙞𝙚𝙨")
            print(f"{_100_COMPLETE} {_100_complete_progress}")
            print("Earn all LittleBigPlanet™ trophies to unlock this platinum trophy. \n")

            print(f"{THE_GARDENS} {the_gardens_trophie_progress}") 
            print("Complete all levels in The Gardens. \n")

            print(f"{THE_SAVANNAH} {the_savannah_trophie_progress}")
            print("Complete all levels in The Savannah. \n")

            print(f"{THE_WEDDING} {the_wedding_trophie_progress}")
            print("Complete all levels in The Wedding. \n")

            print(f"{THE_CANYONS} {the_canyons_trophie_progress}")
            print("Complete all levels in The Canyons. \n")

            print(f"{THE_METROPOLIS} {the_metropolis_trophie_progress}")
            print("Complete all levels in The Metropolis  \n")

            print(f"{EXPERT_CREATOR} {expert_creator_progress}")
            print("Complete all levels in the Tutorials. \n")

            print(f"{ARTIST} {artist_progress}")
            print("Place a sticker. \n")

            print(f"{HOMEMAKER} {homemaker_progress}")
            print("Place 10 stickers or decorations in your pod. \n")

            print(f"{FASHION_SENSE} {fashion_sense_progress}")
            print("Choose a costume for your sackperson with at least one item on your head,")
            print("at least one item on your body, and a material. \n")

            print(f"{TRENDSETTER} {trendsetter_progress}")
            print("Place a sticker or a decoration on another player's sackperson. \n")

            print(f"{FORAGER} {forager_progress}")
            print("Collect 25% of the prize bubbles on the story levels. \n")

            print(f"{STICKY_FINGERS} {sticky_fingers_progress}")
            print("Collect 50% of the prize bubbles on the story levels. \n")

            print(f"{TREASURE_HUNTER} {treasure_hunter_progress}") 
            print("Collect 75% of the prize bubbles on the story levels. \n")  

            print(f"{_2X_MULTIPLIER} {_2x_multiplier_progress}")
            print("Get a 2X Multiplier. \n")

            print(f"{_8X_MULTIPLIER} {_8x_multiplier_progress}")  
            print("Get a 8X Multiplier. \n \n")
        
            # exit to pod prompt
            print("Exit back to your pod [x]")
            
            response = input() # user creates response variable w/input functionality!
            
            if response == "x": # user closes my profile menu system.
                break # escape the my profile loops clause
            else: # re-iterate!
                continue  
                    
    elif resp == "x": # user exits program early!
    
        # user choice to end early uses the sys.exit function call
        while True: # exit program while loop!
            
            print("You will exit Littlebigplanet: Genesis Edition! Are you sure? [y/n]")
            
            resp = input() # takes users input()
            
            if resp == "y": # user closed out of apllication
                
                print("Closing application!")
                
                time.sleep(random.randint(1,3)) # randomize the time to close w/random module!
                
                sys.exit()
                
            elif resp == "n":
                break # returns user to main loop system.
            else: # invalid return!
                print("\n \n")
                continue
    else: # invalid return
        print("\n \n")
        continue

    
        























