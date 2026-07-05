# The Scale Ambiguity Trap\n\nMonocular networks typically struggle transitioning across domains because of the scale ambiguity trap. Multi-dataset mixing strategies and scale-invariant loss functions have become essential to stabilize metric and relative predictions.\n\n## Architecture Diagram\n\n```mermaid
flowchart LR
    A[Indoor Datasets] --> C[Mixed-Objective Training]
    B[Outdoor Datasets] --> C
    C --> D[Scale-Invariant Loss Function]
    D --> E[Robust Global Model]
```\n\n[Back to README](../README.md)\n