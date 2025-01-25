
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from tradingbot.data_ingestion import ingestdata
from tradingbot.constant import  CHAT_MODEL
from tradingbot.constant import OPENAI_API_KEY



def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    LANGCHAIN_TEMPLATE = """
    Your gen ai and langchain bot is an expert in deep leanring and gen ai, langchain, etc.
    Ensure your answers are relevant to the query context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """


    prompt = ChatPromptTemplate.from_template(LANGCHAIN_TEMPLATE)

    llm = ChatOpenAI(model = CHAT_MODEL, api_key = OPENAI_API_KEY)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
"""
if __name__=='__main__':
    vstore = ingestdata("done")
    chain  = generation(vstore)
    print(chain.invoke("what is langchain, how its different from lamaindex?"))
    
"""
    
    
