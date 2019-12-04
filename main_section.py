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
from joke_module import *
from geotext import GeoText
from open_file_module import open_file
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
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech" # couldnt understand what was said

    return response # return what we have recognised


if __name__ == "__main__":
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    time.sleep(3) # allow them to set themselves up
    quit = False
    while quit == False:
        print('Speak!')
        spoken = recognize_speech_from_mic(recognizer, microphone) # run the speech recognition function from above
        if not spoken["success"]:
            print("I didn't catch that. What did you say?\n")



        #speak("you said %s" %(spoken["transcription"]))
        print("You said: %s" %(spoken["transcription"]))
        command = spoken["transcription"]
        if command is not None:
            if "joke" in str(spoken["transcription"]).lower():
                joke_text = str(spoken["transcription"]).lower()
                print(joke_text)
                if "chuck norris" in joke_text:
                    speak(chuck_norris_joke()) # say the chuck norris joke, called from a new file
                if "dad" in joke_text:
                    speak(dad_joke())
            if "temperature" in command:
                geocmd = GeoText(command)
                if len(geocmd.cities) > 0:
                    speak("The temperature in %s is %s degrees celcius" %(geocmd.cities, gettemp(geocmd.cities[0])))
            if "open" in command:
                fto = command.split(" ")[1]
                open_file(fto.lower())
