#Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont

def animal_madlib():
    #prompt the player for words
    animal = input("enter an animal")
    adjective= input("input an adjective")
    place = input ("enter a place")
    verb = input("enter a verb")
    
    madlib = f"I saw a {adjective} {animal} who {verb} in {place}."
    #print the madlib sentence
    print(madlib)
   # get an image
    base = Image.open(r'C:\Users\PC\Desktop\18sep\animal_madlib\madlib2.jpg').convert('RGBA')

   # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

   # get a font
    fnt = ImageFont.truetype('C:\\Users\\PC\\Desktop\\18sep\\animal_madlib\\Ghost-Battle-Personal.otf', 40)

   # get a drawing context
    d = ImageDraw.Draw(txt)

   # draw text, half opacity
    d.text((6,14), madlib, font=fnt, fill=(161, 50, 43,255))

    out = Image.alpha_composite(base, txt)

   #Show image
    out.show()
#call the function to play the game
animal_madlib()
