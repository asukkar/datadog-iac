import pulumi
from monitors.cpu import create_cpu_monitor

# Create the CPU monitor
cpu_monitor = create_cpu_monitor()

# Export the monitor's name and ID
pulumi.export("monitor_name", cpu_monitor.name)
pulumi.export("monitor_id", cpu_monitor.id)