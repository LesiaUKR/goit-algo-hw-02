# goit-algo-hw-02
# MODULE 2 | Basic Data Structures

## Task 1
You need to develop a program that simulates the reception and processing of requests: the program should automatically generate new requests (identified by a unique number or other data), add them to a queue, and then sequentially remove them from the queue for "processing," thus mimicking the operation of a service center.

Here is the pseudocode for the task using a queue (Queue from the queue module in Python) for the request processing system:

```
import queue

# Create the request queue
request_queue = queue.Queue()

# Function to generate a new request
def generate_request():
    # Create a new request
    new_request = ...
    # Add the request to the queue
    request_queue.put(new_request)

# Function to process a request
def process_request():
    if not request_queue.empty():
        # Remove a request from the queue
        request = request_queue.get()
        # Process the request
        ...
    else:
        print("The queue is empty")

# Main program loop
while user_does_not_exit:
    generate_request()  # Generate new requests
    process_request()   # Process requests
```
In this pseudocode, two main functions are used: generate_request(), which generates new requests and adds them to the queue, and process_request(), which processes requests by removing them from the queue. The main program loop runs these functions, simulating a continuous flow of new requests and their processing.

## Task 2
You need to develop a function that takes a string as an input parameter, adds all its characters to a deque (deque from the collections module in Python), and then compares the characters from both ends of the deque to determine if the string is a palindrome. The program should correctly handle strings with both even and odd numbers of characters, and be case-insensitive and ignore spaces.

## Task 3 (Optional)
In many programming languages, we deal with expressions delineated by separator characters such as round ( ), square [ ], or curly braces { }.

Write a program that reads a string with a sequence of separator characters, such as ( ) { [ ] ( ) ( ) { } } }, and provides an appropriate message when the separators are symmetrical, asymmetrical, such as ( ( ( ), or when separators of different kinds are paired, such as ( }.

💡 Use a stack to keep track of currently open separator characters.

Example of Expected Results:
( ){[ 1 ]( 1 + 3 )( ){ }}: Symmetrical
( 23 ( 2 - 3);: Asymmetrical
( 11 }: Asymmetrical