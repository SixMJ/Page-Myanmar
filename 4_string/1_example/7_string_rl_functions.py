str1 = "Hello"
print('ljust      -' + str1.ljust(10,'$')) # left justify
str1 = "     Hello"
print('lstrip     - ' + str1.lstrip()) # left leading

str1 = "Hello  "
print('rstrip     -' + str1.rstrip()) # right leading
str1 = "Hello World"
print('rfind      - ' + str(str1.rfind('o')))
print('rindex      - ' + str(str1.rindex('o'))) # like rfind throw error
print('rjust      - ' + str(str1.rjust(10 ,'$')))
print('rsplit      - ' + str(str1.rsplit('o'))) # returns a list