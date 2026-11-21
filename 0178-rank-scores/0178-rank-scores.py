import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result = (
        scores.groupby('score')
        .size()
        .reset_index()[['score']]
        .sort_values('score', ascending=False)
        .reset_index(drop=True)
    )

    result['rank'] = result.index + 1

    return scores.merge(result, on='score')[['score', 'rank']].sort_values(
        'score', ascending=False
    )