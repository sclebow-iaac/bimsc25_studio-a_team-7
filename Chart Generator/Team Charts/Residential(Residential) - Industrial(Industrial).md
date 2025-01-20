```mermaid
    graph LR
    Residential(Residential) -- Unit Types ---> Industrial(Industrial)
    Residential(Residential) -- Space Layouts ---> Industrial(Industrial)
    Residential(Residential) -- MEP System Consumption ---> Industrial(Industrial)
    Residential(Residential) -- Waste Requirements ---> Industrial(Industrial)
    Industrial(Industrial) -- Building Systems ---> Residential(Residential)

    style Residential fill:#33a9ac, stroke:black, color:#fff
    style Industrial fill:#ffa646, stroke:black
```