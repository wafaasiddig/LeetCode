import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    players_size =  list(players.shape)
    return players_size