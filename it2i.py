"""
############################################################
    i t 2 i                                                
############################################################

    Replace latex italics with html italics.

############################################################

    Example.
    Input:  \\textit{string}
    Output: <i>string</i>

    Note.
    Only works when no other curly braces 
    appear inside \\textit{}.
"""

#!/usr/bin/python
import sys
import re

try:
    sys.argv[2]
    sys.argv[1]
except:
    print __doc__ + "\n    Usage.\n    python it2i.py <input .tex file> <output .html file>"
    print "\n############################################################\n" 
    quit()

outfile = open(sys.argv[2], 'w')

# Compile regex to find italics in latex
regex = re.compile("\\\\textit{.*?}")

with open(str(sys.argv[1]), 'r') as file:
    for line in file:
        match = regex.search(line)

        if match:
            # Iterator is a sequence of instances
            # An instance is a matched string object with attribute 'span'
            # A span is a 2-tuple of the start/end positions of the matched string
            iterator = regex.finditer(line)

            # start_displace accounts for changes in each start_word caused by
            # replacing \textit{ with <i> and } with </i>
            # (a total difference of 2 characters, -5+3=-2)
            start_displace = 0
            for i in iterator:
                # i.span()[0] is the start position of each instance i
                start_word = i.span()[0] - start_displace

                line = line[ : start_word] + line[start_word : ].replace("}", "</i>", 1)
                line = line[ : start_word] + line[start_word : ].replace("\\textit{", "<i>", 1)
    
                start_displace += 2

        outfile.write(line)

outfile.close()
