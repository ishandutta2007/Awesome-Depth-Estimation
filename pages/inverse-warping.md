# Differentiable Inverse Warping Layers\n\nDifferentiable inverse warping is a fundamental layer in unsupervised sequence frameworks. It transforms coordinates from one view into another by injecting continuous gradients backwards during training.\n\n## Architecture Diagram\n\n```mermaid
flowchart TD
    A[Source Pixel Grids] --> C[Spatial Transformer Network]
    B[Target Pose & Depth] --> C
    C --> D[Synthesized Target View]
    D --> E[Loss Calculation]
```\n\n[Back to README](../README.md)\n