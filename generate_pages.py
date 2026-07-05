import os

pages_dir = "pages"
os.makedirs(pages_dir, exist_ok=True)

pages = [
    {
        "filename": "traditional-stereopsis.md",
        "title": "The Traditional Epipolar & Stereopsis Era",
        "diagram": "```mermaid\nflowchart TD\n    A[Left Image] --> C[Feature Matching]\n    B[Right Image] --> C\n    C --> D[Disparity Map]\n    D --> E[Depth Map via Triangulation]\n```",
        "details": "Traditional depth estimation relies heavily on classical multi-view geometry. Using Epipolar geometry, systems match pixels across calibrated stereo images. This technique is accurate under ideal conditions but often fails when facing textureless regions or severe occlusions."
    },
    {
        "filename": "supervised-fcn.md",
        "title": "The Supervised Deep Multi-Scale Era",
        "diagram": "```mermaid\nflowchart LR\n    A[Input Image] --> B[Global Coarse Scale Network]\n    A --> C[Local Fine Scale Network]\n    B --> D[Combined Feature Maps]\n    C --> D\n    D --> E[Refined Depth Map]\n```",
        "details": "Pioneered by Eigen et al. and FCN frameworks, this era marked the beginning of using Convolutional Neural Networks (CNNs) for monocular depth prediction. The architecture leverages multiple scales—one for structural layout and another for local edge refinement."
    },
    {
        "filename": "self-supervised-monocular.md",
        "title": "The Self-Supervised Monocular Warping Era",
        "diagram": "```mermaid\nflowchart TD\n    A[Target Frame t] --> C[Depth Network]\n    B[Source Frame t+1] --> D[Pose Network]\n    A --> D\n    C --> E[Predicted Depth]\n    D --> F[Predicted Pose]\n    E --> G[Inverse Warping & Photometric Loss]\n    F --> G\n```",
        "details": "Self-supervised monocular depth networks mitigate the need for expensive LiDAR ground truth by utilizing sequential image consistency. Through ego-motion estimation and differentiable inverse warping, they optimize a photometric loss."
    },
    {
        "filename": "generative-foundation.md",
        "title": "The Open-Vocabulary Generative Foundation Era",
        "diagram": "```mermaid\nflowchart LR\n    A[Input Images in the Wild] --> B[Vision Transformer (ViT)]\n    B --> C[Masked Autoencoding / Contrastive Learning]\n    C --> D[Zero-Shot Depth Map Generation]\n```",
        "details": "Modern foundation models, like DepthAnything and Marigold, apply massive Vision Transformers pre-trained on varied datasets. They offer powerful zero-shot capabilities to estimate depth maps across domains without explicit retraining."
    },
    {
        "filename": "stereo-depth.md",
        "title": "Stereo Depth Estimation",
        "diagram": "```mermaid\nflowchart TD\n    A[Camera 1] --> C[Stereo Rectification]\n    B[Camera 2] --> C\n    C --> D[Cost Volume Construction]\n    D --> E[Disparity Calculation]\n    E --> F[Metric Depth]\n```",
        "details": "This functional variant triangulates keypoints between parallel cameras. It uses the known baseline and focal length to compute physical metric depth efficiently, largely serving manufacturing and metrology pipelines."
    },
    {
        "filename": "monocular-depth.md",
        "title": "Monocular Depth Estimation",
        "diagram": "```mermaid\nflowchart TD\n    A[Single Image] --> B[Feature Encoder]\n    B --> C[Contextual Bottleneck]\n    C --> D[Decoder with Skip Connections]\n    D --> E[Relative/Metric Depth Map]\n```",
        "details": "Monocular depth infers spatial information strictly from single 2D images. It relies on semantic cues, learned priors, vanishing points, and shading variations rather than explicit geometric triangulation."
    },
    {
        "filename": "active-sensor-fusion.md",
        "title": "Active-Sensor Fusion Models",
        "diagram": "```mermaid\nflowchart LR\n    A[RGB Sensor] --> C[Feature Fusion Block]\n    B[Sparse LiDAR / ToF] --> C\n    C --> D[Dense Metric Depth Map]\n```",
        "details": "Sensor fusion pipelines intertwine dense high-resolution RGB matrices with sparse absolute measurements from active ToF or LiDAR sensors. This effectively neutralizes scale ambiguity while preserving sharp boundaries."
    },
    {
        "filename": "inverse-warping.md",
        "title": "Differentiable Inverse Warping Layers",
        "diagram": "```mermaid\nflowchart TD\n    A[Source Pixel Grids] --> C[Spatial Transformer Network]\n    B[Target Pose & Depth] --> C\n    C --> D[Synthesized Target View]\n    D --> E[Loss Calculation]\n```",
        "details": "Differentiable inverse warping is a fundamental layer in unsupervised sequence frameworks. It transforms coordinates from one view into another by injecting continuous gradients backwards during training."
    },
    {
        "filename": "skip-connections.md",
        "title": "Symmetrical Spatial Skip Connections",
        "diagram": "```mermaid\nflowchart LR\n    A[Encoder Block 1] --> B[Encoder Block 2]\n    B --> C[Bottleneck]\n    C --> D[Decoder Block 1]\n    D --> E[Decoder Block 2]\n    A -- Skip Connection --> E\n    B -- Skip Connection --> D\n```",
        "details": "Within U-Net architectures, skip connections bridge the high-resolution features from early encoder layers directly into the decoder. This mitigates boundary blurring when recreating the dense spatial layout."
    },
    {
        "filename": "memory-wall.md",
        "title": "The Mega-Pixel Activation Memory Wall",
        "diagram": "```mermaid\nflowchart TD\n    A[High-Res Input] --> B[Heavy ViT / FCN Backbone]\n    B --> C{Memory Bottleneck}\n    C -- Teacher Model --> D[Knowledge Distillation]\n    D --> E[Compact Edge Model / SRAM]\n```",
        "details": "Real-world autonomous systems encounter inference bottlenecks due to massive matrix activation structures. Engineers rely on Knowledge Distillation and model quantization (e.g., TensorRT) to shrink these models for embedded devices."
    },
    {
        "filename": "scale-ambiguity.md",
        "title": "The Scale Ambiguity Trap",
        "diagram": "```mermaid\nflowchart LR\n    A[Indoor Datasets] --> C[Mixed-Objective Training]\n    B[Outdoor Datasets] --> C\n    C --> D[Scale-Invariant Loss Function]\n    D --> E[Robust Global Model]\n```",
        "details": "Monocular networks typically struggle transitioning across domains because of the scale ambiguity trap. Multi-dataset mixing strategies and scale-invariant loss functions have become essential to stabilize metric and relative predictions."
    },
    {
        "filename": "autonomous-vehicles.md",
        "title": "Autonomous Vehicle Bird's-Eye-View",
        "diagram": "```mermaid\nflowchart TD\n    A[Multi-Camera Stream] --> B[Depth Estimation Engine]\n    B --> C[3D Frustum Projection]\n    C --> D[Bird's-Eye-View Matrix]\n    D --> E[Trajectory Routing]\n```",
        "details": "Self-driving fleets leverage high-speed depth estimators to warp streaming 2D pixels into a 3D BEV grid. This facilitates highly reliable path planning and obstacle tracking in real-time."
    },
    {
        "filename": "humanoid-robotics.md",
        "title": "Advanced Kinetic Trajectory Guidance",
        "diagram": "```mermaid\nflowchart LR\n    A[Stereo / RGB-D Input] --> B[Spatial Mapping Loop]\n    B --> C[Kinematic Controller]\n    C --> D[Actuator Joint Adjustments]\n```",
        "details": "Bipedal robotics use dense depth topologies up to 100+ Hz loops to execute reliable grab-and-place locomotion. Visual spatial awareness keeps interaction boundaries safe during dynamic maneuvers."
    },
    {
        "filename": "spatial-computing.md",
        "title": "Spatial Computing & AR",
        "diagram": "```mermaid\nflowchart TD\n    A[Wearable Camera] --> B[Real-Time Mesh Reconstruction]\n    B --> C[Occlusion Tracking]\n    C --> D[Virtual Asset Blending]\n```",
        "details": "Augmented Reality headsets mandate accurate edge separation to composite holographic layers realistically into physical rooms. Zero-shot depth prediction powers persistent environmental mapping."
    }
]

for p in pages:
    content = f"# {p['title']}\\n\\n{p['details']}\\n\\n## Architecture Diagram\\n\\n{p['diagram']}\\n\\n[Back to README](../README.md)\\n"
    with open(os.path.join(pages_dir, p['filename']), "w", encoding="utf-8") as f:
        f.write(content)

print("Pages created.")
