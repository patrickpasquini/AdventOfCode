def read_input():
    print("Insert the challenge input")
    document = []
    while True:
        line = input()
        if line == "":
            break
        document.append(line)
    return document