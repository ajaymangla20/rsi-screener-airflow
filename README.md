# 📈 Automated RSI Screener with Python and Airflow

This project builds a daily RSI-based stock screener in Python, automated using Airflow. It fetches stock data, calculates RSI and other metrics, renders a styled image table, and emails it out every weekday at 9:00 AM CST.
The RSI screen is a technical analysis tool that identifies when an asset may be overbought or oversold based on its recent price movements. It's a momentum indicator that oscillates between 0 and 100, with values above 70 typically suggesting overbought conditions and values below 30 suggesting oversold conditions.

---

## 🔧 Features

- ✅ Fetch data using `yfinance`
- ✅ Compute 14-day RSI
- ✅ Show:
  - Ticker
  - RSI
  - Current Price
  - 52-Week High & Low
- ✅ Clean, formatted table image
- ✅ Email report with subject + body + date
- ✅ Scheduled via **Apache Airflow**
<img width="772" alt="Screenshot 2025-04-11 at 11 58 29 PM" src="https://github.com/user-attachments/assets/10e01f11-a137-4f9d-91fc-830203397eb5" />

---

## 📂 Project Structure

\`\`\`
airflow/
└── scripts/
    └── rsi_screener_email.py
README.md
requirements.txt
\`\`\`

---

## 🛠️ Requirements

Install with:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

Or manually:

\`\`\`bash
pip install yfinance pandas matplotlib yagmail
\`\`\`

---

## 🕐 Airflow Schedule

DAG is scheduled to run:

\`\`\`
📅 Monday–Friday
🕘 9:00 AM CST
\`\`\`

Inside your Airflow DAG:

\`\`\`python
schedule_interval="0 9 * * 1-5"
\`\`\`

---

## 📧 Email Report

- Sent using **\`yagmail\`** via Gmail SMTP
- Includes:
  - Subject with today’s date
  - Friendly message body
  - PNG image attachment with table

> 🔒 Gmail Note: Use an **App Password** for secure sending

---

## 💡 Example Stocks

Here\'s a sample set of tickers you might use:

\`\`\`python
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA"]
\`\`\`

---

## 📤 Output Sample

_Attach a sample \`rsi_table.png\` email screenshot if needed._

---

## 🚀 Getting Started

1. Clone this repo
2. Place your script inside \`airflow/scripts/\`
3. Add your \`EMAIL\` and \`APP_PASSWORD\` to your script
4. Set up Airflow scheduler and webserver
5. Enjoy automatic reports in your inbox!

---

## 📌 License

MIT — use freely and improve!' > README.md && \
echo -e "yfinance\npandas\nmatplotlib\nyagmail" > requirements.txt && \
git add README.md requirements.txt && \
git commit -m "📄 Added final README and requirements" && \
git push origin main

## Steps 
1. **Install Airflow** and start the webserver and scheduler.
2. **Create the Python script** that calculates RSI for stock data.
3. **Create the Airflow DAG** to schedule and automate running the RSI script daily.
4. **Upload the DAG** into the `dags/` directory of your Airflow setup.
5. **Monitor the DAG** from the Airflow UI to check execution and logs.

By following these steps, you will have automated your RSI screener using Apache Airflow.



