#!/usr/bin/env python
import sys

for line in sys.stdin:
    separator = "\t"
    line = line.strip(separator)
    connections = line.split()
    key, values = connections[0], list(connections[1:])
    print("{}{}{}".format(key, separator, separator.join(values)))
    if len(values) == 1:
        print("{}{}{}".format(separator.join(values), separator, key))

    for value in values:
        values.remove(value)
        if not values:
            pass
        else:
            print("{}{}{}".format(value, separator, separator.join(values)))


