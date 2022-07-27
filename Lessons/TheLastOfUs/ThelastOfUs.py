"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂


░██████╗░███████╗███╗░░██╗███████╗░██████╗██╗░██████╗░██████╗░██╗██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝██║██╔════╝██╔════╝░██║██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░██║╚█████╗░██║░░██╗░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗██║░╚═══██╗██║░░╚██╗██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██████╔╝██║██████╔╝╚██████╔╝██║██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝╚═════╝░░╚═════╝░╚═╝╚═╝░░╚═╝

▀█▀ █░█ █▀▀   █░░ ▄▀█ █▀ ▀█▀   █▀█ █▀▀   █░█ █▀
░█░ █▀█ ██▄   █▄▄ █▀█ ▄█ ░█░   █▄█ █▀░   █▄█ ▄█

The Last of Us takes place in the year 2033, twenty years after a fungal-based, brain-altering pandemic has spread
and infected over 60 percent of the world's population. Since the outbreak, the world has gone into a state of panic and
frenzy as officials try to fix and keep the situation under control. When the World Health Organization's attempts to
procure a vaccine fail, the United States government does away with the bureaucrats in power and the establishment of
civilian government. The country is turned into a police state under the control of homeland security and the military, 
and cities across the nation are placed under martial law one by one. Survivors of the pandemic are assigned to designated
quarantine zones that are supposed to separate them from the infected and keep them safe.

Sometime within the twenty years leading up to the main events of the game, a paramilitary group calling themselves the 
Fireflies is established, with their main goal being the restoration of lawful government in the United States, as well as
finding and producing a vaccine for the Cordyceps brain infection. The Fireflies attack the military on occasion and encourage 
uprisings.


丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺

𝙏𝙝𝙚 𝙡𝙖𝙨𝙩 𝙤𝙛 𝙪𝙨 𝙬𝙖𝙨 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮 𝙣𝙖𝙪𝙜𝙝𝙩𝙮𝙙𝙤𝙜

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
"""
# program starts at line '37'

# importing modules
import time, sys, random, winsound, webbrowser

from playsound import playsound

# defining variables/constant assets on line '43'

# character constants
JOEL = "Joel" # Joel Miller
SARAH = "Sarah" # Joel's daughter
ELLIE = "Ellie" # Ellie Williams
TESS = "Tess"
MARLENE = "Marlene"
BILL = "Bill"
HENRY = "Henry"
SAM = "Sam"
TOMMY = "Tommy Miller" # Tommy Miller Joel's brother
DAVID = "David"

# group constants
SURVIVORS = "Survivors"
SMUGGLERS = "Smugglers"
FIREFLIES = "Fireflies"
US_MILITARY = "U.S Military"
HUNTERS = "Hunters"
BANDITS = "Bandits"
INFECTED = "Infected" # the infected who have been taken over by the virus

# chapter constants
HOMETOWN = "Hometown Chapter"
QUARANTINE = "The Quarantine Zone Chapter"
THE_OUTSKIRTS = "The Outskirts Chapter"

# melee weapon constants
_2X4 = "2x4"
SHIV = "Shiv"
MACHETE = "Machete"
PIPE = "Pipe"
HACHET = "Hachet"
BASEBALL_BAT = "Baseball bat"
SWITCHBLADE = "Switchblade"

# melee weapon amounts
_2x4_amount = 0
shiv_amount = 0
machete_amount = 0
pipe_amount = 0
hachet_amount = 0
baseball_bat_amount = 0
switchblade_amount = 0

# pistol constants
REVOLVER = "Revolver"
EL_DIABLO = "El Diablo"
SEMI_AUTO_PISTOL = "Semi-auto pistol"
SHORTY = "Shorty"
ELLIES_PISTOL = "Ellie's pistol"

# pistol amounts
revolver_amount = 0
el_diablo_amount = 0
semi_auto_pistol_amount = 0
shorty_amount = 0
ellies_pistol_amount = 1

# long gun constants
BOLT_ACTION_RIFLE = "Bolt Action rifle"
FLAMETHROWER = "Flamethrower"
ASSAULT_RIFLE = "Assault rifle"
BOW = "Bow"
PUMP_SHOTGUN = "Pump shotgun"
MILITARY_SNIPER = "Military sniper"

# long gun amounts
bolt_action_rifle_amount = 0
flamethrower_amount = 0
assault_rifle_amount = 0
bow_amount = 0
pump_shotgun_amount = 0
military_sniper_amount = 0

# craftable items constants
SUGAR = "Sugar Packets" # A box of sugar packets.
SUGAR_CONTAINER = "Sugar Container" # A sugar container.
RAG = "Rag" # A rag.
EXPLOSIVE_POWDER = "Explosive Powder" # A small pouch filled with explosive powder.
FERTILIZER = "Fertilizer" # A bag of fertilizer.
JAR_OF_SCREWS = "Jar of screws" # A jar of screws.
BROKEN_SCISSORS_NAILS = "Broken Scissors & nails" # A broken pair of scissors and some nails.
DUCT_TAPE = "Duct tape" # Duct tape.
ISOPROPYL_ALCOHOL = "Isopropyl Alcohol" # A bottle of isopropyl alcohol.
WHISKEY = "Whiskey" # A bottle of whiskey.
MOLOTOV = "Molotov" # A suburban protest weapon used in civil right movements to deter the police.
MAKE_SHIFT_BOMB = "Make-Shift Bomb" # A make shift explosive.

# craft-able item amounts
sugar_amount = 0
sugar_container_amount = 0
rag_amount = 0
explosive_powder_amount = 0
fertilizer_amount = 0
jar_of_screws_amount = 0
broken_scissors_nails_amount = 0
duct_tape_amount = 0
isopropyl_alcohol_amount = 0
whiskey_amount = 0
molotov_amount = 0
make_shift_bomb_amount = 0

# location constants
AUSTIN = "Austin"
BOSTON = "Boston"
LINCOLN = "Lincoln"
PITTSBURGH = "Pittsburgh"
JACKSON = "Jackson"
SILVER_LAKE = "Silver Lake"
SALT_LAKE_CITY = "Salt Lake City"

# program starts at  line '152'


print("████████╗██╗░░██╗███████╗  ██╗░░░░░░█████╗░░██████╗████████╗  ░█████╗░███████╗  ██╗░░░██╗░██████╗")
print("╚══██╔══╝██║░░██║██╔════╝  ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔════╝  ██║░░░██║██╔════╝")
print("░░░██║░░░███████║█████╗░░  ██║░░░░░███████║╚█████╗░░░░██║░░░  ██║░░██║█████╗░░  ██║░░░██║╚█████╗░")
print("░░░██║░░░██╔══██║██╔══╝░░  ██║░░░░░██╔══██║░╚═══██╗░░░██║░░░  ██║░░██║██╔══╝░░  ██║░░░██║░╚═══██╗")
print("░░░██║░░░██║░░██║███████╗  ███████╗██║░░██║██████╔╝░░░██║░░░  ╚█████╔╝██║░░░░░  ╚██████╔╝██████╔╝")
print("░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░░░░  ░╚═════╝░╚═════╝░  \n \n \n ")



winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\intro.wav", winsound.SND_ASYNC)

# menu U/I prompt
while True: # while loop being used to loop menu U/I prompt
    print("New game [n]")
    print("Exit [x]")

    resp = input(">>>") # user creates resp variable w/input() functionality

    if resp == "n": # user wants to begin a brand new game!
        break
    
    elif resp == "x": # user wants to shut down game early
        
        print("Closing out The Last Of Us!")
        
        time.sleep(1)
        
        print("Thank you for downloading!")
        
        time.sleep(1)
        
        sys.exit()
        
    else: # if user writes anything else execute the else clause
        print("\n \n \n")# (ELOC)
        continue
    
print("\n \n")
     
# program continues on line '195'

print("███╗░░██╗░█████╗░██╗░░░██╗░██████╗░██╗░░██╗████████╗██╗░░░██╗██████╗░░█████╗░░██████╗░")
print("████╗░██║██╔══██╗██║░░░██║██╔════╝░██║░░██║╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝░")
print("██╔██╗██║███████║██║░░░██║██║░░██╗░███████║░░░██║░░░░╚████╔╝░██║░░██║██║░░██║██║░░██╗░")
print("██║╚████║██╔══██║██║░░░██║██║░░╚██╗██╔══██║░░░██║░░░░░╚██╔╝░░██║░░██║██║░░██║██║░░╚██╗")
print("██║░╚███║██║░░██║╚██████╔╝╚██████╔╝██║░░██║░░░██║░░░░░░██║░░░██████╔╝╚█████╔╝╚██████╔╝")
print("╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═════╝░░╚════╝░░╚═════╝░ \n \n \n")

time.sleep(3)

print("                                   𝙥𝙧𝙚𝙨𝙚𝙣𝙩𝙨                                             \n \n \n")


time.sleep(3)

winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\curtin.wav", winsound.SND_ASYNC)

print("                ▀█▀ █░█ █▀▀   █░░ ▄▀█ █▀ ▀█▀   █▀█ █▀▀   █░█ █▀                                 ")
print("                ░█░ █▀█ ██▄   █▄▄ █▀█ ▄█ ░█░   █▄█ █▀░   █▄█ ▄█                         \n \n \n")



time.sleep(3)

print("                                    YEAR 2033 \n \n                                              ")

time.sleep(3)

# prologue

# Ellie Dialog
print(f"{ELLIE}: We been running for days. . ")
input(">>> press enter \n") # enter prompt uses the input() function

# Ellie Dialog
print(f"{ELLIE}: The infected are not letting up. .")
input(">>> press enter \n") # using \n to create an empty line of code on the next line!

# Ellie Dialog
print(f"{ELLIE}: At this point the whole country is overrun. .")
time.sleep(1)

# Ellie Dialog
print(f"{ELLIE}: By those . . things")
input(">>> press enter \n")

# Ellie Dialog
print(f"{ELLIE}: The only person I can rely on is {JOEL} he was been there since day one and you can't really trust")
print("most people now..even before this place went to shit it's hard to trust people. I've been an introvert my entire")
print("life and this mess doesn't seem any different when things were normal.")
input(">>> press enter \n")

# Story Dialog
print(f"- {ELLIE} holds onto {JOEL} as they ride on the horse through the abandoned city of {AUSTIN} and the city is")
print("covered in foliage and burnout cars and the bodies of dead civilians. The year is 2033 and a fungal infection")
print("has overcome the world and 60 percent of the world's population has been effected leaving people in most cases")
print("dead or stranded as lifeless husks of infected scum waiting to kill, spread or be killed by survivers. -")
input(">>> press enter \n") # prompting user to press enter to continue down the lines of code.

# Ellie Dialog
print(f"{ELLIE}: Are we there yet?")
input(">>> press enter \n")

# Joel Dialog
print(f"{JOEL}: You keep asking and we will never be")
input(">>> press enter \n")

# Ellie Dialog
print(f"{ELLIE}: I'm hungry. \n")

time.sleep(1) # delay the execution by one second

print(f"{ELLIE}: I'm tired. \n")

time.sleep(1) # a function call that delays the program execution set by the argument!

# Joel Dialog
print(f"{JOEL}: Quit your nagging we still have to get to {BOSTON}.")
input(">>> press enter \n")

# Ellie Dialog
print(f"{ELLIE}: Once we get to {BOSTON} will it be safer? I mean has to better than how thing's are here.")
input(">>> press enter \n")

# Joel Dialog
print(f"{JOEL}: The {FIREFLIES} did their homework and it's way much safer.")
input(">>> press enter \n")

# Ellie Dialog
print(f"{ELLIE}: Let's hope so.")
input(">>> press enter \n")

# Ellie Dialog
print(f"- {ELLIE} looks over at a store that has {SURVIVORS} running in and out of and has an idea -") 
input(">>> press enter \n")

# Ellie Dialog
print(f"{ELLIE}: We need rations. Let's go inside and see what we can find!")
input(">>> press enter \n")

# supply on rations prompt!
while True: # main loop
    
    # loot state variables
    loot_state = "unlooted" # user has not looted the drug store yet!
    
    # Ellie Action
    print(f"{ELLIE} has spotted a drug store and is in desperate need of rations! \n")
    
    print("Enter the drug store [e]") 
    print("ignore drug store [m]")
    
    choice = input(">>> \n") # user creates the variable for choice w/input() function!
    
    if choice == "e": # user enter's the drug store!
        
        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\Drugstre.wav", winsound.SND_ASYNC)
        # Ellie Action
        print(f"- {ELLIE} enters the drug store and all the people have left but there is a room that has not been looted yet -")
        input(">>> press enter \n")
        
        # Joel Dialog
        print(f"{JOEL}: It's locked we have to get in somehow.")
        input(">>> press enter \n")
        
        # Locked Drug Store door prompt!
        while True: # second loop
            
            print(f"There is a {_2X4} on the ground and can be used to break the lock by force. \n")
            
            print(f"Use {_2X4} to break the lock [b]")
            print("Try to open door with hands [h]")
            
            action = input(">>> \n") # user creates variable w/input()
            
            """ # what are comments? 

█▀▀ █▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
█▄▄ █▄█ █░▀░█ █░▀░█ ██▄ █░▀█ ░█░ ▄█


▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░     𝙏𝙞𝙥: 𝙐𝙨𝙚 # 𝙩𝙤 𝙘𝙧𝙚𝙖𝙩𝙚 𝙖 𝙘𝙤𝙢𝙢𝙚𝙣𝙩

comments can be helpful for people reading your source code or for keeping notes for yourself! You can create a comment
with the hashtag symbol and anything after will be apart of that comment, keep mental reminders or leave notes for
a team working on the same code explain what a certain line of code is trying to do etc. comments will be a very powerful 
tool to use as a programmer and you can even comment out lines of code your having trouble with by putting a # in front
of that line of code to take it out of the program executions path and take it out when you fixed a problem in your project
this is called commenting out code! Give it a try

eg. # this is an example of a comment!

"""
            
            # flow control statements for door prompts.
            if action == "b": # user decides to break lock with 2x4
                
                # adding 1 to the _2x4 amount!
                _2x4_amount += 1 # 2x4 added to users inventory!
                
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\woodFX.wav", winsound.SND_ASYNC)
                # Ellie Action
                print(f"- {ELLIE} acquired the {_2X4}! -")
                input(">>> press enter \n")
                
                winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\2x4attk.wav", winsound.SND_ASYNC)
                # Ellie Action
                print(f"- {ELLIE}: Smashes the lock with the {_2X4}! - \n \n")
                
                time.sleep(1)
                
                # Joel Dialog
                print(f"{JOEL}: That did the trick let's see what they missed out on.")
                input(f">>> press enter to enter the room with {JOEL} \n")
                
                print("- They walk into the room and there is a shelf with supplies and items untouched and unused as they")
                print(f"approach the shelf and spot {WHISKEY}, {JAR_OF_SCREWS}, {ISOPROPYL_ALCOHOL}, {DUCT_TAPE} and a {SHORTY} firearm -")
                input(">>> press enter\n")
                
                # Ellie Dialog
                print(f"{ELLIE}: It's better than nothing at all and we could use the {ISOPROPYL_ALCOHOL} to make some molotovs.")
                input(">>> press enter \n")
            
                print(f"- {ELLIE} looks over at {JOEL} -")
                
                time.sleep(1)
                
                print("- Then turn over to look at the rations - \n")
                
                time.sleep(random.randint(1,2))
                
                """ # playsound module tips and tricks collapse me to start learning!


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
                
                # looting system starts at line '364'
                
                # user chooses to collect whiskey!
                while True: # whiskey loop
                    print(f"Pick up {WHISKEY}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp

                    if resp == "y": # user decides to collect whiskey
                        
                        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\bottle.wav", winsound.SND_ASYNC)
                        
                        whiskey_amount += 5 # amounts increased by 1!
                        
                        # Ellie Action
                        print(f"- {ELLIE} collected "+ "(" + str(5) + ")" + f" {WHISKEY} bottles and put them in her inventory. - \n")
                        break
                    
                    elif resp == "n": # user decides to not collect whiskey
                        
                        whiskey_amount # stays 0
                        
                        print(f"{ELLIE} decided to not pick up the {WHISKEY}.")
                        break # escape while loop!
                    
                    else:
                        print("Select a valid option [y/n]. \n \n \n")
                        continue
                
                # check whiskey amounts    
                if whiskey_amount >= 1: # user collected the whiskey
                    
                    # Joel Dialog
                    print(f"{JOEL}: That {WHISKEY} will be handy in crafting some molotovs. \n")
                    
                    time.sleep(5)
                    
                    # Joel Dialog
                    print(f"{JOEL}: Good thinking kid! \n")
                    
                    time.sleep(5)
                    
                elif whiskey_amount == 0: # user did not collect whiskey
                    
                    # Joel Dialog
                    print(f"{JOEL}: That {WHISKEY} would've come in handy for crafting some molotovs. \n")
                    
                    time.sleep(5)
                
                
                
                
                
                
                # user chooses to collect jar of screws!
                while True: # jar of screws loop 
                    print(f"Pick up {JAR_OF_SCREWS}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                
                    if resp == "y": # user decides to pick up jar of screws
                        
                        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\jar.wav", winsound.SND_ASYNC)
                        
                        jar_of_screws_amount += 6 # increases amount to 1!
                        
                         # Ellie Action
                        print(f"- {ELLIE} collected "+ "(" + str(6) + ")" + f" {JAR_OF_SCREWS} and put them in her inventory. - \n")
                        break
                        
                    elif resp == "n": # user does not pick up jar of screws!
                        
                        jar_of_screws_amount # stays unchanged at 0
                        
                        break # escapes the while loop statement
                    else:
                        print("Select a valid option [y/n]. \n \n \n")
                        continue
                
                # check Jar of screws amounts
                if jar_of_screws_amount >= 1: # user collected jar of screws!
                    
                    # Joel Dialog
                    print(f"{JOEL}: {JAR_OF_SCREWS} can be used to craft make-shift bombs. \n")
                    
                    time.sleep(5)
                    
                    # Joel Dialog
                    print(f"{JOEL}: Nice for blowing things up! \n")
                    
                    time.sleep(3)
                elif jar_of_screws_amount == 0: # user did not collect jar of screws
                    
                    # Joel Dialog
                    print(f"{JOEL}: Without {JAR_OF_SCREWS} we wont be able to craft make-shift bombs. \n")
                    
                    time.sleep(5)
                
                
                
                """ # while loops tips for beginners!

█░█░█ █░█ █ █░░ █▀▀   █░░ █▀█ █▀█ █▀█   █▀ ▀█▀ ▄▀█ ▀█▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
▀▄▀▄▀ █▀█ █ █▄▄ ██▄   █▄▄ █▄█ █▄█ █▀▀   ▄█ ░█░ █▀█ ░█░ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█

While loop statements are loops that can re-iterate indefinitely until the condition is found false! Use while loops
for various tasks and can help when used with flow control statements!

eg. While True:
        print("Hello!")
        
eg. While True:
        break
        
eg. While True:
        continue

The following code in the example will print out the string literal forever, While we are stuck within this loop we are able to use
𝙗𝙧𝙚𝙖𝙠 statements to escape a while loops clause! Also you can use break & continue statements in for loops as well.

──────────────▄▀█▀█▀▄
─────────────▀▀▀▀▀▀▀▀▀ 
─────────────▄─░░░░░▄
───█──▄─▄───▐▌▌░░░░░▌▌  𝙏𝙞𝙥: 𝙒𝙝𝙞𝙡𝙚 𝙡𝙤𝙤𝙥𝙨 𝙡𝙤𝙤𝙥 𝙛𝙤𝙧𝙚𝙫𝙚𝙧 𝙪𝙣𝙩𝙞𝙡 𝙩𝙝𝙚 𝙘𝙤𝙣𝙙𝙞𝙩𝙞𝙤𝙣 𝙞𝙨 𝙛𝙤𝙪𝙣𝙙 𝙛𝙖𝙡𝙨𝙚
▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌      

                                𝙏𝙞𝙥: 𝙔𝙤𝙪 𝙘𝙖𝙣 𝙚𝙨𝙘𝙖𝙥𝙚 𝙤𝙪𝙩 𝙖 𝙬𝙝𝙞𝙡𝙚 𝙡𝙤𝙤𝙥 𝙬𝙞𝙩𝙝 𝙩𝙝𝙚 𝙗𝙧𝙚𝙖𝙠 𝙨𝙩𝙖𝙩𝙚𝙢𝙚𝙣𝙩

"""
                
                
                # user chooses to collect isopropyl alcohol!
                while True: # isopropyl loop
                    print(f"Pick up {ISOPROPYL_ALCOHOL}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                    
                    if resp == "y": # user decides to pick up isopropyl alcohol
                        
                        # implemeanting playsound to play .wav
                        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\bottle.wav", winsound.SND_ASYNC)
                        
                        isopropyl_alcohol_amount += 4 # increases amount to 1!
                        
                         # Ellie Action
                        print(f"- {ELLIE} collected "+ "(" + str(4) + ")" + f" {ISOPROPYL_ALCOHOL} bottles and put them in her inventory. - \n")
                        break
                        
                    elif resp == "n": # user does not pick up isopropyl alcohol!
                        
                        isopropyl_alcohol_amount # stays unchanged at 0
                        
                        print(f"- {ELLIE} decided to not pick up the {ISOPROPYL_ALCOHOL}. - \n")
                        
                        break # escapes the while loop statement
                    else:
                        print("Select a valid option [y/n]. \n \n \n")
                        continue
                
                # check isopropyl alcohol amounts
                if isopropyl_alcohol_amount >= 1: # user collected isopropyl
                    
                    # Joel Dialog
                    print(f"{JOEL}: {ISOPROPYL_ALCOHOL} can be used to craft molotovs as well. \n")
                    
                    time.sleep(5)
                    
                    # Joel Dialog
                    print(f"{JOEL}: Kinda feel bad for the {INFECTED} Sike not really! \n")
                elif isopropyl_alcohol_amount == 0: # user did not collect isopropyl
                    
                    # Joel Dialog
                    print(f"{JOEL}: {ISOPROPYL_ALCOHOL} could have been used to craft molotovs oh well. \n")
                    
                    time.sleep(5) # a time.sleep() function call pauses the program execution set by the arguemeant
                
                
                """ # learn about the round() function!
🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 

▀█▀ █░█ █▀▀   █▀█ █▀█ █░█ █▄░█ █▀▄ ▄▀ ▀▄   █▀▀ █░█ █▄░█ █▀▀ ▀█▀ █ █▀█ █▄░█
░█░ █▀█ ██▄   █▀▄ █▄█ █▄█ █░▀█ █▄▀ ▀▄ ▄▀   █▀░ █▄█ █░▀█ █▄▄ ░█░ █ █▄█ █░▀█

The round() function has its place in source code , by using it you can round off numbers with
its functionalities and make a float into an integer or round down or up but the funtion does this automatically!
Pretty amazing if i do say so myself!

ex. 5.78 is a floating point data type but if we use round() look what happens

ex. round(5.98) > 6 

ex. round(7.15) > 7

Its rounding off to the nearest integer making it easy to round numbers off it does two things at
once. converts the float into an integer and also makes it rounded off! Double the trouble sister!
                                 
                                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀                                 ⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
⠀                                 ⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
                                 ⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀
                                 ⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀
⠀                                 ⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀
                                 ⠀⠀⢸⠃⢀⣇⡈⠀⠀⠀⠀⠀⠀⢀⡑⢄⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
                                 ⠀⠀⢸⠀⢻⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇ "I want to develop" - genesis gir
                                 ⠀⠀⣸⠀⢸⠃⡇⢀⠇⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⢸⠁
                                 ⠀⠀⡏⠀⣼⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔⣸⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
                                 ⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀    "I want my dreams to come true" - genesis gir
                                 ⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⣾⠀⠀
                                 ⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⡇⠀⠀
                                 ⠀⡏⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀⠀⠀⠀⠀⠀⡇⠀⠀      "if I put the time in Ill surely win" - genesis gir
                                 ⢰⠇⡄⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣧⠀⠀
                                 ⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁⠀⢸⠀⠀
                                 ⣿⠀⡇⠀⠀⠀⠀⠀⢀⡤⠤⠶⠶⠾⠤⠄⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀⠀⠈⣇⠀
                                 ⡇⠀⡇⠀⠀⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇⠀⠀⠀⠀⠀⠀⢹⡀
                                 ⡇⠀⠇⠀⠀⡇⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⢧⣀⣻⢂⠀⠀⠀⠀⠀⠀⢧
                                 ⣇⠀⢠⠀⠀⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣆⠀⠀⠀⠀⠀⠘
                                 ⢻⠀⠈⠰⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠘⢮⣧⡀⠀⠀⠀⠀
                                 ⠸⡆⠀⠀⠇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⢢⡀
                                 
                  𝙏𝙞𝙥: 𝘾𝙤𝙙𝙞𝙣𝙜 𝙞𝙨 𝙖 𝙨𝙣𝙤𝙬 𝙗𝙖𝙡𝙡 𝙚𝙛𝙛𝙚𝙘𝙩 , 𝘿𝙤𝙣𝙩 𝙗𝙚 𝙖𝙛𝙧𝙖𝙞𝙙 𝙩𝙤 𝙩𝙧𝙮 𝙣𝙚𝙬 𝙩𝙝𝙞𝙣𝙜𝙨

🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁
"""
                
                
                # user chooses to collect duct tape!
                while True: # duct tape loop
                    print(f"Pick up {DUCT_TAPE}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                
                    if resp == "y": # user decides to pick up duct tape
                        
                        # implemeanting playsound to play .wav
                        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\jar.wav", winsound.SND_ASYNC)
                        
                        duct_tape_amount += 20 # increases amount to 1!
                        
                         # Ellie Action
                        print(f"- {ELLIE} collected "+ "(" + str(20) + ")" + f" {DUCT_TAPE} and put them in her inventory. - \n")
                        break
                    
                    elif resp == "n": # user does not pick up duct tape!
                        
                        duct_tape_amount # stays unchanged at 0
                        
                        print(f"- {ELLIE} decided to not pick up the {DUCT_TAPE}. - \n")
                        
                        break # escapes the while loop statement
                    else:
                        print("Select a valid option [y/n]. \n \n \n")
                        continue
                
                # check duct tape amounts
                if duct_tape_amount >= 1: # user collected duct tape
                    
                    # Joel Dialog
                    print(f"{JOEL}: {DUCT_TAPE} can be used to bind items together. \n")
                    
                    time.sleep(2)
                    
                    # Joel Dialog
                    print(f"{JOEL}: very useful and is needed to craft items! \n")
                    
                    time.sleep(5)
                    
                elif duct_tape_amount == 0: # user did not collect duct tape
                    
                    # Joel Dialog
                    print(f"{JOEL}: without {DUCT_TAPE} we wont be able to craft items! \n")
                    
                    time.sleep(5)
                
                
                """ # learn int() click here!
🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁

▀█▀ █░█ █▀▀   █ █▄░█ ▀█▀ ▄▀ ▀▄   █▀▀ █░█ █▄░█ █▀▀ ▀█▀ █ █▀█ █▄░█
░█░ █▀█ ██▄   █ █░▀█ ░█░ ▀▄ ▄▀   █▀░ █▄█ █░▀█ █▄▄ ░█░ █ █▄█ █░▀█

The int() function is kinda similar to the round() function it converts any other data type to int!
can be used on floating point data types to convert them down to integers as well lets go give it a
whirl and see what it does.

ex. Here we have a float 5.55 and we want to convert it to integer

ex. int(5.55) > 5

as you see it converted pretty simple stuff  and this works like the round() as I said! so make sure
to test it out in your interactive shell and try out different lines of instruction to see what it does
and you learn things better when you do them than just reading also.


                             ⡿⠋⠄⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠻⣿⣿
                             ⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿
                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹
                             ⣿⣿⡟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣿⣿⣿⣮⠛⣿⣿⣿⣿⣿⣿⡆
                             ⡟⢻⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⠄⡀⢬⣭⣻⣷⡌⢿⣿⣿⣿⣿⣿
                             ⠃⣸⡀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣆⢹⣿⣿⣿⡈⢿⣿⣿⣿⣿
                             ⠄⢻⡇⠄⢛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⡆⠹⣿⣆⠸⣆⠙⠛⠛⠃⠘⣿⣿⣿⣿
                             ⠄⠸⣡⠄⡈⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⣠⣉⣤⣴⣿⣿⠿⠿⠿⡇⢸⣿⣿⣿
                             ⠄⡄⢿⣆⠰⡘⢿⣿⠿⢛⣉⣥⣴⣶⣿⣿⣿⣿⣻⠟⣉⣤⣶⣶⣾⣿⡄⣿⡿⢸
                             ⠄⢰⠸⣿⠄⢳⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⡇⢻⡇⢸
                             ⢷⡈⢣⣡⣶⠿⠟⠛⠓⣚⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⠇⠘
                             ⡀⣌⠄⠻⣧⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⢿⣿⣿⣿⣿⣿⡟⠘⠄⠄
                             ⣷⡘⣷⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿⡋⢀⣠⣤⣶⣶⣾⡆⣿⣿⣿⠟⠁⠄⠄⠄⠄
                             ⣿⣷⡘⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⣿⣷⡿⠟⠉⠄⠄⠄⠄⡄⢀
                             ⣿⣿⣷⡈⢷⡀⠙⠛⠻⠿⠿⠿⠿⠿⠷⠾⠿⠟⣛⣋⣥⣶⣄⠄⢀⣄⠹⣦⢹⣿
                             
                             
      𝙏𝙞𝙥: 𝙄𝙛 𝙮𝙤𝙪 𝙚𝙫𝙚𝙧 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙨𝙚𝙚 𝙬𝙝𝙖𝙩 𝙖 𝙛𝙪𝙣𝙘𝙩𝙞𝙤𝙣  𝙙𝙤𝙚𝙨 𝙩𝙧𝙮 𝙪𝙨𝙞𝙣𝙜 𝙩𝙝𝙚𝙢 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙞𝙣𝙩𝙚𝙧𝙖𝙘𝙩𝙞𝙫𝙚 𝙨𝙝𝙚𝙡𝙡𝙨
      
🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁 🅶🅴🅽🅴🆂🅸🆂 🅶🅸🆁      
"""
                
                
                # user chooses to collect shorty!
                while True: # shorty loop
                    print(f"Pick up {SHORTY}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                
                    if resp == "y": # user decides to pick up shorty
                        
                        # implemeanting playsound to play .wav
                        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\shorty.wav", winsound.SND_ASYNC)
                        
                        shorty_amount += 1 # increases amount to 1!
                        
                         # Ellie Action
                        print(f"- {ELLIE} decided to pick up the {SHORTY} and stashed it into her inventory. - \n")
                        break
                    
                    elif resp == "n": # user does not pick up shorty!
                        
                        shorty_amount # stays unchanged at 0
                        
                        print(f"- {ELLIE} decided to not pick up the {SHORTY}. - \n")
                        
                        break # escapes the while loop statement 
                    
                    else: # re-iterate early!
                        print("Select a valid option [y/n]. \n \n \n")
                        continue
                    
                    # check shorty firearm amounts
                if shorty_amount == 1: # user picked up shorty
                    
                    # Joel Dialog
                    print(f"{JOEL}: That Shotgun will make them fear you. \n")
                    
                    time.sleep(5)
                    
                elif shorty_amount == 0: # user did not pick up shorty
                    
                    # Joel Dialog
                    print(f"{JOEL}: You should have really picked up the {SHORTY} \n")
                    
                    time.sleep(3)
                    
                    # Joel Dialog
                    print(f"{JOEL}: Just stay close to me and you should be fine kiddo. \n")
                    
                    time.sleep(5)
                
                # loot state variables
                loot_state = "looted" # user has looted the drug store!
                
                break 
            
            elif action == "h": # user chooses to open the door normally 
                print(f"- {ELLIE} attempt's to open the door with her hands but it is locked maybe the {_2X4} is choice. -")
                input(">>> press enter")
                continue
            else: # user typed something invalid and will result in a re-iteration of the current loop.
                print("\n \n \n") 
                continue
    
        
        break # escape the second while loop's clause
    elif choice == "m": # user chooses to move along and not enter drug store's path
        
        # Joel Dialog
        print(f"{JOEL}: We really should go in and have a peak inside \n \n \n")
        continue
    
    elif loot_state == "looted": # break out the main loop of loot state is == "looted"
        break
    else: # invalid choice re-iterate!
        print(" Please select a valid option [e/m] \n \n \n")
        continue
    
# user has collected loot and program continues

#Ellie Dialog
print(f"{ELLIE}: Okay that's everything lets get out of here before things get bad.")
input(">>> press enter \n")

#Joel Dialog
print(f"{JOEL}: Your right and it's almost night.")
input(">>> press enter \n")

#Ellie Dialog
print(f"{ELLIE}: The {INFECTED} are bad even in daylight I can't imagine what they are like at night. ")
input(">>> press enter \n")

print(f"- The sound of the {INFECTED} closing in on your location can be heard - \n")

playsound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\horde.wav")

#Joel Dialog
print(f"{JOEL}: They are here.")
input(">>> press enter \n")

#Ellie Dialog
print(f"{ELLIE}: Fuck man.")
input(">>> press enter \n")

#Ellie Dialog
print(f"{ELLIE}: What do we do... what do we do?")
input(">>> press enter \n")

#Joel Dialog
print(f"{JOEL}: Relax stick by me and everything should be fine")

time.sleep(3)

#Joel Dialog
print(f"{JOEL}: Did you collect the {SHORTY}? Pull it out. \n")

# user protects themselves path
if shorty_amount == 1: # user owns the shorty firearm
    
    winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\woodFX.wav", winsound.SND_ASYNC)
    
    # Ellie action
    print(f"- {ELLIE} equips the {SHORTY} and prepares herself with holding it up at the drug stores entrance - \n")
    input(">>> press enter \n")
    
    #Joel Dialog
    print(f"{JOEL}: {ELLIE}! make a {MOLOTOV} and throw it at the door! We will escape from the backdoor.")
    input(">>> press enter \n")
    
    print(f"Notifcation: {JOEL} wants you to craft a Molotov to fight against the {INFECTED} \n \n \n")
    
    time.sleep(3)
    
    # user crafts a molotov with inventory U/I
    while True: # inventory loop prompt
        
        # break out the while loops clause if molotovs been crafted.
        
        if molotov_amount >= 1: # self explanatory.
            print("\n \n")
            break
         
        resp = input(f"Press [i] to enter your inventory and craft a {MOLOTOV}! \n \n") # prompting user to open inventory w/i
        
        if resp == "i": # user enters the inventory menu 

            print("                       𝐓𝐡𝐞 𝐥𝐚𝐬𝐭 𝐨𝐟 𝐮𝐬 \n")

            print("██████╗░░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░░█████╗░██╗░░██╗")
            print("██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝")
            print("██████╦╝███████║██║░░╚═╝█████═╝░██████╔╝███████║██║░░╚═╝█████═╝░")
            print("██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔═══╝░██╔══██║██║░░██╗██╔═██╗░")
            print("██████╦╝██║░░██║╚█████╔╝██║░╚██╗██║░░░░░██║░░██║╚█████╔╝██║░╚██╗")
            print("╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ \n \n \n")
            # (ELOC)    
            # (ELOC)
            print("             █ █▄░█ █░█ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █▄█")
            print("             █ █░▀█ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ░█░ \n \n \n")    
            
            
            
            print("𝙀𝙡𝙡𝙞𝙚 𝙒𝙞𝙡𝙡𝙞𝙖𝙢𝙨 \n")
            
            print("(" + str(whiskey_amount) + ") " + f"{WHISKEY}")
            print("(" + str(isopropyl_alcohol_amount) + ") " + f"{ISOPROPYL_ALCOHOL}")
            print("(" + str(shorty_amount) + ") " + f"{SHORTY}")
            print("(" + str(jar_of_screws_amount) + ") " + f"{JAR_OF_SCREWS}")
            print("(" + str(duct_tape_amount) + ") " + f"{DUCT_TAPE}")
            print("\n \n")
            
            
            print("                        𝙘𝙧𝙖𝙛𝙩𝙞𝙣𝙜 𝙢𝙚𝙣𝙪             \n     ")
            
            print(f"                    [b] {MAKE_SHIFT_BOMB}                  ")
            print(f"                    [m] {MOLOTOV}                     \n")
            
            response = input(f"Craft a {MOLOTOV} press [m]! \n") # taking user input for response.
            
            if response == "b": # user attempts to make a make shift bomb
                # game notfication!
                print(f"Notfication: {JOEL} said to craft a {MOLOTOV} not Make-Shift bombs. \n \n \n")
                continue
            
            elif response == "m": # user crafts molotov's
                print()
                print()
                print("█▀▄▀█ █▀█ █░░ █▀█ ▀█▀ █▀█ █░█   █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀   █▀▄▀█ █▀▀ █▄░█ █░█")
                print("█░▀░█ █▄█ █▄▄ █▄█ ░█░ █▄█ ▀▄▀   █▄▄ █▀▄ █▀█ █▀░ ░█░   █░▀░█ ██▄ █░▀█ █▄█ \n \n")
                
                
                print("You will need the following to craft " +"("+ str(int(1.1)) +")"+ " molotov:")
                print("(" + str(1) + ") " f" + {DUCT_TAPE}")
                print("(" + str(1) + ") " f" + {WHISKEY} or {ISOPROPYL_ALCOHOL} \n \n \n")
                
                
                
                            
                resp = input(f"Craft {MOLOTOV} [c] \n") # crafting prompt
                
                if resp == "c":
                    
                    while True: # crafting molotov while loop system!
                        
                        print("craft " +"("+ str(int(1.1)) +")"+ f" {MOLOTOV}? [c]")
                        print("Exit craft menu [x] \n")
                        
                        resp = input() # retriving users input!
                        
                        # checking amounts    
                        if resp == "c" and duct_tape_amount and isopropyl_alcohol_amount >= 1:
                            
                            molotov_amount += 1 # incremeant amount's by 1
                            
                            duct_tape_amount -= 1 # deduct by 1 
                            
                            isopropyl_alcohol_amount -= 1
                            
                            winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\bottle.wav", winsound.SND_ASYNC)
                            
                            print("Crafted " + "(" + str(1) + ") " + f"{MOLOTOV}! \n \n ")
                            
                        elif resp == "c" and duct_tape_amount and isopropyl_alcohol_amount <= 0:
                            
                            # System Dialog
                            print(f"Notifcation: You don't have enough rations to create {MOLOTOV}! \n")
                            continue # re-iterate
                        
                        # exit system
                        elif resp == "x" and molotov_amount >= 1: # exit the while loop if molotov's have been crafted!
                            
                            break # escape the molotov crafting while loop system
                            
                        elif resp == "x" and molotov_amount <= 0: # re-iterate if molotovs have not been crafted.
                            
                            # Ellie Dialog
                            print(f"{ELLIE}: I should make some {MOLOTOV}s.")
                            continue # re-iterate
                            
                        else: # invalid option will result in warning user to press c key!
                            print(f"Craft a {MOLOTOV} by pressing the c key. \n \n \n")
                                  
            else: # user invalid option
                print("\n \n \n")
                continue
    
    
    
# Joel protects user path
elif shorty_amount != 1: # user does not own the shorty
    
    # Ellie Dialog
    print(f"{ELLIE}: I must've forgot or didn't pick it up! \n")

    #Joel Dialog
    print(f"{JOEL}: It's fine I'll protect you no worries kid.")
    input(">>> press enter \n")
    
    winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\rifle.wav", winsound.SND_ASYNC)
    
    # Joel action
    print(f"- {JOEL} pulls out a long gun rifle and prepares for the incoming horde read to break through the drug store doors - \n")
    input(">>> press enter \n")
    
    #Joel Dialog
    print(f"{JOEL}: {ELLIE}! make a {MOLOTOV} and throw it at the door! We will escape from the backdoor.")
    input(">>> press enter \n")
    
    print(f"Notifcation: {JOEL} wants you to craft a Molotov to fight against the {INFECTED} \n \n \n")
    
    time.sleep(3)
    
    
    # user crafts a molotov with inventory U/I
    while True: # inventory loop prompt
        
        # break out the while loops clause if molotovs been crafted.
        
        if molotov_amount >= 1: # self explanatory.
            print("\n \n")
            break
         
        resp = input(f"Press [i] to enter your inventory and craft a {MOLOTOV}! \n \n") # prompting user to open inventory w/i
        
        if resp == "i": # user enters the inventory menu 

            print("                       𝐓𝐡𝐞 𝐥𝐚𝐬𝐭 𝐨𝐟 𝐮𝐬 \n")

            print("██████╗░░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░░█████╗░██╗░░██╗")
            print("██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝")
            print("██████╦╝███████║██║░░╚═╝█████═╝░██████╔╝███████║██║░░╚═╝█████═╝░")
            print("██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔═══╝░██╔══██║██║░░██╗██╔═██╗░")
            print("██████╦╝██║░░██║╚█████╔╝██║░╚██╗██║░░░░░██║░░██║╚█████╔╝██║░╚██╗")
            print("╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ \n \n \n")
            # (ELOC)    
            # (ELOC)
            print("             █ █▄░█ █░█ █▀▀ █▄░█ ▀█▀ █▀█ █▀█ █▄█")
            print("             █ █░▀█ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ░█░ \n \n \n")    
            
            
            
            print("𝙀𝙡𝙡𝙞𝙚 𝙒𝙞𝙡𝙡𝙞𝙖𝙢𝙨 \n")
            
            print("(" + str(whiskey_amount) + ") " + f"{WHISKEY}")
            print("(" + str(isopropyl_alcohol_amount) + ") " + f"{ISOPROPYL_ALCOHOL}")
            print("(" + str(shorty_amount) + ") " + f"{SHORTY}")
            print("(" + str(jar_of_screws_amount) + ") " + f"{JAR_OF_SCREWS}")
            print("(" + str(duct_tape_amount) + ") " + f"{DUCT_TAPE}")
            print("\n \n")
            
            
            print("                        𝙘𝙧𝙖𝙛𝙩𝙞𝙣𝙜 𝙢𝙚𝙣𝙪             \n     ")
            
            print(f"                    [b] {MAKE_SHIFT_BOMB}                  ")
            print(f"                    [m] {MOLOTOV}                     \n")
            
            response = input(f"Craft a {MOLOTOV} press [m]! \n") # taking user input for response.
            
            if response == "b": # user attempts to make a make shift bomb
                # game notfication!
                print(f"Notfication: {JOEL} said to craft a {MOLOTOV} not Make-Shift bombs. \n \n \n")
                continue
            
            elif response == "m": # user crafts molotov's
                print()
                print()
                print("█▀▄▀█ █▀█ █░░ █▀█ ▀█▀ █▀█ █░█   █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀   █▀▄▀█ █▀▀ █▄░█ █░█")
                print("█░▀░█ █▄█ █▄▄ █▄█ ░█░ █▄█ ▀▄▀   █▄▄ █▀▄ █▀█ █▀░ ░█░   █░▀░█ ██▄ █░▀█ █▄█ \n \n")
                
                
                print("You will need the following to craft " +"("+ str(int(1.1)) +")"+ " molotov:")
                print("(" + str(1) + ") " f" + {DUCT_TAPE}")
                print("(" + str(1) + ") " f" + {WHISKEY} or {ISOPROPYL_ALCOHOL} \n \n \n")
                
                
                
                            
                resp = input(f"Craft {MOLOTOV} [c] \n") # crafting prompt
                
                if resp == "c":
                    
                    while True: # crafting molotov while loop system!
                        
                        print("craft " +"("+ str(int(1.1)) +")"+ f" {MOLOTOV}? [c]")
                        print("Exit craft menu [x] \n")
                        
                        resp = input() # retriving users input!
                        
                        # checking amounts    
                        if resp == "c" and duct_tape_amount and isopropyl_alcohol_amount >= 1:
                            
                            molotov_amount += 1 # incremeant amount's by 1
                            
                            duct_tape_amount -= 1 # deduct by 1 
                            
                            isopropyl_alcohol_amount -= 1
                            
                            winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\bottle.wav", winsound.SND_ASYNC)
                            
                            print("Crafted " + "(" + str(1) + ") " + f"{MOLOTOV}! \n \n ")
                            
                        elif resp == "c" and duct_tape_amount and isopropyl_alcohol_amount <= 0:
                            
                            # System Dialog
                            print(f"Notifcation: You don't have enough rations to create {MOLOTOV}! \n")
                            continue # re-iterate
                        
                        # exit system
                        elif resp == "x" and molotov_amount >= 1: # exit the while loop if molotov's have been crafted!
                            
                            break # escape the molotov crafting while loop system
                            
                        elif resp == "x" and molotov_amount <= 0: # re-iterate if molotovs have not been crafted.
                            
                            # Ellie Dialog
                            print(f"{ELLIE}: I should make some {MOLOTOV}s.")
                            continue # re-iterate
                            
                        else: # invalid option will result in warning user to press c key!
                            print(f"Craft a {MOLOTOV} by pressing the c key. \n \n \n")
      
            else: # user invalid option
                print("\n \n \n")
                continue           

        else: # user invalid option
            print("\n \n \n")
            continue

# user crafted molotovs and program continues on line '962'!

# Joel Dialog
print(f"{JOEL}: Great you crafted the {MOLOTOV}s!")
input(">>> press enter \n")

# Joel Dialog
print(f"{JOEL}: THROW THEM AT THE DOOR THEY ARE COMING IN!")
input(">>> press enter \n")

while True: # molotov throw while loop!
    
    print("Notifcation: You have " + "(" + str(molotov_amount) + ") " + f"{MOLOTOV}s! \n")
    
    time.sleep(3)
    
    action = input(f"Throw {MOLOTOV} at drug store door! [m] \n")
    
    if action == "m":
        
        # infected dying!
        winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\Audio Resources\hordecrd.wav", winsound.SND_ASYNC)
        
        # Ellie action
        print(f"- {ELLIE} throws a {MOLOTOV} at the door and " + str(round(120)) + f" {INFECTED} begin to burn and die -") 
        input(">>> press enter \n")
        
        # Joel Dialog
        print(f"{JOEL}: RUN ELLIE RUN! \n")
        input(">>> press enter \n")
        
        print(f"- {ELLIE} & {JOEL} run for their lives as they {INFECTED} burn to a crisp. . . -")
        input("This was a demo press enter to view credits!\n")
        
        winsound.PlaySound(None, winsound.SND_PURGE)

        print("Thank you for downloading GenesisGirLessonsVolume.2! \n")
        print("I want to thank everyone for the support on twitch and my lovely wife for the motivation! These")
        print("programs are really fun to make and I enjoy making them if your new to programming with time and practice")
        print("you can achieve anything you set your mind too!~ \n")

        time.sleep(3)

        print("If you learned something from this lesson & make sure to follow me on github! \n")

        time.sleep(3)


        print("█▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀")
        print("█▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█ \n \n")

        time.sleep(1)

        print("source code by - GenesisGir \n")

        time.sleep(1)

        print("𝙏𝙝𝙚 𝙡𝙖𝙨𝙩 𝙤𝙛 𝙪𝙨 𝙬𝙖𝙨 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮 𝙣𝙖𝙪𝙜𝙝𝙩𝙮𝙙𝙤𝙜 \n ")

        time.sleep(1)

        print("Support the creators of the game and Support me for putting this together! \n")

        while True:
            print()
            print("visit the game page to buy the last of us! [s]")
            print("Visit GenesisGirs Github page! [g]")
            r = input("Goodbye <3 [x]\n")

            if r == "s":
                webbrowser.open("https://store.playstation.com/en-us/product/UP9000-CUSA00552_00-THELASTOFUS00000")
                continue
            elif r == "g":
                webbrowser.open("https://github.com/GenesisGir")
                continue
            elif r == "x":
                sys.exit()
            else:
                continue
            
"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠉⠉⠉⠉⠉⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⡇⠀⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠘⠋⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠿⢦⠤⠤⣤⠤⠤⡤⠤⢼⡧⠤⢼⠀⠀⠿⠤⡄⡠⠤⠴⠿⡇⠀⠀⠧⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢸⠀⠀⣿⠀⠀⡇⠀⢸⡇⠀⢸⠀⠀⠀⠀⡏⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠿⢿⠀⠀⠿⠀⠀⠇⠀⢸⡇⠀⢸⠀⠀⠿⠿⡇⠀⠸⠿⠿⡇⠀⠀⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⢸⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⢸⣄⠀⠀⠀⣧⡀⠀⠀⠀⡇⠀⠀⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢿⣿⣿⡿⢿⣿⣿⣿⢿⣿⡿⢿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
Thank you for downloading this .py find more at my github and learn something new everyday and rememeber
to not give up on coding! its an artform and anbody can be skilled enough to achieve greatness in your code
make sure to check out my twitch streams below
Twitch: https://www.twitch.tv/genesisgir 
Github: https://github.com/GenesisGi
thank you to everyone on twitch who participated in the making of this .py!
"""

"""

█▀█ █▀▀ █▀ █▀█ █░█ █▀█ █▀▀ █▀▀ █▀
█▀▄ ██▄ ▄█ █▄█ █▄█ █▀▄ █▄▄ ██▄ ▄█

link: >>> https://www.twitch.tv/genesisgir  <<< Find Livestreams and more!
link: >>> https://automatetheboringstuff.com <<< Discover and learn how i did!
"""
"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂

▀█▀ █░█░█ █ ▀█▀ █▀▀ █░█   █▀ ▀█▀ █▀█ █▀█ █▀▀ █▀▄   █▄▄ █▀█ █▀█ ▄▀█ █▀▄ █▀▀ ▄▀█ █▀ ▀█▀ █▀
░█░ ▀▄▀▄▀ █ ░█░ █▄▄ █▀█   ▄█ ░█░ █▄█ █▀▄ ██▄ █▄▀   █▄█ █▀▄ █▄█ █▀█ █▄▀ █▄▄ █▀█ ▄█ ░█░ ▄█

Fun Fact this .py was made on stream and can be found on my Twitch page @ GenesisGir! Subscribers can 
go back a re-watch how .pf files are made in cohesion and learn step by step how projects like these are made 
very useful to those starting out. Subscribe and stay in the loop!

link:https://www.twitch.tv/genesisgir Watch resourceful livestreams and chat , code!

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
"""
"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂

█▀▀ █░█ █▀▀ █▀▀ █▄▀   █▀█ █░█ ▀█▀   █▀▄▀█ █▄█   █▀▀ █ ▀█▀ █░█ █░█ █▄▄
█▄▄ █▀█ ██▄ █▄▄ █░█   █▄█ █▄█ ░█░   █░▀░█ ░█░   █▄█ █ ░█░ █▀█ █▄█ █▄█

Discover , Explore and learn from my programs that Ive pushed to my remote repositories!
and dont forget to follow me! (;

link: >>> https://github.com/GenesisGir <<<

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
"""