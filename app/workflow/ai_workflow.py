from app.core.disease_engine import DiseaseEngine
from app.core.gene_engine import GeneEngine
from app.core.protein_engine import ProteinEngine
from app.core.pathway_engine import PathwayEngine

from app.ai.drug_score import DrugScoreEngine
from app.literature.pubmed_engine import PubMedEngine
from app.target.target_engine import TargetEngine
from app.drug_discovery.drug_engine import DrugEngine
from app.drug_details.drug_details_engine import DrugDetailsEngine
from app.clinical_trials.clinical_trials_engine import ClinicalTrialsEngine
from app.pdb.pdb_engine import PDBEngine
from app.bindingdb.bindingdb_engine import BindingDBEngine
from app.docking.docking_engine import DockingEngine
from app.ranking.ranking_engine import RankingEngine
from app.report.report_engine import ReportEngine

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
        self.drug = DrugEngine()
        self.drug_details = DrugDetailsEngine()
        self.clinical = ClinicalTrialsEngine()
        self.pdb = PDBEngine()
        self.binding = BindingDBEngine()
        self.docking = DockingEngine()
        self.ranking = RankingEngine()
        self.report = ReportEngine()

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

        # Drug Discovery

        drugs = self.drug.search_drugs(target["chembl_id"])

        print("\nDrugs Found :", len(drugs))

        if len(drugs) > 0:

            print("\nFirst Drug Information\n")

            first = drugs[0]

            print("Drug :", first.get("molecule_chembl_id", "NA"))
            print("Action :", first.get("action_type", "NA"))

        # Drug Details
        if len(drugs) > 0:
            details = self.drug_details.get_drug_details(drugs[0]["molecule_chembl_id"])

            print("\nDrug Details")
            print("Drug Name :", details["name"])
            print("Drug Type :", details["type"])
            print("Max Phase :", details["max_phase"])

        # Clinical Trials
        if len(drugs) > 0:

            trials = self.clinical.search_trials(details["name"])

            print("\nClinical Trials Found :", len(trials))

            if len(trials) > 0:
                print("\nFirst Clinical Trial\n")

                trial = trials[0]

                print("NCT ID :", trial["NCTId"][0] if trial["NCTId"] else "NA")
                print("Title  :", trial["BriefTitle"][0] if trial["BriefTitle"] else "NA")
                print("Phase  :", trial["Phase"][0] if trial["Phase"] else "NA")
                print("Status :", trial["OverallStatus"][0] if trial["OverallStatus"] else "NA")

        # PDB Structure

        pdbs = self.pdb.search_pdb(protein)

        print("\nPDB Structures Found :", len(pdbs))

        if len(pdbs) > 0:

            first = pdbs[0]

            print("\nFirst PDB Structure\n")
            print("PDB ID :", first["identifier"])

        # BindingDB

        if len(drugs) > 0:

            binding = self.binding.search_binding(details["name"])

            print("\nBindingDB Status :", binding["status"])
            print("Response Size :", binding["response_size"])

        else:

            binding = {
                "status": "NA",
                "response_size": 0
            }

        # Docking

        if len(pdbs) > 0 and len(drugs) > 0:

            docking = self.docking.prepare_docking(
                first["identifier"],
                details["name"]
            )

            print("\nDocking Status :", docking["status"])

        else:

            docking = {
                "status": "NA"
            }

        # AI Ranking

        score = self.ranking.calculate_score(
            len(drugs),
            len(trials) if len(drugs) > 0 else 0,
            len(pdbs),
            binding["status"]
        )

        print("\nAI Drug Score :", score)

        result = {
            "Disease": disease_name,
            "Gene": gene,
            "Protein": protein,
            "CHEMBL_ID": target.get("chembl_id", "NA"),
            "Drug_Count": len(drugs),
            "Drug_Name": details.get("name", "NA"),
            "Clinical_Trials": len(trials) if len(drugs) > 0 else 0,
            "PDB_Count": len(pdbs),
            "BindingDB_Status": binding["status"],
            "BindingDB_Size": binding["response_size"],
            "Docking": docking["status"],
            "AI_Score": score
        }

        report = self.report.generate_report(result)

        print(report)

        return result

