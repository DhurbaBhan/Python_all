with open("sample.txt") as f:
    data=f.read()
    if "Dhurba" in data:
        print("Dhurba is present in sample.txt")
    else:
        print("Dhurba is not present.")