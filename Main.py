from CSV_Demo_00 import Read_ProcessChart_Demo
from CSV_00 import Read_ProcessChart
from LMAS_00 import SPARQL_7Query
import time

#Read_ProcessChart_Demo("P3")
Holon_allocation = Read_ProcessChart("P3")

time.sleep(0.0005)

print('')
print(Holon_allocation)
print('')

#query = SPARQL_7Query("Robot", "Positioning", "Transporting", "Linear_Rails", "Gripping", "RearMember", "RearMember_Gripper")
#print(query)
