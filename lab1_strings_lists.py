
#Modifying sample DNA and exon coordinates
dna = 'atgcgatgcgatgcg'
#Example: exons = [(2,5), (10,12)]

#Entering any position
a = int(input('Enter start of first exon: '))
b = int(input('Enter end of first exon: '))
c = int(input('Enter start of second exon: '))
d = int(input('Enter end of second exon: '))
exons = [(a, b), (c, d)]

#Annotate DNA sequence with exon coordinates
annot = list(dna.lower())
for s,e in exons:    
  for i in range(s,e):        
    annot[i] = annot[i].upper()
print(''.join(annot))  #joins the letters together

#Count how many time each nucleotide [A,T,G,C] appears in the DNA string.
dna = 'gctagctagctagcta'
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}        
print(counts) 

#Reversing a DNA sequence and printing it
dna = 'gctagctagctagcta'
print(dna[::-1])
