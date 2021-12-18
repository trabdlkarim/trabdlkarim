from PIL import Image, ImageDraw, ImageFont

def draw_image_text(image_size, coordinates, text, font):
    img = Image.new('RGB', image_size, "white")
    draw = ImageDraw.Draw(img)
    draw.text(coordinates, text, font = font, fill="black", align='center', anchor="lm")
    return img

def load_image_font(path, size):
    return ImageFont.truetype(path, size)