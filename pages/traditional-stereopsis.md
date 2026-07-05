# The Traditional Epipolar & Stereopsis Era\n\nTraditional depth estimation relies heavily on classical multi-view geometry. Using Epipolar geometry, systems match pixels across calibrated stereo images. This technique is accurate under ideal conditions but often fails when facing textureless regions or severe occlusions.\n\n## Architecture Diagram\n\n```mermaid
flowchart TD
    A[Left Image] --> C[Feature Matching]
    B[Right Image] --> C
    C --> D[Disparity Map]
    D --> E[Depth Map via Triangulation]
```\n\n[Back to README](../README.md)\n