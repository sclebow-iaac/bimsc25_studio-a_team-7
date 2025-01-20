```mermaid
    graph LR
    Residential(Residential) -- Unit Placement ---> Facade(Facade)
    Facade(Facade) -- Daylight/View Access ---> Residential(Residential)
    Facade(Facade) -- Acoustics ---> Residential(Residential)
    Facade(Facade) -- Building Entrances ---> Residential(Residential)

    style Residential fill:#33a9ac, stroke:black, color:#fff
    style Facade fill:#982062, stroke:black, color:#fff
```