string=input("Enter string:")
lowerCase=0
upperCase=0
letters = 0
digits = 0
for i in string:
      if(i.islower()):
            lowerCase=lowerCase+1
      elif(i.isupper()):
            upperCase=upperCase+1
            
for i in string:
    if(i.isnumeric() == True):
        digits = digits+1

letters = upperCase + lowerCase
        

print("The number of lowercase characters is:")
print(lowerCase)
print("The number of uppercase characters is:")
print(upperCase)
print("The Number of Digits in the Sentence is: ")
print(digits)
print("The Number of Letters in the Sentence is: ")
print(letters)