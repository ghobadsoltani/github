import string

print(dir(string))    
# print(var(string))    



# all of methods in (any) madule
print(vars(string))            # complete info about all of methods in (any) madule

# all methods in string

['Formatter', 'Template', '_ChainMap', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']



# print(string.__doc__)   >>
# A collection of string constants.

# Public module variables:

# whitespace -- a string containing all ASCII whitespace
# ascii_lowercase -- a string containing all ASCII lowercase letters
# ascii_uppercase -- a string containing all ASCII uppercase letters
# ascii_letters -- a string containing all ASCII letters
# digits -- a string containing all ASCII decimal digits
# hexdigits -- a string containing all ASCII hexadecimal digits
# octdigits -- a string containing all ASCII octal digits
# punctuation -- a string containing all ASCII punctuation characters
# printable -- a string containing all ASCII characters considered printable

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print(string.printable)
print(string.capwords('ghobad soltani'))
a=string.Template('answer is : $x>$y')
str1=a.substitute(x=23,y=14)
print(str1)





