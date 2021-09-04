#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import pathlib
import random 
import json

ROOTDIR = pathlib.Path(__file__).parent.resolve()
FONT = ImageFont.truetype(str(ROOTDIR / "assets/DoHyeon-Regular.ttf"), 18)

FRAMES = []

def get_inspirational_quote():
    with open(str(ROOTDIR / 'quotes.json')) as fp:
        QUOTES = json.load(fp)
        i = random.randint(0, len(QUOTES)-1)
        return QUOTES[i]
    
def create_textual_image(xy, text):
    img = Image.new('RGB', (840, 60), "white")
    draw = ImageDraw.Draw(img)
    draw.text(xy, text, font = FONT, fill="black", align='center')
    return img
 
def roll(text):
    for i in range(len(text)+1):
        new_frame = create_textual_image((10, 25), text[:i])
        FRAMES.append(new_frame)


def main():
    quote = get_inspirational_quote()
    print(quote['text'])
    print(quote['author'])
    roll(quote['text'])
    roll('- ' + quote['author'])
    FRAMES[0].save(str(ROOTDIR / 'assets/gifs/banner.gif'), format='GIF', 
                   append_images=FRAMES[1:], save_all=True, duration=100, loop=0)

if __name__ == "__main__":
    main()