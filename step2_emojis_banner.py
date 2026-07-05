import os
import re

assets_dir = "assets"
os.makedirs(assets_dir, exist_ok=True)

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(33,150,243);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(156,39,176);stop-opacity:1" />
    </linearGradient>
    <style>
      .title { font: bold 40px sans-serif; fill: white; text-anchor: middle; }
      .subtitle { font: 20px sans-serif; fill: #eee; text-anchor: middle; }
      @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
      }
      .anim { animation: float 3s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" rx="15" ry="15" />
  <g class="anim">
    <text x="400" y="90" class="title">Awesome Depth Estimation</text>
    <text x="400" y="130" class="subtitle">History, Progression, Variants, &amp; Applications</text>
  </g>
</svg>
"""

with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add banner after first heading if not already there
if "assets/banner.svg" not in content:
    content = content.replace("# Awesome-Depth-Estimation\n", "# Awesome-Depth-Estimation\n\n<p align=\"center\">\n  <img src=\"assets/banner.svg\" alt=\"Awesome Depth Estimation Banner\" width=\"800\">\n</p>\n")

# Add emojis
replacements = {
    "# Awesome-Depth-Estimation": "# 🌊 Awesome-Depth-Estimation",
    "## Depth Estimation in AI: History, Progression, Variants, & Applications": "## 🤖 Depth Estimation in AI: History, Progression, Variants, & Applications",
    "## 1. The Macro Chronological Evolution": "## ⏳ 1. The Macro Chronological Evolution",
    "## 2. Core Functional & Data-Space Variants": "## 🛠️ 2. Core Functional & Data-Space Variants",
    "## 3. The Spatio-Temporal Depth Extraction Matrix": "## 🧩 3. The Spatio-Temporal Depth Extraction Matrix",
    "## 4. Production Engineering Challenges & Hardware Solutions": "## 🚧 4. Production Engineering Challenges & Hardware Solutions",
    "## 5. Frontier Real-World AI Industrial Applications": "## 🏭 5. Frontier Real-World AI Industrial Applications",
    "## References": "## 📚 References"
}

for k, v in replacements.items():
    if v not in content:
        content = content.replace(k, v)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Step 2 completed.")
