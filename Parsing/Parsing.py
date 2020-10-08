from itertools import islice
import os
import pandas as pd

#Extracting Proteins in a file
def ExtractingProteins(m):
    f = open('proteins.txt','w')
    infile = open(m, 'r')
    text = infile.readlines()
    for j in (text):
        print (j[0:6])
        f.write(j[0:6])
        f.write('\n')
    f.close()
ExtractingProteins("Bakers.txt")

#Reading Proteins in a list for Using in Sequnce Parsing from YEAST.fasta
lines = [line.rstrip('\n') for line in open('proteins.txt')]

#Parsing Sequences from YEAST.fasta
def ExtractingSequences(m):
    count=0
    pp=0
    ind=0
    f = open('sequences.txt','w')
    infile = open(m, 'r')
    text = infile.readlines()
    for j in (text):
        
        pp=pp+1
        if any(word in j[4:10] for word in lines):
            f.write(j[4:10])
            f.write(',')  
            count=count+1
            ind=pp
            for i in range(100):
                
                if (text[ind][0]==">"):
                    break
                else:
                    f.write(text[ind].rstrip('\n'))
                ind=ind+1
            f.write('\n')           
    f.close()
    print (count)
ExtractingSequences("YEAST.fasta")

#Replacing semicolons with comma    
with open('Bakers.txt', 'r+') as f:
    text = f.read()
    f.seek(0)
    f.truncate()
    f.write(text.replace(' ; ', ','))

#Renaming to a csv file    
os.rename('Bakers.txt', 'Bakers.csv')

m = lambda x: map(str.strip, x.split(','))

#Reading Bakers.csv into pandas Dataframe
with open('Bakers.csv') as f:
    df = pd.DataFrame(
        [[x, y] for x, *ys in map(m, f.readlines()) for y in ys if y],
        columns=['ProteinID', 'Class']
    )
    
#Renaming to a csv file    
os.rename('sequences.txt', 'sequences.csv')

#Reading sequences.csv into pandas Dataframe
with open('sequences.csv') as f:
    df2 = pd.DataFrame(
        [[x, y] for x, *ys in map(m, f.readlines()) for y in ys if y],
        columns=['ProteinID', 'Sequence']
    )

#merge both Dataframes into a single table    
df_new=pd.merge(df, df2, on='ProteinID')

columnsTitles=["ProteinID","Sequence","Class"]
df_new=df_new.reindex(columns=columnsTitles)


#Extracting top 20 frequenct classes (in our case its 21)
countt=df_new['Class'].value_counts()
#Choose all Classes above frequency of 54
df_neww=df_new.groupby('Class')['ProteinID','Sequence','Class'].filter(lambda x: len(x) > 54)
df_neww = df_neww.reset_index(drop=True)

#Saving all values to Dataset.csv
df_neww.to_csv("Dataset.csv", encoding='utf-8', index=False,header=False)

#Saving Class and Sequences into train.csv for usage in ANN
df_neww['Class'] = df_neww['Class'].str[3:]
df_neww.to_csv("train.csv", encoding='utf-8', index=False,columns=['Class','Sequence'],header=False)



