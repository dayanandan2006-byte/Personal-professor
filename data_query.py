import pandas as pd
import os

def get_student_score(student_name):
    # Safe path resolution
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, 'data', 'scores.csv')
    
    try:
        df = pd.read_csv(csv_path)
        record = df[df['student_name'] == student_name]
        if not record.empty:
            return record.iloc[0]['score']
    except Exception:
        pass
    return "No assessment score found."
