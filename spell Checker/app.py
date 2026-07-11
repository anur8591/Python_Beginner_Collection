#pip install pyspellchecker
from spellchecker import SpellChecker

class SpallCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_word = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'correction "{word}" to "{corrected_word}"')
                corrected_word.append(corrected_word)

        return ' '.join(corrected_word)
    
    def run(self):
        print("\n---Spell_Checker---")

        while True:
            text = input("Enter text to check(or type 'exit' to quit): ")
            if text.lower() == 'exit':
                print('closing the program....')
                break
            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {self.correct_text}')

if __name__ == "__main__":
    SpallCheckerApp().run()