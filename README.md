# 📈 FinSight: AI-Powered Financial Sentiment Dashboard

**FinSight** is a real-time financial analytics tool that leverages Large Language Models (LLMs) to analyze market sentiment from unstructured news data. Built with **Python** and **Streamlit**, it provides traders and analysts with instant visual insights into the "mood" of specific stock tickers.

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tech](https://img.shields.io/badge/AI-Hugging%20Face-yellow)

## 🚀 Key Features
* **Real-Time Data Ingestion:** Fetches live financial news headlines using the `yfinance` API.
* **LLM-Based Sentiment Analysis:** Utilizes **FinancialBERT** (via Hugging Face Inference API) to classify unstructured text with high precision.
* **Interactive Visualization:** visualizing sentiment trends and confidence scores using **Streamlit** and **Plotly**.
* **Robust Error Handling:** Implements resilient API calls with automatic retries and error parsing for JSON responses.

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **Language:** Python
* **AI/LLM:** Hugging Face Inference API (FinancialBERT model)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly Express
* **Data Source:** Yahoo Finance (yfinance)

## 📸 Demo
<img width="1917" height="1077" alt="Screenshot 2026-01-15 112141" src="https://github.com/user-attachments/assets/b9ce9489-16b1-4f43-8d74-84ca28aeb7b4" />

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/FinSight.git](https://github.com/yourusername/FinSight.git)
cd FinSight

```

### 2. Set Up Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install streamlit yfinance pandas plotly requests

```

### 4. Configure API Key

Get a free Access Token from [Hugging Face](https://huggingface.co/settings/tokens).
Open `app.py` and create the placeholder:

```python
API_TOKEN = "hf_YourActualTokenHere"

```

### 5. Run the Application

```bash
streamlit run app.py

```

The application will launch in your browser at `http://localhost:8501`.

## 🧠 How It Works

1. **Input:** User enters a stock ticker (e.g., `AAPL`, `NVDA`).
2. **Extraction:** The app scrapes the latest news headlines associated with that ticker.
3. **Inference:** Each headline is sent to the **FinancialBERT** model to determine if the news is *Positive*, *Negative*, or *Neutral*.
4. **Analytics:** The results are aggregated to calculate an "Overall Mood" and displayed via interactive charts.

## 🔮 Future Improvements

* Add historical sentiment tracking (saving data to MongoDB).
* Implement caching to reduce API calls and improve latency.
* Compare sentiment against actual stock price movement.

---

*Built by Aaditya Khare as a project to explore LLM applications in Fintech.*
