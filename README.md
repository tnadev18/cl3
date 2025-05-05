Computer Lab-III
 Oral questions
 
 1. What is RPC and how does it facilitate communication between distributed systems?
=> RPC (Remote Procedure Call) is a way for programs on different computers to talk to each 
other over a network. It works like a regular function call but it happens between processes 
running on different machines. It helps distributed systems communicate by allowing one 
program to call a function on another program running on a different machine.

 2. Explain the basic architecture of an RPC system.
 => In an RPC system, there are typically two main components: the client and the server. The 
client sends a request to the server, which executes the requested procedure and sends back 
the result to the client.

 3. How would you design the client-server interaction?
 => Client-server interaction involves the client sending a request to the server, which then 
processes the request and sends a response back to the client. This interaction follows a 
specific protocol, such as HTTP or TCP/IP, to ensure communication between the client and 
server.

 4. How would you handle scalability and load balancing in a distributed application?
 => Scalability and load balancing in distributed applications involve distributing incoming 
requests evenly across multiple servers to prevent any single server from becoming overloaded. 
Techniques like load balancers and clustering help manage increased traffic and maintain 
system performance.

 5. What are the advantages and disadvantages of using RPC compared to other 
communication protocols?
=> RPC offers simplicity and ease of use, but it may suffer from performance issues and tight 
coupling between client and server. Other protocols like REST or messaging systems offer more 
flexibility but might require more effort to set up and maintain.

 6. What is Socket Programming?
 => Socket programming is a way to enable communication between processes on different 
computers. It allows processes to send and receive data over a network using sockets, which 
are endpoints for communication.

 7. Explain the basic steps involved in establishing a socket connection between a client and 
a server in Python.
=> In Python, establishing a socket connection involves creating a socket object, specifying the 
server address and port, and then using methods like `connect()` to establish a connection and 
`send()` to send data.

 8. What is RMI and how does it differ from other remote communication mechanisms like 
RPC?
=> RMI (Remote Method Invocation) is a Java-specific technology that allows objects in one 
Java Virtual Machine (JVM) to invoke methods on objects in another JVM, making remote 
communication between Java programs easier.

 9. Describe the basic architecture of an RMI-based distributed application.
 => The architecture of an RMI-based distributed application involves clients invoking methods on 
remote objects located on servers. RMI handles the communication between the client and 
server transparently to the programmer. 

 10. What are the advantages and disadvantages of using RMI compared to other remote 
communication technologies?
=> RMI offers ease of use and integration with Java objects but may suffer from compatibility 
issues with non-Java systems. Other technologies like REST or messaging systems offer more 
interoperability but may require more effort to set up.

 11. What is stub, skeleton in RMI?
 => In RMI, stubs act as proxies for remote objects on the client side, while skeletons handle 
incoming requests on the server side.

 12. What is marshaling and unmarshaling?
 => Marshaling is the process of converting data into a format that can be transmitted over a 
network, while unmarshaling is the reverse process of converting received data back into its 
original format.

 13. What is Hadoop?
 => Hadoop is an open-source framework used for distributed storage and processing of large 
datasets across clusters of computers.

 14. Explain MapReduce.
 => MapReduce is a programming model and processing technique used for large-scale data 
processing. It divides data into smaller chunks, processes them in parallel across multiple 
nodes, and then aggregates the results.

 15. What is load balancing?
 =>  Load balancing is the process of distributing incoming network traffic across multiple servers 
to ensure no single server is overwhelmed. 

 16. Load balancing algorithms
 => Load balancing algorithms include round-robin, least connections, and weighted 
round-robin, among others.

 17. Load balancing approaches
 => Load balancing approaches include hardware-based, software-based, and DNS-based load 
balancing. 

 18. What is clonal selection algorithm?
 => The clonal selection algorithm is a computational optimization technique inspired by the 
immune system's ability to produce antibodies to combat pathogens.

 19. What is optimization? What are optimization algorithms?
 => Optimization involves finding the best solution to a problem given certain constraints. 
Optimization algorithms are techniques used to find this best solution.

 20. Explain the basic principles behind the Clonal Selection Algorithm.
 =>The Clonal Selection Algorithm works by iteratively improving a population of candidate 
solutions by mimicking the process of clonal selection and antibody production in the immune 
system.

 21. How does the neural network architecture facilitate the transformation of a given image 
into a stylized artwork?
=> Neural network architecture transforms images into stylized artwork by extracting features 
from the input image and synthesizing a new image based on the style reference.

 22. What are the key components involved in implementing Neural Style Transfer using deep 
learning techniques?
=> Key components of Neural Style Transfer include pre-trained convolutional neural networks 
(CNNs), feature extraction, and loss functions to match content and style.

 23. Describe the key principles behind artificial immune pattern recognition.
 => Artificial immune pattern recognition involves using algorithms inspired by the immune 
system to recognize patterns in data.

 24. How patterns in structural damage are recognized?
 => Patterns in structural damage are recognized through techniques such as anomaly detection 
and pattern matching using data collected from sensors or other sources.

 25. What is evolutionary computation?
 => Evolutionary computation is a family of optimization algorithms inspired by the process of 
natural selection and evolution.

 26. Distributed Evolutionary Algorithms
 => Distributed Evolutionary Algorithms extend evolutionary algorithms to work in distributed 
computing environments, enabling parallel processing and faster optimization.

 27. Explain Ant Colony Optimization (ACO)
 => Ant Colony Optimization (ACO) is a metaheuristic optimization algorithm inspired by the 
foraging behavior of ants to find optimal paths through graphs or networks.

 28. What is Traveling Salesman Problem (TSP)?
 =>  The Traveling Salesman Problem (TSP) is a classic problem in optimization theory that 
involves finding the shortest possible route that visits each city exactly once and returns to the 
origin city.

 29. How do ants mimic the behavior of real ants to find an optimal or near-optimal solution?
 => Ants mimic real ants' behavior by depositing pheromones on paths they explore, preferring 
paths with higher pheromone concentrations, and communicating with other ants through 
pheromone trails.

 30. What are key components of the ACO algorithm?
 => Key components of the ACO algorithm include pheromone updating rules, heuristic 
information, and ant movement strategies such as stochastic and deterministic methods. 
