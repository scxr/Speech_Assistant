def speak(text):
    import pyttsx3
    speech_engine = pyttsx3.init()
    speech_engine.say("%s"%(text))
    speech_engine.runAndWait()
