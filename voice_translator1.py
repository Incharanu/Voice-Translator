import asyncio
import speech_recognition as sr
from gtts import gTTS
import pygame
from googletrans import Translator

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="kn")
    print(text)

async def main():
    translator = Translator()
    translation = await translator.translate(text, dest="en")
    print(translation.text)

    # Convert translated text to audio
    converted_audio = gTTS(translation.text, lang="en")
    converted_audio.save("output.mp3")

    # Play audio after it has been saved
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)  # Non-blocking wait

# Run the async function
asyncio.run(main())
