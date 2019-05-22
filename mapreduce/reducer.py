#!/usr/bin/env python
import sys


aggregate_network = set()
separator = "\t"
key = None
connection_tuple = (key, None)
for line in sys.stdin:
    connections = line.split()
    connection_tuple = (connections[0], set(connections[1:]))

    if key == connection_tuple[0]:
        aggregate_network = aggregate_network.union(connection_tuple[1])
    else:
        if key:
            print("{}{}{}".format(key, separator, separator.join(sorted(aggregate_network))))
        aggregate_network = connection_tuple[1]
        key = connection_tuple[0]

if key == connection_tuple[0]:
    print("{}{}{}".format(key, separator, separator.join(sorted(aggregate_network))))