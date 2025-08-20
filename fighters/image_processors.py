from PIL import Image
from imagekit.processors import Processor

class PreserveTransparencyResize(Processor):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def process(self, image, context):
        # Ensure image is in RGBA to preserve transparency
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        # Resize while keeping transparency
        image = image.resize((self.width, self.height), Image.ANTIALIAS)
        return image