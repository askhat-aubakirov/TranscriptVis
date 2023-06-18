# DNA Toolkit testing file
# Askhat Aubakirov
# e-mail: askhat.aub.work@gmail.com
# January 26, 2021

from DNAToolkit import * #imports everything from DNAToolkit.py file
import random
from utilities import *

#creates a random DNA sequence with length of {n, where n belongs to N}
r = input("give me the number of bp: ")
r = int(r)
randomDNAstr = "".join(random.choice(Nucleotides) for nuc in range(r))

DNAseq = validateSeq(randomDNAstr) #Checking if string is correct

print("----------------------------------------------------------")
print("The sequence is: ", colored(DNAseq))
print("The length of the sequence is", len(DNAseq))
# print("Nucleotides frequency is: ", countNucFreq(randomDNAstr), "\n")
print(colored(f"Nucleotides frequency is: {countNucFreq(randomDNAstr)} \n"))

print("5` ", colored(DNAseq), "  3`")
print("   ", "".join("|" for c in range(len(DNAseq))) )
print("3` ", colored(reverse_complement(DNAseq)), "  5` \n")
print("RNA (transcripted) to the initial DNA is: ", colored(transcription(randomDNAstr)), "\n")
print("----------------------------------------------------------")
