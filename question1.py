count = 0

# loop through all possible first digits
for first in range(1, 10):

    # loop through all possible second digits
    for second in range(first+1, 10):

        # count the number of two-digit numbers with the given digits
        count += 1

        # loop through all possible third digits
        for third in range(second+1, 10):

            # count the number of three-digit numbers with the given digits
            count += 1

            # loop through all possible fourth digits
            for fourth in range(third+1, 10):

                # count the number of four-digit numbers with the given digits
                count += 1

# output the result
print(count)
