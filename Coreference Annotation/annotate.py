import csv
import re
import nltk

#fucntion to add all the numbers and stuff
def unique_worder(ori_text):
    split_ori=nltk.word_tokenize(ori_text)
    for i in range(len(split_ori)):
        curr_word_count=1
        if(re.search("\[|\]|[0-9]+|_",split_ori[i])==None and re.search("[a-zA-Z]", split_ori[i])!=None):
            temp_word=split_ori[i]
            for j in range(i,len(split_ori)):
                if(temp_word==split_ori[j] and i!=j):
                    curr_word_count=curr_word_count+1
                    split_ori[j]="[" + split_ori[j]+"]_"+str(curr_word_count)
            if(curr_word_count!=1 and re.search("\[|\]|[0-9]+|_",split_ori[i])==None and re.search("[a-zA-Z]", split_ori[i])!=None ):
                split_ori[i]="[" + split_ori[i]+"]_1"
            "[a-zA-Z]"
    outputter=""
    for wordd in split_ori:
        outputter=outputter+wordd.strip() + " "
    return outputter


#loading previous progress
previousindexhandle=open("currentindex.txt","r",encoding="utf8")
previousindex=previousindexhandle.read()
if(previousindex!=''):
    print("Previous progress loaded, currently at index:",int(previousindex))
    previousindex=int(previousindex)+1
else:
    print("Previous progress not loaded.")
    previousindex=0
previousindexhandle.close()




#making an array from the input
all_texts=[]
gapdata=open("gapdev_edit.tsv","r",encoding="utf8")
for row in csv.reader(gapdata, delimiter='\t', lineterminator='\n'):
    if(row[0]!='Original Text'):
        all_texts.append(row[0])
gapdata.close()


#opening the output file
tsvfile= open('annotate.tsv', 'a', newline='')
writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
#writer.writerow(["Original Text","Unique-ified Text", "User annotations"])



for current_id_index in range(previousindex,100): #replace 50 with len(all_texts) to do the rest of the texts (there are 241)
    full_annotation=[]
    annotation_state=True
    mod_word_list=nltk.word_tokenize(unique_worder(all_texts[current_id_index]))
    current_unique=unique_worder(all_texts[current_id_index])
    while(annotation_state):
        print()
        print()
        print(current_unique)
        print('TYPE ? to see the original text:')
        print('TYPE THE COREF CHAIN. Type ! to move onto the next text. (CTRL+C to exit):')
        anno_line = input()
        if(anno_line=='!'): #this is the only way you can stop annotating a line?
            anno_line=True
            writer.writerow([all_texts[current_id_index],current_unique, full_annotation])
            #updating current progress 
            currentindex=open("currentindex.txt","r+",encoding="utf8")
            currentindex.write(str(current_id_index))
            currentindex.close()
            break
        elif(anno_line=="?"):
            print()
            print(all_texts[current_id_index])
        else:
            previous_index=-1
            anno_test=True
            if(re.search(",",anno_line)!=None):
                for annotation_word in anno_line.split(','):
                    if(annotation_word not in unique_worder(all_texts[current_id_index])):
                        print("Rejected. " + annotation_word + "is not in the list!")
                        anno_test=False
                        break
                    elif(annotation_word==" "):
                        print("Rejected. A single whitesplace is not a viable option.")
                        anno_test=False
                        break
                    else:
                        if(unique_worder(all_texts[current_id_index]).index(annotation_word)>previous_index):
                            previous_index=unique_worder(all_texts[current_id_index]).index(annotation_word)
                        else:
                            print("Rejected. Put your words in the right order.")
                            anno_test=False
                            break
                if(anno_test==True):
                    full_annotation.append(anno_line)
            else:
                print("Rejected. You need to use commas to seperate the words and have at least two words in a chain.")
tsvfile.close()


