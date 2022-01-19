import csv
from LMAS_00 import SPARQL_2Query
from LMAS_00 import SPARQL_3Query
from LMAS_00 import SPARQL_4Query
from LMAS_00 import SPARQL_5Query
from LMAS_00 import SPARQL_6Query
from LMAS_00 import SPARQL_7Query
from LMAS_00 import SPARQL_8Query
from Allocation_00 import Allocation

def Read_ProcessChart (chart):

    data = ("Process/%s - Sheet1.csv" %chart)

    with open(data) as csv_file:
        csv_reader = list(csv.reader(csv_file))

        #print(csv_reader[1])
        #print(len(csv_reader))
        #print(csv_reader)

        holon_allocation = []
        holon_size = len(csv_reader)

        for holon in range(holon_size-1):

            #print(csv_reader[holon+1])
            Holon_Type = (csv_reader[holon+1][1])   # Allocating Holon Type
            Holon_Cap1 = (csv_reader[holon+1][2])   # Allocating Holon Capability 1
            Holon_Cap2 = (csv_reader[holon+1][3])   # Allocating Holon Capability 2
            Holon_Cap3 = (csv_reader[holon+1][4])   # Allocating Holon Capability 3
            Holon_Cap4 = (csv_reader[holon+1][5])   # Allocating Holon Capability 4
            Holon_Cap5 = (csv_reader[holon+1][6])   # Allocating Holon Capability 5
            Holon_Comp = (csv_reader[holon+1][7])   # Allocating Holon Compatibility
            Holon_Eqip = (csv_reader[holon+1][8])   # Allocating Holon Equipment

            #print(Holon_Type)
            #print(Holon_Cap1)

            if Holon_Comp == 'None' and Holon_Eqip == 'None':

                if Holon_Cap2 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print('')

                    query = SPARQL_2Query(Holon_Type, Holon_Cap1)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap3 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print('')
                    query = SPARQL_3Query(Holon_Type, Holon_Cap1, Holon_Cap2)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap4 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print('')
                    query = SPARQL_4Query(Holon_Type, Holon_Cap1, Holon_Cap2, Holon_Cap3)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print('')
                    query = SPARQL_5Query(Holon_Type, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 != 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print("Holon Capability 5 :%s" % Holon_Cap5)
                    #print('')
                    query = SPARQL_6Query(Holon_Type, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4, Holon_Cap5)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                else:

                    print("Query Function Not Valid")

            elif Holon_Comp != 'None' and Holon_Eqip == 'None':

                if Holon_Cap2 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print('')
                    query = SPARQL_3Query(Holon_Type, Holon_Comp, Holon_Cap1)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap3 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print('')
                    query = SPARQL_4Query(Holon_Type, Holon_Comp, Holon_Cap1, Holon_Cap2)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap4 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print('')
                    query = SPARQL_5Query(Holon_Type, Holon_Comp, Holon_Cap1, Holon_Cap2, Holon_Cap3)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print('')
                    query = SPARQL_6Query(Holon_Type, Holon_Comp, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 != 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print("Holon Capability 5 :%s" % Holon_Cap5)
                    #print('')
                    query = SPARQL_7Query(Holon_Type, Holon_Comp, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4, Holon_Cap5)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                else:

                    print("Query Function Not Valid")

            elif Holon_Comp == 'None' and Holon_Eqip != 'None':

                if Holon_Cap2 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print('')
                    query = SPARQL_3Query(Holon_Type, Holon_Eqip, Holon_Cap1)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap3 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print('')
                    query = SPARQL_4Query(Holon_Type, Holon_Eqip, Holon_Cap1, Holon_Cap2)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap4 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print('')
                    query = SPARQL_5Query(Holon_Type, Holon_Eqip, Holon_Cap1, Holon_Cap2, Holon_Cap3)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print('')
                    query = SPARQL_6Query(Holon_Type, Holon_Eqip, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 != 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print("Holon Capability 5 :%s" % Holon_Cap5)
                    #print('')
                    query = SPARQL_7Query(Holon_Type, Holon_Eqip, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4, Holon_Cap5)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                else:

                    print("Query Function Not Valid")

            elif Holon_Comp != 'None' and Holon_Eqip != 'None':

                if Holon_Cap2 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print('')
                    query = SPARQL_4Query(Holon_Type, Holon_Comp, Holon_Eqip, Holon_Cap1)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap3 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print('')
                    query = SPARQL_5Query(Holon_Type, Holon_Comp, Holon_Eqip, Holon_Cap1, Holon_Cap2)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap4 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print('')
                    query = SPARQL_6Query(Holon_Type, Holon_Comp, Holon_Eqip, Holon_Cap1, Holon_Cap2, Holon_Cap3)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 == 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print('')
                    query = SPARQL_7Query(Holon_Type, Holon_Comp, Holon_Eqip, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                elif Holon_Cap5 != 'None':

                    #print("Holon Type :%s" % Holon_Type)
                    #print("Holon Compatibility :%s" % Holon_Comp)
                    #print("Holon Equipment :%s" % Holon_Eqip)
                    #print("Holon Capability 1 :%s" % Holon_Cap1)
                    #print("Holon Capability 2 :%s" % Holon_Cap2)
                    #print("Holon Capability 3 :%s" % Holon_Cap3)
                    #print("Holon Capability 4 :%s" % Holon_Cap4)
                    #print("Holon Capability 5 :%s" % Holon_Cap5)
                    #print('')
                    query = SPARQL_8Query(Holon_Type, Holon_Comp, Holon_Eqip, Holon_Cap1, Holon_Cap2, Holon_Cap3, Holon_Cap4, Holon_Cap5)
                    #print(query)
                    holon_allocation = Allocation(query, holon_allocation)
                    #print('')

                else:

                    print("Query Function Not Valid")

            else:

                print("Query Function Not Valid")

    return (holon_allocation)
