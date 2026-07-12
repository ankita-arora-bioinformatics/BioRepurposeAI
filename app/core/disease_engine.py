"""
BioRepurposeAI
Disease Knowledge Engine
Version: 2.0
Author: Ankita Arora
"""

class DiseaseEngine:

    def __init__(self):
        print("Disease Engine Started Successfully")

        self.disease_database = {
            "NAFLD": "Liver Disease",
            "Breast Cancer": "Cancer",
            "Diabetes": "Metabolic Disease",
            "Alzheimer": "Neurological Disease"
        }


    def welcome(self):
        print("=" * 50)
        print("      Welcome to BioRepurposeAI")
        print("=" * 50)

    def get_disease(self):
        disease = input("Enter Disease Name: ")
        return disease

    def show_disease(self, disease):

        if disease in self.disease_database:

            print("\nDisease Found")
            print("Disease :", disease)
            print("Type :", self.disease_database[disease])

        else:

            print("\nDisease Not Found")


    def exit_message(self):
        print("=" * 50)
        print(" Thank you for using BioRepurposeAI")
        print(" See you again!")
        print("=" * 50)


engine = DiseaseEngine()

engine.welcome()

disease = engine.get_disease()

engine.show_disease(disease)

engine.exit_message()
