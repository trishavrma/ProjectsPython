src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

with open(src, "r") as f:
    data = f.read()

data = data.upper()

with open(dest, "w") as f:
    f.write(data)

print("Content written in uppercase to", dest)