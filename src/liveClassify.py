from pyAudioAnalysis import audioTrainTest as aT
import sounddevice as sd
from scipy.io.wavfile import write
import time
import os

classes = ['BabyCry', 'GlassBreaking', 'Gunshot', 'Falling', 'Background', 'SmokeAlarm']

freq = 44100 # Sampling frequency
duration = 3 # Recording duration

print("Ready")
time.sleep(1)
while True:
    print("Recording")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()

    write("recording.wav", freq, recording)
    # print("Saved")

    classification = aT.file_classification("recording.wav", "randomForest2","randomforest")[0]
    print(classification,' ',classes[int(classification)])
    # print(classes[int(classification)])

    os.remove("recording.wav")
    # print("Removed")