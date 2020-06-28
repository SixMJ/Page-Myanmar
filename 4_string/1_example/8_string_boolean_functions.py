# 'only alphanumeric characters (no symbols)'
str1 = "Hello"
print('isalnum    -' + str(str1.isalnum()))
str2 = "Hello"
print('isalnum    -' + str(str2.isalnum()))

# 'only alphabetic characters (no symbols)'
print('isalpha    -' + str(str1.isalpha()))
str2 = "Hello123"
print('isalpha    -' + str(str2.isalpha()))

#only numeric characters
print('isnumeric    -' + str(str1.isnumeric()))
str2 = "123"
print('isnumeric    -' + str(str2.isnumeric()))