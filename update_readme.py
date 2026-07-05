import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Depth-Estimation\README.md"

replacements = {
    "**The Traditional Epipolar & Stereopsis Era (Classic Computer Vision Baseline)**": "[**The Traditional Epipolar & Stereopsis Era (Classic Computer Vision Baseline)**](pages/traditional-stereopsis.md)",
    "**The Supervised Deep Multi-Scale Era (Eigen et al., 2014 / FCN, 2015)**": "[**The Supervised Deep Multi-Scale Era (Eigen et al., 2014 / FCN, 2015)**](pages/supervised-fcn.md)",
    "**The Self-Supervised Monocular Warping Era (SfMLearner / Monodepth, ~2017–2022)**": "[**The Self-Supervised Monocular Warping Era (SfMLearner / Monodepth, ~2017–2022)**](pages/self-supervised-monocular.md)",
    "**The Open-Vocabulary Generative Foundation Era (~2023–Present)**": "[**The Open-Vocabulary Generative Foundation Era (~2023–Present)**](pages/generative-foundation.md)",
    "**A. Stereo Depth Estimation (Multi-View Triangulation)**": "[**A. Stereo Depth Estimation (Multi-View Triangulation)**](pages/stereo-depth.md)",
    "**B. Monocular Depth Estimation (Single-Frame Inference)**": "[**B. Monocular Depth Estimation (Single-Frame Inference)**](pages/monocular-depth.md)",
    "**C. Active-Sensor Fusion Models (RGB-D Infrastructure)**": "[**C. Active-Sensor Fusion Models (RGB-D Infrastructure)**](pages/active-sensor-fusion.md)",
    "**Differentiable Inverse Warping Layers**": "[**Differentiable Inverse Warping Layers**](pages/inverse-warping.md)",
    "**Symmetrical Spatial Skip Connections (U-Net Dense Enclaves)**": "[**Symmetrical Spatial Skip Connections (U-Net Dense Enclaves)**](pages/skip-connections.md)",
    "**The Mega-Pixel Activation Memory Wall & Inference Latency Ceilings**": "[**The Mega-Pixel Activation Memory Wall & Inference Latency Ceilings**](pages/memory-wall.md)",
    "**The Scale Ambiguity and Domain Drift Stagnation**": "[**The Scale Ambiguity and Domain Drift Stagnation**](pages/scale-ambiguity.md)",
    "**Autonomous Vehicle Bird's-Eye-View (Perception Perception Stacks)**": "[**Autonomous Vehicle Bird's-Eye-View (Perception Perception Stacks)**](pages/autonomous-vehicles.md)",
    "**Advanced Kinetic Trajectory Guidance for Humanoid Robotics**": "[**Advanced Kinetic Trajectory Guidance for Humanoid Robotics**](pages/humanoid-robotics.md)",
    "**Spatial Computing & Augmented Reality Environment Mapping**": "[**Spatial Computing & Augmented Reality Environment Mapping**](pages/spatial-computing.md)"
}

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

for k, v in replacements.items():
    content = content.replace(k, v)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated with links.")
