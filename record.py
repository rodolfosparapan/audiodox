import pyaudio
import wave
from datetime import datetime

class AudioRecorder:
    
    def __init__(self):
        self.chunk = 1024  # Number of frames in the buffer
        self.audio_format = pyaudio.paInt16  # 16-bit resolution
        self.channels = 1  # Stereo
        self.sample_rate = 44100  # Standard sample rate
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.file_name = ""
        self.should_record = False

    def start(self, detected_word):
        self.should_record = True
        self.file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + detected_word + "_detected.wav"
        print("Detected word [" + detected_word + "]. Recording started.")

        self.stream = self.p.open(format=self.audio_format,
                                  channels=self.channels,
                                  rate=self.sample_rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
        
        while self.should_record:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop(self, detected_word):
        self.should_record = False
        print("Detected word [" + detected_word + "]. Stopping recording.")

        # Stop and close the audio stream
        self.stream.stop_stream()
        self.stream.close()
        #self.p.terminate()
        self.save_file()

    def save_file(self):
        # Save the recorded audio to a file
        wf = wave.open(self.file_name, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
