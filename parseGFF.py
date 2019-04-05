
#watermelon.fsa
#watermelon.gff

import argparse

parser = argparse.ArgumentParser(description = "examine any 2 files")

#add positional arguement
parser.add_argument("--data1", help = "the gff file", default = 'watermelon.gff')
parser.add_argument("--data2", help = "the fsa file", default = 'watermelon.fsa')

#command line arguements
args = parser.parse_args()

data = open(args.data1)
dataf = open (args.data2).readlines()

#the variable 'genome' holds the genome sequence
genome = []

#read gff line by line
for line in data:
    #skip blank lines

    #remove line breaks
    line = line.rstrip("\n")
    #print(num)
    #split each line on the tab character
    
    # sequence, source, feature, begin, end, length, strand, phase,  att = line.split("\.t")
    fields = line.split("\t")
    start = int(fields[3])
    stop = int(fields [4])
     
    #extrct the dna sequence from the genome for this feature
    substring = dataf[start:stop]
    genome = genome + substring
    #print the dna_sequence for this feature
    #print(genome)
#write the code for extracting the substring
    
    
#caculate the GC content for this feature, and print it to the screen
    G = str(genome).count('G')
    C = str(genome).count('C')
    total = len(str(genome))
    GCtotal = G+C
    GCcon = GCtotal/total
    print(GCcon)    
    
#save it, track it with GIT, push it to GIThub. We will continue to modify and upload to GITHUB

