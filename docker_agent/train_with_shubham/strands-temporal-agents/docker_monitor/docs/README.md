# Docker Container Health Monitor - Documentation

This directory contains all documentation for the Docker Container Health Monitor demo.

## Demo Guides

### DEMO-QUICK-START.md
**Duration:** 2 minutes  
**Purpose:** Fast walkthrough for quick demos  
**Best for:** Time-constrained presentations, initial overview

Quick setup and basic queries to show the core functionality.

### DEMO-GUIDE.md
**Duration:** 5-7 minutes  
**Purpose:** Comprehensive demo script with talking points  
**Best for:** Full presentations, technical deep dives, sales demos

Includes:
- Part 1: Simple Agent Demo (2 minutes)
- Part 2: Temporal Agent Demo (3-4 minutes)
- Part 3: Temporal UI Deep Dive (1-2 minutes)
- Cool demo scenarios
- Talking points for each section

### DEMO-CHEATSHEET.md
**Duration:** Reference only  
**Purpose:** Quick reference during live demos  
**Best for:** Having open during presentations

Contains:
- Common queries
- Expected outputs
- Troubleshooting quick fixes
- Key talking points

### DEMO-READY.md
**Duration:** Pre-demo checklist  
**Purpose:** Ensure everything is set up before demo  
**Best for:** Pre-demo preparation

Checklist of:
- Services to start
- Containers to verify
- URLs to open
- Test queries to validate

## Usage

### Before Your Demo
1. Read `DEMO-READY.md` and complete the checklist
2. Choose your demo length (2 min or 5-7 min)
3. Open the corresponding guide
4. Keep `DEMO-CHEATSHEET.md` open for reference

### During Your Demo
- Follow the script in your chosen guide
- Reference the cheatsheet for queries
- Use talking points to explain features

### After Your Demo
- Stop demo containers: `./demo-setup.sh stop`
- Review questions and feedback

## Quick Links

- **Main README:** `../README.md` - Complete technical documentation
- **Setup Script:** `../demo-setup.sh` - Manage demo containers
- **Source Code:** `../docker_agent.py`, `../docker_temporal_agent.py`

## Tips for Great Demos

1. **Start with the simple agent** - Show how easy it is to get started
2. **Highlight the Temporal UI** - This is the "wow" factor
3. **Demonstrate fault tolerance** - Kill and restart the worker
4. **Show retry policies** - Explain different strategies for different operations
5. **Compare side-by-side** - Simple vs Temporal for impact

## Customizing Demos

Feel free to:
- Modify queries to match your audience
- Add your own demo scenarios
- Adjust timing based on audience engagement
- Focus on specific features (retries, monitoring, etc.)

## Feedback

If you find issues or have suggestions for improving the demo guides, please update the documentation or create an issue.
