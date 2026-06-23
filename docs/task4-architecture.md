# Task 4 – High Availability and Scalability Proposal

## Current Architecture

The current middleware consists of a single Publish/Subscribe server that accepts connections from publishers and subscribers. All communication passes through this server.

### Limitation

The server is a single point of failure. If it crashes, publishers and subscribers lose communication.

---

## Proposed Architecture

The following improvements are proposed:

- Deploy multiple middleware servers.
- Place a load balancer in front of the servers.
- Store topic information in a shared message broker or replicated storage.
- Implement health checks to detect failed servers.
- Automatically redirect clients to healthy servers when failures occur.

## Benefits

- High Availability
- Fault Tolerance
- Horizontal Scalability
- Improved Reliability