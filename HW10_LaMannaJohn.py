def read_word_list():
    davidC =open('ENGLISH_LIT.txt')
    print ("OPEN")
    s=davidC.read()
    print ("DONE")
    return s.split() 
 


def build_dictionary(word_list):
    davidDict={}
    for word in word_list:
        if word not in davidDict:
            davidDict[word]=1
        else:
            davidDict[word]+=1
    return davidDict 


word_list = read_word_list()
print("FILE READ.")


dictionary = build_dictionary(word_list)
print ("DICTIONARY CREATED.")
L= []

num= int(input("Enter freq:"))

for key in dictionary:
    if dictionary[key] > num:
        L.append((dictionary[key], key))

print (sorted(L))
        
