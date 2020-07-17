#part 1
#get input from user
userInput = str(input("Enter a phrase: "))
#convert to lower and print
newInput = userInput.lower()
print(newInput)

#part 2
#create vowel list
vowels = ["a", "e", "i", "o", "u"]
for i in newInput:
  if i in vowels: #check the vowel list
    print(i + " is a vowel")
  else:
    print(i + " is a consonant")


