# OP_CodingChallenge
OP coding assessment


### How does my code work?
My code works by using a backing dictionary, list, and set. 
The dictionary maps ips to the number of times they've been seen. 
The list is used as a heap and keeps track of the top 100 ip addresses, stored in tuples in the format (count, address). It is a min heap so the smallest value can be removed quickly. 
The set is used as a way to keep track of what addresses are already inside the heap, to avoid many repeated lookups on the list. 


### Runtime Complexity
clear is constant, as it's just dropping each data structure.

top100 is constant, as it's 100 repeated pops of the heap which are O(1) and a copy operation of the existing heap (O(N) with respect to the size of the list, which is fixed at 100). 

requestHandled is constant too, as it's an update to a hashmap value (O(1)),  a removal and a heapify on the list (both operations are O(N) but the list is max size 100), and a push to the heap (O(logN) on max size 100). This is followed by a pop from the heap and a removal of a set item, both O(1) operations.

### Alternative approaches
I initially wanted to heavily optimize the insertion of new ips into the top 100, but I realized that because the top 100 only has 100 entries, it's fine to have less optimized code as it will still run relatively quickly. 
It could be more heavily optimized with some binary tree swaps instead of removing existing entries and re-heapifying the top 100 array every time, which should make it run in O(logN) instead of O(N), but it was a lot easier to understand and implement the function calls to remove and heapify. 



### Testing?
I tested this in the main method very rudimentarily, but if it were part of an actual automated web service I would use automated testing libraries and unit tests to ensure the runtime complexity and functionality was correct.