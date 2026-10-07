class RankingEngine:

    def __init__(self):
        print("Ranking Engine Loaded Successfully")

    def calculate_score(
        self,
        drug_count,
        clinical_trials,
        pdb_count,
        binding_status
    ):

        score = 0

        # Drug availability
        score += drug_count * 20

        # Clinical trials
        score += clinical_trials * 15

        # Protein structures
        score += pdb_count * 10

        # BindingDB evidence
        if binding_status not in ("NA", "Not Found", "NOT_FOUND", None):
            score += 25

        if score > 100:
            score = 100

        return score
