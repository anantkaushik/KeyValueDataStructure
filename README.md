# KeyValueDataStructure (Integer Key only)

## **Instructions to run the program**

Clone this repo and run the following commands:

To run unit tests:

`make test`

To run the program:

`make run`

## Assumptions:
1. Key will always be integers.
2. Value will always be converted into string by the program.

## Design

### User Interface

There are 4 Options:
1. `Insert` - It will insert the key and value in the hash map, in case key already exists it'll override the value of that key.
2. `Retrieve` - It will retrieve the value of the key if exists otherwise it'll print **None**.
3. `Display` - It will display all the values and keys present in the hashmap.
4. `Exit` - It will terminate the program.

### Methodology
1. For the hash method, I used the **multiplicative hashing method**.
2. For the storage size, by default I used 19997, we can increase it if we're expecting too many elements.
3. To handle collision, I used the concept of chaining i.e. storing more than one element at one index and chain them using Linked List.

### Time Complexity:
1. `Insert` - In general cases, it'll be O(1) but in case of collision it can be O(k), where k will be the maximum number of collisions at one index. 
2. `Retrieve` - In general cases, it'll be O(1) but in case of collision it can be O(k), where k will be the maximum number of collisions at one index.
3. `Display` - It'll be O(N), where N will be the number of keys present in our data structure.

## Improvements:

1. Increase storage size - By default I kept the size 19997. If we're expecting more data, we can increase it accordingly.
2. Instead of using LinkedList, we can use list and store keys in sorted order and use binary search to get element. It will decrease the time complexity of retrieving the key value in case of collision but increase the complexity of insert. 