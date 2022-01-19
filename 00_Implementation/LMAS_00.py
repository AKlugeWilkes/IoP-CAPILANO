from owlready2 import *
import owlready2


def SPARQL_2Query (type, cap1):

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

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

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

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

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

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

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

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

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

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

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

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

    owlready2.JAVA_EXE = "C:/Program Files/Java/jre1.8.0_301/bin/java.exe"

    onto_path.append("D:/Data/RWTH/WZL/Thesis/Ontology")
    onto = get_ontology("LMAS_02.owl")
    onto.load()

    sync_reasoner(onto)

    #type = "MobileManipulator"
    #cap1 = "Screwing"
    #cap2 = "Transporting"

    #print("Testing %s" % (para))

    test = list(default_world.sparql("""SELECT ?holon WHERE {?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s . ?holon rdf:type LMAS_02:%s}""" % (type, cap1, cap2, cap3, cap4, cap5, cap6, cap7)))

    #graph = onto.world.as_rdflib_graph()
    #test = list(graph.query_owlready("""SELECT ?holon WHERE {?holon LMAS_02:Robot . }"""))

    #print(test)
    return (test)
