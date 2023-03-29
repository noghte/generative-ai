import json
import numpy as np
import simpleaudio as sa

def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    audio_data = sine_wave * (2**15 - 1) / np.max(np.abs(sine_wave))
    return audio_data.astype(np.int16)

def play_notes_from_file(file_name):
    with open(file_name, 'r') as file:
        notes = json.load(file)

    for note in notes:
        frequency = note['frequency']
        duration = note['duration']
        audio_data = generate_sine_wave(frequency, duration)
        play_obj = sa.play_buffer(audio_data, 1, 2, 44100)
        play_obj.wait_done()

if __name__ == '__main__':
    play_notes_from_file('notes/gpt4.json')
