import os
import glob
from typing import List
from multiprocessing import Pool
from tqdm import tqdm
from constants import CHROMA_SETTINGS
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
#from langchain.document_loaders import DirectoryLoader, PDFMinerLoader


from langchain.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PyMuPDFLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
    DirectoryLoader,
    PDFMinerLoader,
    PyPDFLoader

    
)

EMBEDDINGS_MODEL_NAME = 'all-MiniLM-L6-v2'
persist_directory = 'db'
# Load environment variables
#persist_directory = os.environ.get('persist_directory')
#source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
#embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME')
chunk_size = 500
chunk_overlap = 50

# Map file extensions to document loaders and their arguments



def main():
    for root,files in os.walk("souce_documents"):
         for file in files:
             if file.endswith(".pdf"):
                 print(file)
                 #pdf_path= os.path.join(root, file)
                 loader = PDFMinerLoader(os.path.join(root, file))
                # splitter= RecursiveCharacterTextSplitter()
                 #vectorstore= Chroma(CHROMA_SETTINGS)
    documents=loader. load()
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=500)
    text=text_splitter.split_documents(documents)
    embeddings= SentenceTransformerEmbeddings(EMBEDDINGS_MODEL_NAME)
    db= Chroma. fromdocuments(text,embeddings,persist_directory=persist_directory)
    client_settings= CHROMA_SETTINGS
    db.persist()
    db=None
   
if __name__ == "__main__":
    main()







