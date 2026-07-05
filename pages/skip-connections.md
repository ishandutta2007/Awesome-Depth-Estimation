# Symmetrical Spatial Skip Connections\n\nWithin U-Net architectures, skip connections bridge the high-resolution features from early encoder layers directly into the decoder. This mitigates boundary blurring when recreating the dense spatial layout.\n\n## Architecture Diagram\n\n```mermaid
flowchart LR
    A[Encoder Block 1] --> B[Encoder Block 2]
    B --> C[Bottleneck]
    C --> D[Decoder Block 1]
    D --> E[Decoder Block 2]
    A -- Skip Connection --> E
    B -- Skip Connection --> D
```\n\n[Back to README](../README.md)\n