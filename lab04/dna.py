#Task 3

# set up a mapping from bases to their complements (a <-> t, g <-> c)
base_str = 'atgc'
comp_str = 'tacg'

# generate strands of dna
dna1 = 'atgcaattgcaattcgtagc'
dna2 = 'cagttgaccagttgaccagt'
dna3 = 'tagccgattgaccgattgac'
dna4 = 'gacttacggacttacggact'
dna5 = 'cgtaatgccgtaatgccgta'

# FUNCTION REVERSE  #

#REVERSE: reverses the strand of DNA given
#input: strand of dna
#output: reversed strand of dna

def reverse(dna):
    # store reverse as list to allow mutability, use dummy values initially
    reverse_list = ['0'] * len(dna)
    # now fill in dummy values by going through dna forwards and filling in
    # reverse_list backwards
    for i in range(1,len(dna)+1):
        reverse_list[-i] = dna[i-1]
        # now form list into string
        reverse_dna1 = ''.join(reverse_list)
        return dna[::-1]

print 'Reverse should be\t', reverse(dna1)
print 'Reverse should be\t', reverse(dna2)
print 'Reverse should be\t', reverse(dna3)
print 'Reverse should be\t', reverse(dna4)
print 'Reverse should be\t', reverse(dna5)

print '----------------'

# FUNCTION COMPLEMENT  #

#COMPLEMENT: prints the complementary strand of DNA given
#input: strand of dna
#output: complementary strand of dna

comp_dna = ''

def complement(dna):
    comp_dna = ''
    for char in dna:
        # find the index of char in base_str
        i = base_str.index(char)
        # now find the associated char in the mapped string comp_str
        comp_dna += comp_str[i]
    else:
        return comp_dna

print 'complement should be\t', 'tacgttaacgttaagcatcg'
print 'complement is\t\t\t', complement(dna1)

print 'complement should be\t', 'gtcaactggtcaactggtca'
print 'complement is\t\t\t', complement(dna2)

print 'complement should be\t', 'atcggctaactggctaactg'
print 'complement is\t\t\t', complement(dna3)

print 'complement should be\t', 'ctgaatgcctgaatgcctga'
print 'complement is\t\t\t', complement(dna4)

print 'complement should be\t', 'gcattacggcattacggcat'
print 'complement is\t\t\t', complement(dna5)

print '------------'


# FUNCTION REVERSE COMPLEMENT  #

#REVERSE_COMPLEMENT: reverses and complements the strand of DNA given
#input: strand of dna
#output: reversed complement strand of dna

def reverse_complement(original_dna):
    # store reverse as list to allow mutability, use dummy values initially
    reverse_list = ['0'] * len(original_dna)
    # now fill in dummy values by going through dna forwards and filling in
    # reverse_list backwards
    for i in range(1,len(original_dna)+1):
        char = original_dna[i-1]
        j = base_str.index(char)
        reverse_list[-i] = comp_str[j]
    reverse_complement = ''.join(reverse_list)
    return reverse_complement

print 'Reverse complement should be\t gctacgaattgcaattgcat'
print 'Reverse complement is\t\t\t', reverse_complement(dna1)

print 'Reverse complement should be\t actggtcaactggtcaactg'
print 'Reverse complement is\t\t\t', reverse_complement(dna2)

print 'Reverse complement should be\t gctaatcggctaatcggcta'
print 'Reverse complement is\t\t\t', reverse_complement(dna3)

print 'Reverse complement should be\t agtccgtaagtccgtaagtc'
print 'Reverse complement is\t\t\t', reverse_complement(dna4)

print 'Reverse complement should be\t tacggcattacggcattacg'
print 'Reverse complement is\t\t\t', reverse_complement(dna5)

print '------------'

#Task 4

#COMPLEMENT: creats a complementary strand of DNA
#input: dictionary of DNA bases
#output: complementary strand of DNA

def complement(s):
    my_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    letters = list(s)
    letters = [my_dictionary[base] for base in letters]
    return ''.join(letters)

#REVERSECOM: creats a reversed complementary strand of given DNA
#input: dictionary of DNA bases
#output: reversed complementary strand of DNA

def reversecom(s):
    complement(s[::-1])
    return complement(s[::-1])

print("ACGTTAGC")
print complement("ACGTTAGC")
print reversecom("ACGTTAGC")