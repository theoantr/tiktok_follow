import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

class TikTokSafeBot:
    def __init__(self):
        self.driver = self._init_browser()
        self.actions = ActionChains(self.driver)
        self.like_prob = 0.6  # 60% chance to like videos
        self.follow_prob = 0.3  # 30% chance to follow users
        self.min_watch = 5  # Minimum watch time (seconds)
        self.max_watch = 25  # Maximum watch time (seconds)

    def _init_browser(self):
        options = uc.ChromeOptions()
        
        # Anti-detection settings
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-notifications')
        
        # Mobile user agent
        options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1')
        
        return uc.Chrome(options=options)

    def _human_delay(self, min_sec=2, max_sec=7):
        """Random delay with mouse movement"""
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay/2)
        
        # Random mouse movement
        if random.random() > 0.5:
            x = random.randint(-20, 20)
            y = random.randint(-20, 20)
            self.actions.move_by_offset(x, y).perform()
            
        time.sleep(delay/2)

    def login(self, username, password):
        self.driver.get("https://www.tiktok.com/login")
        self._human_delay(3, 5)
        
        # Switch to email login
        try:
            self.driver.find_element(By.XPATH, '//a[contains(text(), "Log in with email")]').click()
            self._human_delay(1, 3)
        except:
            pass
            
        # Human-like typing
        username_field = self.driver.find_element(By.NAME, "username")
        for char in username:
            username_field.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
            
        self._human_delay(1, 2)
        
        password_field = self.driver.find_element(By.NAME, "password")
        for char in password:
            password_field.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
            
        self._human_delay(1, 2)
        
        # Click login
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Log in")]').click()
        time.sleep(8)

    def _watch_video(self):
        """Watch video for random duration"""
        watch_time = random.uniform(self.min_watch, self.max_watch)
        print(f"Watching video for {watch_time:.1f} seconds")
        time.sleep(watch_time)

    def _like_video(self):
        if random.random() < self.like_prob:
            try:
                like_btn = self.driver.find_element(By.XPATH, '//span[contains(@data-e2e, "like-icon")]/..')
                self.actions.move_to_element(like_btn).pause(0.5).click().perform()
                print("Liked video")
                self._human_delay(1, 3)
            except:
                pass

    def _follow_user(self):
        if random.random() < self.follow_prob:
            try:
                follow_btn = self.driver.find_element(By.XPATH, '//button[contains(text(), "Follow")]')
                self.actions.move_to_element(follow_btn).pause(0.5).click().perform()
                print("Followed user")
                self._human_delay(3, 7)
            except:
                pass

    def run_session(self, username, password, max_actions=10):
        try:
            self.login(username, password)
            self.driver.get("https://www.tiktok.com/for-you")
            time.sleep(5)
            
            actions_completed = 0
            while actions_completed < max_actions:
                self._watch_video()
                self._like_video()
                self._follow_user()
                
                # Scroll to next video
                scroll_px = random.randint(300, 600)
                self.driver.execute_script(f"window.scrollBy(0, {scroll_px})")
                self._human_delay(2, 5)
                
                actions_completed += 1
                print(f"Actions completed: {actions_completed}/{max_actions}")
                
        finally:
            self.driver.quit()

# Usage
if __name__ == "__main__":
    bot = TikTokSafeBot()
    bot.run_session(
        username="your_username_here",
        password="your_password_here",
        max_actions=8  # Start with low numbers for safety
    )