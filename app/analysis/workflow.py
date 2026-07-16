import sys
import os

sys.path.append(os.path.abspath(".."))

from core.disease_engine import DiseaseEngine
from core.gene_engine import GeneEngine
from core.protein_engine import ProteinEngine

print("=" * 60)
print("BioRepurposeAI Disease Workflow")
print("=" * 60)

print("\nStep 1 : Disease Search")
print("Step 2 : Gene Analysis")
print("Step 3 : Protein Analysis")
print("Step 4 : Research Paper Search")

print("\nWorkflow Ready!")

print("\nLoading Engines...\n")

disease_engine = DiseaseEngine()
gene_engine = GeneEngine()
protein_engine = ProteinEngine()

print("All Engines Loaded Successfully!")
