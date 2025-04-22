import pandas as pd
import numpy as np
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return (
        activity.loc[
            activity
            .groupby('player_id')['event_date']
            .idxmin(),
            ['player_id' , 'event_date']]
        .rename(columns={'event_date':'first_login'})
        )