#Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont

def animal_madlib():
    #prompt the player for words
    animal = input("enter an animal")
    adjective= input("input an adjective")
    colour= input("enter a colour")
    place = input ("enter a place")
    verb = input("enter a verb")
    verb2 =input("enter another verb")
    #write the code using concatenate the strings together
    madlib = "There was a story book about a " + adjective + ", " + colour + " " + animal 
    madlib2 = " who " + verb + " and " + verb2 + " in a " + place + "."
    #print the madlib sentence
    print(r""+madlib + madlib2)
   # get an image
    base = Image.open(r'C:\Users\PC\Desktop\18sep\animal_madlib\madlib4.jpg').convert('RGBA')

   # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

   # get a font
    fnt = ImageFont.truetype('C:\\Users\\PC\\Desktop\\18sep\\animal_madlib\\Ghost-Battle-Personal.otf', 20)

   # get a drawing context
    d = ImageDraw.Draw(txt)

   # draw text, half opacity
    d.text((6,14), madlib, font=fnt, fill=(161, 50, 43,255))
    d.text((6,35), madlib2, font=fnt, fill=(161, 50, 43,255))
    out = Image.alpha_composite(base, txt)

   #Show image
    out.show()

    
#call the function to play the game
animal_madlib()
