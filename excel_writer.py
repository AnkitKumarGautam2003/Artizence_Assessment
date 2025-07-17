import pandas as pd

def save_to_excel_multi(results_dict, filename):
    with pd.ExcelWriter(filename) as writer:
        for sheet_name, data in results_dict.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
