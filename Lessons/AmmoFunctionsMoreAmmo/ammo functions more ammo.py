"""

░██████╗░███████╗███╗░░██╗███████╗░██████╗██╗░██████╗
██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝██║██╔════╝
██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░██║╚█████╗░
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗██║░╚═══██╗
╚██████╔╝███████╗██║░╚███║███████╗██████╔╝██║██████╔╝
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝╚═════╝░

Welcome to the ammo , functions , more ammo .py! in this script we are using modules, print(), variables, functions,
string concatanation and more to apply the logic we need to make this program run programming is about creativity and
this project has tons of that! review the source code to learn more about why we are doing the actions we have
this program tells user his/her inventory amount than makes them wait 5 seconds to retrive 100 bullets of ammunition
in turn after we are using flow control staements to make user choose if they wish to close the program with the
'y/n' text values. Combining flow control and other methods to compact code is the fun and interesting part of coding.
import statements and moudle names like sys,webbrowser,time do various actions google the modules to see what each module does
and you can use them in your own projects!
丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺

"""
# importing modules

import sys,time,webbrowser

"""

█ █▀▄▀█ █▀█ █▀█ █▀█ ▀█▀
█ █░▀░█ █▀▀ █▄█ █▀▄ ░█░

import statements allow the user to import modules into their source code and can be very useful
try importing mods into your code with the 'import' statement. 

ex. import sys

sys in a module that allows the user to terminate their program early and there are millions of functions you
can download using pip or use the modules that come built in in python from the standard library!

"""

# Item amounts variables

ammo_amount = 0
hand_gun_amount = 1
medkit_amount = 44

"""

█░█ ▄▀█ █▀█ █ ▄▀█ █▄▄ █░░ █▀▀ █▀
▀▄▀ █▀█ █▀▄ █ █▀█ █▄█ █▄▄ ██▄ ▄█

variables are like tiny storage units that contains the values and data types you store within them with something 
called an assignment statement! you can store intergers ,floating point numbers , stirs (strings) within these cells
and can be a big weapon in your arsenal when it comes to coding later on. you can overwrite variables with another
assignment statement also variables are case sensitive nad makes them more flexible to use. in line 42 we start
declaring our amount variables to later use in our program.

to create a variable start off with the following below

the variable name , a eqaul operator , and the value to be stored on the right a representation of this below shows
what this would look like in real-time.

eg. box = 'cat'

eg. unit_1 = 1

eg. _unit_2 = 1.1

eg. Box = True

above are some examples you could make variables and as you can see you can begin variables with underscores
Box and box are two different variables and contain different values. A variable cannot begin with a number
but can have them in them as long as the variable begins with a letter, Variables can contain any data type in them including 
boolean values! True and False can be used in variables so why not have a go at it?

"""

# defining functions
def inv():
    print('          𝙈𝙖𝙩𝙚𝙧𝙞𝙖𝙡𝙨') 
    print('You have ' + str(ammo_amount) + ' ammo, ' + str(hand_gun_amount) + ' pistol ' + str(medkit_amount) + ' medkits!\n')

def exit(): # defines the exit() function
    import webbrowser,time
    resp = input('Close program? y/n ')
    if resp == 'y': # condion if users input is yes!
        print('Thank you for trying out this program!') # what the function will evaluate to with the return statement
        time.sleep(1)
        print('You will be directed to genesisgirs Github channel goodbye!')
        time.sleep(1)
        webbrowser.open('https://github.com/GenesisGir')
        sys.exit() # terminate program
    elif resp =='n':
        pass  

def time():
    import time
    print('Please wait ' , str(5) , ' seconds')
    for sec in range(5,0,-1):
        print('Please wait ' , '(' , str(sec) , ')' , ' seconds')
        time.sleep(1)
        
"""

█▀▀ █░█ █▄░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
█▀░ █▄█ █░▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█

functions are really powerful they allow you to declutter your code by withholding some code in the 'body'
of a function you can create your own functions like print() input() len() and that's done using a def statement
these def statements create the actual function it's self. a def statement is made up out of the def statement,
the name of the function it can by anything as long as it's followed by it's paraenthesis () and a colon afterwards
procceeds with indented code called 'The body of the function'. Store your code methods within these functions and
call them into action with 'function calls' a function call consists of the function name , it's paraenthesis ()
and any arguments within the '()' when in turn this send it to the function's variable creating something called a paramenter,
paramenters are interchangable so have fun with these!

example of a def statement can be seen below

def obj():
    obj_amount = str(0)
    if obj_amount == '100'
        print('Collected ' + str(obj_amount) + ' objects!')
        
we start off by using the def keyword followed by the name of the function we want it to be
afterwards we add () with a colon : to indent the code and write our code within the body of the functionality
when we use a obj() function call anywhere in our code this function call will call to the function starting from
the top of the functions code and iteraring all the way to the bottom. Once the code reaches the end of the function
call it the program execution will return to it's destination where it was called from! Functions make it easy, 
simple to not have to copy and paste your code over and over again saving you time and efficiancy in programming.


     /  /\         /  /\         /  /\         /  /\         /  /\           ___        /  /\    
    /  /::\       /  /::\       /  /::|       /  /::\       /  /::\         /__/\      /  /::\   
   /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\     /__/:/\:\        \__\:\    /__/:/\:\  
  /  /:/  \:\   /  /::\ \:\   /  /:/|:|__   /  /::\ \:\   _\_ \:\ \:\       /  /::\  _\_ \:\ \:\ 
 /__/:/_\_ \:\ /__/:/\:\ \:\ /__/:/ |:| /\ /__/:/\:\ \:\ /__/\ \:\ \:\   __/  /:/\/ /__/\ \:\ \:\
 \  \:\__/\_\/ \  \:\ \:\_\/ \__\/  |:|/:/ \  \:\ \:\_\/ \  \:\ \:\_\/  /__/\/:/~~  \  \:\ \:\_\/
  \  \:\ \:\    \  \:\ \:\       |  |:/:/   \  \:\ \:\    \  \:\_\:\    \  \::/      \  \:\_\:\  
   \  \:\/:/     \  \:\_\/       |__|::/     \  \:\_\/     \  \:\/:/     \  \:\       \  \:\/:/  
    \  \::/       \  \:\         /__/:/       \  \:\        \  \::/       \__\/        \  \::/   
     \__\/         \__\/         \__\/         \__\/         \__\/                      \__\/   
"""

inv() # function call being used!
input('(press enter to gather more ammo!)')
time()# function call being used!
print('SUCCESS!') # printing the text values 'SUCCESS' onto stream or stream with print functionality!

# giving user more ammunition by overwriting the variable
ammo_amount = ammo_amount + 100

inv() # function call being used!
print() # ELOC
print('You collected ' + str(ammo_amount) + ' ammunition!')
exit() # function call being used!
"""
|¯¯¯¯¯¯¯|°|\¯¯ (/\)¯¯ /|' |¯¯¯| |¯¯¯¯¯¯¯|°   /¯¯¯/\__)°|¯¯¯|_|¯¯¯| 
|¯¯|__|¯¯|'  \ \__/\__/ / |___| |¯¯|__|¯¯|' |\   \/¯¯¯)|___|¯|___| 
 ¯¯|__|¯¯     \|_|/'\|_|/ |___|  ¯¯|__|¯¯   \|¯¯¯¯¯¯  ||___|¯|___| 
 
Thank you for downloading this .py and I'm sure you'll get the hang of things but make sure not to rush the learning process
our brains are not central processing units they are way more advanced we don't think in binary we think in human
with practice and motivation you'll be able to write programs with logic and choices as long as you practice.

Twitch: https://www.twitch.tv/genesisgir 
Github: https://github.com/GenesisGir

thank you to everyone on twitch who participated in the making of this .py!
"""