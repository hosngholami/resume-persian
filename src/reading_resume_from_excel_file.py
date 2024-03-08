import pandas as pd

def read_file (file_excel):

    resume_data = pd.read_excel(file_excel)
    
    return resume_data