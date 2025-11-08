
#6 Reading fasta file 
def read_fasta(file_path): 
    with open(file_path) as f: 
        lines = f.readlines() 
        header = lines[0].strip() 
        sequence = ''.join(line.strip() for line in lines[1:]) 
        return header, sequence 

header, dna_seq = read_fasta(r"c:\Users\kimas\Downloads\sequence.fasta") 
print(header) 
print(dna_seq[:100]) # print first 100 bases

#7 Writing base percentages
def base_percentages(seq): 
    seq = seq.upper()
    return {b: seq.count(b)/len(seq)*100 for b in 'ATGC'}

print(base_percentages('ATGCATGC'))
