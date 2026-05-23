# Datadog Monitoring Strategy & Design Principles

This document outlines the core design principles and Datadog best practices that guide our monitoring setup via Pulumi. All infrastructure as code defined in this repository should adhere to these standards.

## Core Principles

### 1. Unified Service Tagging
The foundation of effective Datadog monitoring is tagging. We rely on the following universally applied tags at the deployment level:
- `env`: The environment (e.g., `prod`, `staging`).
- `service`: The specific microservice or application name.
- `version`: The deployed version or git commit hash.
- `team`: Ownership tag (e.g., `team:<our-team>`).

**Why:** Universal tagging automatically correlates metrics, distributed traces, and logs, making troubleshooting drastically faster.

### 2. Infrastructure as Code (IaC) First
All Datadog resources (Monitors, Dashboards, SLOs, Synthetics) must be managed through this Pulumi project.
**Why:** Prevents "click-ops" configuration drift in the UI, ensures version control, allows peer review, and makes reproducing setups across environments trivial.

### 3. Multi-Alerts Over Individual Alerts
Avoid creating a separate monitor for every individual service. Instead, create a single "Multi-Alert" grouped by the `service` tag and scoped to our `team` tag.
**Example:** `avg(last_5m):anomalies(sum:trace.flask.request.errors{team:<our-team>} by {service})`
**Why:** When a new application is deployed with the team tag, it automatically inherits all baseline monitoring. Zero additional configuration is required.

### 4. Alert on Symptoms, Not Causes
Focus primary alerting (pages) on user-facing symptoms rather than infrastructure utilization.
- **Good (Pageable):** "High error rate on the checkout API (Symptom)."
- **Bad (Informational):** "CPU utilization is at 85% (Cause)."
**Why:** Reduces alert fatigue. High resource usage is only an emergency if it causes latency or errors for the user.

### 5. Actionable Alert Messages
Every triggered monitor must include:
- A clear description of the impact.
- Template variables (e.g., `{{service.name}}` or `{{env.name}}`) to provide immediate context.
- A direct link to the relevant Runbook or Troubleshooting Dashboard.
- Clear routing to the correct notification channel (e.g., `@slack-team-alerts`).

### 6. Dashboards by Persona
Dashboards should be designed with specific use cases in mind:
- **Overview Dashboards:** High-level health of all team services, active alerts, and aggregate error rates. Designed for daily standups or leadership visibility.
- **Troubleshooting / Service Dashboards:** Deep-dive metrics including JVM/Node.js stats, infrastructure health, and trace queries. Designed for engineers actively debugging an incident.
