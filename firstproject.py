def is_palindrome(input):
    #it converts the input to a string to deal with both number and word 
    input_str=str(input)
    input_str=''.join(char for char in input_str if char.isalnum())
    #now we check if the input string is equal to its reverse
    return input_str==input_str[::-1]
#user inputs their data
user_input=input('Enter a number or word:')
#using if-else we check if the input is a palindrome or not
if is_palindrome(user_input):
    print('Yes, it is a palindrome.')
else:
    print('No, it is not a palindrome.')