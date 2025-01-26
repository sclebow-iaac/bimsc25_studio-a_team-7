```mermaid
    graph LR
    Structure(Structure) -- Structural Elements ---> Service(Service)
    Structure(Structure) -- Building Circulation ---> Service(Service)
    Service(Service) -- Building Circulation ---> Structure(Structure)
    Service(Service) -- Equipment Placement<br> and Weight ---> Structure(Structure)

    style Structure fill:#f86041, stroke:black, color:#fff
    style Service fill:#343779, stroke:black, color:#fff
```