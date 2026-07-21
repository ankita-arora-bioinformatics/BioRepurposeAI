from .gene_engine import GeneEngine
import json
from pathlib import Path

"""
BioRepurposeAI
Disease Knowledge Engine
Version: 2.0
Author: Ankita Arora
"""

class DiseaseEngine:

    def __init__(self):
        print("Disease Engine Started Successfully")

        try:
            base_dir = Path(__file__).resolve().parents[2]
            database_file = base_dir / "database" / "diseases.json"

            with open(database_file, "r") as file:
                self.disease_database = json.load(file)
            print("Disease Database Loaded Successfully")

        except FileNotFoundError:
            print("Error: diseases.json file not found.")
            self.disease_database = {}

    def welcome(self):
        print("=" * 50)
        print("      Welcome to BioRepurposeAI")
        print("=" * 50)

    def get_disease(self):
        disease = input("Enter Disease Name: ")
        return disease

    def show_disease(self, disease):

        if disease in self.disease_database:

            info = self.disease_database[disease]

            print("\nDisease Found")
            print("Disease :", disease)
            print("Type :", info["type"])
            print("Gene :", info["gene"])
            print("Organ :", info["organ"])
            print("Description :", info["description"])

            gene_engine = GeneEngine()
            gene_engine.analyze_gene(info["gene"])

        else:
            print("\nDisease Not Found")


    def search_disease(self, disease):

        if disease in self.disease_database:
            return self.disease_database[disease]

        return {"error": "Disease not found"}

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
