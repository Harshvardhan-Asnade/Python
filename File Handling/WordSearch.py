with open("sample.txt", "r") as f:
    data = f.read()

if "Python" in data:
    print("Word found")
else:
    print("Word not found")