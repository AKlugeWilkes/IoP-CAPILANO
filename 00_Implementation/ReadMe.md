# Implementation

This section provides the basic instructions to Implement the CAPILANO system on any Windows 10 based environment. The necessary programing environments and their relevant packages are listed below. A short description of the roles of each Python program along with the list of necessary programs required to run the CAPILANO system are also listed below.

# **Python Programs**

## Allocation_00.py

This program is responsible for Checking the SPARQL query results extracted from the CAPILANO ontology and to ensure that the right tasks are allocated to the right resourses through the means of a primary function key initialized during the process chart initilization process, and it prevents duplication of tasks or resources.

## CSV_00.py

This program reads the process chart in the CSV format and converts into a custom Python object, which consists of the various capabilities and their respective parameters the resource must have to fulfil a particular task. The process chart is in a particular order and the resource allocation has to follow this order, to ensure the data is locked in the order in which it is read through a primary function key, which is used during allocation.

## LMAS_00.py

This program initializes the OWLReady2.0 package along with the Java environment, Cython Phaser, SPARQL querying environment and the HermiT Reasoner. The user must update this program with a valid path for the JAVA.EXE file, the ontology and its IRI name and the HermiT Reasoner. Therefor one has to follow the comments on the program and ensure that the path is in the correct syntax. This program is responsible for processing the SPARQL queries, once the queries are processed it passes it to the the SPARQL query environment. Based on the query pattern the HermiT Reasoner acts on the OWL ontology object and returns the query results back to this program as a custom Python object.

## Main.py

This is the main Python program. It handles the sequence of operation of the CAPILANO system. It is also responsible for the diagonistic module ports and the terminal functions. Ensure that the every other python programs are witin the root source of this program, if it is not the case correct the package/function import commands with the respective paths.

## Test_00.py

This is a diagnostic module which tests the CAPALIONO program with a standardised set of queries to ensure proper working of all sub-systems and functions related to the system. It also produces a log of all the terminal commands that were processed during the run-time of the CPAIALNO system to help with the diagnostic process. This program is incapable of fixing any erros or exceptions that may arise during the run-time.

## Time.py

In case the run-time of the system needs to be timed, the CAPILANO system is initiated through this program instead of the main.py program. This program counts the number of processing cycles utilized by the CAPILANO system during its run-time and compares it to the clock speed of the host system to provide an accurate overall run-time of the system. It is also utilized by the diagnostic module (Test_00.py) to check of any host system based errors. The evalautation of the CAPILANO system and its performance analysis untilizes thos program to get the run-time of the system.

# **Necessary Programs**

- Main.py
- LMAS_00.py
- Allocation_00.py
- CSV_00.py

# **Necessary Packages**

- OWLReady2.0
- Cython Phaser
- HermiT Reasoner
- Java Environment
- NumPy
- Pandas
- time

# Steps to run CAPILANO

1. Open LMAS_00.py and update the paths for JAVA.EXE, Ontology, Ontology IRI, and HermiT Reasoner.
2. Open CSV_00.py and update the path for the process chart and if applicable change the naming according to the convection.
3. Open Main.py and run the program to execute the CAPLILANO system.
4. (Optional) If the run-time of the system has to be monitored open Time.py and run the program to execute the CAPLILANO system.
