# Complete the following challenges on the Codewars Platform:

# Even or Odd - https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

# Convert a Number to a String - https://www.codewars.com/kata/5265326f5fda8eb1160004c8

# Vowel Count - https://www.codewars.com/kata/54ff3102c1bad923760001f3

# Once you’ve come up with a solution that has been tested and passes the attempt do the following:
# In VS Code, copy and paste all three solutions into a single .py file 
# Separate the solutions with a comment identifying each one
# Create a GitHub repository to host your assignment 
# Add, commit, push your code to the repository
# Submit the repository link here in Google Classroom

# 1 challange: odd or even
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# 2 challange: convert a number to a string
def number_to_string(num):
    return str(num)


# 3 challange: vowel count
def get_count(sentence):
    vowels = "aeiou"
    count = 0

    for vowel in sentence:
        if vowel in vowels:
            count += 1
    
    return count


