# Chapter Three Exercises:

# Exercise 1: Splitting genomic DNA
# Look in the chapter_3 folder for a file called genomic_dna.txt – it contains the same piece of genomic DNA that we were using in the final exercise from chapter 2.
# Write a program that will split the genomic DNA into coding and non-coding parts, and write these sequences to two separate files.

# Here's a short section of genomic DNA:
# ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
# It comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence.


file = open("genomic_dna.txt")
file_contents = file.read()
print(file_contents)

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
first_exon = my_dna[0:62]
second_exon = my_dna[90:124]
coding_region = first_exon + second_exon
the_intron = my_dna[62:90]

print(coding_region)
print(the_intron)


new_file1 = open(r"Coding.txt", "w")
new_file1.write("Coding region is " + coding_region)
new_file1.close()

new_file2 = open(r"Noncoding.txt", "w")
new_file2.write("Noncoding region is " + the_intron)
new_file2.close()



# Exercise 2: Two-Part Question
# Example:
# FASTA file format is a commonly-used DNA and protein sequence file format. A single sequence in FASTA format looks like this:
# >sequence_name
# ATCGACTGATCGATCGTACGAT
# Where sequence_name is a header that describes the sequence (the greater-than symbol indicates the start of the header line). Often, the header contains an accession number that relates to the record for the sequence in a public sequence database.
# A single FASTA file can contain multiple sequences, like this:
# >sequence_one
# ATCGATCGATCGATCGAT
# >sequence_two
# ACTAGCTAGCTAGCATCG
# >sequence_three
# ACTGCATCGATCGTACCT


# Part One: Writing a FASTA file
# Write a program that will create a FASTA file for the following three sequences – make sure that all sequences are in upper case and only contain the bases A, T, G and C.
# ABC123 ---> ATCGTACGATCGATCGATCGCTAGACGTATCG
# DEF456 ---> actgatcgacgatcgatcgatcacgact
# HIJ789 ---> ACTGAC-ACTGT--ACTGTA----CATGTG


first_sequence_name = "ABC123"
sequence_one = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
print(">" + first_sequence_name + sequence_one)


second_sequence_name = "DEF456"
sequence_two = "actgatcgacgatcgatcgatcacgact"
sequence_two_upper = sequence_two.upper()
print(">" + second_sequence_name + sequence_two_upper)


third_sequence_name = "HIJ789"
sequence_three = "ACTGAC-ACTGT--ACTGTA----CATGTG"
sequence_three_corrected = sequence_three.replace("-", "")
print(">" + third_sequence_name + sequence_three_corrected)



fasta_file = open(r"Single_FASTA_file.txt", "w")
fasta_file.write(">" + first_sequence_name + '\n' + sequence_one + '\n' + ">" + second_sequence_name + '\n' + sequence_two_upper + '\n' + ">" + third_sequence_name + '\n' + sequence_three_corrected)
fasta_file.close()

# ok this is what I did ... let me check the book's
# oh ok I forgot to add '\n' in the print let me correct
print(">" + first_sequence_name + '\n' + sequence_one)
print(">" + second_sequence_name + '\n' + sequence_two_upper)
print(">" + third_sequence_name + '\n' + sequence_three_corrected)

# ok MUCH BETTER



# Part Two: Writing multiple FASTA files
# Use the data from the previous exercise, but instead of creating a single FASTA file,create three new FASTA files – one per sequence. The names of the FASTA files should be the same as the sequence header names, with the extension .fasta
# .fasta


ABC123 = open(r"ABC123.fasta","w")
ABC123.write(">" + first_sequence_name +'\n'+ sequence_one)
ABC123.close()

DEF456 = open(r"DEF456.fasta","w")
DEF456.write(">" + second_sequence_name +'\n'+ sequence_two_upper)
DEF456.close()

HIJ789 = open(r"HIJ789.fasta","w")
HIJ789.write(">" + third_sequence_name +'\n'+ sequence_three_corrected)
HIJ789.close()

