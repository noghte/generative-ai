import math
import wave
import struct
import json
import simpleaudio as sa

# Load the notes from the JSON file
with open('notes/gpt3.5.json', 'r') as f:
    notes = json.load(f)

# Load the note map from the JSON file
with open('note_map.json', 'r') as f:
    note_map = json.load(f)

# Define a function to create a WAV file for a single note
def create_note_wav(note):
    # Convert note name to frequency
    note_name = note['pitch']
    frequency = 440 * (2 ** ((note_map[note_name] - 69) / 12))
    duration = note['duration']

    # Create the WAV file
    sample_rate = 44100  # samples per second
    num_channels = 1  # mono
    sample_width = 2  # 2 bytes per sample (16-bit)
    num_samples = int(sample_rate * duration)
    amplitude = 32767  # maximum amplitude
    frequency = float(frequency)

    with wave.open(f'notes/wavs/{note_name}.wav', 'w') as f:
        f.setparams((num_channels, sample_width, sample_rate, num_samples, 'NONE', 'Uncompressed'))
        for i in range(num_samples):
            t = float(i) / sample_rate
            value = int(amplitude * math.sin(2.0 * math.pi * frequency * t))
            data = struct.pack('<h', value)
            f.writeframesraw(data)

# Create a WAV file for each note
for note in notes:
    create_note_wav(note)

# Define a function to play a single note
def play_note_wav(note):
    note_name = note['pitch']
    wav_file = f'notes/wavs/{note_name}.wav'
    wave_obj = sa.WaveObject.from_wave_file(wav_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Define a function to play a sequence of notes
def play_notes(notes):
    for note in notes:
        play_note_wav(note)

# Play the notes
play_notes(notes)
