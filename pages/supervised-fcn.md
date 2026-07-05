# The Supervised Deep Multi-Scale Era\n\nPioneered by Eigen et al. and FCN frameworks, this era marked the beginning of using Convolutional Neural Networks (CNNs) for monocular depth prediction. The architecture leverages multiple scales—one for structural layout and another for local edge refinement.\n\n## Architecture Diagram\n\n```mermaid
flowchart LR
    A[Input Image] --> B[Global Coarse Scale Network]
    A --> C[Local Fine Scale Network]
    B --> D[Combined Feature Maps]
    C --> D
    D --> E[Refined Depth Map]
```\n\n[Back to README](../README.md)\n