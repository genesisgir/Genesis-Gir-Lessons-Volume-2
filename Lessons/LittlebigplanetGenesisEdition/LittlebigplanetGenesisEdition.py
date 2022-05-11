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

# importing modules
import winsound, time, random, sys, webbrowser
from playsound import playsound

# defining variables/constants

# sackboy/sackgirl constants
SACKBOY = "Sackboy™" # a friendly creative lot!
SACKGIRL = "Sackgirl™" # sackboy's bestfriend!

# mode constants
CREATIVE = "Create mode"

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



print("                                               a                                   \n")

print("                     █▀▄▀█ █▀▀ █▀▄ █ ▄▀█   █▀▄▀█ █▀█ █░░ █▀▀ █▀▀ █░█ █░░ █▀▀")
print("                     █░▀░█ ██▄ █▄▀ █ █▀█   █░▀░█ █▄█ █▄▄ ██▄ █▄▄ █▄█ █▄▄ ██▄ \n \n")


print("                                           𝙥𝙧𝙤𝙙𝙪𝙘𝙩𝙞𝙤𝙣                          \n \n")

time.sleep(5)


print("██╗░░░░░██╗████████╗████████╗██╗░░░░░███████╗██████╗░██╗░██████╗░██████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗████████╗")
print("██║░░░░░██║╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██╔══██╗██║██╔════╝░██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝╚══██╔══╝")
print("██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░██████╦╝██║██║░░██╗░██████╔╝██║░░░░░███████║██╔██╗██║█████╗░░░░░██║░░░")
print("██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░██╔══██╗██║██║░░╚██╗██╔═══╝░██║░░░░░██╔══██║██║╚████║██╔══╝░░░░░██║░░░")
print("███████╗██║░░░██║░░░░░░██║░░░███████╗███████╗██████╦╝██║╚██████╔╝██║░░░░░███████╗██║░░██║██║░╚███║███████╗░░░██║░░░")
print("╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░")

winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\LittlebigplanetGenesisEdition\Audio Resources\Phrase05.wav", winsound.SND_ASYNC)













































