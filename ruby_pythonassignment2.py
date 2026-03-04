                    ## Python Assignment 2 ##

##Section A:

#1. Create a string variable with your name and print it.
first_one="My name is Ruby Sangwan"
print(first_one)
#Output:- My name is Ruby Sangwan

#2. Store a string "Python" and print its length.
second_one="Python"
print(len(second_one))
#Output:- 6

#3. Create two string variables and join them using the + operator.
var1="Radha"
var2="Krishan"
print(var1 +var2)
#Output:- RadhaKrishan

#4. Store a word and print it 3 times using an operator.
one_word="time"
print(one_word*3)
#Output:- timetimetime

#5. Given a string "Hello World", print only "Hello".
two_words="Hello World"
print(two_words[:5])
#Output:- Hello

#6. Create a string and print its first and last character.
str1="myassignment"
print(str1[0])
print(str1[-1])
#Output:- m
#Output:- t

#7. Check whether the word "Python" exists in the string "I am learning Python".
my_word="I am learning python"
print(my_word.find("python"))
#Output:- 14

#8. Store a string with extra spaces at the beginning and end and remove the spaces.
extra_word="  accord "
print(extra_word.strip())
#Output:- accord

#9. Convert the string "python" to uppercase.
l_word="python"
print(l_word.upper())
#Output:- PYTHON

#10. Count how many times the letter "a" appears in "banana".
letter="banana"
print(letter.count("a"))
#Output:- 3

##Section B: Medium

#11. Given a string "Python Programming", print "Programming" using slicing.
char1="Python Programming"
print(char1[7:])
#Output:- Programming

#12. Store a string and check whether it starts with "Py".
star1="python"
print(star1[:2])
#Output:- py

#13. Store a string and check whether it ends with ".py".
#14. Replace "Java" with "Python" in the string "I like Java".
line1="I like Java"
print(line1.replace("Java", "Python"))
#Output:- I like Python

#15. Split the string "apple,banana,orange" into a list.
list1="apple,banana,orange"
print(list1.split(","))
#Output:- ['apple', 'banana', 'orange']

#16. Join the list ["I", "love", "Python"] into a single string.
list2= ["I", "love", "Python"]
print(" ".join(list2))
#Output:- I love Python

#17. Find the index of "data" in the string "big data engineering".
star2="big data engineering"
print(star2.find("data"))
#Output:- 4

#18. Compare two strings and print True if they are equal.
string_1="apple"
string_2="apple"
print(string_1 == string_2)
#Output:- True

#19. Use logical operators to check if a number is greater than 10 and less than 50.
value=30
print((value>10) and (value<50))
#Output:- True

#20. Use arithmetic operators to calculate the result of (20 + 10) * 2.
print((20 + 10) * 2)
#Output:- 60