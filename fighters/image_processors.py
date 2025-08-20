from PIL import Image
from imagekit.processors import ResizeToFit

class PreserveTransparencyResize(ResizeToFit):
    def process(self, image, context):
        # Convert to RGBA to preserve transparency
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        # Use the ResizeToFit to resize the image
        image = super().process(image, context)
        return image