# modified file
###......................
# Class 

class myClass:
	def __init__ (self,name):
		self.name = name
		print("Welcome " + self.name)
		
obj = myClass("Talqeen Ahmad")

#............................................................................



# for finding occurences in string

def findOccurence(a,b):
	print(a.count(b))			

# for replacing substring in a string

def replaceString(a,b,c):
	print("Your desired string is: "),a.replace(b,c)



userString = input("Enter a string: ")
print("You entered: "),userString
subString = input("Enter a letter or word to check its occurences in this string: ")
findOccurence(userString,subString)



replaceStr = input("Enter a string you want to replace: ")
replaceStringWith = input("Enter a string you want to replace with: ")
replaceString(userString,replaceStr,replaceStringWith)
