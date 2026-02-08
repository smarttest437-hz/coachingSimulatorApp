# Scenario Extraction Feature - Quick Guide

**Added:** February 7, 2026
**Time to implement:** 12 minutes

---

## ✅ What Was Added

### 1. **Scenario Manager Module** (`scenario_manager.py`)
- Extracts client statements from transcripts
- AI categorizes and scores quality (1-10)
- Stores in `custom_scenarios.json`
- Merges with Excel scenarios automatically

### 2. **Extraction Interface** (in Transcript Analysis mode)
- **"Extract Scenarios" button** appears after transcript analysis
- AI finds and categorizes client statements
- Review interface with quality filter
- One-click approve or bulk approve

### 3. **Library Manager** (in sidebar)
- Shows total scenarios, categories, avg quality
- Expandable details by category
- "Manage Library" button for full management

### 4. **Auto-Merged Practice Scenarios**
- Practice modes now use Excel + JSON scenarios
- Scenarios marked "From Real Transcript"
- Library grows automatically

---

## 🚀 How to Use

### After Analyzing a Transcript:

1. **Scroll down** - You'll see "📚 Extract Practice Scenarios"
2. **Click "🔍 Extract Scenarios from This Transcript"**
   - AI finds all client statements (>20 characters)
   - Shows count of potential scenarios

3. **Click "🤖 Auto-Categorize with AI"**
   - AI categorizes each statement (Career, Leadership, etc.)
   - AI scores quality (1-10)
   - Takes 30-60 seconds depending on transcript length

4. **Review Scenarios**
   - Use quality slider to filter (default: 6+)
   - See AI's category and reasoning
   - Change category if needed

5. **Approve Scenarios**
   - Click "✅ Add to Practice Library" for individual scenarios
   - Or click "✅ Approve All" to add all filtered scenarios

6. **Done!**
   - Scenarios saved to `custom_scenarios.json`
   - Immediately available in practice modes

---

## 📊 Library Manager

### In Sidebar:

**"📚 Scenario Library"** section shows:
- Total scenarios count
- Average quality score
- Expandable category breakdown

**Click "🔧 Manage Library"** to:
- See detailed statistics
- Export library as JSON
- Clear all scenarios (danger zone)

---

## 🎯 Practice with Your Scenarios

Your custom scenarios automatically appear in:

**General Coaching Practice:**
- Select any category
- Your scenarios appear alongside Excel scenarios
- Marked with "Source: Real Transcript"

**Bottom-Lining Practice:**
- Same merged approach
- Practice with your own clients' statements

---

## 📁 Files Created

| File | Purpose |
|------|---------|
| `scenario_manager.py` | Core extraction & management logic |
| `custom_scenarios.json` | Your growing scenario library (auto-created) |

---

## 🔍 What Gets Extracted

**Criteria for extraction:**
- Client statements (lines starting with "Client:")
- At least 20 characters long
- Substantive content (not just "Yes" or "Okay")

**AI Categorization:**
- Career
- Leadership
- Relationship
- Self Improvement
- Value System

**Quality Scoring (1-10):**
- 8-10: Excellent coaching moment
- 6-7: Good practice opportunity
- 4-5: Decent scenario
- 1-3: Too simple or unclear

---

## 💡 Best Practices

### 1. **Set Quality Threshold**
- Start at 6+ to get good scenarios
- Lower to 4+ if you want more quantity
- Raise to 8+ for only exceptional moments

### 2. **Review AI Categories**
- AI is usually accurate but can be changed
- Some statements fit multiple categories
- Choose what makes sense for your practice goals

### 3. **Build Gradually**
- Add 5-10 scenarios per transcript
- Focus on quality over quantity
- Your library will grow naturally over time

### 4. **Regular Practice**
- After adding scenarios, practice with them immediately
- See how it feels to work with your own coaching moments
- Identify patterns in your client conversations

---

## 📈 Example Workflow

```
Week 1: Analyze 2 transcripts
        → Extract 15 scenarios (quality 7+)
        → Practice library: 15 scenarios

Week 2: Analyze 2 more transcripts
        → Extract 12 scenarios
        → Practice library: 27 scenarios

Week 3: Analyze 2 more transcripts
        → Extract 10 scenarios
        → Practice library: 37 scenarios

Month 2: Continue weekly
         → Practice library: 100+ scenarios
         → Rich, personalized practice experience!
```

---

## 🔧 Technical Details

### Storage Format (JSON):

```json
[
  {
    "id": "custom_20260207174530_0",
    "statement": "I've been struggling with work-life balance lately...",
    "context": "What would you like to focus on today?",
    "category": "Self Improvement",
    "quality_score": 8,
    "reason": "Clear challenge with emotional weight",
    "extracted_date": "2026-02-07T17:45:30",
    "source": "transcript_extraction"
  }
]
```

### Merging Logic:

1. Load Excel scenarios (original library)
2. Load JSON scenarios (custom library)
3. Convert JSON to DataFrame matching Excel format
4. Concatenate by category
5. Return merged dictionary

---

## 🎨 UI Changes

### Transcript Analysis Mode:
```
[Existing sections...]
├── Upload transcript
├── Analyze button
├── Comprehensive analysis
├── Download button
└── 📚 Extract Practice Scenarios (NEW)
    ├── Extract button
    ├── Auto-categorize button
    └── Review interface
        ├── Quality slider
        ├── Category selector
        ├── Approve buttons
        └── Bulk approve
```

### Sidebar:
```
├── AI Provider selection
├── Model selection
└── 📚 Scenario Library (NEW)
    ├── Total scenarios
    ├── Avg quality
    ├── Category breakdown
    └── Manage library button
```

### Library Manager Page:
```
📚 Scenario Library Manager
├── Statistics
│   ├── Total scenarios
│   ├── Categories count
│   ├── Avg quality
│   └── Last added
├── Category breakdown
├── Export options
└── Danger zone (clear all)
```

---

## ⚠️ Important Notes

### Data Storage:
- **Excel file**: Original scenarios (never modified)
- **JSON file**: Your custom scenarios (grows over time)
- **Both used**: Merged automatically when loading

### Privacy:
- All data stored locally
- No cloud sync
- Backup `custom_scenarios.json` regularly

### Performance:
- Extraction: ~5 seconds for 30-line transcript
- Categorization: ~30-60 seconds (depends on transcript length)
- Each statement requires 1 AI call for categorization

---

## 🐛 Troubleshooting

### "No scenarios found"
**Cause:** Transcript has no substantive client statements (>20 chars)
**Solution:** Check transcript format - lines should start with "Client:"

### Categorization takes forever
**Cause:** Long transcript with many client statements
**Solution:** Be patient - 50 statements = ~1-2 minutes

### Categories seem wrong
**Cause:** AI misinterprets context
**Solution:** Use category dropdown to override before approving

### Scenarios not appearing in practice
**Cause:** Cache not refreshed
**Solution:** Refresh the page or restart the app

---

## 📚 Example Scenarios from Real Transcripts

**Before (Excel only):**
- Generic career scenarios
- Generic leadership scenarios
- Fixed library

**After (Excel + Your Transcripts):**
- "I'm torn between accepting a promotion and staying with my team" (YOUR client)
- "My manager doesn't listen to my ideas" (YOUR client)
- Plus all original scenarios
- Growing library every week

---

## 🎯 Success Metrics

Track your progress:
- **Week 1**: 10-20 custom scenarios
- **Month 1**: 50-100 custom scenarios
- **Month 3**: 150+ custom scenarios
- **Month 6**: 300+ personalized practice moments

Your practice becomes increasingly tailored to YOUR coaching style and YOUR clients' common challenges!

---

## 🚀 Next Steps

1. **Analyze your first transcript** (if you haven't already)
2. **Click "Extract Scenarios"**
3. **Review and approve 5-10 good ones**
4. **Try practicing with them immediately**
5. **Repeat weekly** to build your library

---

**Your coaching practice tool now learns from your actual coaching!** 🎉

---

**Files:**
- Implementation: `scenario_manager.py`
- Integration: `app_AI_feedback.py`
- Storage: `custom_scenarios.json` (auto-created)
- Guide: This file

**Time to get started:** 2 minutes (analyze a transcript you already have)
