pweight = int(input("Enter the # of kiograms of the Package:"))
plength = int(input("Enter the length of the Package in centimeters:"))
pwidth  = int(input("Enter the width of the Package in centimeters:"))
pheight = int(input("Enter the height of the Package in centimeters:"))

if pweight > 27:
    print "Package is too heavy"
if plength > 100000:
    print "Package is too large"
if pwidth > 100000:
    print "Package is too large"
if pheight > 100000:
    print "Package is too large"

input()