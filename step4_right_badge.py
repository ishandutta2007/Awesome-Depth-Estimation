import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Depth-Estimation\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

right_badge = " <a href=\"https://github.com/ishandutta2007\"><img alt=\"GitHub followers\" src=\"https://img.shields.io/github/followers/ishandutta2007?label=Follow\" /></a>"

# Find the badges paragraph. It's the first <p align="center"> that has Awesome and Discord badges.
badge_str = "alt=\"Discord\" /></a>"
if badge_str in content and right_badge not in content:
    idx = content.find(badge_str) + len(badge_str)
    content = content[:idx] + right_badge + content[idx:]

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
