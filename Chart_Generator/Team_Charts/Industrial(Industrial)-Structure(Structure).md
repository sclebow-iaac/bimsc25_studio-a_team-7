```mermaid
    graph LR
    Industrial(Industrial) -- Building Service Routing<br>Curves ---> Structure(Structure)
    Industrial(Industrial) -- Equipment Placement<br>Rectangular Prisms<br>and Weight<br>floats ---> Structure(Structure)
    Structure(Structure) -- Building Circulation ---> Industrial(Industrial)
    Structure(Structure) -- Structural Elements ---> Industrial(Industrial)
    Structure(Structure) -- Building Circulation ---> Industrial(Industrial)

    style Industrial fill:#ffa646, stroke:black
    style Structure fill:#f86041, stroke:black, color:#fff
```
