# 🚀 Deployment Guide

Complete deployment guide for AI Dev Team

---

## Quick Deploy (3 minutes)

### Option 1: Fly.io (Recommended - FREE!)

```bash
# 1. Install Fly CLI
brew install flyctl  # macOS
curl -L https://fly.io/install.sh | sh  # Linux/WSL

# 2. Login
flyctl auth login

# 3. Create app
flyctl apps create ai-dev-team-YOUR_NAME

# 4. Set secrets
flyctl secrets set GROQ_API_KEY=your_groq_api_key_here

# 5. Deploy!
flyctl deploy
```

**Done!** Your app is live at `https://ai-dev-team-YOUR_NAME.fly.dev`

---

## Deployment Options

| Platform | Cost | Setup Time | Credit Card Required |
|----------|------|------------|---------------------|
| **Fly.io** | $0 (256MB) | 3 min | Yes (no charge) |
| **Railway** | $0 ($5 credit) | 5 min | No |
| **Render** | $0 (with sleep) | 5 min | No |
| **Google Cloud Run** | $0 (2M requests) | 10 min | Yes |

---

## Detailed Guides

### 📘 [Fly.io Complete Guide](./FLY_DEPLOY_GUIDE.md)
- Free tier setup
- Custom domains
- Scaling options
- Monitoring

### 📗 [Railway Guide](./RAILWAY_DEPLOY.md)
- No credit card needed
- $5/month free credit
- Auto-deploy from GitHub

### 📙 [Render Guide](./RENDER_DEPLOY.md)
- Completely free
- Auto-sleep after 15min
- GitHub integration

### 📕 [Google Cloud Run Guide](./CLOUD_RUN_DEPLOY.md)
- 2 million requests/month free
- Auto-scaling
- Pay per use

---

## Environment Variables

Required:
```bash
GROQ_API_KEY=your_groq_api_key_here
LLM_PROVIDER=groq  # or openai, anthropic
PORT=8080
```

Optional:
```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

---

## Cost Comparison

### Free Tiers

**Fly.io**:
- ✅ 3 VMs × 256MB RAM
- ✅ 160GB outbound/month
- ✅ Auto-suspend when idle

**Railway**:
- ✅ $5 credit/month
- ✅ 512MB RAM
- ✅ No sleep

**Render**:
- ✅ 512MB RAM
- ✅ Unlimited bandwidth
- ⚠️ Sleeps after 15min

**Cloud Run**:
- ✅ 2M requests/month
- ✅ 360,000 GB-seconds
- ✅ Pay per use

---

## Monitoring

### Health Check
```bash
curl https://your-app.fly.dev/health
```

### Logs
```bash
# Fly.io
flyctl logs -a your-app

# Railway
railway logs

# Render
render logs your-service
```

### Status
```bash
# Fly.io
flyctl status -a your-app

# Railway
railway status
```

---

## Troubleshooting

### Build Failures
```bash
# Test locally first
docker build -t ai-dev-team .
docker run -p 8080:8080 --env-file .env ai-dev-team
```

### API Key Issues
```bash
# Fly.io - reset secrets
flyctl secrets unset GROQ_API_KEY
flyctl secrets set GROQ_API_KEY=new_key

# Check secrets list
flyctl secrets list
```

### Out of Memory
```bash
# Increase memory (costs money)
flyctl scale memory 512  # 256MB → 512MB
```

---

## Next Steps

- 📖 [API Documentation](../API.md)
- 🎨 [Customization Guide](./CUSTOMIZATION.md)
- 🔒 [Security Best Practices](./SECURITY.md)
- 📈 [Scaling Guide](./SCALING.md)

---

**Need help?** [Open an issue](https://github.com/your-username/langGraph/issues)
