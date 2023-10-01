import os
import pandas as pd
import sys



# Load the JSONL data
data_folder = '1.1/data'

pivotLanguage = os.path.join(data_folder, 'en-US.jsonl')

english = pd.read_json(pivotLanguage, lines=True)
english = english[['id', 'utt', 'annot_utt']]

def generate_excel(language):
    if language == 'en-US.jsonl':
        return
    try:
        json_path = os.path.join(data_folder, language)
        df = pd.read_json(json_path, lines=True)
        df = df[['id', 'utt', 'annot_utt']]
        mergedPdf = pd.merge(english, df, on='id')
        output_folder = '1.1/excel'
        os.makedirs(output_folder, exist_ok=True)
        output_file_path = os.path.join(output_folder, f'en-{language[:2]}.xlsx')
        mergedPdf.to_excel(output_file_path, index=True)
        print(f"Finished processed {language}")
    
    except Exception as e:
        print(f"Error in file {language}: {e}")

if __name__ == '__main__':
    language = sys.argv[1]
    generate_excel(language)

