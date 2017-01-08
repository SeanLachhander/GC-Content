# Calculates GC Content

gene = open("sequence.txt", "r")

# Set the values to zero.

g = 0;
a = 0;
c = 0;
t = 0;

# Skip the first line of header

gene.readline()

for line in gene:
	line = line.lower()
	for char in line:
		if char == "g":
			g += 1
		if char == "a":
			a += 1
		if char == "c":
			c += 1
		if char == "t":
			t+=1
print "The number of g's: " + str(g)
print "The number of c's: " + str(c)
print "The number of a's: " + str(a)
print "The number of t's: " + str(t)

# 0. = Convert to floating point

gc = (g + c + 0.) / (a + t + c + g + 0.)
print "gc content: " + str(gc)