import os
import shutil

mainDir = os.getcwd()
toCopy = list(os.walk(mainDir))
print(toCopy)
