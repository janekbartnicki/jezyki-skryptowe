def is_palindrome(word):
    word = word.lower()

    if len(word) <= 1:
        return True

    if word[::-1] == word:
        return True

    return False


user_input = input("Podaj słowo: ")
print('Palindrom' if is_palindrome(user_input) else 'To nie palindrom')
