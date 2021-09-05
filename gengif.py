#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import pathlib
import random 
import json
import textwrap

ROOTDIR = pathlib.Path(__file__).parent.resolve()
FONT = ImageFont.truetype(str(ROOTDIR / "assets/Hack-Bold.ttf"), 24)
FRAMES = []

def get_inspirational_quote():
    with (ROOTDIR / 'quotes.json').open() as fp:
        QUOTES = json.load(fp)
        i = random.randint(0, len(QUOTES)-1)
        return QUOTES[i]
    
def create_textual_image(xy, text):
    img = Image.new('RGB', (840, 60), "white")
    draw = ImageDraw.Draw(img)
    draw.text(xy, text, font = FONT, fill="black", align='center', anchor="lm")
    return img
 
def roll(text):
    for i in range(len(text)+1):
        new_frame = create_textual_image((0, 30), text[:i])
        FRAMES.append(new_frame)


def main():
    quote = get_inspirational_quote()
    print(quote['text'])
    print(quote['author'])
    lines =  textwrap.wrap(quote['text'], width=54)
    for line in lines:
        roll(line)
    roll('- ' + quote['author'])
    FRAMES[0].save(str(ROOTDIR / 'assets/gifs/banner.gif'), format='GIF', 
                   append_images=FRAMES[1:], save_all=True, duration=100, loop=0)

if __name__ == "__main__":
    main()
