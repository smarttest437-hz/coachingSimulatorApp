# Coaching Practice Simulator (ICF PCC-Level)

**Version:** 2.0 (with Transcript Analysis)
**Last Updated:** February 7, 2026

---

## Overview

An interactive Streamlit application for coaching practice and development, powered by AI feedback based on ICF (International Coaching Federation) standards.

### Three Practice Modes:

1. **General Coaching Practice** - Practice any coaching response with comprehensive ICF feedback
2. **Bottom-Lining Practice** - Develop the skill of distilling client narratives into their essence
3. **Transcript Analysis** ⭐ NEW - Upload complete coaching sessions for comprehensive ACC-level analysis

---

## Features

### Mode 1: General Coaching Practice

- Random coaching scenarios from 5 categories (Career, Leadership, Relationship, Self Improvement, Value System)
- AI-powered feedback on ICF competencies
- ACC and PCC-level example responses
- Immediate, specific, developmental feedback

### Mode 2: Bottom-Lining Practice

- Focused practice on concise reflections (1-2 sentences)
- Word count tracking
- Evaluation of essence capture, client-centeredness, and conciseness
- Examples of ACC vs PCC-level bottom-lining

### Mode 3: Transcript Analysis ⭐ NEW

- **Upload or paste** complete coaching session transcripts
- **Comprehensive 10-point analysis** including:
  - ACC-level competencies demonstrated (with examples)
  - Missed opportunities to evoke awareness
  - Questions quality analysis (open vs closed, powerful vs leading)
  - Tone and attunement assessment
  - Acknowledgment effectiveness
  - Observations shared
  - Clean language usage (client's words vs. coach's interpretation)
  - Overall strengths (top 3)
  - Priority development areas (top 3)
  - Actionable next steps (3 specific practices)
- **Download analysis** as text file for your records
- Perfect for post-session review and ICC credential preparation

---

## Quick Start

### Installation

```bash
# Navigate to project directory
cd /Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester

# Activate virtual environment
source ../../venv/bin/activate

# Install dependencies (if not already installed)
pip install streamlit pandas openai openpyxl
```

### Configuration

Create `.streamlit/secrets.toml` with your OpenAI API key:

```toml
OPENAI_API_KEY = "your-openai-api-key-here"
```

### Run the App

```bash
streamlit run app_AI_feedback.py
```

The app will open in your browser at `http://localhost:8501`

---

## File Structure

```
PythonAppTester/
├── app.py                              # Basic version (no AI)
├── app_AI_feedback.py                  # Full version with AI (recommended)
├── scenario_manager.py                 # Scenario extraction & management
├── Coach_Training_Scenarios_ICF_PCC.xlsx  # Original scenario database
├── custom_scenarios.json               # Your extracted scenarios (auto-created)
├── start_app.sh                        # Easy startup script
├── transcripts/                        # Coaching transcripts folder
│   ├── README.md                       # Transcripts guide
│   ├── coaching_transcript_cleaned.txt # Sample transcript (ready for app)
│   └── sample_coaching_transcript.txt  # Original WEBVTT format
├── TRANSCRIPT_ANALYSIS_GUIDE.md        # Detailed guide for transcript analysis
├── SCENARIO_EXTRACTION_GUIDE.md        # Guide for extracting scenarios
├── OLLAMA_SETUP.md                     # Free local AI setup guide
├── README.md                           # This file
└── .streamlit/
    └── secrets.toml                    # API keys (optional with Ollama)
```

---

## Usage

### For General and Bottom-Lining Practice:

1. Launch the app: `streamlit run app_AI_feedback.py`
2. Select practice mode (General or Bottom-Lining)
3. Choose a category (Career, Leadership, etc.)
4. Read the client scenario
5. Type your coaching response
6. Click "Get Feedback"
7. Review AI feedback and example responses
8. Click "New Scenario" to practice more

### For Transcript Analysis:

1. Launch the app and select "Transcript Analysis" mode
2. **Option A:** Upload a `.txt` file containing your transcript
   - OR -
   **Option B:** Paste your transcript directly into the text area
3. Ensure transcript format: Each line starts with "Coach:" or "Client:"
4. Click "🔍 Analyze Transcript"
5. Review the comprehensive 10-point analysis
6. Download the analysis for your records
7. Apply action steps in your next session

**Example Transcript Format:**
```
Coach: What would you like to focus on today?
Client: I'm struggling with work-life balance.
Coach: Tell me more about that.
Client: I work late every night and feel guilty.
...
```

See `transcripts/coaching_transcript_cleaned.txt` for a complete example.

---

## Documentation

- **TRANSCRIPT_ANALYSIS_GUIDE.md** - Comprehensive guide to using the transcript analysis feature
  - Format requirements
  - What gets analyzed
  - Tips for best results
  - Privacy & security considerations
  - Troubleshooting

---

## AI Model

- **Model:** OpenAI GPT-4o-mini
- **Temperature:** 0.7 (balanced creativity and consistency)
- **Purpose:** Evaluates coaching responses using ICF PCC-level criteria
- **Cost:** Typical analysis costs $0.01-$0.05 per session

---

## ICF Competencies Covered

The app evaluates based on all 8 ICF Core Competencies:

1. **Establishes and Maintains Agreements**
2. **Cultivates Trust and Safety**
3. **Maintains Presence**
4. **Listens Actively**
5. **Evokes Awareness**
6. **Facilitates Client Growth**
7. **Embodies a Coaching Mindset**
8. **Demonstrates Ethical Practice** (implied in all feedback)

---

## Tips for Effective Practice

### General Practice:
- Practice for 15-30 minutes daily
- Focus on one competency at a time
- Try different phrasing for the same scenario
- Reflect on example responses before moving to next scenario

### Bottom-Lining Practice:
- Aim for 20-40 words (concise!)
- Use client's exact language
- Capture essence, not details
- Avoid interpretation or advice

### Transcript Analysis:
- Analyze one session per week
- Pick ONE action step to focus on
- Track progress over multiple analyses
- Review feedback before your next session
- Share insights with a mentor or peer group

---

## Privacy & Confidentiality

⚠️ **Important for Transcript Analysis:**

Before uploading any coaching transcript:

1. **Obtain written client consent** for using the transcript in your development
2. **Remove all identifying information**:
   - Names (use "Client" instead)
   - Company names
   - Specific locations or identifying details
3. **Review OpenAI's privacy policy** - transcripts are sent to their API for analysis
4. **Store transcripts securely** - don't include client names in filenames

The app does NOT store transcripts - analysis happens in real-time only.

---

## Development History

**Version 1.0** (Initial Release)
- General Coaching Practice mode
- Basic rule-based feedback
- Excel scenario database

**Version 1.5** (AI Integration)
- OpenAI GPT-4o-mini integration
- PCC-level AI feedback
- Bottom-Lining Practice mode added
- ACC and PCC example responses

**Version 2.0** (Current) ⭐
- **NEW:** Transcript Analysis mode
- Comprehensive 10-point session analysis
- File upload and paste options
- Downloadable feedback reports
- Sample transcript included
- Detailed documentation

---

## Requirements

### Python Packages:
```
streamlit>=1.30.0
pandas>=2.0.0
openai>=1.0.0
openpyxl>=3.1.0
```

### Files Required:
- `Coach_Training_Scenarios_ICF_PCC.xlsx` (for General/Bottom-Lining modes)
- `.streamlit/secrets.toml` (with OpenAI API key)

---

## Troubleshooting

### App won't start
- Check that virtual environment is activated
- Verify all dependencies are installed: `pip list`
- Ensure you're in the correct directory

### "Missing OpenAI API key" error
- Create `.streamlit/secrets.toml` file
- Add `OPENAI_API_KEY = "your-key"`
- Restart the app

### "File not found" error
- Ensure `Coach_Training_Scenarios_ICF_PCC.xlsx` is in the same directory as `app_AI_feedback.py`
- Check file name spelling (case-sensitive)

### Transcript analysis not working
- Verify transcript format (lines start with "Coach:" or "Client:")
- Check transcript length (minimum 5-10 exchanges)
- See TRANSCRIPT_ANALYSIS_GUIDE.md for detailed troubleshooting

---

## Future Enhancements

Potential features for future versions:

- [ ] Audio file upload with automatic transcription
- [ ] Multi-session trend analysis
- [ ] Competency scoring dashboard
- [ ] Export to PDF with formatting
- [ ] Integration with Zoom/recording tools
- [ ] Group coaching support (multiple coaches/clients)
- [ ] Custom scenario creation
- [ ] Progress tracking over time

---

## Support

For issues or questions:
1. Check TRANSCRIPT_ANALYSIS_GUIDE.md for detailed guidance
2. Test with sample_coaching_transcript.txt to isolate issues
3. Verify API key configuration

---

## Related Documentation

- **Main Codebase Documentation:** `/Users/hattie.zhang/Documents/claudecode/CLAUDE.md`
- **Transcript Analysis Guide:** `TRANSCRIPT_ANALYSIS_GUIDE.md`
- **Sample Transcript:** `sample_coaching_transcript.txt`

---

## Command Reference

```bash
# Navigate to project
cd /Users/hattie.zhang/Documents/claudecode/projects/PythonAppTester

# Activate virtual environment
source ../../venv/bin/activate

# Run app
streamlit run app_AI_feedback.py

# Run basic version (no AI)
streamlit run app.py
```

---

**Happy Coaching! 🎯**

*Powered by OpenAI GPT-4o-mini + ICF Coaching Framework*
