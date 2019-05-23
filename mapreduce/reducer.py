#!/usr/bin/env python
import sys


class Reducer:
    def __init__(self, separator="\t", source=sys.stdin):
        self.separator = separator
        self.input = source
        self.aggregate_network = set()
        self.key = None
        self.connection_tuple = (self.key, None)

    def reduce_task(self):
        """
        Simply read a key - value pair as (k , set(values)) and union + sort the set(values) grouped by key
        """

        for line in self.input:
            connections = line.split()
            self.connection_tuple = (connections[0], set(connections[1:]))

            if self.key == self.connection_tuple[0]:
                self.aggregate_network = self.aggregate_network.union(self.connection_tuple[1])
            else:
                if self.key:
                    print("{}{}{}".format(self.key, self.separator, self.separator.join(sorted(self.aggregate_network))))
                self.aggregate_network = self.connection_tuple[1]
                self.key = self.connection_tuple[0]

        if self.key == self.connection_tuple[0]:
            print("{}{}{}".format(self.key, self.separator, self.separator.join(sorted(self.aggregate_network))))


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce_task()
