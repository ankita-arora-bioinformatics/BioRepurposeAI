from app.core.disease_engine import DiseaseEngine
from app.core.gene_engine import GeneEngine
from app.core.protein_engine import ProteinEngine
from app.core.pathway_engine import PathwayEngine

from app.ai.drug_score import DrugScoreEngine
from app.literature.pubmed_engine import PubMedEngine
from app.target.target_engine import TargetEngine

class AIWorkflow:

    def __init__(self):
        print("AI Workflow Loaded Successfully")

        self.disease = DiseaseEngine()
        self.gene = GeneEngine()
        self.protein = ProteinEngine()
        self.pathway = PathwayEngine()

        self.score = DrugScoreEngine()
        self.pubmed = PubMedEngine()
        self.target = TargetEngine()

    def run_workflow(self, disease_name):

        print("=" * 60)
        print("Starting AI Drug Repurposing Workflow")
        print("=" * 60)

        print(f"\nDisease : {disease_name}")

        # Disease Search
        disease = self.disease.search_disease(disease_name)

        if "error" in disease:
            return {"error": "Disease not found"}

        print("\nDisease Found")

        gene = disease["gene"]

        print("Biomarker Gene :", gene)

        # Gene Search
        gene_info = self.gene.search_gene(gene)

        if "error" in gene_info:
            return {"error": "Gene not found"}

        protein = gene_info["protein"]

        print("Protein :", protein)

        # Protein Analysis
        self.protein.analyze_protein(protein)

        # Pathway Analysis
        self.pathway.analyze_pathway(protein)

        # PubMed Search
        papers = self.pubmed.search_papers(gene)

        print("\nPubMed Papers Found :", len(papers))

        if len(papers) > 0:

            print("\nLatest Paper Details\n")

            details = self.pubmed.get_paper_details(papers[0])

            print("Title   :", details["title"])
            print("Journal :", details["journal"])
            print("Date    :", details["pubdate"])

        # Target Resolver

        target = self.target.search_target(protein)

        if "error" in target:
            print("\nTarget Not Found")

        else:
            print("\nTarget Found")
            print("CHEMBL ID :", target["chembl_id"])
            print("Target Name :", target["target_name"])

        return {
            "Disease": disease_name,
            "Gene": gene,
            "Protein": protein,
            "CHEMBL_ID": target.get("chembl_id", "NA")
        }

