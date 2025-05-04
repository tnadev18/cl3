import Pyro4

uri = input("Enter the URI of the PalindromeChecker object: ")
palindrome_checker = Pyro4.Proxy(uri)

string = input("Enter a string to check if it's a palindrome: ")

if palindrome_checker.is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
