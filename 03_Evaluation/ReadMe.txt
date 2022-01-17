
##Evaluation and results

An **application ontology** was implemented to validate the framework within its intended scope and determine whether its output behavior provides an acceptable accuracy.
Use-case-specific instances are modeled according to the conceptual ontology, creating a knowledge base/description model on an operational level. 
## The process of truck chassis assembly is used as an application scenario: 
The parts ‘cross member’, ‘front member’ and ‘rear member’ have to be transported from storage to the chassis and have to be screwed onto ‘chassis’. 
To fulfill this process, the capabilities ‘Screwing’, ‘Transporting’ and ‘Posi-tioning’ are requested with differing property parameters of acceleration, velocity, jerk, etc. 
As resources, several stationary robots (ABB_4600, ABB_2600), mobile robots (Kairos) and equipment (gripper, screwdriver) are available, which provide the requested capabilities in varying resource combinations.

A **video** of the evaluation scenario, implemented by the group Model-based Systems of the Laboratory for Machine Tools and Production Engineering WZL of RWTH Aachen, Chair of Production Metrology and Quality Management, Department Model-based Systems, can be found here: 
https://futureassemblydemonstrator.dashboards.vfk.ipt.fraunhofer.de/

Based on the application ontology, the framework’s performance is analyzed by measuring the time to process a task allocation. 
Twenty unique queries  with varying degrees of complexity were created and used as the seed for a randomizer to generate processes charts. 
For each data point, five process charts with the same number of queries, but unique randomized queries are processed and the run-time of these five charts is averaged to ensure uniform distribution of complexity within the five process charts. 

The graph ** “Average runtime vs. number of queries” ** presents the scaling performance of the ontology. 
The querying was carried out for 5, 25, 50, 100, 250, 500, 1000, 1500 and then every 1500 queries. 
Based on the test data, it shows linear scaling behavior. 
The graph ** “Runtime per query vs. number of queries” ** along with an R-Squared trendline, presents an upward trend, representing a non-linear behavior. 
When normalized to an error percentage of 0.8385, a linear behavior is obtained. 
t is concluded that the developed ontology has a linear scaling behavior within a margin of 0.8385 %.
 
It was shown that the developed framework is **scalable** as one can integrate new entities for application and inherit other ontologies. 

- As visualized in the figures querying and matching resources to tasks based on the required and provided capabilities was realized through SPARQL querying and Python-based allocation. 
- Capabilities resulting from combining resources to a new one can be inherited from one instance to another. 
- The needed interfaces for integrating a Python-based task allocation were developed and discussed. 

In summary, the derived requirements were met and a formal description model for resources as a base for task allocation was developed, reducing the time for task allocation, formally done manually. 
For application in automatic station formation planning further measures, like reachability and manipulability, path and trajectory planning with collision avoidance have to be included. 
Moreover, time relevance during application (e.g. traveling salesman problem) should be incorporated during task allocation, providing optimized allocation. 
