import speech_recognition as sr

whisper_silent_words = [" you", " Thank you.", ""]

def recognize_using_whisper():
    
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    recognized_speech = ""
    
    try:
        recognized_speech = r.recognize_whisper(audio, language="english")

        if recognized_speech in whisper_silent_words:
            recognized_speech = "silence_detected"

        print("Whisper thinks you said [" + recognized_speech + "]")
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper")

    return recognized_speech
    
