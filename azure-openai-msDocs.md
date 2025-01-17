## Why Azure OpenAI
Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-3, Codex, and DALL-E models with the security and enterprise promise of Azure. Azure OpenAI codevelops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.

With Azure OpenAI, customers get the security capabilities of Microsoft Azure while running the same models as OpenAI.

Does Azure OpenAI support VNETs and Private Endpoints?
Yes, as part of Azure AI services, Azure OpenAI supports VNETs and Private Endpoints.
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
> Azure OpenAI resource used in your Data Zone deployment is located in the United States, the data will be processed within the United States
- **Data zone deployments** use Azure’s global infrastructure for optimal traffic routing within a specified data zone.
- **Elevated quota limits** while keeping data processing within the Microsoft-defined data zone.
- Data stored at rest remains in the **Azure geography** of the resource (e.g., Sweden, US, EU).
- **Data processing compliance** and **Azure commitments** apply for all deployment types.

> For both Global and DataZone deployment types, any data you upload is stored in the location you choose (your designated geography). The only thing that changes with Global or DataZone deployments is where the data is processed. Azure still follows its data processing rules and commitments. Yes, that's correct! In both Global and DataZone deployment types, the **storage** (where your data is saved) is in the location you choose, but the **compute** (where your data is processed) can be in a different location. This means the data processing happens in one region, while the storage stays in the region you selected.

## Model FAQ
> I asked the model a question about something that happened recently before the knowledge cutoff and it got the answer wrong.
 First there's no guarantee that every recent event was part of the model's training data. And even when information was part of the training data, without using additional techniques like Retrieval Augmented Generation (RAG) to help ground the model's responses there's always a chance of ungrounded responses occurring. Both Azure OpenAI's use your data feature and Bing Chat use Azure OpenAI models combined with Retrieval Augmented Generation to help further ground model responses.
> Fine Tune Model: Q=> whats NP A=> 30 days
A base model is a model that hasn't been customized or fine-tuned for a specific use case. Fine-tuned models are customized versions of base models where a model's weights are trained on a unique set of prompts. Fine-tuned models let you achieve better results on a wider number of tasks without needing to provide detailed examples for in-context learning as part of your completion prompt. To learn more, review our fine-tuning guide.

## Temperature
- Temperature in prompt generation controls response randomness. A low temperature (e.g., 0.2) makes the output more deterministic and focused, while a high temperature (e.g., 0.8) increases randomness, allowing for more creative and varied responses. It balances predictability versus creativity in generated content.
The temperature value depends on the desired output:

- **Low temperature (0.1–0.5):** Use for precise, consistent, and focused answers, where accuracy is important.
- **Higher temperature (0.6–1):** Use for creative, diverse, and exploratory responses, where variety is valued.

Values over 1 can make output overly random and less coherent, so typically, temperatures are set below 1.
