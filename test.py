def findMinOperations(processingQueue):
    pattern = "abc"
    pointer = 0
    insertions = 0

    for char in processingQueue:
        while char != pattern[pointer]:
            instertions += 1
            pointer += (pointer + 1) % 3

        pointer = (pointer + 1) % 3

    while pointer != 0:
        insertions += 1
        pointer = (pointer + 1) % 3


    return insertions