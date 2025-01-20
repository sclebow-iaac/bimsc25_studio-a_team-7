```mermaid
    graph LR
    Industrial(Industrial) -- Shaft Requirements ---> Service(Service)
    Industrial(Industrial) -- Utility Requirements ---> Service(Service)
    Industrial(Industrial) -- Waste Requirements ---> Service(Service)
    Service(Service) -- Circulation ---> Industrial(Industrial)
    Service(Service) -- Service Consumption ---> Industrial(Industrial)

    style Industrial fill:#ffa646, stroke:black
    style Service fill:#343779, stroke:black, color:#fff
```