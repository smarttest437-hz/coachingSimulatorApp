#!/bin/bash

# Activate virtual environment
source ../../venv/bin/activate

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "⚠️  Ollama is not running. Starting Ollama..."
    brew services start ollama
    sleep 3
fi

# Start Streamlit
echo "🚀 Starting Coaching Practice Simulator..."
echo "📍 The app will open at: http://localhost:8502"
echo ""
echo "✅ Select 'Ollama (Free, Local)' in the sidebar"
echo "✅ Choose model: llama3.1:8b"
echo ""
streamlit run app_AI_feedback.py --server.port 8502
