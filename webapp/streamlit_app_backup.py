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

st.subheader("AI-Powered Drug Repurposing Platform")

disease = st.text_input("Enter Disease Name", "NAFLD")

if st.button("Run AI Workflow"):
    with st.spinner("Running AI Workflow..."):
        result = workflow.run_workflow(disease)

    st.success("Workflow Completed!")

    st.subheader("Results")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("🦠 Disease", result["Disease"])
        st.metric("🧬 Gene", result["Gene"])
        st.metric("🧪 Protein", result["Protein"])
        st.metric("🎯 Target", result["CHEMBL_ID"])
        st.metric("⭐ AI Score", f'{result["AI_Score"]}/100')
        score = result["AI_Score"]
        st.progress(score / 100)
        st.caption(f"Confidence Score : {score}%")

    with col2:
        st.metric("💊 Drugs", result["Drug_Count"])
        st.metric("📚 Clinical Trials", result["Clinical_Trials"])
        st.metric("🧬 PDB Structures", result["PDB_Count"])
        st.metric("🔗 BindingDB", result["BindingDB_Status"])
        st.metric("⚓ Docking", result["Docking"])
        st.divider()
        st.subheader("AI Recommendation")

        if score >= 80:
            st.success("🟢 Excellent Drug Candidate")

        elif score >= 60:
            st.warning("🟡 Moderate Drug Candidate")

        else:
            st.error("🔴 Low Confidence Candidate")
