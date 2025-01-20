```mermaid
    graph LR
    Residential(Residential) -- Unit Types ---> Industrial(Industrial)
    Residential(Residential) -- Space Layouts ---> Industrial(Industrial)
    Residential(Residential) -- MEP System Consumption ---> Industrial(Industrial)
    Residential(Residential) -- Waste Requirements ---> Industrial(Industrial)
    Residential(Residential) -- Unit Placement ---> Structure(Structure)
    Residential(Residential) -- Unit Weight ---> Structure(Structure)
    Residential(Residential) -- Unit Placement ---> Facade(Facade)
    Residential(Residential) -- Unit Placement ---> Service(Service)
    Industrial(Industrial) -- Building Systems ---> Residential(Residential)
    Structure(Structure) -- Structural Elements ---> Residential(Residential)
    Facade(Facade) -- Daylight/View Access ---> Residential(Residential)
    Facade(Facade) -- Acoustics ---> Residential(Residential)
    Facade(Facade) -- Building Entrances ---> Residential(Residential)
    Service(Service) -- Circulation ---> Residential(Residential)
    Service(Service) -- Service Access ---> Residential(Residential)

    style Residential fill:#33a9ac, stroke:black, color:#fff
    style Industrial fill:#ffa646, stroke:black
    style Structure fill:#f86041, stroke:black, color:#fff
    style Facade fill:#982062, stroke:black, color:#fff
    style Service fill:#343779, stroke:black, color:#fff
```