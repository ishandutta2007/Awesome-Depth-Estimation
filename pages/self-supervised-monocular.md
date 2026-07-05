# The Self-Supervised Monocular Warping Era\n\nSelf-supervised monocular depth networks mitigate the need for expensive LiDAR ground truth by utilizing sequential image consistency. Through ego-motion estimation and differentiable inverse warping, they optimize a photometric loss.\n\n## Architecture Diagram\n\n```mermaid
flowchart TD
    A[Target Frame t] --> C[Depth Network]
    B[Source Frame t+1] --> D[Pose Network]
    A --> D
    C --> E[Predicted Depth]
    D --> F[Predicted Pose]
    E --> G[Inverse Warping & Photometric Loss]
    F --> G
```\n\n[Back to README](../README.md)\n