"""Docker Monitor Temporal Worker.

Usage:
    python dockerworker.py
"""

import sys
import asyncio
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from temporalio.client import Client
from temporalio.worker import Worker

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import TEMPORAL_HOST, DOCKER_MONITOR_TASK_QUEUE
from docker_monitor.docker_temporal_agent import (
    DockerMonitorWorkflow,
    get_container_status_activity,
    check_container_health_activity,
    get_container_logs_activity,
    restart_container_activity,
    ai_orchestrator_activity,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

ALL_ACTIVITIES = [
    get_container_status_activity,
    check_container_health_activity,
    get_container_logs_activity,
    restart_container_activity,
    ai_orchestrator_activity,
]


async def run_worker():
    """Start the Docker Monitor Temporal worker."""
    print("=" * 60)
    print("Docker Monitor - Temporal Worker")
    print("=" * 60)
    print()

    try:
        print(f"Connecting to Temporal at {TEMPORAL_HOST}...")
        client = await Client.connect(TEMPORAL_HOST)
        print("✓ Connected to Temporal")
        print(f"✓ Listening on task queue: {DOCKER_MONITOR_TASK_QUEUE}")
        print()
        print("Press Ctrl+C to stop")
        print("=" * 60)
        print()

        worker = Worker(
            client,
            task_queue=DOCKER_MONITOR_TASK_QUEUE,
            workflows=[DockerMonitorWorkflow],
            activities=ALL_ACTIVITIES,
            activity_executor=ThreadPoolExecutor(max_workers=5),
        )
        await worker.run()

    except KeyboardInterrupt:
        print("\nShutting down worker...")
    except Exception as e:
        logger.exception("Worker failed")
        print(f"\n✗ Worker error: {e}")
        print("Make sure Temporal server is running: temporal server start-dev")


if __name__ == "__main__":
    asyncio.run(run_worker())
