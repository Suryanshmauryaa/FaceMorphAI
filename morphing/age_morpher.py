# morphing/age_morpher.py

from PIL import ImageEnhance

def morph_age(image, age):
    if age < 18:
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(1.3)
    elif age > 60:
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(2.0)
    else:
        return image
