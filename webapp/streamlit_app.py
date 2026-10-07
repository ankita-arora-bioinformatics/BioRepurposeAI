import streamlit as st
from app.workflow.ai_workflow import AIWorkflow

st.markdown("""
<style>

/* Main Page */
.main {
    background-color: #0f172a;
}

/* Card */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
}

/* Title */
.card-title{
    color:#94a3b8;
    font-size:15px;
    margin-bottom:8px;
}

/* Value */
.card-value{
    color:white;
    font-size:32px;
    font-weight:bold;
}

/* Dashboard Heading */
.dashboard-title{
    font-size:34px;
    font-weight:700;
    color:white;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="BioRepurposeAI",
    page_icon="🧬",
    layout="wide"
)

workflow = AIWorkflow()

st.markdown(
    '<div class="dashboard-title">🧬 BioRepurposeAI</div>',
    unsafe_allow_html=True
)

st.markdown("""
# 🧬 Discover Drug Repurposing Opportunities

Analyze diseases using integrated bioinformatics,
AI-powered target discovery, literature mining,
protein structure analysis, clinical trial data,
and intelligent drug repurposing analytics.

---
""")

disease = st.text_input(
    "🔍 Search Disease",
    placeholder="e.g. NAFLD, Breast Cancer, Alzheimer's Disease, Diabetes"
)

if st.button("🚀 Analyze Disease", use_container_width=True):

    if not disease:
        st.warning("⚠ Please enter a disease name.")
        st.stop()

    with st.spinner("Running AI Workflow..."):
        result = workflow.run_workflow(disease)
    st.success("Workflow Completed!")

    st.markdown("---")
    st.subheader("📊 Platform Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🧬 Diseases", "250+")

    with col2:
        st.metric("🎯 Targets", "5000+")

    with col3:
        st.metric("💊 Drugs", "12000+")

    with col4:
        st.metric("📚 Papers", "40M+")

    st.markdown("---")
    st.subheader("🧬 Disease Analysis")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.markdown("### 🔬 Biological Profile")
        st.write(f"**Disease:** {result['Disease']}")
        st.write(f"**Gene:** {result['Gene']}")
        st.write(f"**Protein:** {result['Protein']}")
        st.write(f"**Target:** {result['CHEMBL_ID']}")

    with result_col2:
        st.markdown("### 🤖 AI Assessment")
        score = result["AI_Score"]

        st.metric("AI Drug Repurposing Score", f"{score}/100")
        st.progress(score / 100)

        if score >= 80:
            st.success("🟢 High-confidence candidate")
        elif score >= 60:
            st.warning("🟡 Moderate-confidence candidate")
        else:
            st.error("🔴 Low-confidence candidate")

    st.markdown("---")
    st.subheader("💊 Drug Discovery Evidence")

    evidence1, evidence2, evidence3, evidence4 = st.columns(4)

    with evidence1:
        st.metric("💊 Drug Candidates", result["Drug_Count"])

    with evidence2:
        st.metric("🧪 Clinical Trials", result["Clinical_Trials"])

    with evidence3:
        st.metric("🧬 PDB Structures", result["PDB_Count"])

    with evidence4:
        st.metric("🔗 BindingDB", result["BindingDB_Status"])

    st.subheader("⚓ Molecular Docking")
    st.info(f"Docking Status: {result['Docking']}")
