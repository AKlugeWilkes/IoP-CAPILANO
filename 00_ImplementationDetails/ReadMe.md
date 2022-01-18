## Implementation

The framework consists of a means of storing and retrieving data (**data lake**), converting this data into a tailored schema (**data conversion**), querying the data in the ontology (here: CAPILANO) followed by **allocation** of the querying results, and converting the results back into a storable data format and thus closing the circle to the data lake. 
Realizing the frameworks goal to match the task´s requirements to the resources´ capabilities, the process of querying and consecutive task allocation is detailed. 
 
In a **pre-processing** stage the input process chart is retrieved from the data lake and converted into a custom schema adapted from the functional methodology of the MaRCO ontology, and the C4I metamodel. 
The process chart contains the information regarding the requirements to perform the tasks and the task order. 
Moreover the ontology including the resource and capability modelling is extracted. 
The information contained is resource identifier, resource type, resource capabilities, resource compatibility and resource equipment. 
A resource can have multiple capabilities, so each capability is allotted its column. 


During the **processing step**, querying and task allocation are carried out. 
The Python program communicates with the OWL-based ontological system through the Python add-on package "owlReady2".
To generate the inferred hierarchy with OwlReady2 an external virtually isolated Java environment is deployed for the HermiT Reasoner. 
The resulting inferred hierarchy is used as foundation for the querying of matching capabilities and is derived at request.
Enabling duplex data transmission a communication channel between the Python environment and the virtually isolated Java environment is established through a Cython phaser. 
Through the Cython phaser advanced reasoner commands can be sent to the virtually isolated Java environment and the inferred hierarchy can be accessed for querying. 
For querying, the requested list of capabilities of the process chart is converted in a SPARQL query by the Python-based Cython Phaser. 

Fig. 4 visualizes one **query loop** for the capabilities of ‘Screwing’, ‘Positioning’ and ‘Transporting’. 
The SPARQL queries are forwarded to the JAVA-based HermiT Reasoner and the output is cached by checking the compatibility of capabilities and inferring implicit capabilities. 
At first, individuals, which provide the requested capability are identified (e.g. ‘ScrewDriver_1’ and ‘ScrewDriver_2’ for ‘Screwing’), then the HermiT Reasoner checks for combinable capabilities of the resources, e.g., if a capability is required, which could be provided by a specific robot in combination with a particular end-effector (here: ‘Screw-Driver_1’ and ‘MobileManipulator’ are combinable through ‘EndEffector Type 01’).
This function facilitates the combinatory capability inheritance requirement. 
If several resources match the capabilities, they are chosen in descending order, thus in the first query loop, the one with the closest matching parameter is selected (e.g. a pay-load of 20 kg is requested a gripper providing a payload of 25 kg would be preferred over one providing 40 kg), represented in Fig. 4 by a white square.
The loop continues until all possible combinations of resources are listed in descending order. 

Once the Cython Phaser processed all queries, the cached results are converted into CSV/TSV and forwarded to the **task allocation** step. 
(Depending on the interchangeable third-party system carrying out the task alloca-tion, this conversion could be adapted, providing compatibility to other programs.) 
During task allocation the best possible resource is selected. The ‘best’ is currently defined by the criteria 1) necessary equipment is already equipped on the robot 2) highest battery charge 3) first item of query list. 


During **post-processing** the list of allocated resources and task is converted to be OWL readable and the result are integrated and updated in CAPILANO. 

 



During **post-processing** and once all queries are processed by the Cython phaser, the cached results are converted into CSV/TSV and forwarded to the task allocation step. 
In dependence on the interchangeable third-party system carrying out the task allocation, this conversion could be adapted, providing compatibility to other programs. 
During **task allocation** the best possible resource is selected (currently through depending on the criteria of: Equipped end-effector, highest battery charge and first result, in case the first two do not lead to a decision) for each task within the process chart. 


Even though the query is passed through multiple programming environments, the SPARQL specific syntax and the keywords remains the same across these environments.

