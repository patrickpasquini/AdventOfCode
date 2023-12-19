def read_input():
    print("Insert the challenge input")
    documents = []
    while True:
        line = input()
        if line == "":
            break
        documents.append(line)
    return documents
