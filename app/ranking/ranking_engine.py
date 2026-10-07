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
        # Maximum 20 points
        if drug_count >= 1:
            score += min(drug_count * 10, 20)

        # Clinical trial evidence
        # Maximum 30 points
        if clinical_trials >= 1:
            score += min(clinical_trials * 10, 30)

        # Protein structural evidence
        # Maximum 20 points
        if pdb_count >= 1:
            score += min(pdb_count * 5, 20)

        # BindingDB experimental evidence
        # Maximum 30 points
        if binding_status not in (
            "NA",
            "Not Found",
            "NOT_FOUND",
            None
        ):
            score += 30

        # Final score cannot exceed 100
        score = min(score, 100)

        return score
