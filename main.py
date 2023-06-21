import voice_recognition as r
import record as rec
import threading
from files import search as files_search

rec_started = False
recorder = rec.AudioRecorder()

try:

    while True:
        
        word = r.recognize_using_whisper()

        if rec_started == False:
            
            start_key_word_detected = files_search.search_for_starter_keyword(word)
            if start_key_word_detected != "":
                threading.Thread(target=lambda: recorder.start(start_key_word_detected)).start()
                rec_started = True

        if rec_started == True:

            stop_key_word_detected = files_search.search_for_stop_keyword(word)
            if stop_key_word_detected != "":
                threading.Thread(target=lambda: recorder.stop(stop_key_word_detected)).start() 
                rec_started = False
                
except KeyboardInterrupt:
    pass

print("Loop ended. Keyboard input detected.")
