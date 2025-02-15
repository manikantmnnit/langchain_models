#%%
from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2')

result=embedding.embed_query("The capital of India is New Delhi")

print(result)
#%%

docs=['A democratic system allows citizens to elect their leaders through free and fair elections.',
'In a democracy, every individual has the right to express their opinions and participate in decision-making.',
'A strong democratic system ensures equality, justice, and freedom for all citizens.',
'Many countries follow a democratic system where power is distributed among different branches of government.',
'A well-functioning democracy requires transparency, accountability, and active participation from the people.']

result=embedding.embed_documents(docs)
print(result)
#%%
dic = {"documents": [], "docs_embedding": []}

for index, single in enumerate(result):
    dic["documents"].append(docs[index])
    dic["docs_embedding"].append(single)
   
# %%
import pandas as pd
pd.DataFrame(dic)
# %%
