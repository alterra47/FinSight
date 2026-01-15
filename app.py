import streamlit as st
import yfinance as yf
import requests
import pandas as pd
import plotly.express as px

# --- CONFIGURATION ---
# Using a free, pre-trained Financial Sentiment model from Hugging Face
API_URL = "https://router.huggingface.co/hf-inference/models/ahmedrachid/FinancialBERT-Sentiment-Analysis"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(text):
    """Send text to Hugging Face LLM API with DEBUGGING enabled"""
    try:
        payload = {"inputs": text}
        response = requests.post(API_URL, headers=headers, json=payload)
        json_data = response.json()
        
        # --- DEBUGGING: Print the raw response to the app ---
        if "error" in json_data:
            st.warning(f"⚠️ API Error: {json_data['error']}")
            if "estimated_time" in json_data:
                st.info(f"⏳ Model is waking up... Please wait {json_data['estimated_time']} seconds and click Run again.")
        
        return json_data
        
    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
        return [{"label": "Error", "score": 0.0}]

# --- APP LAYOUT ---
st.set_page_config(page_title="FinSight AI", layout="wide")
st.title("📈 FinSight: AI-Powered Financial News Analysis")
st.markdown("Uses **FinancialBERT (LLM)** via Hugging Face API to analyze market sentiment.")

ticker = st.text_input("Enter Stock Ticker:", "NVDA")

if st.button("Run AI Analysis"):
    if API_TOKEN == "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx":
        st.error("🚨 Please paste your Hugging Face API Token in the code!")
    else:
        with st.spinner(f"Fetching news for {ticker} & querying LLM..."):
            # 1. Get Real Data
            stock = yf.Ticker(ticker)
            news = stock.news
            
            if not news:
                st.warning("No news found.")
            else:
                results = []
                progress_bar = st.progress(0)
                
                # 2. Process Top 5 Articles
                for i, item in enumerate(news[:5]):
                    title = item.get('title', 'No Title')
                    
                    # Call the API
                    api_response = query_huggingface(title)

                    # robust parsing logic
                    label = "Neutral"
                    score = 0.5
                    
                    if isinstance(api_response, list):
                        # Case A: It's a list inside a list [[{...}]]
                        if len(api_response) > 0 and isinstance(api_response[0], list):
                            data = api_response[0][0]
                            label = data.get('label', 'Neutral')
                            score = data.get('score', 0.5)
                        # Case B: It's just a flat list [{...}]
                        elif len(api_response) > 0 and isinstance(api_response[0], dict):
                            data = api_response[0]
                            label = data.get('label', 'Neutral')
                            score = data.get('score', 0.5)
                    elif isinstance(api_response, dict) and "error" in api_response:
                         st.error(f"API Error: {api_response['error']}")
                         # If loading, stop loop to save time
                         if "loading" in api_response['error']:
                             break

                    results.append({
                        "Title": title,
                        "Sentiment": label,
                        "Confidence": score,
                        "URL": item.get('link', '#')
                    })
                    progress_bar.progress((i + 1) / 5)

                # 3. Visualization
                df = pd.DataFrame(results)
                
                # Metrics
                st.write("### AI Analysis Results")
                col1, col2 = st.columns(2)
                col1.metric("Top Sentiment", df['Sentiment'].mode()[0])
                col2.metric("Avg Confidence", f"{df['Confidence'].mean():.2f}")
                
                # Color map for chart
                color_map = {"positive": "green", "negative": "red", "neutral": "gray"}
                fig = px.bar(df, x='Sentiment', y='Confidence', color='Sentiment',
                             title="Model Confidence Levels", hover_data=['Title'],
                             color_discrete_map=color_map)
                st.plotly_chart(fig, use_container_width=True)
                
                # Data Table
                st.dataframe(df[['Sentiment', 'Confidence', 'Title']])