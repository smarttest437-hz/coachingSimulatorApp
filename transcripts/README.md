# Coaching Transcripts Folder

This folder contains coaching session transcripts used for analysis and scenario extraction.

---

## 📁 Files in This Folder

### 1. **coaching_transcript_cleaned.txt** (13 KB)
- **Format:** Clean format with "Coach:" and "Client:" labels
- **Status:** ✅ Ready for analysis in the app
- **Purpose:** Main transcript for testing and practice
- **Content:** ~25-minute coaching session about exercise and self-talk
- **Source:** Original WEBVTT converted to clean format

### 2. **sample_coaching_transcript.txt** (24 KB)
- **Format:** Original WEBVTT format with timestamps
- **Status:** ⚠️ Not ready for app (needs cleaning)
- **Purpose:** Original source file / backup
- **Note:** Use cleaned version for app

---

## 📝 How to Use

### Upload to App:

1. **Start the app:**
   ```bash
   streamlit run app_AI_feedback.py --server.port 8502
   ```

2. **Select "Transcript Analysis" mode**

3. **Upload file:**
   - Use: `transcripts/coaching_transcript_cleaned.txt`
   - Format must have "Coach:" and "Client:" labels

4. **Analyze and extract scenarios**

---

## 🔄 Adding New Transcripts

### Option 1: Clean Format (Recommended)

Create a new `.txt` file with this format:

```
Coach: What would you like to focus on today?
Client: I've been struggling with work-life balance.
Coach: Tell me more about that.
Client: I work late every night and feel guilty.
...
```

**Requirements:**
- Each line starts with "Coach:" or "Client:"
- No timestamps or extra formatting
- Save as `.txt` file

### Option 2: WEBVTT Format

If you have WEBVTT files (video captions):

1. Save original WEBVTT file here
2. Use Python script to clean it:

```python
# Clean WEBVTT to app format
with open('transcripts/your_file.txt', 'r') as f:
    lines = f.readlines()

cleaned = []
for line in lines:
    line = line.strip()
    # Skip timestamps and metadata
    if line.startswith('Coach:') or line.startswith('Client:'):
        cleaned.append(line)

with open('transcripts/your_file_cleaned.txt', 'w') as f:
    f.write('\n'.join(cleaned))
```

3. Upload the `_cleaned.txt` version to the app

---

## 📊 Transcript Organization

Recommended naming convention:

```
transcripts/
├── YYYYMMDD_client_topic_cleaned.txt    # For app use
├── YYYYMMDD_client_topic_original.txt   # Backup/source
├── 20260207_liz_exercise_cleaned.txt
├── 20260207_liz_exercise_original.txt
├── 20260214_john_career_cleaned.txt
└── 20260214_john_career_original.txt
```

**Format:** `YYYYMMDD_clientname_topic_cleaned.txt`
- Date first (easy sorting)
- Client name (pseudonym for privacy)
- Topic (brief description)
- `_cleaned` suffix for app-ready files

---

## 🔒 Privacy & Confidentiality

### CRITICAL REMINDERS:

1. **Client Consent:** Only transcribe sessions with written client permission
2. **Remove Identifying Info:**
   - Replace real names with pseudonyms (e.g., "Client", "Liz")
   - Remove company names, locations, specific identifying details
3. **Secure Storage:**
   - Keep transcripts on your local machine only
   - Don't upload to cloud storage without encryption
   - Don't share transcripts without anonymization

### Before Saving Transcripts:

- [ ] Written consent obtained from client
- [ ] All identifying information removed/changed
- [ ] Client name replaced with pseudonym
- [ ] Company/location details removed
- [ ] File named with date + pseudonym only

---

## 🧹 Maintenance

### Regular Cleanup:

**Monthly:**
- Review old transcripts - keep only useful ones
- Archive transcripts older than 6 months (if not needed)
- Check for any accidentally saved identifying information

**Delete transcripts when:**
- No longer useful for practice
- Client withdraws consent
- Beyond retention period

---

## 📈 Current Library

| File | Date | Status | Purpose |
|------|------|--------|---------|
| coaching_transcript_cleaned.txt | 2026-02-07 | ✅ Ready | Testing & practice |
| sample_coaching_transcript.txt | 2026-02-07 | ⚠️ WEBVTT | Original backup |

**Total Transcripts:** 1 ready for analysis

---

## 💡 Tips

### For Best Results:

1. **Transcription Quality:**
   - Use good transcription service (Otter.ai, Whisper, etc.)
   - Review and fix errors before analyzing
   - Remove excessive filler words ("um", "uh")

2. **Session Selection:**
   - Choose sessions with rich client exploration
   - 20-45 minute sessions work best
   - Avoid sessions with technical difficulties

3. **File Management:**
   - Keep original and cleaned versions
   - Use consistent naming convention
   - Document any special notes about sessions

---

## 🔗 Related Files

- **App:** `../app_AI_feedback.py`
- **Scenario Manager:** `../scenario_manager.py`
- **Extracted Scenarios:** `../custom_scenarios.json` (auto-created)
- **Original Scenarios:** `../Coach_Training_Scenarios_ICF_PCC.xlsx`

---

## 📖 Quick Reference

**To analyze a transcript:**
```bash
cd /Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester
streamlit run app_AI_feedback.py --server.port 8502

# Then:
# 1. Select "Transcript Analysis"
# 2. Upload: transcripts/coaching_transcript_cleaned.txt
# 3. Click "Analyze Transcript"
# 4. Click "Extract Scenarios" (optional)
```

---

**Last Updated:** February 7, 2026
**Files:** 2 (1 ready for analysis, 1 original backup)
