import pathlib
import random 
import json
import textwrap

from . import pilutils

FONT_SIZE =  24

class Quote:
    def __init__(self, quote_path = 'data/quotes.json', font_path='assets/fonts/Hack-Bold.ttf') -> None:
        self.root = pathlib.Path(__file__).parent.parent.resolve()
        self.path = self.root / quote_path
        self.font = pilutils.load_image_font(str(self.root / font_path), FONT_SIZE)
        self.frames = []
        
    def get_random_quote(self):
        with (self.path).open() as quotes:
            repository = json.load(quotes)
            i = random.randint(0, len(repository)-1)
            quote = repository[i]
            print(quote['text'])
            print('- ' + quote['author'])
            return quote
    
    def __create_textual_image(self, coordinates, text, image_size = (840, 60)):
        return pilutils.draw_image_text(image_size, coordinates, text, self.font)
 
    def __roll(self, text, coordinates = (0, 30)):
        for i in range(len(text)+1):
            frame = self.__create_textual_image(coordinates, text[:i])
            self.frames.append(frame)
            
    def generate_quote_gif(self, output='assets/gifs/quote.gif'):
        quote = self.get_random_quote()
        lines =  textwrap.wrap(quote['text'], width=54)
        for line in lines:
           self.__roll(line)
        self.__roll('- ' + quote['author'])     
        self.frames[0].save(str(self.root / output), format='GIF', append_images=self.frames[1:], save_all=True, duration=100, loop=0)

