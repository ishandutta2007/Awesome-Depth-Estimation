import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Depth-Estimation\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

seo_keywords = "\n**Keywords**: *Depth Estimation, Computer Vision, Artificial Intelligence, Machine Learning, Deep Learning, Monocular Depth, Stereo Vision, Autonomous Vehicles, Robotics, Spatio-Temporal Vision, Foundation Models, ViT*\n"
left_badges = "\n<p align=\"center\">\n  <a href=\"https://github.com/ishandutta2007/Awesome-Awesome-Awesome\"><img src=\"https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github\" alt=\"Awesome\"/></a> <a href=\"https://discord.gg/jc4xtF58Ve\"><img src=\"https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white\" alt=\"Discord\" /></a>\n</p>\n"

banner_end = "</p>\n"
if left_badges not in content:
    idx = content.find(banner_end) + len(banner_end)
    content = content[:idx] + left_badges + seo_keywords + content[idx:]

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
