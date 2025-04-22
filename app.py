import streamlit as st
import json
from agents.extractor import extract_info
from agents.persona_builder import build_personas
from agents.debater import simulate_debate
from agents.summarizer import summarize_and_analyze
from utils.visualizer import generate_visuals

st.set_page_config(page_title="DecisionForge", layout="wide")
st.title("🧠 DecisionForge MVP")
st.markdown("Simulate complex decisions with agentic AI.")

if "step" not in st.session_state:
    st.session_state.step = 1
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Step 1: Input
if st.session_state.step == 1:
    st.subheader("Step 1: Describe your decision dilemma")
    dilemma = st.text_area("Describe your decision dilemma:")
    process = st.text_area("What do you know about the decision-making process?")
    st.markdown("**💡 Example:**\n- Process: Propose > Review > Vote\n- Stakeholders: CTO, CFO, Legal")
    if st.button("✅ Extract Problem & Process"):
        st.session_state.extracted = extract_info(dilemma, process)
        st.session_state.step = 2
        st.experimental_rerun()

# Step 2: Extraction Result
elif st.session_state.step == 2:
    st.subheader("🤖 Here's what the AI understood")
    st.json(st.session_state.extracted)
    if st.button("Generate Stakeholder Personas"):
        st.session_state.personas = build_personas(st.session_state.extracted.get("stakeholders", []))
        st.session_state.step = 3
        st.experimental_rerun()

# Step 3: Persona Display
elif st.session_state.step == 3:
    st.subheader("🎭 Stakeholder Personas")
    for persona in st.session_state.personas:
        st.markdown(f"**{persona['name']}**: Goals: {persona['goals']}, Biases: {persona['biases']}")
    if st.button("Run AI Discussion"):
        st.session_state.transcript = simulate_debate(st.session_state.personas, st.session_state.chat_log)
        st.session_state.step = 4
        st.experimental_rerun()

# Step 4: Display Debate
elif st.session_state.step == 4:
    st.subheader("💬 Agentic AI Discussion")
    for line in st.session_state.transcript:
        st.markdown(f"**{line['agent']}**: {line['message']}")
    if st.button("Summarize & Visualize"):
        st.session_state.summary, st.session_state.keywords = summarize_and_analyze(st.session_state.transcript)
        generate_visuals(st.session_state.keywords)
        st.session_state.step = 5
        st.experimental_rerun()

# Step 5: Summary and Download
elif st.session_state.step == 5:
    st.subheader("📝 Summary")
    st.markdown(st.session_state.summary)
    st.image("visualization.png", caption="Debate Visualization")
    st.download_button("Download Debate Log", data=json.dumps(st.session_state.transcript), file_name="debate_log.json")
    st.download_button("Download Summary", data=st.session_state.summary, file_name="summary.txt")