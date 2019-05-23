## Test:

Given a set **S** of pairs of usernames corresponding to mutual friendships in
a social network, write a program to output each user’s **i**-th degree friends,
for every positive **i** less than or equal to **N**, for a fixed **N**. A
successful solution can be scaled to very large **S**, using parallel and
distributed computing techniques.

Input:
------

Input is a text file, where each line contains a tab-separated pair of user
names:

```
davidbowie  omid
davidbowie  kim
kim         torsten
torsten      omid
brendan	    torsten
ziggy       davidbowie
mick        ziggy
```

The input file is not sorted. Each pair of usernames appears only once, in unspecified order, eg. the relationship between `mick` and `ziggy` might appear as `mick ziggy` **or** `ziggy mick`, but not both.


Output:
------

For **N** = 2, the output should look like:

```
brendan    kim        omid       torsten
davidbowie kim        mick       omid    torsten ziggy
kim        brendan    davidbowie omid    torsten ziggy
mick       davidbowie ziggy
omid       brendan    davidbowie kim     torsten ziggy
torsten    brendan    davidbowie kim     omid
ziggy      davidbowie kim        mick    omid
```

where each line begins with a username and is followed by all 1st and 2nd degree
friends of that user, separated by tabs and sorted lexicographically. The lines
are as well sorted by the first username on each line.

## How to test:

```
chmod +x ./mapreduce/mapper.py ./mapreduce/reducer.py
```

eg: for N == 1, single stage map-reduce
```
 cat mapreduce/stream.txt | ./mapreduce/mapper.py | sort -k1,1 | ./mapreduce/reducer.py 
 ```
eg: for N == 2, two stage map-reduce
````
 cat mapreduce/stream.txt | ./mapreduce/mapper.py | sort -k1,1 | ./mapreduce/reducer.py | ./mapreduce/mapper.py | sort -k1,1 | ./mapreduce/reducer.py 
```