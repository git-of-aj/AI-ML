## Pricing
- based on Standard (On-Demand): Pay-as-you-go for input and output tokens.
- [How tokens calculated](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#tokens)
- [Quota - subscription wise / model wise](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits)

## Deployment Types: 
> offers two main types of deployments: standard and provisioned.
- customers can align their workloads with their data processing requirements by choosing an
1. Azure geography (Standard or Provisioned-Managed)
2. Microsoft specified data zone (DataZone-Standard or DataZone Provisioned-Managed)
3. Global (Global-Standard or Global Provisioned-Managed) processing options.

- All deployments can perform the exact same inference operations, however the billing, scale, and performance are substantially different. As part of your solution design, you will need to make two key decisions:
1. Data processing location
2. Call volume

- Global standard is the recommended starting point.
**Global**:
- **Global deployments** use Azure’s global infrastructure for optimal traffic routing.
- **High throughput and model availability** with Global deployments.
- **Uptime SLA** and **low latency** are maintained.
- **Increased latency variation** may occur at high volumes.
- **Provisioned deployments** recommended for low latency variance at large workloads.

**Data Zone**:
- **Data zone deployments** use Azure’s global infrastructure for optimal traffic routing within a specified data zone.
- **Elevated quota limits** while keeping data processing within the Microsoft-defined data zone.
- Data stored at rest remains in the **Azure geography** of the resource (e.g., Sweden, US, EU).
- **Data processing compliance** and **Azure commitments** apply for all deployment types.
