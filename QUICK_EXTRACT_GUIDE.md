# Quick Extract Feature - Usage Guide

**Added:** February 7, 2026
**Fixes:** Session state persistence + Quick extraction option

---

## ✅ What Was Fixed

### Issue 1: Review Interface Disappearing ✅ FIXED
**Problem:** After clicking "Extract Scenarios", the page refreshed and the review interface didn't show.

**Solution:** Added `st.rerun()` after setting session state to force proper refresh.

**Now:** Review interface appears immediately after extraction!

### Issue 2: No Quick Extract Option ✅ ADDED
**Problem:** Had to run full analysis (10-point comprehensive feedback) before extracting scenarios.

**Solution:** Added "⚡ Quick Extract" button that skips analysis and goes straight to scenario extraction.

**Now:** Two options available - Full Analysis or Quick Extract!

---

## 🚀 How to Use

### After Uploading Transcript:

You'll see **TWO buttons**:

```
┌─────────────────────────┬──────────────────────────┐
│  🔍 Full Analysis       │  ⚡ Quick Extract        │
│  Complete 10-point ICF  │  Skip analysis, extract  │
│  analysis + scenarios   │  scenarios directly      │
└─────────────────────────┴──────────────────────────┘
```

---

## Option 1: Full Analysis (Original Flow)

**When to use:**
- You want comprehensive ICF feedback on the session
- You're reviewing your coaching performance
- You want both analysis AND scenario extraction

**What happens:**
1. Click "🔍 Full Analysis"
2. Wait 20-60 seconds for AI analysis
3. Review 10-point comprehensive feedback
4. Download analysis (optional)
5. Scroll down to see "📚 Extract Practice Scenarios"
6. Click "Extract Scenarios"
7. Review and approve scenarios

**Time:** 3-5 minutes (includes reading feedback)

---

## Option 2: Quick Extract ⚡ NEW!

**When to use:**
- You just want to add scenarios to your practice library
- You've already reviewed the session elsewhere
- You want to quickly build your scenario collection
- You're processing multiple transcripts in batch

**What happens:**
1. Click "⚡ Quick Extract"
2. See "📚 Extract Practice Scenarios" immediately
3. Click "🔍 Extract Scenarios from This Transcript"
4. Review shows up automatically ✅ (fixed!)
5. Click "🤖 Auto-Categorize with AI"
6. Review and approve scenarios

**Time:** 1-2 minutes

---

## 🔄 Step-by-Step: Quick Extract

### 1. Upload Transcript
```
Upload: transcripts/coaching_transcript_cleaned.txt
✅ File uploaded: coaching_transcript_cleaned.txt (13,456 characters)
```

### 2. Choose Quick Extract
```
Click: ⚡ Quick Extract
```

### 3. Extract Scenarios
```
📚 Extract Practice Scenarios

Current Library:
Total: 15    Categories: 4    Avg Quality: 7.3

Click: 🔍 Extract Scenarios from This Transcript
```

### 4. See Results (Immediately!)
```
✅ Found 30 potential scenarios!

✅ Review & Approve Scenarios

Click: 🤖 Auto-Categorize with AI
```

### 5. Review Interface Appears
```
AI is categorizing scenarios... (30-60 seconds)
✅ Categorization complete!

Quality threshold: ───●──────── 6

Showing 22 scenarios (quality >= 6)

▼ Scenario 1 - Self Improvement (Quality: 8/10)
  Client Statement: "I've been struggling with work-life balance..."
  Context: "What would you like to focus on today?"
  AI Assessment: Clear challenge with emotional weight

  Category: [Self Improvement ▼]  [✅ Add to Practice Library]
```

### 6. Approve Scenarios
```
Option A: Click "✅ Add to Practice Library" for each good one
Option B: Click "✅ Approve All" to add all filtered scenarios
```

### 7. Done!
```
Added 22 scenarios to library!

Your scenarios are now available in General Coaching Practice
and Bottom-Lining Practice modes.
```

---

## 🆚 Comparison

| Feature | Full Analysis | Quick Extract |
|---------|---------------|---------------|
| **Time** | 3-5 minutes | 1-2 minutes |
| **ICF Feedback** | ✅ Yes (10 points) | ❌ No |
| **Scenario Extraction** | ✅ Yes | ✅ Yes |
| **Best For** | Session review | Building library |
| **AI Calls** | 1 (analysis) + N (categorization) | N (categorization only) |

---

## 💡 Pro Tips

### Batch Processing Transcripts:

If you have 5 transcripts to process:

**Efficient approach:**
1. Full Analysis on your BEST session (learn from it)
2. Quick Extract on the other 4 sessions (build library fast)

**Result:** Detailed feedback on one + scenarios from all five!

### Quality Threshold:

- Start at **6** (good scenarios)
- Lower to **4** if you want more quantity
- Raise to **8** if you want only exceptional moments

### When to Use Each Mode:

**Full Analysis:**
- Weekly: Analyze your best session of the week
- Monthly: Review a challenging session
- Prep: Before coaching certification submission

**Quick Extract:**
- Daily: Add scenarios from every session
- Batch: Process multiple transcripts quickly
- Ongoing: Build library continuously

---

## 🐛 Troubleshooting

### "Review interface still doesn't show"

**Try:**
1. Refresh the browser page (F5)
2. Clear session state: Switch practice modes and back
3. Restart the app

### "Scenarios not appearing in practice"

**Solution:**
1. Check sidebar: "📚 Scenario Library" should show total > 0
2. Refresh practice mode by selecting different category
3. Restart app to reload data

### "Quick extract button not showing"

**Check:**
- Did you upload a transcript first?
- Is transcript content valid (has "Coach:" and "Client:" labels)?
- Try pasting directly instead of uploading file

---

## 📊 Workflow Examples

### Example 1: Weekly Session Review
```
Monday:    Full Analysis (30 min session with top client)
            → Review 10-point feedback
            → Extract 8 high-quality scenarios

Tuesday:   Quick Extract (3 other sessions)
            → 15 scenarios from session 1
            → 12 scenarios from session 2
            → 18 scenarios from session 3

Result: 53 new scenarios + detailed feedback on best session
Time: ~20 minutes total
```

### Example 2: Building Initial Library
```
Week 1: Quick Extract 10 recent sessions
         → 150+ scenarios in library
         → Ready for daily practice

Week 2: Full Analysis on 2 best sessions
         → Identify coaching strengths
         → Focus development areas
         → Continue adding scenarios

Result: Rich practice library + self-awareness
```

---

## 🎯 Best Practices

### 1. **Start with Quick Extract**
Build your library fast, then analyze in detail later.

### 2. **Use Quality Filter**
Don't approve everything - quality > quantity.

### 3. **Review Categories**
AI categorization is good but not perfect. Override when needed.

### 4. **Practice Immediately**
After adding scenarios, practice with them right away to see how they feel.

### 5. **Track Progress**
Check sidebar stats weekly to see library growth.

---

## 🔧 Technical Changes

### Files Modified:

1. **scenario_manager.py**
   - Added `st.rerun()` after "Extract Scenarios" button (line 288)
   - Added `st.rerun()` after "Auto-Categorize" button (line 299)
   - Added unique keys to buttons to prevent conflicts

2. **app_AI_feedback.py**
   - Added two-button interface (Full Analysis / Quick Extract)
   - Added session state management (`analysis_mode`)
   - Added Quick Extract path that skips analysis
   - Added "Back" buttons to reset session state

### Session State Variables:

```python
st.session_state.analysis_mode         # 'full' | 'quick' | None
st.session_state.extracted_scenarios   # List of extracted statements
st.session_state.reviewing_scenarios   # Boolean: show review UI
st.session_state.categorized_scenarios # List of categorized scenarios
```

---

## ✨ Summary

**Two Ways to Extract Scenarios:**

1. **🔍 Full Analysis** - Complete ICF feedback + extraction (3-5 min)
2. **⚡ Quick Extract** - Skip analysis, extract only (1-2 min)

**Both paths now work smoothly with:**
- ✅ Persistent session state
- ✅ Immediate UI updates
- ✅ Clear navigation (back buttons)
- ✅ No page refresh issues

**Your library builds faster now!** 🚀

---

## 📖 Quick Reference

```bash
# Start app
./start_app.sh

# Upload transcript
transcripts/coaching_transcript_cleaned.txt

# Choose mode:
Option 1: Full Analysis → Review feedback → Extract scenarios
Option 2: Quick Extract → Extract scenarios immediately

# Review & Approve
1. Extract → 2. Auto-Categorize → 3. Filter quality → 4. Approve

# Practice
Switch to General/Bottom-Lining Practice
Select category → See your scenarios!
```

---

**Happy scenario building!** 🎯

**Time saved with Quick Extract:** 60-70% faster than full analysis
**Recommended mix:** 1 Full Analysis + 4 Quick Extracts per week
