import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class RedditBot:
    def __init__(self):
        # Basic Appium setup
        self.capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android',
            browserName='Chrome',
            chromedriverExecutable=r'C:\Users\manoj\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
        )
        self.appium_server_url = 'http://localhost:4723'
        self.driver = None
        
        # Placeholder for user inputs
        self.subreddit = ""
        self.post_title = ""
        self.post_content = ""
        
    def start_session(self):
        """Initialize the Appium session"""
        self.driver = webdriver.Remote(
            self.appium_server_url,
            options=UiAutomator2Options().load_capabilities(self.capabilities)
        )
        self.wait = WebDriverWait(self.driver, 50)
        
    def close_session(self):
        """Close the Appium session"""
        if self.driver:
            self.driver.quit()
            
    def reddit_login(self, username, password):
        """Handle Reddit login"""
        print("\nStarting login process...")
        self.driver.get('https://www.reddit.com/login')
        try:
            # Wait for and fill username
            print("Entering username...")
            username_field = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'username')]"))  # Update if needed after inspection
            )
            username_field.send_keys(username)
        
        # Fill password
            print("Entering password...")
            password_field = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Password')]")  # Update if needed after inspection
            password_field.send_keys(password)
        
        # Click login button
            print("Clicking login button...")
            login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")
            login_button.click()
        
        # Wait for login completion
            time.sleep(5)
            print("Login process completed.")
            return True
        
        except TimeoutException:
            print("Failed to login to Reddit - elements not found or timeout")
            return False


        
    def reddit_post(self):
        """Create a post in specified subreddit"""
        try:
            print(f"\nNavigating to r/{self.subreddit}...")
            self.driver.get(f'https://www.reddit.com/r/{self.subreddit}/submit')
            time.sleep(3)
            
            # Select post type (text post)
            print("Selecting post type...")
            post_type = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Post')]"))
            )
            post_type.click()
            
            # Fill title
            print("Entering post title...")
            title_field = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//textarea[contains(@placeholder, 'Title')]"))
            )
            title_field.send_keys(self.post_title)
            
            # Fill content
            print("Entering post content...")
            content_field = self.driver.find_element(By.XPATH, "//div[@role='textbox']")
            content_field.send_keys(self.post_content)
            
            # Submit post
            print("Submitting post...")
            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            
            time.sleep(5)
            print("Post submission completed.")
            return True
            
        except TimeoutException:
            print("Failed to create Reddit post - elements not found or timeout")
            return False

def main():
    bot = RedditBot()
    
    # Get credentials and post details
    print("Welcome to Reddit Post Bot!")
    username = input("Enter Reddit username: ")
    password = input("Enter Reddit password: ")
    bot.subreddit = input("Enter subreddit name: ")
    bot.post_title = input("Enter post title: ")
    bot.post_content = input("Enter post content: ")
    
    # Initialize session
    print("\nInitializing Appium session...")
    bot.start_session()
    
    try:
        # Login and create post
        if bot.reddit_login(username, password):
            if bot.reddit_post():
                print("\nSuccess! Post has been created.")
            else:
                print("\nFailed to create post.")
        else:
            print("\nLogin failed!")
            
    finally:
        print("\nClosing Appium session...")
        bot.close_session()

if __name__ == "__main__":
    main()
