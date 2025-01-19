```mermaid
    graph LR
    Industrial -- Building Service Routing --> Structure
    Industrial -- Shaft Requirements --> Service
    Industrial -- Utility Requirements --> Service
    Industrial -- Waste Requirements --> Service
    Service -- Circulation --> Industrial
    Service -- Service Consumption --> Industrial
```