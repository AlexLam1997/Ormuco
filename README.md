# Alexander_Lam_test - Ormuco 2019

Hey there! This is my attempt at solving Ormocu's interview coding challenge. Below you will find the problem descriptions along with any notes I may have added to describe my design. 

# Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
 
# Question B
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
 
 
# Question C
At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
 
1.	Simplicity. Integration needs to be dead simple.
2.	 Resilient to network failures or crashes.
3.	 Near real time replication of data across Geolocation. Writes need to be in l time.
4.	 Data consistency across regions
5.	 Locality of reference, data should almost always be available from the closest region
6.	 Flexible Schema
7.	 Cache can expire 

## Notes: 
For this question, I wanted to try experimenting with consistent caching using a consistent hash circle that I discovered by reading Tom White's article on consistent hashing  (http://www.tom-e-white.com/2007/11/consistent-hashing.html) which I implemented as best I could. 
The benefit of this caching approach is that it distributes the load across the multiple caches added to the hash circle. Another inherit benefit to this approach is the consistent mapping of a data element to a particular cache machine despite possible cache failures in the network. The consistent hash circle also allows for addition and removal of caches from the network by adding or removing nodes, which I discuss below. 
In consistent hashing both the caches and the objects to be cached are hashed and mapped to a circle such that the values wrap around. There will then be objects points and cache points mapped to the hash circle. To determine in which cache an object belongs we move clockwise along the circle until we hit a cache point. The first cache point hit is the cache in which the object belongs. When a cache, or a node, is added to the circle, many replicas of that node are also added along the circle in order to achieve a more uniform distribution of objects among the caches.
My implementation of the consistent hash implements a dictionary interface to be used to easily add and access nodes to/from the circle.  
## Missing features: 
Despite my best efforts I was not able to make sure that data was always accessed from the closest region. I believe it would be possible by somehow adding the location of the node (cache) to the hashing function but since I am relatively new at python I was not able to figure it out. I also was not sure how to make cache entries expire without creating a new service that would periodically scan through cache elements and delete stale entries (which I think is beyond the scope of the test). 
However, my cache implementation is very resistance to failure and crashes and, through the dictionary interface, is also fairly simple to integrate. I also managed to deliver quality, scalable, and testable code throughout the test and I am more than willing to learn how to get around the problems that I was unable to solve. Hope to hear from you soon!
