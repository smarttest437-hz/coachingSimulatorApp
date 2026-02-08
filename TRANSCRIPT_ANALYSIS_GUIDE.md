# Transcript Analysis Feature Guide

**Last Updated:** February 7, 2026

---

## Overview

The **Transcript Analysis** feature allows you to upload or paste complete coaching session transcripts and receive comprehensive ACC-level feedback based on ICF (International Coaching Federation) competencies.

Unlike the single-response practice modes, this feature analyzes an entire coaching conversation and provides detailed insights on:
- ACC-level competencies demonstrated
- Missed opportunities to evoke awareness
- Quality of questions
- Tone and attunement
- Acknowledgment
- Observations
- Clean language usage

---

## How to Use

### Step 1: Select Practice Mode

1. Launch the app: `streamlit run app_AI_feedback.py`
2. Select **"Transcript Analysis"** from the practice mode options at the top

### Step 2: Provide Your Transcript

You have two options:

**Option A: Upload a File**
- Click "Upload transcript file (.txt)"
- Select a plain text file containing your coaching transcript
- The file must be in `.txt` format

**Option B: Paste Directly**
- Scroll to the text area labeled "Coaching Transcript"
- Paste your transcript directly into the box
- Format requirements described below

### Step 3: Analyze

1. Click the **"🔍 Analyze Transcript"** button
2. Wait for the AI analysis (typically 10-30 seconds depending on transcript length)
3. Review the comprehensive feedback
4. Download the analysis using the **"💾 Download Analysis"** button

---

## Transcript Format Requirements

### Required Format

Each line should identify the speaker using one of these prefixes:
- `Coach:` - for coach statements/questions
- `Client:` - for client statements

### Example Format

```
Coach: What would you like to focus on today?
Client: I've been struggling with work-life balance.
Coach: Tell me more about that.
Client: I work late every night and feel guilty about missing time with my family.
Coach: What's important to you about family time?
Client: My kids are growing up fast, and I don't want to miss these years.
```

### Formatting Tips

✅ **Do:**
- Start each turn with "Coach:" or "Client:"
- Include the complete conversation from opening to closing
- Keep the natural flow - don't edit out "mistakes"
- Include all coach responses, even simple acknowledgments

❌ **Don't:**
- Mix multiple speakers into one line
- Skip parts of the conversation
- Edit your responses to make them "better"
- Include timestamps or other metadata

---

## What Gets Analyzed

The AI evaluation covers these key areas:

### 1. ACC-Level Competencies Demonstrated
Identifies which of the 8 ICF competencies you demonstrated:
- Establishes and Maintains Agreements
- Cultivates Trust and Safety
- Maintains Presence
- Listens Actively
- Evokes Awareness
- Facilitates Client Growth
- Embodies a Coaching Mindset

Includes specific examples from your transcript.

### 2. Missed Opportunities to Evoke Awareness
Identifies 3-5 specific moments where:
- A more powerful question could have been asked
- An observation could have deepened awareness
- The conversation stayed surface-level when it could have gone deeper

For each opportunity:
- Your actual statement (quoted)
- What was missed
- Example of what could have been said

### 3. Questions Analysis
Evaluates:
- Open vs. closed questions ratio
- Powerful and evocative vs. leading/directive
- Questions that explore deeply vs. stay surface-level
- Examples of strong questions and areas to improve

### 4. Tone and Attunement
Assesses:
- Matching client's energy and pace
- Moments of deep empathy
- Full presence and engagement
- Opportunities for stronger attunement

### 5. Acknowledgment
Reviews:
- Genuine acknowledgment vs. praise
- Recognition of client's strengths, growth, insights
- Examples of effective acknowledgments
- Missed opportunities

### 6. Observations
Examines:
- What you noticed and shared with the client
- Whether observations were offered tentatively (as gifts, not judgments)
- Examples and missed opportunities

### 7. Clean Language
Evaluates:
- Use of client's own words and metaphors
- Moments of interpretation or assumption
- Examples of good clean language usage
- Areas for improvement

### 8. Overall Strengths
Summary of top 3 strengths demonstrated in the session.

### 9. Priority Development Areas
Top 3 areas for focused development to progress toward PCC level.

### 10. Action Steps
3 specific, actionable practices to implement in your next session.

---

## Sample Transcript

A sample transcript is provided in `sample_coaching_transcript.txt` demonstrating:
- Proper formatting
- Natural conversation flow
- Mix of powerful questions and areas for improvement
- Complete session from opening to closing

Feel free to test the feature with this sample before uploading your own transcripts.

---

## Tips for Best Results

### Recording Your Sessions

1. **Get Permission**: Always obtain written client consent before recording
2. **Quality Matters**: Use a good microphone for clear audio
3. **Transcription Tools**: Use AI transcription services (Otter.ai, Whisper, etc.)
4. **Clean Up**: Remove filler words ("um", "uh") for cleaner analysis

### Preparing Transcripts

1. **Keep It Real**: Don't edit your responses to sound better
2. **Complete Sessions**: Include opening, middle, and closing
3. **Context**: If the session referenced prior sessions, consider adding a brief note at the top
4. **Length**: Ideal length is 20-45 minute sessions (full conversation)

### Using the Feedback

1. **Read Thoroughly**: Don't skip sections - each provides unique insights
2. **Identify Patterns**: Look for recurring themes across multiple analyses
3. **Focus on One Thing**: Pick one action step to practice in your next session
4. **Track Progress**: Analyze multiple sessions over time to see growth
5. **Reflect**: Consider journaling about the feedback before your next session

---

## Comparison: Practice Modes

| Feature | General Practice | Bottom-Lining | Transcript Analysis |
|---------|-----------------|---------------|---------------------|
| **Input** | Single response | Single response | Complete session |
| **Focus** | Any coaching skill | Specific skill (bottom-lining) | Comprehensive review |
| **Feedback** | Competencies + examples | Bottom-lining specific | 10-point analysis |
| **Best For** | Quick practice | Skill refinement | Deep session review |
| **Time** | 2-5 minutes | 2-5 minutes | 10-20 minutes |

---

## Example Use Cases

### Use Case 1: Post-Session Review
**When:** After each client session (same day)
**Goal:** Identify what went well and areas to improve
**Action:** Upload transcript → Review feedback → Journal key insights

### Use Case 2: Skill Development
**When:** Weekly practice
**Goal:** Focus on one competency (e.g., "Evokes Awareness")
**Action:** Analyze multiple sessions → Track progress on that competency

### Use Case 3: ACC Certification Prep
**When:** Preparing for ACC credential application
**Goal:** Ensure you consistently demonstrate all 8 competencies
**Action:** Analyze 5-10 sessions → Identify gaps → Practice deliberately

### Use Case 4: Peer Learning
**When:** Coaching study group
**Goal:** Learn from each other's sessions
**Action:** Share anonymized transcripts → Discuss AI feedback → Role-play improvements

---

## Privacy & Security

### Client Confidentiality

⚠️ **IMPORTANT:** Before uploading any transcript:

1. **Obtain Consent**: Get written permission from your client to use the transcript for your development
2. **Remove Identifying Information**:
   - Replace client name with "Client"
   - Remove company names, specific locations
   - Remove any personally identifiable details
3. **Secure Storage**: Don't store transcripts with client names in file names
4. **Local Processing**: The app sends transcripts to OpenAI API - review their privacy policy

### Data Handling

- Transcripts are NOT stored by the app
- Analysis happens in real-time via OpenAI API
- Downloaded analysis files are saved locally on your machine
- No transcript data is logged or saved to any database

---

## Troubleshooting

### Issue: "Please upload a file or paste transcript text first"

**Cause:** No transcript provided
**Solution:** Either upload a .txt file OR paste text into the text area (not both required)

### Issue: Analysis seems generic or unhelpful

**Cause:** Transcript may be too short, poorly formatted, or missing speaker labels
**Solution:**
- Ensure each line starts with "Coach:" or "Client:"
- Include complete session (not just excerpts)
- Minimum 5-10 exchanges for meaningful analysis

### Issue: Analysis takes too long

**Cause:** Very long transcript (>5000 words)
**Solution:**
- Break into smaller sessions if analyzing training recordings
- Typical 30-45 minute session should process in 20-30 seconds

### Issue: App doesn't recognize speakers

**Cause:** Inconsistent speaker labels
**Solution:**
- Use exact format: "Coach:" or "Client:" (with colon)
- Don't use variations like "Me:", "Them:", "C:", etc.

---

## Integration with Other Modes

You can use all three practice modes together:

**Workflow Example:**

1. **General Practice** (10 min) - Warm up with scenario practice
2. **Bottom-Lining Practice** (10 min) - Focus on concise reflections
3. **Transcript Analysis** (15 min) - Review your recent real session
4. **Practice** - Apply one insight from transcript analysis in your next session
5. **Repeat** - Analyze that next session to track improvement

---

## API Requirements

### OpenAI API Key

The transcript analysis feature requires an OpenAI API key (same as other modes).

**Setup:**
1. Create `.streamlit/secrets.toml` in the PythonAppTester directory
2. Add your key:
   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```

**Cost:**
- Model used: GPT-4o-mini
- Typical cost per analysis: $0.01 - $0.05 (depending on transcript length)
- Average 30-minute session transcript: ~3000 tokens input, ~1500 tokens output

---

## Future Enhancements (Potential)

Ideas for future versions:

- [ ] Support for audio file uploads (with automatic transcription)
- [ ] Multi-session trend analysis (track progress over time)
- [ ] Competency scoring (0-10 for each competency)
- [ ] Compare to PCC-level benchmarks
- [ ] Export to PDF with formatting
- [ ] Highlight specific quotes in transcript that demonstrate/miss competencies
- [ ] Integration with recording tools (Zoom, etc.)
- [ ] Support for group coaching transcripts (multiple coaches/clients)

---

## Support

If you encounter issues or have suggestions:

1. Check the troubleshooting section above
2. Review the sample transcript for correct formatting
3. Verify your OpenAI API key is properly configured
4. Test with the sample transcript first to isolate issues

---

## Summary

The **Transcript Analysis** feature provides:
✅ Comprehensive ACC-level feedback on complete sessions
✅ Specific examples from your actual coaching
✅ Actionable development areas
✅ Track progress over multiple sessions
✅ Prepare for ICF credential applications

**Best Practice:** Analyze one session per week, focus on one action step, track improvement over time.

---

**File Locations:**
- Main App: `/Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester/app_AI_feedback.py`
- Sample Transcript: `/Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester/sample_coaching_transcript.txt`
- This Guide: `/Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester/TRANSCRIPT_ANALYSIS_GUIDE.md`

**Quick Start Command:**
```bash
cd /Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester
source ../../venv/bin/activate
streamlit run app_AI_feedback.py
```

---

*Happy Coaching! 🎯*
