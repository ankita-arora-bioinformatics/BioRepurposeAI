# DNA Analyzer

dna = input("Enter DNA sequence: ")

dna = dna.upper()

length = len(dna)

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

gc_content = ((g + c) / length) * 100

print("\n----- DNA Analysis -----")
print("Length:", length)
print("A Count:", a)
print("T Count:", t)
print("G Count:", g)
print("C Count:", c)
print("GC Content:", round(gc_content, 2), "%")
