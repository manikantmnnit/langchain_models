#%%
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs=['A democratic system allows citizens to elect their leaders through free and fair elections.',
'In a democracy, every individual has the right to express their opinions and participate in decision-making.',
'A strong democratic system ensures equality, justice, and freedom for all citizens.',
'Many countries follow a democratic system where power is distributed among different branches of government.',
'A well-functioning democracy requires transparency, accountability, and active participation from the people.']

embedding=OpenAIEmbeddings(model='text-embedding-3-small',dimensions=30)
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
