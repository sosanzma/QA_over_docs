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
    - You can modify the URLs in `data/article_urls.py` to scrape information from different sources for the QA system.


2. Run the `main.py` script to start the QA system:
    ```bash
    python main.py
    ```

3. You will be prompted to enter your questions in real-time. Type your question and press Enter to get the response. Type `exit` to quit the program.



### Example Output

```plaintext
Please enter your question (or type 'exit' to quit): ¿Qué hace que gastar en experiencias sea mejor que gastar en cosas?

Response:
Una razón es que nos adaptamos más rápido a los bienes materiales. Además, las experiencias suelen disfrutarse en compañía de amigos y generan felicidad en tres tiempos: antes, durante y después.

Sources:
- https://joantubau.substack.com/p/la-gente-feliz-no-consume

Please enter your question (or type 'exit' to quit): ¿En qué consta el modelo mental del coste de oportunidad?

Response:
El modelo mental del coste de oportunidad consta de la utilidad marginal decreciente y el coste de oportunidad.

Sources:
- https://joantubau.substack.com/p/compra-el-dinero-la-felicidad
- https://joantubau.substack.com/p/dacia-sandero

Please enter your question (or type 'exit' to quit): ¿Cómo funciona un motor a combustión?

Response:
No se menciona cómo funciona un motor a combustión.

Sources:
-