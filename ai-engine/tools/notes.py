_notes=[]
def add_note(text):
    _notes.append(text); return "note_saved"
def get_notes(): return list(_notes)
