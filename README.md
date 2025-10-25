# Stock-Market-Analysis
A beginner-friendly Stock Market Analysis Assistant built using Python. It fetches real-time stock data, analyzes recent trends, and visualizes price movements using Matplotlib. The project integrates SpeechRecognition and Pyttsx3 for voice interaction, allowing users to ask for stock updates and receive both spoken and visual responses.



========================
README.md
========================

# Stock Market Assistant

This Python desktop assistant gives you the current stock price for any company and shows a simple 7-day closing price chart. You speak the stock symbol, and it tells you the price and displays a graph.

## Features
- Get real-time stock price for any company
- Shows a 7-day closing price chart using Matplotlib
- Voice-controlled input and spoken output
- Stop the assistant by saying "exit"

## How to Run
1. Make sure Python (3.9+) is installed
2. Install required libraries:
pip install -r requirements.txt
3. Get a free API key from [Finnhub](https://finnhub.io)  
4. Replace `"YOUR_FINNHUB_API_KEY"` in `stock_assistant.py` with your key  
5. Run the assistant:  python stock_assistant.py
6. Speak the stock symbol clearly. Say **exit** to stop.

## Tech Stack
- Python
- SpeechRecognition (voice input)
- pyttsx3 (text-to-speech)
- requests (API requests)
- pandas (data handling)
- matplotlib (plotting charts)


========================
requirements.txt
========================

SpeechRecognition
PyAudio
pyttsx3
requests
pandas
matplotlib

