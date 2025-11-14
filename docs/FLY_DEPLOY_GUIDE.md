# ✈️ Fly.io Deployment Guide

Complete guide for deploying AI Dev Team on Fly.io

---

## Prerequisites

1. **Groq API Key** (free)
   - Get it from: https://console.groq.com
   - Copy your API key

2. **Fly.io Account** (free)
   - Sign up: https://fly.io/app/sign-up
   - Credit card required (but won't be charged)

---

## Step-by-Step Deployment

### 1. Install Fly CLI

**macOS**:
```bash
brew install flyctl
```

**Linux/WSL**:
```bash
curl -L https://fly.io/install.sh | sh
```

**Windows (PowerShell)**:
```powershell
pwsh -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

### 2. Login to Fly.io

```bash
flyctl auth login
```

This will open your browser for authentication.

### 3. Create Your App

```bash
# Navigate to project directory
cd /path/to/langGraph

# Create app (replace YOUR_NAME with something unique)
flyctl apps create ai-dev-team-YOUR_NAME
```

### 4. Set Environment Variables

```bash
flyctl secrets set GROQ_API_KEY=your_groq_api_key_here -a ai-dev-team-YOUR_NAME
flyctl secrets set LLM_PROVIDER=groq -a ai-dev-team-YOUR_NAME
```

### 5. Deploy!

```bash
flyctl deploy -a ai-dev-team-YOUR_NAME
```

**First deployment takes 3-5 minutes** (building Docker image).

### 6. Verify Deployment

```bash
# Check status
flyctl status -a ai-dev-team-YOUR_NAME

# Open in browser
flyctl open -a ai-dev-team-YOUR_NAME

# Test health endpoint
curl https://ai-dev-team-YOUR_NAME.fly.dev/health
```

---

## Configuration

### fly.toml

The `fly.toml` file configures your app:

```toml
app = "ai-dev-team-YOUR_NAME"
primary_region = "nrt"  # Tokyo (closest to Korea)

[[vm]]
  memory = '256mb'  # FREE tier!
  cpu_kind = 'shared'
  cpus = 1

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = "suspend"  # Save money
  min_machines_running = 0  # Scale to zero

[env]
  PORT = "8080"
  LLM_PROVIDER = "groq"
```

### Regions

**Closest to Korea**:
- `nrt` - Tokyo ⭐ (recommended)
- `hkg` - Hong Kong
- `sin` - Singapore

**Change region**:
```bash
flyctl regions set nrt -a your-app
```

---

## Cost Management

### Free Tier (No Charges!)

Fly.io free tier includes:
- ✅ 3 shared-cpu-1x VMs (256MB RAM each)
- ✅ 160GB outbound data transfer/month
- ✅ 3GB persistent storage

**Current setup uses**:
- 2 VMs × 256MB = FREE! ✅
- Auto-suspend when idle = $0 ✅

### Monitor Usage

```bash
# Check billing
flyctl dashboard billing

# View metrics
flyctl dashboard -a your-app
```

### Reduce Costs

**1. Single machine** (instead of 2):
```toml
# fly.toml
[http_service]
  min_machines_running = 0

# Then deploy
flyctl deploy
```

**2. Manual scaling**:
```bash
# Scale down to 1 machine
flyctl scale count 1 -a your-app
```

---

## Custom Domain

### 1. Add Certificate

```bash
flyctl certs create yourdomain.com -a your-app
```

### 2. Configure DNS

Add these records to your DNS provider:

```
Type  | Name | Value
------|------|------
A     | @    | [Fly.io IPv4 from cert command]
AAAA  | @    | [Fly.io IPv6 from cert command]
```

### 3. Verify

```bash
flyctl certs show yourdomain.com -a your-app
```

---

## Scaling

### Vertical Scaling (More Resources)

```bash
# Increase memory
flyctl scale memory 512 -a your-app  # $5-7/month

# More CPUs
flyctl scale vm shared-cpu-2x -a your-app
```

### Horizontal Scaling (More Machines)

```bash
# Add more machines
flyctl scale count 3 -a your-app

# Auto-scale
flyctl autoscale set min=1 max=5 -a your-app
```

### Geographic Distribution

```bash
# Add regions
flyctl regions add sin hkg -a your-app

# Deploy to all regions
flyctl deploy -a your-app

# Scale per region
flyctl scale count 2 --region nrt -a your-app
```

---

## Monitoring

### Real-time Logs

```bash
# All logs
flyctl logs -a your-app

# Follow mode
flyctl logs -a your-app --follow

# Specific machine
flyctl logs -a your-app -i [machine-id]
```

### Metrics

```bash
# Dashboard
flyctl dashboard -a your-app

# Open in browser
open https://fly.io/apps/your-app/monitoring
```

### Alerts

Set up in Fly.io dashboard:
- CPU usage > 80%
- Memory usage > 90%
- Response time > 1s
- Error rate > 5%

---

## Maintenance

### Update Code

```bash
# 1. Make changes locally
git add .
git commit -m "Update feature"

# 2. Redeploy
flyctl deploy -a your-app
```

### Rollback

```bash
# List releases
flyctl releases -a your-app

# Rollback to previous
flyctl releases rollback -a your-app

# Rollback to specific version
flyctl releases rollback v5 -a your-app
```

### Restart

```bash
# Restart all machines
flyctl apps restart your-app

# Restart specific machine
flyctl machine restart [machine-id] -a your-app
```

---

## SSH Access

### Connect to Machine

```bash
# SSH into running machine
flyctl ssh console -a your-app

# Run command
flyctl ssh console -a your-app -C "python --version"
```

### SFTP

```bash
# Open SFTP session
flyctl ssh sftp shell -a your-app
```

---

## Secrets Management

### Set Secrets

```bash
# Set single secret
flyctl secrets set API_KEY=value -a your-app

# Set multiple
flyctl secrets set \
  GROQ_API_KEY=value1 \
  OPENAI_API_KEY=value2 \
  -a your-app
```

### List Secrets

```bash
flyctl secrets list -a your-app
```

### Remove Secrets

```bash
flyctl secrets unset API_KEY -a your-app
```

---

## CI/CD with GitHub Actions

### 1. Get Fly API Token

```bash
flyctl auth token
```

### 2. Add to GitHub Secrets

`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

Name: `FLY_API_TOKEN`
Value: [your token]

### 3. Create Workflow

`.github/workflows/fly-deploy.yml`:

```yaml
name: Deploy to Fly.io

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: superfly/flyctl-actions/setup-flyctl@master

      - run: flyctl deploy --remote-only -a ai-dev-team-YOUR_NAME
        env:
          FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
```

Now every `git push` auto-deploys! 🚀

---

## Troubleshooting

### Build Fails

```bash
# Build locally first
docker build -t test .

# If works, try remote build
flyctl deploy --remote-only -a your-app
```

### Out of Memory

```bash
# Check logs
flyctl logs -a your-app | grep "out of memory"

# Increase memory
flyctl scale memory 512 -a your-app
```

### Health Check Fails

```bash
# Check health endpoint
curl https://your-app.fly.dev/health

# View logs during startup
flyctl logs -a your-app --follow
```

### Secrets Not Working

```bash
# List secrets
flyctl secrets list -a your-app

# Reset secret
flyctl secrets unset GROQ_API_KEY -a your-app
flyctl secrets set GROQ_API_KEY=new_value -a your-app

# Restart app
flyctl apps restart your-app
```

---

## Advanced Features

### Database

```bash
# Create Postgres
flyctl postgres create --name your-db

# Attach to app
flyctl postgres attach your-db -a your-app
```

### Redis

```bash
# Create Redis (Upstash)
flyctl redis create

# Get connection string
flyctl redis status your-redis
```

### Volumes (Persistent Storage)

```bash
# Create volume
flyctl volumes create data --size 1 -a your-app

# Mount in fly.toml
[mounts]
  source = "data"
  destination = "/data"
```

---

## Best Practices

1. **Always use secrets** for API keys
2. **Enable auto-suspend** to save costs
3. **Monitor your usage** regularly
4. **Use health checks** for reliability
5. **Set up CI/CD** for easy updates
6. **Test locally first** before deploying

---

## Resources

- 📖 [Fly.io Docs](https://fly.io/docs/)
- 💬 [Fly.io Community](https://community.fly.io/)
- 🐛 [Report Issues](https://github.com/your-repo/issues)

---

**Happy Deploying!** 🚀
