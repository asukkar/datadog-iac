import pulumi
import pulumi_datadog as datadog

def create_cpu_monitor():
    """
    Creates a Datadog monitor for CPU idle time.
    """
    monitor = datadog.Monitor("example-cpu-monitor",
        name="Example Monitor - CPU Idle",
        type="metric alert",
        query="avg(last_5m):avg:system.cpu.idle{*} < 20",
        message="The average CPU idle time is below 20% over the last 5 minutes.",
        tags=["pulumi", "example", "cpu"]
    )
    return monitor