import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return (
        actor_director
        .groupby(['actor_id', 'director_id'])
        .filter(lambda x: len(x)>= 3)
        .drop_duplicates(['actor_id', 'director_id'])
        [['actor_id', 'director_id']]
    )
    