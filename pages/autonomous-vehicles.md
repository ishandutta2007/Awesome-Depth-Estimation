# Autonomous Vehicle Bird's-Eye-View\n\nSelf-driving fleets leverage high-speed depth estimators to warp streaming 2D pixels into a 3D BEV grid. This facilitates highly reliable path planning and obstacle tracking in real-time.\n\n## Architecture Diagram\n\n```mermaid
flowchart TD
    A[Multi-Camera Stream] --> B[Depth Estimation Engine]
    B --> C[3D Frustum Projection]
    C --> D[Bird's-Eye-View Matrix]
    D --> E[Trajectory Routing]
```\n\n[Back to README](../README.md)\n