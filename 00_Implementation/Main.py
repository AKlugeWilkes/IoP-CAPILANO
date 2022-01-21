#
# CAPILANO - Module
#
#Document Control
#
#
#V3.3 - 19.01.2022 - Adapted the system to be agnostic - KLW_GNS
#V3.2 - 03.01.2022 - Adjusted query lengtlh overflow - KLW_GNS
#V3.1 - 27.12.2021 - Variable renaming - KLW_GNS
#V3.0 - 20.12.2021 - V3.0 Stable Release - KLW_GNS
#V2.3 - 15.12.2021 - Updated HermiT reasoning logic - KLW_GNS
#V2.2 - 12.12.2021 - Added SPARQL query verification step - KLW_GNS
#V2.1 - 11.12.2021 - Adapting Functional operation from the root - KLW_GNS
#V2.0 - 22.11.2021 - V2.0 Stable Release - KLW_GNS
#V1.3 - 10.11.2021 - Integrated Diagonisis module into the terminal - KLW_GNS
#V1.2 - 05.11.2021 - Integrated Cython phaser for Windows 10 - KLW_GNS
#V1.1 - 02.11.2021 - Finalizing allocation logics - KLW_GNS
#V1.0 - 15.10.2021 - Draft Program - KLW_GNS
#
#Author(s):
#
#KLW_GNS - Balaji Gunaseelan
#

from CSV_Demo_00 import Read_ProcessChart_Demo
from CSV_00 import Read_ProcessChart
from LMAS_00 import SPARQL_7Query
import time

#Read_ProcessChart_Demo("P2")
Holon_allocation = Read_ProcessChart#("Insert Process Chart Name")

time.sleep(0.0005)

print('')
print(Holon_allocation)
print('')

#query = SPARQL_7Query("Robot", "Positioning", "Transporting", "Linear_Rails", "Gripping", "RearMember", "RearMember_Gripper")
#print(query)
