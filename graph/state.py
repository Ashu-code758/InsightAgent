from typing import TypedDict
import pandas as pd

class AgentState(TypedDict):
    url: str
    dataframe: pd.DataFrame
    analysis: str
    pdf: str