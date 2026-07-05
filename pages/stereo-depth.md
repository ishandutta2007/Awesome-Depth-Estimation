# Stereo Depth Estimation\n\nThis functional variant triangulates keypoints between parallel cameras. It uses the known baseline and focal length to compute physical metric depth efficiently, largely serving manufacturing and metrology pipelines.\n\n## Architecture Diagram\n\n```mermaid
flowchart TD
    A[Camera 1] --> C[Stereo Rectification]
    B[Camera 2] --> C
    C --> D[Cost Volume Construction]
    D --> E[Disparity Calculation]
    E --> F[Metric Depth]
```\n\n[Back to README](../README.md)\n