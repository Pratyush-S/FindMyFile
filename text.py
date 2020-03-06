from matplotlib import pyplot as plt


############################################################
#Functions

def get_scrap():
    file = open("randcom.txt","r") 
    a=file.readlines()
    
    c=string_srom_file(a)
    
   
    e=set(c)
    file.close()
    return list(e)

def string_srom_file(file_buffer):
    
    string_buffer=[]
    for i in range(len(file_buffer)):
        buffer=file_buffer[i].lower()
        
        string_buffer=string_buffer+buffer.split()
    return string_buffer

#############################################################

scrap=get_scrap()


file = open("space.txt","r") 
raw_text=file.readlines()

text=''
for i in raw_text:
    print(i)
    text=text+i

text = text.translate ({ord(c): " " for c in "!@#$%^&*\"\'()[]{};:,./<>?\|`~-=_+"})

        
                        
words=string_srom_file(text)


words.sort()

filtered_words=[x for x in words if x not in scrap]

bins=set(filtered_words)

count=[0]*len(bins)


#file.close()
 


for i in filtered_words:
    if len(i)<4:
        print(i)
        
        



























