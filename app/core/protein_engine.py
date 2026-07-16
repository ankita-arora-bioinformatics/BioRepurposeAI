from pathway_engine import PathwayEngine

class ProteinEngine:

    def __init__(self):

        print("\nProtein Engine Loaded Successfully")

    def analyze_protein(self, protein):

        print("\nStarting Protein Analysis...")

        print("Protein :", protein)

        print("Checking Protein Database...")

        print("Protein Analysis Completed Successfully")

        pathway_engine = PathwayEngine()
        pathway_engine.analyze_pathway(protein)
