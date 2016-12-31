print()
print("############  next call  ###################")
word1 = 'Wow'
word2 = 'Wow'
print('Equality:  word1 == word2  Alias word1 is word2')
print('Equality:', word1 == word2, ' Alias:', word1 is word2)

print()
print("############  next call  ###################")
name = input("Please enter your name: ")
print("Hello " + name.upper() + ", how are you?")

print()
print("############  next call  ###################")
word = "ABCD"
print(word.rjust(10, "*"))
print(word.rjust(3, "*"))
print(word.rjust(15, ">"))
print(word.rjust(10))

print()
print("############  next call  ###################")
# Strip leading and trailing whitespace and count substrings
s = " ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ "
print("[", s, "]", sep="")
s = s.strip()
print("[", s, "]", sep="")
# Count occurrences of the substring "BCD"
print(s.count("BCD"))