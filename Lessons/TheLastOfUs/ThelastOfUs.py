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

# craftable item amounts
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

winsound.PlaySound(r"Genesis-Gir-Lessons-Volume-2\Lessons\TheLastOfUs\ThelastOfUs.py", winsound.SND_ASYNC)

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
print("covered in foilage and burnout cars and the bodies of dead civilians. The year is 2033 and a fungal infection")
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

time.sleep(1) # a function call that delays the program execution set by the arguement!

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

# supply on rations propmt!
while True: # main loop
    
    # loot state variables
    loot_state = "unlooted" # user has not looted the drug store yet!
    
    # Ellie Action
    print(f"{ELLIE} has spotted a drug store and is in desprate need of rations! \n")
    
    print("Enter the drug store [e]") 
    print("Move along [m]")
    
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
                
                
                
                
                
                
                # user chooses to collect isopropyl alcohol!
                while True: # isopropyl loop
                    print(f"Pick up {ISOPROPYL_ALCOHOL}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                    
                    if resp == "y": # user decides to pick up isopropyl alcohol
                        
                        # implementing playsound to play .wav
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
                    
                    time.sleep(5) # a time.sleep() function call pauses the program execution set by the arguement
                
                
                
                
                
                # user chooses to collect duct tape!
                while True: # duct tape loop
                    print(f"Pick up {DUCT_TAPE}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                
                    if resp == "y": # user decides to pick up duct tape
                        
                        # implementing playsound to play .wav
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
                
                
                
                
                
                # user chooses to collect shorty!
                while True: # shorty loop
                    print(f"Pick up {SHORTY}? [y/n] \n")
                    
                    resp = input() # takes users input and creates the variable resp
                
                    if resp == "y": # user decides to pick up shorty
                        
                        # implementing playsound to play .wav
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
        
        print(f"{JOEL}: We really should go in and have a peak inside \n \n \n")
        continue
    elif loot_state == "looted": # break out the main loop of loot state is == "looted"
        break
    else: # invalid choice re-iterate!
        print(" Please select a valid option [e/m] \n \n \n")
        continue
    
# user has collected loot and program continues

print("You broke out of all loops!")






















































