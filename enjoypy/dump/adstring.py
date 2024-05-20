def is_caps_lock(text):
    # Sprawdzamy, czy większość liter w tekście jest dużych
    letters = [char for char in text if char.isalpha()]
    
    if not letters:  # Jeśli nie ma liter w tekście, trudno stwierdzić stan Caps Locka
        return False
    
    upper_case_count = sum(1 for char in letters if char.isupper())
    lower_case_count = len(letters) - upper_case_count
    
    return upper_case_count > lower_case_count

# Przykłady użycia
texts = [
    "THIS IS A TEST.",
    "this is a test.",
    "This Is A Test.",
    "tHIS IS A TEST."
]

for text in texts:
    if is_caps_lock(text):
        print(f'"{text}" was typed with Caps Lock on.')
    else:
        print(f'"{text}" was not typed with Caps Lock off.')
