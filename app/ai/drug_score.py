class DrugScoreEngine:

    def __init__(self):
        print("Drug Score Engine Loaded Successfully")

    def calculate_score(self,
                        ic50,
                        papers,
                        pathway_match,
                        disease_match,
                        clinical_phase):

        score = 0

        # IC50 Score
        if ic50 <= 10:
            score += 50
        elif ic50 <= 100:
            score += 40
        elif ic50 <= 500:
            score += 30
        elif ic50 <= 1000:
            score += 20
        else:
            score += 10

        # Literature Score
        if papers >= 20:
            score += 20
        elif papers >= 10:
            score += 15
        elif papers >= 5:
            score += 10
        else:
            score += 5

        # Pathway Score
        if pathway_match:
            score += 15

        # Disease Score
        if disease_match:
            score += 10

        # Clinical Phase
        score += clinical_phase

        return score
