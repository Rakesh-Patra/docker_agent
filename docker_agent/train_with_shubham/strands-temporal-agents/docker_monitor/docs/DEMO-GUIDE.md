# Docker Container Health Monitor - Demo Guide

## Quick Start

### 1. Start Demo Containers (1 minute)

```bash
docker compose -f docker-compose.demo.yml up -d
```

This starts 3 containers:
- **demo-nginx** - Healthy web server with health checks
- **demo-redis** - Redis with verbose logging
- **demo-logger** - Python app generating continuous logs

### 2. Run the Simple Agent

```bash
source venv/bin/activate
python docker_agent.py
```

### 3. Try These Queries

**Basic Status:**
```
Check container status
```

**Health Monitoring:**
```
Is demo-nginx healthy?
Check health of all running containers
```

**Log Viewing:**
```
Show me logs for demo-logger
Show me the last 20 lines from demo-redis
```

**Container Management:**
```
Restart demo-nginx
```

---

## Full Demo Script (5-7 minutes)

### Part 1: Simple Agent Demo (2 minutes)

**Terminal 1: Start Simple Agent**
```bash
cd strands-temporal-agents
source venv/bin/activate
python docker_agent.py
```

**Demo Queries:**

1. **"Check container status"**
   - Shows all 3 demo containers
   - Points out: name, status, uptime, ports

2. **"Is demo-nginx healthy?"**
   - Shows health check status
   - CPU and memory usage
   - Restart count

3. **"Show me logs for demo-logger"**
   - Displays recent log entries
   - Shows INFO, DEBUG, WARN, ERROR messages

4. **"Check health of all running containers"**
   - Aggregated health summary
   - Shows X/3 containers healthy

### Part 2: Temporal Agent Demo (3-4 minutes)

**Terminal 1: Temporal Server**
```bash
temporal server start-dev
```

**Terminal 2: Worker**
```bash
cd strands-temporal-agents
source venv/bin/activate
python docker_worker.py
```

**Terminal 3: Client**
```bash
cd strands-temporal-agents
source venv/bin/activate
python docker_client.py
```

**Browser: Open Temporal UI**
```
http://localhost:8233
```

**Demo Queries:**

1. **"Check demo-nginx health and show logs"**
   - Complex multi-step query
   - Switch to Temporal UI
   - Show workflow execution
   - Point out AI orchestrator activity
   - Show health check activity
   - Show logs activity

2. **"Is demo-redis healthy?"**
   - Quick health check
   - Show in UI: single activity execution
   - Point out retry policy configuration

3. **Demonstrate Fault Tolerance:**
   - Start query: "Show me logs for demo-logger"
   - While running, kill worker (Ctrl+C in Terminal 2)
   - Restart worker: `python docker_worker.py`
   - Show in UI: workflow continues!

### Part 3: Temporal UI Deep Dive (1-2 minutes)

**In the Temporal UI:**

1. **Workflows Tab**
   - Show list of all executed workflows
   - Filter by status (Running, Completed, Failed)
   - Click on a workflow

2. **Workflow Details**
   - Show execution timeline
   - Click on AI orchestrator activity
   - Show input (user query) and output (operation plan)
   - Click on Docker operation activities
   - Show retry attempts if any

3. **Search & Filter**
   - Search for specific container names
   - Filter by time range
   - Show audit trail capabilities

---

## Cool Demo Scenarios

### Scenario 1: Multi-Container Health Check
```
Query: "Check health of all running containers"

Shows:
✓ demo-nginx: Healthy
  Status: running
  Health Check: healthy
  CPU: 0.5%
  Memory: 2.1%

✓ demo-redis: Healthy
  Status: running
  Health Check: healthy
  CPU: 0.3%
  Memory: 1.8%

✓ demo-logger: Healthy
  Status: running
  CPU: 0.1%
  Memory: 0.5%

Summary: 3/3 containers healthy
```

### Scenario 2: Log Analysis
```
Query: "Show me the last 30 lines from demo-logger"

Shows:
[INFO] Processing request #12847 at Thu Jan 16 16:30:45 UTC 2026
[DEBUG] Cache hit ratio: 87%
[WARN] High memory usage detected: 76%
[INFO] Processing request #29384 at Thu Jan 16 16:30:50 UTC 2026
[ERROR] Connection timeout to database
...
```

### Scenario 3: Container Restart
```
Query: "Restart demo-nginx"

Shows:
✓ Successfully restarted container 'demo-nginx'

Then verify:
Query: "Is demo-nginx healthy?"
Shows: Container just restarted, uptime: 10 seconds
```

### Scenario 4: Complex Orchestration
```
Query: "Check demo-redis health and show me its logs"

Temporal UI shows:
1. ai_orchestrator_activity
   Input: "Check demo-redis health and show me its logs"
   Output: "health:demo-redis,logs:demo-redis"

2. check_container_health_activity
   Input: "demo-redis"
   Output: Health status with metrics

3. get_container_logs_activity
   Input: "demo-redis", lines: 100
   Output: Redis logs
```

---

## Talking Points

### Simple Agent
- ✅ Natural language interface
- ✅ Instant feedback
- ✅ Perfect for development
- ✅ User-friendly error messages

### Temporal Agent
- ✅ Automatic retries (show retry policy)
- ✅ Complete audit trail (show UI)
- ✅ Fault tolerance (demonstrate)
- ✅ Production-ready monitoring
- ✅ AI-powered orchestration

### Technical Highlights
- ✅ Real Docker SDK integration
- ✅ Health checks with CPU/memory metrics
- ✅ Configurable retry policies per operation
- ✅ Proper error handling (retryable vs non-retryable)
- ✅ Comprehensive logging

---

## Cleanup

Stop demo containers:
```bash
docker compose -f docker-compose.demo.yml down
```

Check status:
```bash
docker ps --filter "name=demo-"
```

View logs:
```bash
docker logs demo-nginx --tail 20
docker logs demo-redis --tail 20
docker logs demo-logger --tail 20
```

---

## Troubleshooting

**Containers not starting?**
```bash
docker ps -a | grep demo-
./demo-setup.sh restart
```

**No logs showing?**
```bash
# Wait a few seconds for logs to generate
sleep 10
./demo-setup.sh logs
```

**Temporal UI not accessible?**
```bash
# Check Temporal server is running
curl http://localhost:8233
```

---

## Pro Tips

1. **Keep Temporal UI open** during demo - it's the "wow" factor
2. **Use complex queries** to show AI orchestration
3. **Demonstrate failure recovery** - it's impressive
4. **Show the retry policies** in code - technical credibility
5. **Compare simple vs Temporal** side-by-side for impact

## The Punchline

"This is production-ready DevOps automation. Start simple for development, add Temporal for production. Same code, enterprise features when you need them."
