#!/usr/bin/env python
# coding: utf-8


import os
from ms3 import Score



def is_detuned_note(tag) -> bool:
    if tag.name != "Note":
        return False
    return bool(tag.find("tuning"))

def adjust_tag(tag):
    """Diminishes the tag's integer string by 2, mutating it in-place."""
    adjusted_value = int(tag.string) - 2
    tag.string = str(adjusted_value)

def change_pitches(score):
    """Mutates XML in Score object."""
    soup = score.mscx.parsed.soup
    notes = soup.find_all(is_detuned_note)
    for note_tag in notes:
        tuning_tag = note_tag.tuning
        if tuning_tag.string != "-200":
            raise ValueError(note_tag)
        tuning_tag.decompose()
        adjust_tag(note_tag.tpc)
        adjust_tag(note_tag.pitch)
    print(f"Adjusted {len(notes)} detuned notes.")
    
def write_modified_score(filename, new_filename):
    """Assumes current working directory to be where the file is located."""
    s = Score(filename)
    change_pitches(s)
    print(filename)
    s.mscx.store_score(new_filename)
    print(f"Wrote the adjusted score to {new_filename}.")

def modify_all_scores_having_prefix(directory, prefix="detuned_"):
    for filename in os.listdir(directory):
        if not filename.endswith('.mscx') or not filename.startswith(prefix):
            continue
        filepath = os.path.join(directory, filename)
        new_filename = filepath.replace(prefix, "")
        write_modified_score(filepath, new_filename)
    
if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    modify_all_scores_having_prefix(directory)


# In[ ]:




