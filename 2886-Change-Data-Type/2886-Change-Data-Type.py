import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"]=students["grade"].astype({"grade":int})
    return students