# 🚀 Quick Demo Start

## Setup (30 seconds)

```bash
# 1. Start demo containers
docker compose -f docker-compose.demo.yml up -d

# 2. Verify containers are running
docker ps | grep demo-
```

You should see:
- ✅ demo-nginx (web server)
- ✅ demo-redis (cache)
- ✅ demo-logger (log generator)

---

## Simple Agent Demo (2 minutes)

```bash
source venv/bin/activate
python docker_agent.py
```

### Try These Queries:

```
Check container status
```
→ Shows all 3 containers with details

```
Is demo-nginx healthy?
```
→ Shows health status, CPU, memory

```
Show me logs for demo-logger
```
→ Displays recent logs with INFO/DEBUG/WARN/ERROR

```
Check health of all running containers
```
→ Aggregated health summary

---

## Temporal Agent Demo (3 minutes)

### Terminal 1: Temporal Server
```bash
temporal server start-dev
```

### Terminal 2: Worker
```bash
cd strands-temporal-agents
source venv/bin/activate
python docker_worker.py
```

### Terminal 3: Client
```bash
cd strands-temporal-agents
source venv/bin/activate
python docker_client.py
```

### Browser: Temporal UI
```
http://localhost:8233
```

### Try These Queries:

```
Check demo-nginx health and show logs
```
→ Multi-step operation, watch in Temporal UI!

```
Is demo-redis healthy?
```
→ Single health check with retry policy

---

## The "Wow" Moments

### 1. AI Orchestration
Query: `"Check demo-nginx health and show logs"`

In Temporal UI, you'll see:
1. AI breaks it into: `health:demo-nginx,logs:demo-nginx`
2. Each step executes separately
3. Different retry policies per step

### 2. Fault Tolerance
1. Start: `"Show me logs for demo-logger"`
2. Kill worker (Ctrl+C in Terminal 2)
3. Restart: `python docker_worker.py`
4. Operation continues! ✨

### 3. Execution History
- Browse all past operations
- Click into any workflow
- See exact timing, retries, errors
- Complete audit trail

---

## Cool Queries to Try

```
Show me all stopped containers
```

```
Check health of all running containers
```

```
Show me the last 50 lines from demo-logger
```

```
Restart demo-nginx
```

```
Is demo-redis consuming too much memory?
```

---

## Cleanup

```bash
docker compose -f docker-compose.demo.yml down
```

---

## Quick Troubleshooting

**No containers?**
```bash
./demo-setup.sh status
./demo-setup.sh restart
```

**Need more logs?**
```bash
# Wait a bit for logs to accumulate
sleep 10
./demo-setup.sh logs
```

**Temporal not working?**
```bash
# Check server is running
curl http://localhost:8233
```

---

## The Pitch

**"This is production-ready DevOps automation."**

- ✅ Natural language interface
- ✅ Real Docker integration
- ✅ AI-powered orchestration
- ✅ Automatic retries
- ✅ Complete audit trail
- ✅ Fault tolerance

**"Start simple for dev, add Temporal for production."**
