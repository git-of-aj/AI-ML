SaaS is a business and software delivery model that gives organizations the ability to offer their solutions in a low-friction, service-centric model that maximizes value for customers and providers. It relies on agility and operational efficiency as pillars of a business strategy that promotes growth, reach, and innovation.
- SaaS places more emphasis on the experience customers will have with your service
- how rapidly you can introduce features that address customer needs. Details associated with how your service is built, operated, and managed are out of your customer’s view.
> we think about this SaaS service as we would with any other service we might consume. If we’re in a restaurant, we certainly care about the food, but we also care about the service. How quickly does your server come to your table, how often do they refill your water, how fast does the food come—these are all measures of the service experience. This is the same mindset and value system that should shape how we think about building a SaaS service.
## Traditional Software 
![17276050717514779273197687129444](https://github.com/user-attachments/assets/c22489b4-1be1-4744-a159-ee6d257d88e4)
- Each customer have own version installed
- hard for provider to centrally manage all customer and support app
- hard to scale / adds more operational costs, Eroding profit margin
## SaaS
![17276056223915009599594455256520](https://github.com/user-attachments/assets/e37dadbf-8be6-4a70-b702-d0deba66e109)

- tenant could be a company with many users, or it could correlate directly to an individual user.
- Gone is the idea of having separate, one-off versions running for each customer. Having all tenants running the same version represents one of the fundamental distinguishing attributes of a SaaS environment
- Gmail Webapp : Same for All || Mobile App - Backend is same as Webapp, its juts the frontend that we update and install on mobile
- - This is a core part of the SaaS value proposition that gives teams the ability to reduce operational expenses, and improve overall organizational agility.

## Architecture 
![17276066828643259927561390082523](https://github.com/user-attachments/assets/ba189e10-ab27-48fd-83e2-049811ff336d)

- Control Plane : regardless of application deployment and isolation scheme—must include those services that give you the ability to manage and operate your tenants through a single, unified experience

- `Control Plane = Common Core services + Interface` 
web application, a command line interface, or an API) that might be used by a SaaS provider to manage their multi-tenant environment 

- An important caveat is that the control plane and its services are not actually multi-tenant. The functionality is not providing the actual functional attributes of your SaaS application (which does need to be multi-tenant). If you look inside any one of the core services, for example, you won’t find tenant isolation and the other constructs that are part of your multi-tenant application functionality. These services are global to all tenants.
- `Data Isolation ensured by adding Tenant Id / Metadata Driven Request`

- **App Plane** : Multi Tenant: Tenant Provising Components here as based on license you purchased ... services given --> Some could argue that this belongs in the control plane. However, we’ve placed it in the application domain, because the resources it must provision and configure are more directly connected to services that are created and configured in the application plane.

## Variations of tenancy in SaaS 
![17276078773112382967450171170585](https://github.com/user-attachments/assets/3d752b0e-34bd-4974-ac0c-7d973c7680dd)

- term silo is meant to describe scenarios where a resource is dedicated to a given tenant. Conversely, the pool model is used to describe scenarios where a resource is shared by tenants.

![17276080012843924395817433491562](https://github.com/user-attachments/assets/c0d0b005-76e0-425c-a026-5cda79150905)

## MSP vs SaaS
> MSP aim :The focus is on offloading the management responsibility.
![17276080954719042004813822687364](https://github.com/user-attachments/assets/236cb25c-5746-4a19-a668-fff167ccc93c)

- approach here would be to use whatever automation is available to provision each customer environment, and install the software for that customer.

## SaaS Identity 
As each user is authenticated, they must be connected to a specific tenant context. This tenant context provides essential information about your tenant that is used throughout your SaaS environment.
- The token from this identity process flows into the microservices of your application and is used to create tenant aware logs, record metrics, meter billing, enforce tenant isolation, and so on.

## Tenant Isolation and Data Partitions 
- Partitioning data does not ensure that the data is isolated. Isolation must still be applied separately to ensure that one tenant can’t access the resources of another tenant.
- As an example, with Amazon DynamoDB, a siloed model uses a separate table for each tenant. Pooling data in Amazon DynamoDB is achieved by storing the tenant identifier in the partition key of each Amazon DynamoDB table that manages data for all tenants.
- 

