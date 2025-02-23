# Amazon Price Tracker

This is a Python script that tracks the price of an item on Amazon and sends an email alert when the price drops below a specified threshold.

**Features**

Scrapes Amazon for the current price of an item.

Sends an email alert when the price drops below the target.

Uses environment variables to keep credentials secure.

**Requirements**

Python 3.x

requests package

beautifulsoup4 package

smtplib (built-in Python library)

python-dotenv package

**Setup Instructions**

**1. Install Dependencies**

Run the following command to install required Python packages:

pip install requests beautifulsoup4 python-dotenv

**2. Create a .env File**

You need to create a .env file in the project directory and add your email credentials:

SMTP_ADDRESS=smtp.gmail.com

EMAIL_ADDRESS=your_email@gmail.com

EMAIL_PASSWORD=your_email_password

Note: If using Gmail, you may need to set up an App Password instead of your regular password.

**3. Update the Tracking URL and Buy Price**

In the script, modify the following variables:

URL = "https://www.amazon.com/your-product-url"

BUY_PRICE = 20  # Set your desired price threshold

Change the URL to the product you want to track and adjust the BUY_PRICE value accordingly.

**4. Run the Script**

Execute the script using:

python main.py

If the item's price drops below your **BUY_PRICE**, an **email alert** will be sent.

**Notes**

Ensure your email provider allows SMTP access.

Amazon may block frequent scraping, so avoid running this too frequently.

**License**

This project is for educational purposes only. Use responsibly!

