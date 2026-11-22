def check_palindrome():
     word = input("what is your name: ").strip().lower()
     if not word:
            print("abeg put correct answer, joor.")
            return
        # turn the word around using slicing[::-1]
     if word == word[::-1]:
            print(f"yes, {word} na palindrome true true.")
     else:
            print(f"no, {word} no be palindrome.")

# call the function to check for palindrome
check_palindrome()