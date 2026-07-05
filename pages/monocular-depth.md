# Monocular Depth Estimation\n\nMonocular depth infers spatial information strictly from single 2D images. It relies on semantic cues, learned priors, vanishing points, and shading variations rather than explicit geometric triangulation.\n\n## Architecture Diagram\n\n```mermaid
flowchart TD
    A[Single Image] --> B[Feature Encoder]
    B --> C[Contextual Bottleneck]
    C --> D[Decoder with Skip Connections]
    D --> E[Relative/Metric Depth Map]
```\n\n[Back to README](../README.md)\n