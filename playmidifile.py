import pretty_midi

def notes_to_midi(notes, output_file='output.mid', tempo=120):
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create an Instrument instance
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    # Define some constants for clarity
    time = 0
    velocity = 100

    # Add notes
    for note_str in notes:
        if note_str.isdigit():
            # Rest
            time += int(note_str)
        else:
            note_number = pretty_midi.note_name_to_number(note_str)
            note = pretty_midi.Note(
                velocity=velocity, pitch=note_number, start=time, end=time + 1)
            piano.notes.append(note)
            time += 1

    # Add the piano instrument to the MIDI object
    midi_data.instruments.append(piano)

    # Adjust tempo by stretching or compressing the notes
    tempo_ratio = tempo / 120.0
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            note.start *= tempo_ratio
            note.end *= tempo_ratio

    # Write the MIDI data to disk
    midi_data.write(output_file)

notes = ['11', 'F#3', 'F#4', 'A2', 'F#4', 'B2', 'D3', 'E4', 'E2', 'D3', 'D3', 'F#4', 'G2', 'E2', 'D3', 'B4', 'G2', 'A2', 'D4', 'A2', 'F#4', 'B2', 'C#4', 'B4', 'F#4', 'A4', 'F#4', 'A2', 'B2', 'G2', 'A4', 'E2', 'E4', 'A4', 'D4', 'A2', 'G2', 'F#4', 'E2', 'D2', 'D4', 'B2', 'A4', 'E2', 'A2', 'F#4', 'A4', 'E2', 'B2', 'E2', 'E4', 'B2', 'A2', 'B2', 'E2', 'E4', 'A2', 'B2', 'B2', 'A2', 'A4', 'A4', 'B2', 'D2', 'B2', 'A2', 'B2', 'A2', 'F#4', 'D3', 'D3', 'F#4', 'B2', 'D4', 'F#4', 'G4', 'B2', 'B2', 'A4', 'G2', 'B2', 'B2', 'C#4', 'B2', 'F#4', 'D2', 'A2', 'D3', 'E2', 'E2', 'E4', 'G2', 'D3', 'C#4', 'C#4', 'A4', 'F#4', 'A4', 'F#4', 'A2']
output_file = 'output.mid'
tempo = 50

notes_to_midi(notes, output_file, tempo)
