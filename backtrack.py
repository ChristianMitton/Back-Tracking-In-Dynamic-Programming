# In dynamic programming, when you want to return a specific sequence of data in an array (a1), you can use an auxiliary array (a2).

# Each idx AT a2 is used to reference the data in a1, and each idx STORED IN a2 points to the next idx AT a2 to go to.

# using a pointer, you can backtrack with an array like this.

    # Say we have this array (a1):

        # a1 = ['f','e','d','c','b','a']

    # And after dynamic programming, we obtain this array (a2):

        # a2 = [None, None, 0, 2, None, 3]

    # The sequence that would be printed, using a1 and a2, is: ['a' 'c' 'd' 'f']

array_1 = ['f','e','d','c','b','a']
array_2 = [None, None, 0, 2, None, 3]
startingIdx = 5

def backTrack(array_1, array_2, ptr):
    sequence = []
    while ptr != None:
        sequence.append(array_1[ptr])
        ptr = array_2[ptr]
    print(sequence)


backTrack(array_1, array_2, startingIdx)