import Pyro4
@Pyro4.expose
class PalindromeChecker:
    
    def is_palindrome(self, string):
        string = string.lower()  # Convert string to lowercase for case-insensitive palindrome check
        return string == string[::-1]  # Check if the string is equal to its reverse

daemon = Pyro4.Daemon()
uri = daemon.register(PalindromeChecker)

print("Ready. Object uri =", uri)
daemon.requestLoop()

###################################################################################################
import Pyro4

uri = input("Enter the URI of the PalindromeChecker object: ")
palindrome_checker = Pyro4.Proxy(uri)

string = input("Enter a string to check if it's a palindrome: ")

if palindrome_checker.is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

