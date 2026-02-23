# Docker Monitor Directory Structure

## Overview

The `docker_monitor/` directory is organized to separate code, configuration, and documentation clearly.

## Directory Layout

```
docker_monitor/
│
├── Core Implementation (Python files)
│   ├── __init__.py                    # Package initialization
│   ├── docker_utils.py                # Docker SDK wrapper & data models
│   ├── docker_agent.py                # Simple agent with @tool decorators
│   ├── docker_temporal_agent.py       # Temporal workflows & activities
│   ├── docker_worker.py               # Temporal worker process
│   └── docker_client.py               # Temporal client interface
│
├── Demo & Testing
│   ├── docker-compose.demo.yml        # Demo container definitions
│   ├── test_docker_agent_basic.py     # Basic functionality tests
│   └── validate_docker_monitor.py     # Installation validation
│
├── Documentation (docs/)
│   ├── README.md                      # Documentation overview
│   ├── DEMO-GUIDE.md                  # Full demo script (5-7 min)
│   ├── DEMO-QUICK-START.md            # Quick demo (2 min)
│   ├── DEMO-CHEATSHEET.md             # Quick reference
│   ├── DEMO-READY.md                  # Pre-demo checklist
│   ├── REORGANIZATION-COMPLETE.md     # Reorganization notes
│   └── STRUCTURE.md                   # This file
│
└── README.md                          # Main documentation

```

## File Purposes

### Core Implementation

**docker_utils.py**
- Docker SDK wrapper with error handling
- Data models: `ContainerInfo`, `HealthStatus`, `OperationResult`
- Exception classes: `DockerConnectionError`, `ContainerNotFoundError`

**docker_agent.py**
- Simple agent using Strands framework
- Four @tool decorated functions for Docker operations
- Interactive CLI interface
- Direct execution (no Temporal)

**docker_temporal_agent.py**
- Five Temporal activities for Docker operations
- AI orchestrator activity for task planning
- DockerMonitorWorkflow class
- Configurable retry policies per operation

**docker_worker.py**
- Registers workflows and activities with Temporal
- Connects to Temporal server
- Processes tasks from queue

**docker_client.py**
- Interactive CLI for submitting workflows
- Generates unique workflow IDs
- Executes workflows and displays results

### Demo & Testing

**docker-compose.demo.yml**
- Defines 3 demo containers: nginx, redis, logger
- Health checks configured
- Ports exposed for testing

**demo-setup.sh**
- Commands: start, stop, restart, status, logs
- Colored output for better UX
- Validates Docker installation

**test_docker_agent_basic.py**
- Tests data model creation
- Tests Docker client wrapper
- Basic functionality validation

**validate_docker_monitor.py**
- Comprehensive installation check
- Validates all dependencies
- Tests imports and connections

### Documentation

**README.md** (main)
- Complete technical documentation
- Setup instructions
- Architecture overview
- Troubleshooting guide

**docs/README.md**
- Documentation overview
- Guide to choosing the right demo
- Tips for great demos

**docs/DEMO-GUIDE.md**
- 5-7 minute comprehensive demo
- Three parts: Simple, Temporal, UI Deep Dive
- Talking points and scenarios

**docs/DEMO-QUICK-START.md**
- 2 minute fast demo
- Essential queries only
- Quick setup steps

**docs/DEMO-CHEATSHEET.md**
- Quick reference during demos
- Common queries with expected outputs
- Troubleshooting quick fixes

**docs/DEMO-READY.md**
- Pre-demo checklist
- Services to start
- Validation steps

## Navigation Tips

### For Development
Start with: `README.md` → `docker_utils.py` → `docker_agent.py`

### For Demos
Start with: `docs/DEMO-READY.md` → Choose your demo length → Follow the guide

### For Testing
Start with: `validate_docker_monitor.py` → `test_docker_agent_basic.py`

### For Understanding Temporal
Start with: `README.md` (Why Temporal section) → `docker_temporal_agent.py` → `docker_worker.py`

## Design Principles

1. **Separation of Concerns**
   - Code in root
   - Documentation in `docs/`
   - Demo infrastructure separate

2. **Self-Contained**
   - All Docker monitor files in one directory
   - No dependencies on parent directory (except config.py)
   - Can be copied/moved independently

3. **Progressive Disclosure**
   - README.md for overview
   - docs/ for detailed guides
   - Code comments for implementation details

4. **Demo-Ready**
   - Multiple demo lengths
   - Pre-flight checklist
   - Quick reference available

## Adding New Features

When adding new features:

1. **Code**: Add to appropriate .py file
2. **Tests**: Update test_docker_agent_basic.py
3. **Docs**: Update README.md
4. **Demo**: Add to DEMO-GUIDE.md if demo-worthy

## Related Documentation

- **Main Repo**: `../README.md` - Overview of both demos
- **Config**: `../config.py` - Shared configuration
- **Original Demo**: `../agent.py`, `../temporal_agent.py` - Original simple agent
