# Using Ollama (Free Local LLM)

**Last Updated:** February 7, 2026

---

## Why Ollama?

✅ **Completely FREE** - No API costs, no quotas
✅ **Private** - Runs locally on your Mac
✅ **No Internet Required** - Works offline after model download
✅ **No API Keys** - No sign-ups or credentials needed
✅ **Unlimited Usage** - Analyze as many transcripts as you want

---

## Setup Instructions

### Step 1: Install Ollama

```bash
# Install via Homebrew
brew install ollama
```

### Step 2: Start Ollama Service

```bash
# Start Ollama (runs in background)
ollama serve &
```

Or open a new terminal window and run:
```bash
ollama serve
```

Keep this terminal window open while using the app.

### Step 3: Download a Model

Choose one model based on your needs:

**Option A: Fast & Good (Recommended)**
```bash
ollama pull llama3.1:8b
```
- Size: ~4.7GB
- Speed: Fast
- Quality: Good for coaching analysis
- RAM needed: 8GB

**Option B: Alternative Fast Model**
```bash
ollama pull mistral:7b
```
- Size: ~4.1GB
- Speed: Fast
- Quality: Also good

**Option C: Best Quality (Slower)**
```bash
ollama pull llama3.1:70b
```
- Size: ~40GB
- Speed: Slower
- Quality: Excellent
- RAM needed: 64GB

### Step 4: Verify Installation

```bash
# Test that Ollama is working
ollama list

# Should show your downloaded models
# Example output:
# NAME              ID              SIZE    MODIFIED
# llama3.1:8b       42182419e950    4.7GB   2 minutes ago
```

---

## Using with the Coaching App

### Start the App

```bash
cd /Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester
source ../../venv/bin/activate
streamlit run app_AI_feedback.py --server.port 8502
```

### Configure the App

1. **In the sidebar**, select: **"Ollama (Free, Local)"**
2. Choose your model from the dropdown (e.g., `llama3.1:8b`)
3. You should see: "💡 Using Ollama (Free)"

### Test It

1. Select "Transcript Analysis" mode
2. Upload `coaching_transcript_cleaned.txt`
3. Click "🔍 Analyze Transcript"
4. Wait 20-60 seconds (local processing is slower than cloud)
5. Review feedback!

---

## Comparison: Ollama vs OpenAI

| Feature | Ollama (Free) | OpenAI (Paid) |
|---------|---------------|---------------|
| **Cost** | Free | ~$0.02 per analysis |
| **Speed** | Slower (20-60s) | Fast (10-20s) |
| **Quality** | Good | Excellent |
| **Privacy** | 100% private | Sent to OpenAI |
| **Internet** | Not required | Required |
| **Setup** | One-time install | API key + credits |
| **Limits** | None | Quota/billing limits |

---

## Troubleshooting

### Issue: "Connection refused" or "Failed to connect"

**Cause:** Ollama service not running

**Solution:**
```bash
# Start Ollama in a separate terminal
ollama serve
```

Keep that terminal window open while using the app.

---

### Issue: "Model not found"

**Cause:** Model not downloaded

**Solution:**
```bash
# Download the model you selected in the app
ollama pull llama3.1:8b
```

---

### Issue: Analysis takes forever or times out

**Cause:** Model too large for your hardware or RAM insufficient

**Solution:**
- Use a smaller model: `ollama pull llama3.1:8b`
- Close other applications to free up RAM
- Be patient - first analysis can take 1-2 minutes

---

### Issue: "Rate limit" or "Insufficient quota" error

**This can't happen with Ollama!** If you see this error, you're still using OpenAI mode.

**Solution:**
- In the sidebar, select "Ollama (Free, Local)"
- Restart the app if needed

---

## Performance Tips

### Speed Up Analysis:

1. **Use Smaller Models:** `llama3.1:8b` is much faster than `llama3.1:70b`
2. **Close Other Apps:** Free up RAM for faster processing
3. **First Run is Slow:** Model loads into memory (subsequent runs are faster)
4. **Keep Ollama Running:** Don't stop/restart between analyses

### Quality Tips:

1. **For Best Quality:** Use `llama3.1:70b` if you have 64GB+ RAM
2. **For Speed:** Use `llama3.1:8b` or `mistral:7b`
3. **Good Balance:** `llama3.1:8b` provides good coaching feedback

---

## Disk Space Requirements

Models require disk space:

- `llama3.1:8b` → 4.7GB
- `mistral:7b` → 4.1GB
- `llama3.1:70b` → 40GB
- `llama3.2:latest` → 2.0GB (smaller, less capable)

**Tip:** You can delete models you don't use:
```bash
ollama rm llama3.1:70b
```

---

## Advanced: Using Multiple Models

You can download multiple models and switch between them in the app:

```bash
# Download multiple models
ollama pull llama3.1:8b
ollama pull mistral:7b

# List available models
ollama list
```

Then in the app sidebar, select different models from the dropdown.

---

## Switching Between Ollama and OpenAI

You can use both! Switch anytime in the sidebar:

- **Ollama** for free, private, unlimited analysis
- **OpenAI** when you need faster results or slightly better quality

No code changes needed - just select in the sidebar.

---

## Uninstalling

If you want to remove Ollama later:

```bash
# Stop the service
killall ollama

# Remove models
ollama rm llama3.1:8b

# Uninstall Ollama
brew uninstall ollama

# Remove model data (optional)
rm -rf ~/.ollama
```

---

## Resources

- **Ollama Website:** https://ollama.ai
- **Available Models:** https://ollama.ai/library
- **Documentation:** https://github.com/ollama/ollama

---

## Summary

**Quick Start:**
```bash
# 1. Install
brew install ollama

# 2. Start service
ollama serve &

# 3. Download model
ollama pull llama3.1:8b

# 4. Run app
streamlit run app_AI_feedback.py --server.port 8502

# 5. Select "Ollama (Free, Local)" in sidebar
```

**Done!** You now have unlimited, free coaching transcript analysis. 🎉

---

**Cost Comparison:**

Analyzing 100 coaching sessions:
- OpenAI: ~$2-5
- Ollama: **$0** (completely free)

---

*Happy coaching with free AI! 🎯*
