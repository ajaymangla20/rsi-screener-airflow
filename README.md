# rsi-screener-airflow
Automated RSI screener with email alerts using Airflow
# 📈 RSI Screener with Airflow

A Python-based RSI stock screener that emails a snapshot of selected stocks' RSI, prices, and 52-week stats every weekday at 9:00 AM CST using Airflow.

## 🔧 Features

- Fetch stock data using `yfinance`
- Compute RSI
- Display current price, RSI, 52-week high/low
- Render table as image
- Email report via `yagmail`
- Scheduled with Airflow

## 📂 Project Structure

## 🚀 Setup Instructions

1. Clone the repo
2. Install requirements:

## Airflow Schedule
schedule_interval="0 9 * * 1-5"


