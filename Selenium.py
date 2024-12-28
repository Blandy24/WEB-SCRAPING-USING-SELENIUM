import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Set up the WebDriver
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'  # The website we are scraping
driver_path = r'C:\Users\kakor\Desktop\SELENIUM\chromedriver-win64\chromedriver.exe'  # Path to ChromeDriver

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(driver_path))

# Open the website
driver.get(website)

# Wait for the table to appear on the page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

# 2. Collect Data from the Table
dates = []
home_teams = []
scores = []
away_teams = []

# Find all table rows
rows = driver.find_elements(By.TAG_NAME, 'tr')

# Loop through each row
for row in rows:
# Get the table data in each row
    columns = row.find_elements(By.TAG_NAME, 'td')  
# Making sure the row has at least 4 columns
    if len(columns) >= 4:  
        # Extract the data from each column
        date = columns[0].text
        home_team = columns[1].text
        score = columns[2].text
        away_team = columns[3].text
        
        # Append the data to the lists
        dates.append(date)
        home_teams.append(home_team)
        scores.append(score)
        away_teams.append(away_team)

# 3. Print the Data (it can be optional)
for i in range(len(dates)):
    print(f"Date: {dates[i]} | Home Team: {home_teams[i]} | Score: {scores[i]} | Away Team: {away_teams[i]}")

# 4. Save the Data to a CSV File
#creating a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Home Team': home_teams,
    'Score': scores,
    'Away Team': away_teams
})

 # Saving the DataFrame to a CSV file
df.to_csv('football_matches.csv', index=False) 

# Close the browser
driver.quit()
