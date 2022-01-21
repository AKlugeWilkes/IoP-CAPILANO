#
# CAPILANO - Diagonostic Module
#
#Document Control
#
#V1.1 - 17.01.2022 - Adapted for V3.X CAPILANO module - KLW_GNS
#V1.0 - 15.12.2021 - Draft Program - KLW_GNS
#
#Author(s):
#
#KLW_GNS - Balaji Gunaseelan
#

from Allocation_00 import Allocation

holon_allocation = []
#print(holon_allocation)
query = [['Holon1'], ['Holon2'], ['Holon3']]

holon_allocation = Allocation(query, holon_allocation)
print(holon_allocation)
holon_allocation = Allocation(query, holon_allocation)
print(holon_allocation)
holon_allocation = Allocation(query, holon_allocation)
print(holon_allocation)
holon_allocation = Allocation(query, holon_allocation)
print(holon_allocation)

