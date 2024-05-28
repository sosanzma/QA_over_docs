# QA Bot with Source Verification

This project implements a Question-Answer (QA) system that extracts information from a set of articles and verifies the sources of the answers. It uses various technologies including `requests` for web scraping, `newspaper3k` for article parsing, and `langchain` for creating and running the QA model with source verification.

## Project Structure

```plaintext
.
├── config/
│   └── config.py
├── data/
│   ├── article_urls.py
│   └── scrape_articles.py
├── embeddings/
│   └── embeddings.py
├── chains/
│   └── qa_chain.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/qa_project.git
    cd qa_project
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

1. Add your article URLs to `data/article_urls.py`.

2. Run the `main.py` script to start the QA system:
    ```bash
    python main.py
    ```

3. You will be prompted to enter your questions in real-time. Type your question and press Enter to get the response. Type `exit` to quit the program.
