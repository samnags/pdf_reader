import pdfplumber
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store
from langchain.docstore.document import Document

# def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100,
#     )
#     loader = PyPDFLoader(pdf_path)
    # docs = loader.load_and_split(text_splitter)

#     for doc in docs:        
#         doc.metadata = {
#             "page": doc.metadata["page"],
#             "text": doc.page_content,
#             "pdf_id": pdf_id,
#         }

#     vector_store.add_documents(docs) 

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    docs = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            doc = Document(page_content=page_text, metadata={'page_number': page.page_number, 'pdf_id': pdf_id})
            docs.append(doc)      
    documents = text_splitter.split_documents(docs)
    vector_store.add_documents(docs) 

    pass

    
