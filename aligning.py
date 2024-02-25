import mido

# Load the MIDI file
midi_file = mido.MidiFile('/content/output (2).mid')

# Define tempo (adjust as necessary)
tempo = 50

# Function to convert ticks to seconds based on the tempo
def ticks_to_seconds(ticks, tempo):
    return ticks * tempo / (1000 * midi_file.ticks_per_beat)

# Function to extract note events from MIDI file
def extract_notes(midi_file):
    notes = []
    current_time = 0
    for msg in midi_file:
        current_time += msg.time
        if msg.type == 'note_on':
            notes.append((current_time, msg.note))
    return notes

# Function to convert MIDI note number to note name
def note_number_to_name(note_number):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note_number // 12) - 1
    note = note_number % 12
    return f"{note_names[note]}{octave}"

# Function to align notes with lyrics
def align_notes_with_lyrics(lyrics, notes):
    aligned_lyrics = []
    note_index = 0
    for line in lyrics.split('\n'):
        line_notes = []
        words = line.split()
        for word in words:
            if word.isalpha():
                if note_index < len(notes):
                    line_notes.append(note_number_to_name(notes[note_index][1]))
                    note_index += 1
                else:
                    line_notes.append(None)
            else:
                for _ in range(len(word)):
                    if note_index < len(notes):
                        line_notes.append(note_number_to_name(notes[note_index][1]))
                        note_index += 1
                    else:
                        line_notes.append(None)
        aligned_lyrics.append((line, line_notes))
    return aligned_lyrics

# Load the lyrics
lyrics = """
But I don't want you never try round why alone
You're the only one I want yeah me through me time oh now up
In case it is the past night met me breathless
I know I left you speechless see me again deep for you
"""

# Call the function to extract notes from the MIDI file
notes = extract_notes(midi_file)

# Align notes with lyrics
aligned_lyrics = align_notes_with_lyrics(lyrics, notes)

# Output aligned lyrics with notes
for line, line_notes in aligned_lyrics:
    print(line)
    for note in line_notes:
        if note:
            print('{:<8}'.format(note), end='')
        else:
            print(' ' * 8, end='')
    print()
