matMarks = int(input("Enter Math Mark"))
phyMarks = int(input("Enter Physics Mark"))
cheMarks = int(input("Enter Chemistry Mark"))

if (matMarks < 35):
    print("Failed in Math: ", matMarks)
elif (phyMarks < 35):
    print("Failed in Physics: ", phyMarks)
elif (cheMarks < 35):
    print("Failed in Chemistry: ", cheMarks)
else:
    avgMarks = (matMarks + phyMarks + cheMarks) / 3
    if (avgMarks <= 59):
        print("Grade C, Avg: ", avgMarks)
    elif (avgMarks <= 69):
        print("Grade B, Avg: ", avgMarks)
    else:
        print("Grade A, Avg: ", avgMarks)
