#! /usr/bin/env python3

import argparse

def parse():
    parser = argparse.ArgumentParser(description = "examine any 2 files")

    #add positional arguement
    parser.add_argument("data1", help = "the gff file")
    parser.add_argument("data2", help = "the fsa file")

    #command line arguements
    args = parser.parse_args()

    #data = open(args.data1)
    #dataf = open (args.data2).readlines()

    return args




def Bioparse():
    # bio python to parse fsa file

    from Bio import SeqIO

    genome1 =SeqIO.read(args.data2, 'fasta')

    #directory of different functions
    print(dir(genome1))

    #fasta header line
    print(genome1.description)

    #print the length of the sequence
    print(len(genome1.seq))
    #print the sequence itself
    print(genome1.seq)

    #print the complement
    print(reverse_complement(genome1))



def csvparse():
    #csv to parse gff file

    import csv

    #the variable 'genome' holds the genome sequence

    genome = []


    #open data file

    with open(args.data1, 'r') as gff_file:

    #create a csv reader object
    #have to give the reader what the delimiter is, i.e. comma

        csvr = csv.reader(gff_file, delimiter='\t')

        for line in csvr:

#conditional formatting to skip empty lines

            if not line:
                continue
            else:
                start = int([3])
            stop = int([4])



        substring = sequence[start:stop]
        genome = genome + substring
        print(genome)
            #print GC content

        G = str(genome).count('G')
        C = str(genome).count('C')
        total = len(str(genome))
        GC_total = G+C
        GC_content = GC_total/total
        print(GC_content)

    return genome

def main():
   Bioparse()
   csvparse()

args = parse()

if __name__ == "__main__":
	main()
#write the code for extracting the substring
#caculate the GC content for this feature, and print it to the screen
#save it, track it with GIT, push it to GIThub. We will continue to modify and upload to GITHUB


