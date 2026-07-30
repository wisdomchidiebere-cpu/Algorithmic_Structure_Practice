#isPalindrome("racecar") → true
#isPalindrome("A man a plan a canal Panama") → true
#isPalindrome("hello") → false

def isPalindrome(text):
	if isinstance(text, str) != True or text.strip() == "":
		return False
	
	text = text.lower()
	
	textList = [item for item in text if item.strip() != ""]
	
	return "".join(reversed(textList)) == "".join(textList)

print(isPalindrome("racecar"))


#This code checks if a string is a palindrome, returning true if it is and false if it isn't. It does this by converting the string to lowercase and then using list comprehension it filters only the letters of the string into a list thereby ignoring whitespaces, afterwhich the string is reversed and compaired to the original arrangement to comfirm if it is the same when reversed. The code also handles edge cases such as numbers or empty string by returning false early.