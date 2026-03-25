#! /usr/bin/env python3

import re

if __name__ == "__main__":
    herit_pattern_str = r"\w*herit\w*"
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)

    print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening herit_in_origin.txt')
    with open('herit_in_origin.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream):
            line = line.strip()
            word_list = line.split()
            word_list.sort()
            for word in word_list:
                out_stream.write(f'{line_index + 1}\t{word}\n')
print("Done!")
print('dummy.txt is closed?', in_stream.closed)
print('output.txt is closed?', out_stream.closed)