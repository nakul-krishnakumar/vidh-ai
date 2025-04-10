from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
from io import BytesIO
import tempfile

def chunk_file_data(file_datas: list[BytesIO]) -> list[Document]:
   chunks: list[Document] = []

   # splits the characters into chunks
   splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

   try:
      for file_data in file_datas:
         # creating a tempfile to write the file_data, then delete it
         with tempfile.NamedTemporaryFile(delete=True, suffix=".pdf") as tmp_file:
            tmp_file.write(file_data.read())
            tmp_file.flush()

            loader = PyPDFLoader(tmp_file.name)  # loads the file_data
            documents = loader.load() # load PDFs into Document objects
            document_chunk = splitter.split_documents(documents)
            chunks.extend(document_chunk) # append chunking of multiple PDFs into a single list
      
      print(f"Successfully chunked the data into {len(chunks)} parts!")
      
   except Exception as e:
      print(f"Could not chunk the data, \nerror: {e}")

   return chunks
