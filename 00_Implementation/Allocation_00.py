#
# CAPILANO - Resource Allocation Module
#
#Document Control
#
#V3.3 - 19.01.2022 - Adapted the system to be agnostic - KLW_GNS
#V3.2 - 03.01.2022 - Adjusted query lengtlh overflow - KLW_GNS
#V3.1 - 27.12.2021 - Variable renaming - KLW_GNS
#V3.0 - 20.12.2021 - V3.0 Stable Release - KLW_GNS
#V2.1 - 11.12.2021 - Adapting Functional operation from the root - KLW_GNS
#V2.0 - 22.11.2021 - V2.0 Stable Release - KLW_GNS
#V1.1 - 02.11.2021 - Finalizing allocation logics - KLW_GNS
#V1.0 - 15.10.2021 - Draft Program - KLW_GNS
#
#Author(s):
#
#KLW_GNS - Balaji Gunaseelan
#

def Allocation(input, output):

    query_len = len(input)

    for holon in range(query_len):

        if input[holon] in output:

            a = 0

        else:

            output.append (input[holon])
            break

    return (output)
