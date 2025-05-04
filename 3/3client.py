import Pyro4

uri=input("enter uri of server")
concatenator=Pyro4.Proxy(uri)

str1=input("enter string 1")
str2=input("enter string 2")

result=concatenator.concatenate(str1,str2)
print(result)