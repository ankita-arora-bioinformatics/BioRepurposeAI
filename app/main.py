from app.core.disease_engine import DiseaseEngine
from app.core.gene_engine import GeneEngine
from app.core.protein_engine import ProteinEngine
from app.core.pathway_engine import PathwayEngine

from app.ai.drug_score import DrugScoreEngine
from app.reporting.report_generator import ReportGenerator
from app.workflow.ai_workflow import AIWorkflow


def main():

    print("=" * 60)
    print("        BioRepurposeAI")
    print("=" * 60)

    print("\nLoading Modules...\n")

    disease = input("\nEnter Disease Name : ").upper()
    print("\nSearching Disease...\n")

    disease_engine = DiseaseEngine()
    gene_engine = GeneEngine()
    protein_engine = ProteinEngine()
    pathway_engine = PathwayEngine()

    score_engine = DrugScoreEngine()
    report = ReportGenerator()

    print("\nAll Modules Loaded Successfully!")

    print("\nProject Ready!\n")

    workflow = AIWorkflow()
    workflow.run_workflow(disease)


if __name__ == "__main__":
    main()
