# The Open-Vocabulary Generative Foundation Era\n\nModern foundation models, like DepthAnything and Marigold, apply massive Vision Transformers pre-trained on varied datasets. They offer powerful zero-shot capabilities to estimate depth maps across domains without explicit retraining.\n\n## Architecture Diagram\n\n```mermaid
flowchart LR
    A[Input Images in the Wild] --> B[Vision Transformer (ViT)]
    B --> C[Masked Autoencoding / Contrastive Learning]
    C --> D[Zero-Shot Depth Map Generation]
```\n\n[Back to README](../README.md)\n