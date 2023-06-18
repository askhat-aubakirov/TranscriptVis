# DNA Toolkit file
# Askhat Aubakirov
# e-mail: askhat.aubakirov@yahoo.com
# January 26, 2021

# import collections
# later in code:  return dict(collections.Counter(anyGivenSeq))
from structures import * #imports everything from structures.py file

# Checking the sequence for being DNA only
def validateSeq(dnaSeq):
    tmpseq = dnaSeq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

#counting Nucleotides frequency in the sequence
def countNucFreq(seq):
    """ counts the frequency of Nucleotides present in the string of DNA sequence """
    tmpFreqDict = {"A": 0, "T": 0, "G": 0, "C": 0}
    for i in seq:
        tmpFreqDict[i] += 1
    return tmpFreqDict

def transcription(seq):
    """ DNA -> RNA (replaces Thymine with Uracil) """
    return seq.replace("T", "U")

def reverse_complement(seq):
    return "".join(DNA_reverse_complement[nuc] for nuc in seq) #[::-1]
