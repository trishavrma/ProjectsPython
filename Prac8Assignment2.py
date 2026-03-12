src = input("Enter source python file: ")
dest = input("Enter destination file: ")

with open(src, "r") as f:
    lines = f.readlines()

with open(dest, "w") as f:
    for line in lines:
        if not line.strip().startswith("#"):
            f.write(line)

print("\nSource File Content:\n")
with open(src, "r") as f:
    print(f.read())

print("\nDestination File Content (without comments):\n")
with open(dest, "r") as f:
    print(f.read())