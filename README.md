# Question Answering System

## Prerequisites

- Python 3.6 or higher
- Elasticsearch
- Streamlit
- Hugging Face Transformers
- Docker (optional, for containerization)
- OpenAI API key

## Installation

1. **Clone the Repository**:

    ```
    git clone https://github.com/johnabednego/question-answering-system.git
    cd question-answering-system
    ```

2. **Install Required Packages**:

    ```
    pip install -r requirements.txt
    ```

## Code Update

1. **Update gen_ai.py**
    ### Set up your OpenAI API key
    openai.api_key = 'YOUR_OPENAI_API_KEY'

## Usage

1. **Run the Elasticsearch Server**:

    Ensure Elasticsearch is running locally on port 9200.

2. **Run the the Flask  Server**:

    CD into the app/ folder and run the command below
    ```
    python app.py  
    ``` 
    #### or
    ```
    python3 app.py  
    ``` 

3. **Run the Streamlit App**:

    ```
    streamlit run app/gui.py
    ```
    #### or
     
    CD into the app/ folder

    ```
    streamlit run gui.py
    ```

    Access the app at [http://localhost:8501](http://localhost:8501) in your web browser.

## Docker Setup (Optional)

1. **Build the Docker Image**:

    ```
    docker build -t question-answering-app .
    ```

2. **Run the Docker Container**:

    ```
    docker run -p 8501:8501 -d question-answering-app
    ```
