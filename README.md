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
⚙️ Configuration
Create a .env file:

ini
Copy
TIKTOK_USERNAME=your_username
TIKTOK_PASSWORD=your_password
Adjust settings in bot.py:

python
Copy
# Engagement probabilities (0-1)
self.like_prob = 0.6  # 60% chance to like
self.follow_prob = 0.3  # 30% chance to follow

# Watch time range (seconds)
self.min_watch = 5
self.max_watch = 25
🚀 Usage
bash
Copy
python bot.py
Recommended Session Settings
8-15 actions per session

2-3 sessions per day

4+ hours between sessions

🔧 Troubleshooting
Error	Solution
ChromeDriver issues	Run chromedriver-autoinstaller
Login failures	Verify credentials in .env
Detection warnings	Reduce action frequency
⚠️ Important Notes
This bot should be used responsibly

TikTok may suspend accounts for automation

Never share your .env file

📜 License
MIT © [Your Name]

Copy

Key features of this README:
1. **Visual Badges** - Shows Python version and license at a glance
2. **Clear Sections** - Separated installation, config, usage
3. **Troubleshooting Table** - Quick reference for common issues
4. **Safety Notices** - Promotes responsible usage
5. **Mobile-Friendly Formatting** - Proper spacing and headers
