import pyaudio
import wave

# Define the audio parameters
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100              # Sample rate (samples per second)
RECORD_SECONDS = 5       # Duration of recording
OUTPUT_FILENAME = "output.wav"  # Output file name

p = pyaudio.PyAudio()

# Open a stream to capture audio from the microphone
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=1024)

print("Recording...")

frames = []

# Record audio for the specified duration
for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
    data = stream.read(1024)
    frames.append(data)

print("Finished recording.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
p.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
