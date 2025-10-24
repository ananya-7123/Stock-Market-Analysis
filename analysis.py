import requests
import pyttsx3
import speech_recognition as sr
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for stock symbol...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not catch that. Please repeat.")
            return ""
        except sr.RequestError:
            print("Connection error.")
            return ""
        return command.lower()

def get_stock_price(symbol):
    api_key = "YOUR_FINNHUB_API_KEY"  # Signup at finnhub.io
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol.upper()}&token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_price = data['c']
        high_price = data['h']
        low_price = data['l']
        speak(f"The current price of {symbol.upper()} is ${current_price}. Today's high is ${high_price}, low is ${low_price}.")
        return current_price
    else:
        speak(f"Sorry, I couldn't find data for {symbol.upper()}.")
        return None

def plot_stock_chart(symbol):
    api_key = "YOUR_FINNHUB_API_KEY"
    end = int(datetime.now().timestamp())
    start = int((datetime.now() - timedelta(days=7)).timestamp())  # last 7 days
    url = f"https://finnhub.io/api/v1/stock/candle?symbol={symbol.upper()}&resolution=D&from={start}&to={end}&token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['s'] != 'ok':
            speak("No chart data available.")
            return
        df = pd.DataFrame({
            'Date': [datetime.fromtimestamp(ts) for ts in data['t']],
            'Close': data['c']
        })
        plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='blue')
        plt.title(f"{symbol.upper()} - Last 7 Days Price")
        plt.xlabel("Date")
        plt.ylabel("Closing Price ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        speak("Unable to fetch chart data.")

def run_stock_assistant():
    speak("Hello! I can give you current stock prices and show a chart. Say 'exit' to stop.")
    while True:
        speak("Please tell me the stock symbol (like AAPL for Apple).")
        symbol = listen_command()
        if symbol == "" or symbol == "exit":
            speak("Stopping Stock Market Assistant. Stay smart!")
            break
        price = get_stock_price(symbol)
        if price:
            plot_stock_chart(symbol)

if __name__ == "__main__":
    run_stock_assistant()
