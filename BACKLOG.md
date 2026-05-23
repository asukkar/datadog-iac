# Datadog Monitoring Backlog

This document outlines the backlog for implementing best practice Datadog monitoring and dashboards using Pulumi for our team's 30 applications.

## Prerequisite: Tagging Strategy (Option A)
- [ ] **Action:** Ensure all 30 applications are emitting the `team:<your-team-name>` tag.
- **Details:** This needs to be configured at the deployment level (e.g., via the `DD_TAGS` environment variable). By tagging at the source, we can write global monitors and dashboards in Pulumi that automatically scope to all apps owned by the team without hardcoding service names.

---

## Phase 1: Standardization & Golden Signal Monitors
*Goal: Create global, reusable monitors scoped to the team tag.*

- [ ] **1. Implement Error Rate Monitor (5xx or APM Errors)**
  - Alert on high error rates across any service owned by the team.
- [ ] **2. Implement Latency Monitor**
  - Alert when p95 or p99 response times exceed acceptable limits for our services.
- [ ] **3. Implement Traffic/Anomaly Monitor**
  - Alert on unexpected drops in request volume or throughput.
- [ ] **4. Set Up Alert Routing**
  - Configure the Pulumi monitors to route alerts to our team's specific notification channels (e.g., Slack, PagerDuty).

## Phase 2: Visualization & Dashboards
*Goal: Provide immediate visibility into the health of all team applications.*

- [ ] **5. Build a "Team Overview" Dashboard**
  - Create a single, high-level dashboard using Pulumi that aggregates the health, error rates, latency, and active alerts across all services tagged with our team name.
- [ ] **6. Build a Standard Service Dashboard Template**
  - Create a reusable Pulumi module that generates an in-depth dashboard template. When filtering by a specific `service`, it will display its golden signals, infrastructure health, and recent errors.

## Phase 3: Advanced Reliability (Future)
*Goal: Measure impact and ensure external availability.*

- [ ] **7. Define Service Level Objectives (SLOs)**
  - Implement availability and latency SLOs for the most critical apps.
- [ ] **8. Synthetic Monitoring**
  - Set up HTTP/API check synthetics to ensure critical endpoints are reachable from the outside.
