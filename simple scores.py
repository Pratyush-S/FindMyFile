import glob

name=input("Enter file name")

files=glob.glob("*.txt")


files=[i[:-4] for i in files]

print(files)


k1_scores=[0]*len(files)   #name match
k2_scores=[0]*len(files)   #synonym match 
k3_scores=[0]*len(files)    #tag match

