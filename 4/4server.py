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
