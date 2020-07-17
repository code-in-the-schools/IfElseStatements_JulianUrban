#part 1
#get input from user
userInput = str(input("Enter a phrase: "))
#convert to lower and print
newInput = userInput.lower()
print(newInput)

#part 2
#create vowel list
vowels = ["a", "e", "i", "o", "u"]
#variables for tracking vowels and consonants
numVowels = 0
numConsonants = 0
for i in newInput:
  if i in vowels: #check the vowel list
    print(i + " is a vowel")
    numVowels = numVowels + 1
  else: #otherwise it's a consonant
    print(i + " is a consonant")
    numConsonants = numConsonants + 1
#print vowels and consonants
print("# of vowels: " + str(numVowels))
print("# of consonants: " + str(numConsonants))
