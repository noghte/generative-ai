import simpleaudio as sa
import json
import numpy as np

# Load notes from JSON file
with open('notes/bing.json', 'r') as f:
    notes = json.load(f)

# Create a list of WaveObject instances for each note
wave_objects = []
for note in notes:
    frequency = note['frequency']
    duration = note['duration']
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave_data = np.sin(2 * np.pi * frequency * t)
    wave_objects.append(sa.WaveObject(wave_data, 1, 2, sample_rate))

# Play the notes
for wave_object in wave_objects:
    play_obj = wave_object.play()
    play_obj.wait_done()