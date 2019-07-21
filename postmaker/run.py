from PIL import Image, ImageDraw, ImageFont
import time, glob, os, sys
import subprocess
#shower_knowledge_maker

try:
    subprocess.call([r'py_lib_check.bat'])
except:
    sys.exit()

def image_renderer(sentence, i, image):
    x1 = 1024
    y1 = 1024

    tag = "@instagram_handle"

    im = Image.open("./images/"+image)
    im = im.resize((1024, 1024), Image.ANTIALIAS)

    fnt = ImageFont.truetype('arial.ttf', 60)
    img = Image.new('RGB', (x1, y1), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    img.paste(im)

    sum = 0
    for letter in sentence:
      sum += d.textsize(letter, font=fnt)[0]
    average_length_of_letter = sum/len(sentence)


    number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
    incrementer = 0
    fresh_sentence = ''

    #line breaks
    for letter in sentence:
      if(letter == '-'):
        fresh_sentence += '\n\n' + letter
      elif(incrementer < number_of_letters_for_each_line):
        fresh_sentence += letter
      else:
        if(letter == ' '):
          fresh_sentence += '\n'
          incrementer = 0
        else:
          fresh_sentence += letter
      incrementer+=1
    

    #render
    dim = d.textsize(fresh_sentence, font=fnt)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1/2 - x2/2)
    qy = (y1/2- y2/4)
    d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(255,255,255))
    img.save("./exports/export_"+str(i)+".png")
    print("export_"+str(i)+".png")


print("Starting.")
start = time.time()

#main read file
data = []

with open("data.txt", "r") as f:
    for line in f:
        data.append(line)
f.close()

#wipe data file
f = open("data.txt", "w")
f.write("")
f.close()

#write memory file
f = open("memory.txt", "a")
for i in data:
    f.write(i+"\n")
f.close()

#image handler
images = [f for f in os.listdir("./images") if f.endswith (".jpg")]

#execute/massrender
counter = 0
text_counter = 0
nested_counter = 0
overall_image_counter = 0

for text in data:
    image_renderer(text, text_counter, images[overall_image_counter])
    text_counter += 1

    overall_image_counter += 1

    counter += 1

    if overall_image_counter >= len(images):
        overall_image_counter = 0

    if text_counter >= len(data):
        break

end = time.time()

print("Finished "+str(counter)+" photos. Time Taken: "+str(end-start)+" seconds.")
input()



