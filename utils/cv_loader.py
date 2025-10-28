from langchain_community.document_loaders import PyPDFLoader, UnstructuredImageLoader, UnstructuredHTMLLoader
from PIL import Image
import tempfile

def load_cv(file):
    if file.type == "application/pdf":
        loader = PyPDFLoader(file)
    elif file.type.startswith("image/"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name
        loader = UnstructuredImageLoader(tmp_path)
    elif file.type == "text/html":
        loader = UnstructuredHTMLLoader(file)
    else:
        raise ValueError("Formato de arquivo não suportado.")
    
    return loader.load()
