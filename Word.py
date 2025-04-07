from datetime import date

class Word:
    def __init__(self, word: str):
        self.word = word
        self.date_to_add = date.today()

    def __str__(self):
        return f"Word('{self.word}', Date Added: {self.date_to_add})"
    
    def __len__(self):
        return len(self.word)
    
    def get_word(self):
        return self.word


# Example usage
if __name__ == "__main__":
    w = Word(word="example")
    print(w)
