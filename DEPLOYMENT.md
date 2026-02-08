# Deployment Guide - Render.com

## 🚀 Quick Deploy to Render

### Option 1: Automatic Deploy (Recommended)

Click this button to deploy directly:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/smarttest437-hz/coachingSimulatorApp)

### Option 2: Manual Deploy via Render Dashboard

1. **Go to Render Dashboard**
   - Visit https://dashboard.render.com/
   - Sign in (or create a free account)

2. **Create New Web Service**
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub account if not already connected
   - Select the repository: `smarttest437-hz/coachingSimulatorApp`

3. **Configure the Service**
   Render will auto-detect the `render.yaml` file, but verify these settings:

   - **Name:** `coaching-simulator-app`
   - **Region:** Oregon (US West)
   - **Branch:** `main`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app_AI_feedback.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`
   - **Plan:** Free

4. **Set Environment Variables**
   - Click **"Advanced"** → **"Add Environment Variable"**
   - Add:
     - **Key:** `OPENAI_API_KEY`
     - **Value:** Your OpenAI API key (starts with `sk-...`)
   - Click **"Add"**

5. **Deploy**
   - Click **"Create Web Service"**
   - Render will build and deploy your app (takes 2-5 minutes)
   - Once deployed, you'll get a URL like: `https://coaching-simulator-app.onrender.com`

---

## 🔑 Getting Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Click **"Create new secret key"**
3. Copy the key (starts with `sk-...`)
4. Add it to Render as environment variable

---

## 📊 Monitoring Your Deployment

- **Logs:** View real-time logs in Render dashboard
- **Metrics:** Check CPU, memory usage in the Metrics tab
- **Sleep Mode:** Free tier apps sleep after 15 min of inactivity (first request takes ~30s to wake)

---

## 🔄 Updating Your App

When you push changes to GitHub:

```bash
git add .
git commit -m "Your update message"
git push origin main
```

Render will **automatically redeploy** your app within 1-2 minutes.

---

## ⚠️ Important Notes

### Free Tier Limitations:
- **750 hours/month** (enough for one always-on app)
- Apps **sleep after 15 min** of inactivity
- **50 GB bandwidth/month**
- Slower CPU compared to paid tiers

### For Better Performance:
- Upgrade to **Starter plan** ($7/month) for:
  - No sleep
  - Faster CPU
  - More memory

---

## 🐛 Troubleshooting

### App won't start:
- Check logs in Render dashboard
- Verify `OPENAI_API_KEY` is set correctly
- Ensure all files pushed to GitHub

### "Module not found" errors:
- Check `requirements.txt` has all dependencies
- Trigger manual redeploy in Render dashboard

### API key errors:
- Verify key is valid: https://platform.openai.com/api-keys
- Check key is set as environment variable (not in secrets.toml)
- Ensure no extra spaces in the key value

---

## 📞 Support

- **Render Docs:** https://render.com/docs
- **Streamlit Docs:** https://docs.streamlit.io/
- **OpenAI Docs:** https://platform.openai.com/docs

---

## 🎯 Your App URLs

- **GitHub Repo:** https://github.com/smarttest437-hz/coachingSimulatorApp
- **Render App:** (will be available after deployment)

---

**Ready to deploy? Follow the steps above!** 🚀
