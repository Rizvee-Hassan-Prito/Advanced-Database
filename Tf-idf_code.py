# -*- coding: utf-8 -*-
"""
Created on Fri May 12 05:21:37 2023

@author: User
"""

docs=[]
with open('documents.txt', 'r') as file:
    for line in file:
        docs.append(line.replace(".\n", ""))
#%%
doc=[]
doc2=[[]]
for i in range (0,len(docs)):
  doc.append(list(set(docs[i].split(" "))))
  doc[i] = [word.replace(",", "").replace(".", "") for word in doc[i]]
  doc[i] = [x.lower() for x in doc[i]]
  doc2[0].extend(set(doc[i]))

doc2[0]=list(set(doc2[0]))

print("\nList of vocabulary:",(doc2[0]))
print()
#%%
tf=[]
for i in range (0,len(doc)):
  tf_each_doc=[]
  docmnt=docs[i].split(" ")
  docmnt = [word.replace(",", "").replace(".", "") for word in docmnt]
  docmnt=[x.lower() for x in docmnt]
  for j in range(0,len(doc[i])):
    tf_each_doc.append(docmnt.count(doc[i][j]))

  tf.append(tf_each_doc)

for i in range(0,len(tf)):
  print("Unique Words in document "+str(i+1)+":\n",doc[i])
  print("tf vector representations of document "+str(i+1)+":\n",tf[i])
  print()

#%%
import math

tf_idf=[]
idf=[]
N=len(doc)

for i in range(0,len(doc2[0])):
  c=0
  for j in range(0,len(doc)):
    if doc2[0][i] in doc[j]:
      c+=1
    #idf_each_doc.append[c]
  each_w_idf = math.log2(N/c)
  idf.append(each_w_idf)

print("idf:",idf)
print()
#%%
tf_idf=[]

for i in range(0,len(doc)):
  empty_tfidf=[0.0 for i in range(0,len(idf))]
  for j in range(0,len(doc[i])):
      index=doc2[0].index(doc[i][j])
      empty_tfidf[index] = tf[i][j] * idf[index]
  tf_idf.append(empty_tfidf)

print("Total unique words:\n",doc2[0])
print()
for i in range(0,len(tf_idf)):
  print("tf-idf vector representations of document "+str(i+1)+":\n",tf_idf[i])
  print()
