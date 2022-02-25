try:
    klu = open("file.txt", "r+")
    try:
        klu.write("This is Section-3")
    finally:
        klu.close()
except IOError:
    print("File not Found")
else:
    print("File Opened Successfully")
    klu.close()
