# TikTok Automation Suite 🤖

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)

## 📌 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Disclaimer](#disclaimer)
- [License](#license)

## 🌟 Features

| Feature          | Description                                      |
|-----------------|--------------------------------------------------|
| 🧠 Smart Following | Human-like follow patterns with randomized delays |
| ❤️ Auto-Liking | Natural like behavior with configurable rates |
| ⏱️ Time Controls | Adjustable watch durations (5-25s) |
| 🔒 Anti-Detection | Mobile emulation + Chrome stealth |
| 📊 Activity Logs | Detailed session reporting |

## 🛠 Installation <a name="installation"></a>

### Prerequisites
- Python 3.8+
- Google Chrome (latest version)
- TikTok account credentials

```bash
# Clone the repository
git clone https://github.com/theoantr/tiktok_follow.git
cd tiktok_follow

# Install dependencies
pip install -r requirements.txt

# (Optional) Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
⚙️ Configuration <a name="configuration"></a>
Create .env file:

ini
Copy
TIKTOK_USERNAME="your_username"
TIKTOK_PASSWORD="your_password"
Adjust settings in bot.py:

python
Copy
# Engagement probabilities (0-1)
self.like_prob = 0.6  # 60% chance to like
self.follow_prob = 0.3  # 30% chance to follow

# Watch duration (seconds)
self.min_watch = 5    # Minimum watch time
self.max_watch = 25   # Maximum watch time
🚀 Usage <a name="usage"></a>
Run the bot with:

bash
Copy
python bot.py
Recommended Settings
Setting	Value	Description
Sessions/Day	2-3	Maximum recommended
Actions/Session	8-15	Follows + Likes
Cooldown	4+ hrs	Between sessions
🚨 Troubleshooting <a name="troubleshooting"></a>
Issue	Solution
CAPTCHA loops	Pause for 24h + complete manually
Login failures	Verify .env credentials + check account locks
Browser errors	Update Chrome + chromedriver
⚠️ Disclaimer <a name="disclaimer"></a>
This tool is for educational purposes only. Using automation may violate TikTok's Terms of Service. The developers assume no responsibility for account restrictions.

📝 License <a name="license"></a>
This project is licensed under the MIT License.

<div align="center"> <a href="https://github.com/theoantr/tiktok_follow/issues">Report Issue</a> • <a href="https://github.com/theoantr/tiktok_follow/discussions">Get Help</a> • <a href="https://github.com/theoantr/tiktok_follow/wiki">Documentation</a> </div> ```
