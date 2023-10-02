import pandas as pd

def split_data(file_name):
    data = pd.read_json(file_name, lines=True)
    train = data[:int(len(data)*0.8)]
    dev = data[int(len(data)*0.8):int(len(data)*0.9)]
    test = data[int(len(data)*0.9):]
    return train, dev, test

def write_data(file_name, data):
    data.to_json(file_name, orient='records', lines=True)

def pretty_print_json(file_path):
    data = pd.read_json(file_path, lines=True)
    print(data.to_json(orient='records', lines=True, indent=4))

def combine_data(en_file, sw_file, de_file):
    en_train, _, _ = split_data(en_file)
    sw_train, _, _ = split_data(sw_file)
    de_train, _, _ = split_data(de_file)

    combined_data = pd.concat([en_train.add_prefix('en_'), sw_train.add_prefix('sw_'), de_train.add_prefix('de_')], axis=1)
    combined_data.to_json('combined.json', orient='records', lines=True)

# Split the data into train/dev/test and write to separate files
for lang_file in ['en-US.jsonl', 'de-DE.jsonl', 'sw-KE.jsonl']:
    train, dev, test = split_data(lang_file)
    write_data(f'train_{lang_file}', train)
    write_data(f'dev_{lang_file}', dev)
    write_data(f'test_{lang_file}', test)

# Combine the train data from all languages into one file
combine_data('train_en-US.jsonl', 'train_sw-KE.jsonl', 'train_de-DE.jsonl')
pretty_print_json('combined.json')
print("Executed Successfully")
