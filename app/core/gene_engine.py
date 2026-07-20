from .protein_engine import ProteinEngine
import json
from pathlib import Path


class GeneEngine:

    def __init__(self):

        print("Gene Engine Loaded Successfully")

        try:
            base_dir = Path(__file__).resolve().parents[2]
            database_file = base_dir / "database" / "genes.json"

            with open(database_file, "r") as file:
                self.gene_database = json.load(file)

        except Exception as e:
            print("DEBUG ERROR:", e)
            self.gene_database = {}

    def analyze_gene(self, gene):

        print("\nStarting Gene Analysis...")

        if gene in self.gene_database:

            info = self.gene_database[gene]

            print("Biomarker Gene :", gene)
            print("Full Name :", info["fullname"])
            print("Protein :", info["protein"])
            print("Chromosome :", info["chromosome"])
            print("Organism :", info["organism"])
            print("Function :", info["function"])

            protein_engine = ProteinEngine()
            protein_engine.analyze_protein(info["protein"])

        else:

            print("Gene Not Found")

