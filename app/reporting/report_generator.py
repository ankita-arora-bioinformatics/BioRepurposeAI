class ReportGenerator:

    def __init__(self):
        print("Report Generator Loaded Successfully")

    def generate_report(self,
                        disease,
                        gene,
                        protein,
                        pathway,
                        drug,
                        score):

        print("\n" + "=" * 60)
        print("BioRepurposeAI Final Report")
        print("=" * 60)

        print("Disease :", disease)
        print("Gene :", gene)
        print("Protein :", protein)
        print("Pathway :", pathway)
        print("Drug :", drug)
        print("AI Drug Score :", score, "/100")

        print("=" * 60)

        if score >= 90:
            print("⭐⭐⭐⭐⭐ Excellent Candidate")

        elif score >= 75:
            print("⭐⭐⭐⭐ Very Strong Candidate")

        elif score >= 60:
            print("⭐⭐⭐ Moderate Candidate")

        else:
            print("⭐⭐ Weak Candidate")
