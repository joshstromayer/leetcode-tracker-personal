import os
import pandas as pd
from datetime import date
import sys

df = pd.read_csv("data.csv")

problem_title = df["title"]

problem_number = input("Enter LeetCode problem number: ").zfill(4)
print("Paste your solution code below. Press Ctrl+D (or Ctrl+Z on Windows) when you're done:")
solution_code = sys.stdin.read()

leetcode_folder = "leetcode"
progress_folder = "leetcode_progress"
today = date.today().strftime("%Y-%m-%d")
day_folder = os.path.join(progress_folder, today)

os.makedirs(day_folder, exist_ok=True)

matching_files = [f for f in os.listdir(leetcode_folder) if f.startswith(problem_number)]
if not matching_files:
    print(f"❌ Problem {problem_number} not found in leetcode folder.")
    exit()

leetcode_filename = matching_files[0]
title_slug = leetcode_filename[5:-3]
new_filename = f"{problem_number}-{title_slug}.py"

new_file_path = os.path.join(day_folder, new_filename)
with open(new_file_path, "w") as f:
    f.write(f"# Problem {problem_number}: {title_slug.replace('-', ' ').title()}\n")
    f.write("# Your solution:\n")
    f.write(solution_code + "\n")

print(f"✅ Created: {new_file_path}")

old_file_path = f"leetcode/{new_filename}"
with open(old_file_path, "w") as leet_file:
    leet_file.write(f"# Problem {problem_number}: {title_slug.replace('-', ' ').title()}\n")
    leet_file.write("# Your solution:\n")
    leet_file.write(solution_code + "\n")
