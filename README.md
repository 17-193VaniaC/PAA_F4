# PAA_F4
DAA -F4 
Risky Aswi Narni (05111740000014) 
Zahrul Zizki Dinanto (05111740000168) 
Vania Cikanindi (05111740000193) 

## 1. Description 
We are lived in Indonesia. Indonesia is a big country and has many cities. When long holiday arrived, usually on national 
holidays or Eid, many families have day off from work. In general they have plans for family vacations. 
It is a tradition every year to refresh their mind.   
But, to know how exhausting the course to get to the destination, it’s good to take a break once in while in some places. 
So we made a program, to make easier and better for the family on their way. Using shortest path to the other city, 
their family can get around many cities during the holidays so they can take some rest in some city on their way to the destination.

## 2. Abstraction 
To find out the shortest path from city to another city, we must find out the location of the cities, which city that’s connected 
with each other and the distance between two city that connected by a path. 
After knowing the cities, path, and the distance between two cities, we can implement the ways to find the shortest path. 
Here we are using greedy algorithm to know which city to be pass the best to get at destination from a city. 
The greedy algorithm chooses the shortest city for each step from overall way but not really the shortest. 

## 3. Solution
As the start, the program will ask the name of the city in Java to become the start point. 
Then, the program will ask for the destination city in Java to become the end point.  
Showing the list of the cities: 
Every 4 cities will be printed on each line. In order to do that, there will be an array named citylist and an integer named count.
To show the cities, the array citylist require the list of the city, named cityname. Whenever the name of a city is appended to the
citylist, the counter variable will count will be increased. So, whenever the counter reaches a number that can be divided by three,
a new line will be added to citylist. Hence the citylist would contain a new line after 4 cities are appended. 
After all of the cities are inserted on the citylist, the program will show the list in the citylist and put a space on every 
element in citylist. 

## 4. How to use 
1)	run the program 
2)	enter your initial state 
3)	enter your goal state 
    the program will suggest cities that are located between city using algorithm greedy 

we have source code
1. daftarkota.py

2. greedy.py
  Description: 
    We need initial state , goal 
    We use Heap queue (or heapq) 
    -heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. 
                    The order is adjusted, so as heap structure is maintained. 
    -heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, 
                    so as heap structure is maintained. 

    Before that, to find the way we must mark visited city, mark source to reach a city, and has list named pq. First find the 
    neighbor from current city, if neighbor has been visited than continue next step. If neighbor hasn`t been visit than print 
    neighbor with its distance and heappush  to priorityque than  other neighbors, other neighbors from the current city also do
    the same command. Distance must save in a variable, and if there are distance which smaller than distance previous. 
    than update distance. Heapque has min heap than set as current city. the order will run until it meets the goal. 
    If current city same as goal than we must find the parent from current city until we meet initial state, the all parents must
    save in path than revers it. 

3. main.py
  Description:
    In Source code Above we set Kota variable to set list of city that we will explore,and set Jarak Variabel to set the distance
    of city to city  
    To print list of city list we use daftarkota() function  
    by using the greedy algorithm that focuses on how close the next city is, we would be able to get the path from a city to the
    destination that would take short trip every moving from a city to another. We use Greedy() Function 
    After we get the path we print the result of path 
