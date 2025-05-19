# Simple Chatbot

A basic chatbot built with Streamlit and Google Gemini.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Application

To run the chatbot, execute:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Features

- Simple chat interface
- Real-time responses from Google's Gemini model
- Chat history persistence during the session
- Clean and modern UI using Streamlit

## Requirements

- Python 3.7+
- Google API key (for Gemini)
- Internet connection for API calls