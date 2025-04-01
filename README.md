# 🤖 TikTok Engagement Bot

A Python-based automation tool for safe TikTok engagement (follows/likes) using Selenium with human-like behavior patterns.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features
- 🧠 Human-like engagement patterns
- ⏱️ Randomized delays between actions
- 📱 Mobile user-agent emulation
- 🔒 Undetected ChromeDriver
- 📊 Configurable engagement rates

## 🛠 Installation

### Prerequisites
- Python 3.8+
- Chrome browser installed
- TikTok account credentials

```bash
# Clone the repository
git clone https://github.com/theoantr/tiktok_follow.git
cd tiktok_follow

# Install dependencies
pip install -r requirements.txt
```
⚙️ Configuration
Create .env file:

ini
Copy
# .env
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
Star on GitHub
License

</div> ```
Key Improvements:
Visual Badges - Colorful version indicators

Emoji Icons - Better visual scanning

Responsive Tables - Clean settings display

Center-Aligned Elements - Professional layout

Social Badges - Star/License indicators

Pro Tips Section - Helpful usage advice

How to Use:
Copy this entire text

Create new file named README.md

Paste the content

Save in your project root
