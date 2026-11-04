from builtins import print


file = open("sample.txt", "w")
file.write("Hello, World!\n")
file.write("Welcome to Python Programming.\n")
file.write("This is my first file handling program.")

# Close the file
file.close()

print("Text successfully written to sample.txt!")