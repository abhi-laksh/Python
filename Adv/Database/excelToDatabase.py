import pandas as pd
from urllib.request import Request, urlopen 

print("Opening Google...")
req=Request("https://www.brainwareuniversity.ac.in/")

google = urlopen(req)
print(google.read())
print("Google opened.")

# print "Opening localhost..."
# localhost = url.urlopen("http://localhost:8280/")
# print localhost.read(100)
# print "localhost opened."