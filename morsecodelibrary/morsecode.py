from morsecodelibrary import alphabet


def text_to_code(text):
    code = []
    for word in text.split():
        morse_word = []
        for character in word:
            morse_word.append(alphabet.letters_to_code.get(character.upper()))
        code.append('_'.join(morse_word))
    return '|'.join(code)


def code_to_text(code):
    text = []
    for morse_word in code.split('|'):
        word = []
        for morse_sequence in morse_word.split('_'):
            letter = alphabet.code_to_letters.get(morse_sequence)
            word.append(letter)
        text.append(''.join(word))
    return ' '.join(text)
