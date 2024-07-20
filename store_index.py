from src.helper import load_pdf , text_split ,down_embedding
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')

extracted_data=load_pdf("data/")
text_chunks=text_split(extracted_data)
embedding=down_embedding()
pc = Pinecone()
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("medical-chatbot")
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embedding=embedding, index_name="medical-chatbot")


