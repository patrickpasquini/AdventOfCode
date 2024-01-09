def read_input():
    print("Insert the challenge input")
    documents = []
    count = 0
    while True:
        line = input()

        if line == "":
            count += 1
        if count == 2:
            break
        documents.append(line)
    return documents
