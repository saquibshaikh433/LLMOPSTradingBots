from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
import openai
from tradingbot.helper import load_file
from tradingbot.constant import OPENAI_API_KEY
from tradingbot.constant import EMBEDDED_MODEL
load_dotenv()

ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


embedding = OpenAIEmbeddings(model = EMBEDDED_MODEL, api_key = OPENAI_API_KEY )

def ingestdata(status):
    vstore = AstraDBVectorStore(
            embedding=embedding,
            collection_name=COLLECTION_NAME,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
    
    storage=status
    
    if storage==None:
        docs=load_file()
        inserted_ids = vstore.add_documents(docs)
        return vstore, inserted_ids
    else:
        return vstore
"""
if __name__=='__main__':
    status_check = "done"
    if status_check == "done":
        vstore=ingestdata(status_check)
    else: 
        vstore, insert_id =ingestdata(None)

    results = vstore.similarity_search("what is langchain ?")
    print(results)
"""          

