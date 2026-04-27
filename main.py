def is_palindrome(text):
    cleaned=""
    for char in text:
        if char.isalnum():
            cleaned +=char.lower()
    length=len(cleaned)
    for i in range(length//2):
        if cleaned[i]!=cleaned[length-1-i]:
            print(f"'{text}' is not a palindrome")
    print(f"'{text}' is a palindrome!")

text=input("enter text: ")
is_palindrome(text)