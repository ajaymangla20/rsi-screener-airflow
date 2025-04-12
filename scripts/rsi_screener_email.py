import os
import yfinance as yf
import pandas as pd
import yagmail
import matplotlib.pyplot as plt
from datetime import datetime

# CONFIGURATION
SENDER_EMAIL = "xxx@gmail.com"
APP_PASSWORD = "xxx"  # use Gmail app password
RECIPIENT_EMAIL = "xxxx@gmail.com"
TICKERS = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]
IMAGE_PATH = os.path.abspath("rsi_table.png")

# RSI Calculation Function
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Fetch Data & Generate Table
def generate_rsi_data():
    results = []

    for ticker in TICKERS:
        try:
            df = yf.download(ticker, period="1y", interval="1d")
            df.dropna(inplace=True)

            df["RSI"] = calculate_rsi(df)

            current_price = float(df["Close"].iloc[-1].item())
            high_52w = float(df["High"].max().item())
            low_52w = float(df["Low"].min().item())
            latest_rsi = float(df["RSI"].iloc[-1].item())

            signal = "Oversold" if latest_rsi < 30 else "Overbought" if latest_rsi > 70 else "Neutral"

            results.append({
                "Ticker": ticker,
                "Current Price": f"${current_price:.2f}",
                "52W High": f"${high_52w:.2f}",
                "52W Low": f"${low_52w:.2f}",
                "RSI": f"{latest_rsi:.2f}",
                "Signal": signal
            })

        except Exception as e:
            print(f"[ERROR] {ticker}: {e}")

    return pd.DataFrame(results)

# Save DataFrame as Image (Matplotlib)
def save_image_with_matplotlib(df, image_path):
    try:
        fig, ax = plt.subplots(figsize=(10, len(df) * 0.6 + 1))
        ax.axis('off')
        table = ax.table(cellText=df.values,
                         colLabels=df.columns,
                         cellLoc='center',
                         loc='center',
                         colLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        plt.tight_layout()
        plt.savefig(image_path, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"[OK] Image saved to: {image_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Exporting image failed: {e}")
        return False

# Send Email


def send_email(image_path):
    if not os.path.isfile(image_path):
        print(f"[ERROR] File not found: {image_path}")
        return

    today_str = datetime.now().strftime("%B %d, %Y")  # e.g., April 11, 2025

    body = f"""
Hi,

Here is your Daily RSI Screener report for {today_str}.

This report includes:
• Tickers scanned: {', '.join(TICKERS)}
• Current Price, 52-Week High/Low, and RSI (Relative Strength Index)
• RSI signals:
   - Overbought (RSI > 70)
   - Oversold (RSI < 30)
   - Neutral (in between)

Please find the snapshot attached.

Best regards,  
📈 RSI Screener Bot
    """

    try:
        yag = yagmail.SMTP(user=SENDER_EMAIL, password=APP_PASSWORD)
        yag.send(
            to=RECIPIENT_EMAIL,
            subject=f"📊 RSI Screener Report – {today_str}",
            contents=body,
            attachments=image_path
        )
        print("[OK] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Sending email failed: {e}")


# Run Screener
def main():
    df = generate_rsi_data()
    if df.empty:
        print("[WARNING] No RSI data found.")
        return

    if save_image_with_matplotlib(df, IMAGE_PATH):
        send_email(IMAGE_PATH)

if __name__ == "__main__":
    main()

