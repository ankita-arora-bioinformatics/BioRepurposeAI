class ReportEngine:

    def __init__(self):
        print("Report Engine Loaded Successfully")

    def generate_report(self, result):

        report = f"""
=========================================
 BioRepurposeAI Recommendation Report
=========================================

Disease           : {result["Disease"]}
Gene              : {result["Gene"]}
Protein           : {result["Protein"]}

Target            : {result["CHEMBL_ID"]}

Drug              : {result["Drug_Name"]}
Clinical Trials   : {result["Clinical_Trials"]}
PDB Structures    : {result["PDB_Count"]}

AI Drug Score     : {result["AI_Score"]}/100

=========================================
"""

        return report
