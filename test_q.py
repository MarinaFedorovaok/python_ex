def palindrome_or_not(string):
    reversed_string = string[::-1]
    return string == reversed_string
print(palindrome_or_not('12321'))
a=5
b=4
a,b = b,a
print(a)
print(b)