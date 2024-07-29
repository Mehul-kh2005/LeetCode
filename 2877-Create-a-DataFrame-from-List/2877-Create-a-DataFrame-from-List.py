import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    result=pd.DataFrame(student_data,columns=["student_id" ,"age"])
    return result