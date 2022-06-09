def search(text,word):
   if word in text:
      print("Word found")
   else:
      print("Word not found")
text = str(input("Enter a text   " ))
word = str(input("Enter a word   " ))
search(text,word)
