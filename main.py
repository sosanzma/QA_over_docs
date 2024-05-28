
from chains.qa_chain import get_response

while True:
    question = input("Please enter your question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        break

    response = get_response(question)

    print("\nResponse:")
    print(response["answer"])
    print("\nSources:")
    for source in response["sources"].split(", "):
        print("- " + source)
    print("\n")

