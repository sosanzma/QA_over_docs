# chains/qa_chain.py
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
from embeddings.embeddings import db

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)

chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm,
                                                    chain_type="stuff",
                                                    retriever=db.as_retriever())

def get_response(question):
    response = chain({"question": question})
    return response
