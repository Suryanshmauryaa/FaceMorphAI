# morphing/emotion_morpher.py

from PIL import ImageEnhance

def morph_emotion(image, emotion):
    enhancer = ImageEnhance.Color(image)
    if emotion == "happy":
        return enhancer.enhance(1.5)
    elif emotion == "sad":
        return enhancer.enhance(0.5)
    elif emotion == "angry":
        return enhancer.enhance(2.0)
    elif emotion == "surprise":
        return enhancer.enhance(1.8)
    else:
        return enhancer.enhance(1.0)
