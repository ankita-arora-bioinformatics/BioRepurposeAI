from app.core.gene_engine import GeneEngine
from fastapi import FastAPI

app = FastAPI(
    title="BioRepurposeAI",
    description="AI-powered Drug Repurposing Platform",
    version="1.0"
)

gene_engine = GeneEngine()

@app.get("/")
def home():
    return {
        "message": "Welcome to BioRepurposeAI"
    }


@app.get("/disease/{disease}")
def disease_search(disease: str):
    return {
        "Disease": disease,
        "Status": "Found"
    }


@app.get("/gene/{gene}")
def gene_search(gene: str):

    result = gene_engine.search_gene(gene)

    return result


@app.get("/protein/{protein}")
def protein_search(protein: str):
    return {
        "Protein": protein,
        "Database": "UniProt"
    }


@app.get("/pathway/{pathway}")
def pathway_search(pathway: str):
    return {
        "Pathway": pathway,
        "Database": "KEGG"
    }


@app.get("/papers/{gene}")
def papers(gene: str):
    return {
        "Gene": gene,
        "Database": "PubMed"
    }
