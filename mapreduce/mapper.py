#!/usr/bin/env python
import sys


class Mapper:
    def __init__(self, separator="\t", source=sys.stdin):
        self.separator = separator
        self.input = source

    def map_task(self):
        for line in self.input:
            line = line.strip()
            connections = line.split()
            key, values = connections[0], tuple(connections[1:])
            print("{}{}{}".format(key, self.separator, self.separator.join(values)))

            if len(values) == 1:
                """
                Capture the bi-directional relationship of key - value pair in the first map task
                """
                print("{}{}{}".format(self.separator.join(values), self.separator, key))

            for value in values:
                """
                Capture the nth degree relationship between values related to the key
                """
                n_degree_connections = list(values)
                n_degree_connections.remove(value)
                if not n_degree_connections:
                    pass
                else:
                    print("{}{}{}".format(value, self.separator, self.separator.join(n_degree_connections)))


if __name__ == "__main__":
    mapper = Mapper()
    mapper.map_task()



