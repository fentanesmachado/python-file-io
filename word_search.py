#! /usr/bin/env python3

# A script to find regular expressions within a txt file
import re

if __name__ == "__main__":
    herit_pattern_str = r"^\w*herit\w*$"
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)

print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening herit_in_origin.txt')
    with open('herit_in_origin.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream):
            line = line.strip()
            word_list = line.split()
            for word in word_list:
                if herit_pattern.search(word):
                    out_stream.write(f'{line_index + 1}\t{word}\n')

print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('herit_in_origin.txt is closed?', out_stream.closed)