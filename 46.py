# Python program to remove vowels from a string 
# Function to remove vowels 
def rem_vowel(string): 
	vowels = ('a', 'e', 'i', 'o', 'u') 
	for x in string.lower(): 
		if x in vowels: 
			string = string.replace(x, "") 
			
	# Print string without vowels 
	print(string) 

# Driver program 
string = input("Enter the string")
rem_vowel(string) 
