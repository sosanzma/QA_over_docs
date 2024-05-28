from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import DeepLake
from config.config import ACTIVELOOP_ID
from data.scrape_articles import pages_content

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

my_activeloop_dataset_name = "qabot_with_source"
dataset_path = f"hub://{ACTIVELOOP_ID}/{my_activeloop_dataset_name}"

db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

all_texts, all_metadatas = [], []
for d in pages_content:
    chunks = text_splitter.split_text(d["text"])
    for chunk in chunks:
        all_texts.append(chunk)
        all_metadatas.append({"source": d["url"]})

db.add_texts(all_texts, all_metadatas)
