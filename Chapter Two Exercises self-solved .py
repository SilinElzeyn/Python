# Chapter Two- Exercises:

# Exercise 1: Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
# Write a program that will print out the AT content of this DNA sequence.
# Hint: you can use normal mathematical symbols like add (+), subtract (-), multiply (*), divide (/) and parentheses to carry out calculations on numbers in Python.

Short_DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_count = Short_DNA.count("A") # ---> The output should be: 16
T_count = Short_DNA.count("T") # ---> The output should be: 21
AT_count = A_count + T_count # ---> The output should be: 37
Length_DNA = len(Short_DNA) # ---> The output should be: 54

AT_content = AT_count / Length_DNA
print (AT_content) # AT content = A + T / length  ---> The output should be: 0.6851851851851852 ... easy one ... on to the next one



# Exercise 2: Complementing DNA ... Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
# Write a program that will print the complement of this sequence.

short_DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

replacement_1 = short_DNA.replace("A", "t")
replacement_2 = replacement_1.replace("T", "a")
replacement_3 = replacement_2.replace("C", "g")
replacement_4 = replacement_3.replace("G", "c")
# I will be making it like from A to t not T as upper case because I have another goal which is to convert T to A, and if the first replacement converted A to T then I will be doing the return back to original when running the next replacement

# At the end, I will be converting all the letters into upper case with this

final_replacement = replacement_4.upper()

# now printing
print (Short_DNA)
print (replacement_1)
print (replacement_2)
print (replacement_3)
print (replacement_4)

print ("The original DNA is " + short_DNA)
print ("The complement DNA is " + final_replacement)



# Exercise 3: Restriction fragment lengths ... Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
# The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk).
# Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI.

new_DNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
original_length = len(new_DNA)

first_segment = (new_DNA[0:22])
second_segment = (new_DNA[22:55])

first_length = len(first_segment)
second_length = len(second_segment)

print (" The length of the original DNA segment is " + str(original_length))

print (" The first segment is " + str(first_segment))
print (" The length of the first segment is " + str(first_length))

print (" The second segment is " + str(second_segment))
print (" The length of the second segment is " + str(second_length))

# ok going back to the book's solution, it is much simpler, but for now I will be sticking to my answer, and as I practice along, I will learn the easy way to do it
# ok I just noticed, because my dna length is short, I was able to manually locate the exact location of the motif, but If I imagined it on a very long dna segment, it will be difficult to locat, especially if I am dealing with multiple segments

# Book's solution
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = my_dna.find("GAATTC") + 1
# ok let's break the answer: I want the program to find the exact position, GAATTC, by making find, I am locating the exact location where this segment starts, and since I want to include the final position which is G, I will be adding +1 to count the last position

frag2_length = len(my_dna) - frag1_length  # Measuring the remaining length which is the original dna length minus the half fragment generated
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))

# The book's solution solves this issue! :)


# Exercise 4: Splicing out introns
# Part one
# Here's a short section of genomic DNA:
# ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
# It comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence.
# Write a program that will print just the coding regions of the DNA sequence.

# Part two
# Using the data from part one, write a program that will calculate what percentage of the DNA sequence is coding.

# Part three
# Using the data from part one, write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.



# part one - answer:
long_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# figuring out the exact dna length
dna_length = len(long_dna)
print("length of the long dna is " + str(dna_length))

first_exon = long_dna[0:62]
second_exon = long_dna[90:124]
coding_region = first_exon + second_exon
the_intron = long_dna[62:90]

print("The intron is " + the_intron)
print ("The exon (the coding region) is " + coding_region)


# part two - answer:
dna_length = len(long_dna)
coding_region = first_exon + second_exon
coding_length = len(coding_region)
percentage = (coding_length/dna_length) * 100
print (percentage) # which is correct ---> 77.23577235772358


# part three - answer:
coding_region = first_exon + second_exon
the_intron = long_dna[62:90]
print (first_exon + the_intron.lower() + second_exon)


