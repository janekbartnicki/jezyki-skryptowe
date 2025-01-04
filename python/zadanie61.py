class ReverseText:
    def reverse(self, text):
        sentences = text.split(' ')
        sentences.append(sentences.pop(0))
        return ' '.join(sentences)



text = "Jestem studentem. Jestem studentem."
reverser = ReverseText()
output = reverser.reverse(text)
print(output)
