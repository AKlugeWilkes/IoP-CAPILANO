

def Allocation(input, output):

    query_len = len(input)

    for holon in range(query_len):

        if input[holon] in output:

            a = 0

        else:

            output.append (input[holon])
            break

    return (output)
