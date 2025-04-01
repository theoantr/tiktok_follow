# 🚀 TikTok Engagement Bot 🤖

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green?logo=selenium)
![License](https://img.shields.io/badge/License-MIT-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

*A smart automation tool for organic TikTok engagement with human-like behavior patterns*

</div>

## ✨ Features
- 🧠 Intelligent activity randomization
- ⏱️ Natural delay patterns (5-25s between actions)
- 📱 Mobile device emulation
- 🔒 Undetectable browsing
- ⚙️ Fully configurable settings

## 🛠 Installation

### Prerequisites
- 🐍 [Python 3.8+](https://www.python.org/downloads/)
- 🌐 [Google Chrome](https://www.google.com/chrome/)
- 🔑 TikTok account credentials

```bash
# Clone the repository
git clone https://github.com/theoantr/tiktok_follow.git
bash
Copy
# Navigate to project directory
cd tiktok_follow
bash
Copy
# Install dependencies
pip install -r requirements.txt
⚙️ Configuration
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
🚀 Usage
bash
Copy
python bot.py
Recommended Settings
Setting	Value	Description
Sessions/Day	2-3	Maximum recommended
Actions/Session	8-15	Follows + Likes
Cooldown	4+ hrs	Between sessions
🌟 Pro Tips
🕒 Vary your usage times

🔄 Mix follow/unfollow patterns

📈 Start slow (5-10 actions/day)

📊 Monitor account notifications

⚠️ Important Notes
❗ TikTok may suspend accounts for automation
❗ Never share your .env file
❗ Use a dedicated account if possible

<div align="center">
