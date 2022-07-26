from PIL import Image, ImageChops
import os
import shutil

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

path = target = os.getcwd() + '\old'
if not os.path.exists(path):
  os.makedirs(path)
  print("A new folder called 'old' is created")

# don't really need any suffix since the old file gets moved to a new folder
suffix = ''

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f[-4:] == ".png":
        
        im = Image.open(f)
        im = trim(im)

        oldFileName = f[:-4] + suffix + ".png"
        os.rename(f, oldFileName)
        original = os.getcwd() + '\\' + oldFileName
        shutil.move(original, target)
        
        im.save(f)
        print(f + ' has successfully cropped')




        
