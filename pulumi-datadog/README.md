# Pulumi Datadog Project

This project uses Pulumi to manage Datadog resources.

## Configuration

To use this project, you need to configure your Datadog credentials. The Datadog provider uses the following environment variables:

- `DATADOG_API_KEY`: Your Datadog API key.
- `DATADOG_APP_KEY`: Your Datadog application key.

You can set these environment variables in your shell:

```bash
export DATADOG_API_KEY="<YOUR_API_KEY>"
export DATADOG_APP_KEY="<YOUR_APP_KEY>"
```

Replace `<YOUR_API_KEY>` and `<YOUR_APP_KEY>` with your actual Datadog credentials. It is recommended to use a secret manager to handle these secrets in a production environment.