#
# CAPILANO - OWLReady2.0 Integration Module
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

from owlready2 import *
import owlready2


def SPARQL_2Query (type, cap1):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)


def SPARQL_3Query (type, cap1, cap2):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)


def SPARQL_4Query (type, cap1, cap2, cap3):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2, cap3)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)


def SPARQL_5Query (type, cap1, cap2, cap3, cap4):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2, cap3, cap4)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)


def SPARQL_6Query (type, cap1, cap2, cap3, cap4, cap5):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2, cap3, cap4, cap5)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)


def SPARQL_7Query (type, cap1, cap2, cap3, cap4, cap5, cap6):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2, cap3, cap4, cap5, cap6)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)


def SPARQL_8Query (type, cap1, cap2, cap3, cap4, cap5, cap6, cap7):

    owlready2.JAVA_EXE = #"Insert JAVA.exe path" 

    onto_path.append#("Insert Ontology Path")
    onto = get_ontology#("Insert ontology name")
    onto.load()

    sync_reasoner(onto) #HermiT reasoner

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2, cap3, cap4, cap5, cap6, cap7)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)
