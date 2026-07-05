# Active-Sensor Fusion Models\n\nSensor fusion pipelines intertwine dense high-resolution RGB matrices with sparse absolute measurements from active ToF or LiDAR sensors. This effectively neutralizes scale ambiguity while preserving sharp boundaries.\n\n## Architecture Diagram\n\n```mermaid
flowchart LR
    A[RGB Sensor] --> C[Feature Fusion Block]
    B[Sparse LiDAR / ToF] --> C
    C --> D[Dense Metric Depth Map]
```\n\n[Back to README](../README.md)\n