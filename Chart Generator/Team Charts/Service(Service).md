```mermaid
    graph LR
    Residential(Residential) -- Unit Placement ---> Service(Service)
    Industrial(Industrial) -- Shaft Requirements ---> Service(Service)
    Industrial(Industrial) -- Utility Requirements ---> Service(Service)
    Industrial(Industrial) -- Waste Requirements ---> Service(Service)
    Structure(Structure) -- Structural Elements ---> Service(Service)
    Structure(Structure) -- Building Cores ---> Service(Service)
    Facade(Facade) -- Daylighting ---> Service(Service)
    Facade(Facade) -- Climate Response ---> Service(Service)
    Facade(Facade) -- Building Entrances ---> Service(Service)
    Service(Service) -- Circulation ---> Residential(Residential)
    Service(Service) -- Service Access ---> Residential(Residential)
    Service(Service) -- Circulation ---> Industrial(Industrial)
    Service(Service) -- Service Consumption ---> Industrial(Industrial)
    Service(Service) -- Circulation ---> Structure(Structure)
    Service(Service) -- Equipment Weight ---> Structure(Structure)

    style Residential fill:#33a9ac, stroke:black, color:#fff
    style Industrial fill:#ffa646, stroke:black
    style Structure fill:#f86041, stroke:black, color:#fff
    style Facade fill:#982062, stroke:black, color:#fff
    style Service fill:#343779, stroke:black, color:#fff
```