#################################################
# Charlie                                       #
# A multi-functional speech recognition project #
# This is the main section of the code          #
#################################################

# imports #
import random, time,urllib.request, json, ast
import speech_recognition as sr
from weather_module import gettemp
from text_to_speech_module import speak
def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # try and mitigate the background noise
        audio = recognizer.listen(source) # convert the given audio to a decodeable file

    response = {
        "success": True,
        "error": None,
        "transcription": None
    } # allows us to check if the speech recognition was a fail success or not
    try:
        response["transcription"] = recognizer.recognize_google(audio) # if it has caught something then try and recongise it
    except sr.RequestError:
        response["success"] = False # we couldnt get the speech so we set the success to false because ofcourse... it was not succesful
        response["error"] = "API unavailable" # the api could not be fetched for some reason.......
    except sr.UnknownValueError:f
        response["error"] = "Unable to recognize speech" # couldnt understand what was said

    return response # return what we have recognised


if __name__ == "__main__":
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    time.sleep(3) # allow them to set themselves up
    print('Speak!')
    spoken = recognize_speech_from_mic(recognizer, microphone) # run the speech recognition function from above
    if not spoken["success"]:
        print("I didn't catch that. What did you say?\n")

    speak("you said %s" %(spoken["transcription"]))
    print("You said: %s" %(spoken["transcription"]))
    command = spoken["transcription"]
    speak("The temperature in %s is %s degrees celcius" %(command, gettemp(command)))
