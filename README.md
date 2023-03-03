# Streamlit + ChatGPT

![alt text](https://github.com/joeychrys/streamlit-chatGPT/blob/master/docs/application_image.jpg?raw=true)
## Overview

This is a sample Streamlit application that demonstrates how to use Streamlit as a UI with OpenAI's Chat API.

## Installation

1. Clone the repository

```bash
git clone https://github.com/joeychrys/streamlit-chatGPT.git
```

2. Create a `.env` file based on the `.env.example` file inside the `src` directory and add your `OPENAI_API_KEY`

```bash
OPENAI_API_KEY=yourapikey
```

3. Create and activate a new virtual environment

```bash
python -m venv env
source env/bin/activate
```
4. Move to project directory

```bash
cd streamlit-chatGPT
```

5. Install the required packages

```bash
pip install -r requirements.txt
```

6. Run the Streamlit application

```bash
streamlit run src/main.py
```

## Usage

Once the application is running, you can interact with it by following the on-screen instructions at `http://localhost:8501`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License
