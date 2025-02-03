
import os
import datetime
import random

repo_path = "/Users/dhruvbhanderi/Documents/Greenlit"  # Replace with your repository path
os.chdir(repo_path)

start_date = datetime.date.today() - datetime.timedelta(days=365)  # Start from 1 year ago

for i in range(366):  # 366 days to cover an entire year
    date = start_date + datetime.timedelta(days=i)
    num_commits = random.randint(1, 5)  # Random commits per day (adjust range as needed)

    for j in range(num_commits):  # Loop to create multiple commits per day
        commit_message = f"Random commit {j+1} on {date.strftime('%Y-%m-%d')}"
        
        with open("activity.log", "a") as file:
            file.write(f"{commit_message}\n")

        os.system(f'git add activity.log')
        os.system(f'git commit --date="{date.strftime("%Y-%m-%d %H:%M:%S")}" -m "{commit_message}"')

os.system("git push origin main")  # Change 'main' if your branch is different
