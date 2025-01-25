
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from tradingbot.constant import DATA_PATH

def load_file():
    loader = PyPDFLoader(DATA_PATH)
    pages = loader.load()

    raw_text = ''
    for i, doc in enumerate(pages):
        text = doc.page_content
        if text:
            raw_text += text
            
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap  = 100,
    )

    docs = text_splitter.split_text(raw_text)
    
    return docs
        
