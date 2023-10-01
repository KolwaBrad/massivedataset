import json
import jsonlines

def split_data(file_name):
    with jsonlines.open(file_name) as reader:
        data = list(reader)
    train = data[:int(len(data)*0.8)]
    dev = data[int(len(data)*0.8):int(len(data)*0.9)]
    test = data[int(len(data)*0.9):]
    return train, dev, test

def write_data(file_name, data):
    with jsonlines.open(file_name, mode='w') as writer:
        writer.write_all(data)

def combine_data(en_file, sw_file, de_file):
    en_train, _, _ = split_data(en_file)
    sw_train, _, _ = split_data(sw_file)
    de_train, _, _ = split_data(de_file)

    combined_data = []

    for en, sw, de in zip(en_train, sw_train, de_train):
        combined_data.append({
            'en_id': en['id'],
            'en_utt': en['utt'],
            'sw_id': sw['id'],
            'sw_utt': sw['utt'],
            'de_id': de['id'],
            'de_utt': de['utt']
        })

    with open('combined.json', 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)

# Split the data into train/dev/test and write to separate files
for lang_file in ['en-US.jsonl', 'de-DE.jsonl', 'sw-KE.jsonl']:
    train, dev, test = split_data(lang_file)
    write_data(f'train_{lang_file}', train)
    write_data(f'dev_{lang_file}', dev)
    write_data(f'test_{lang_file}', test)

# Combine the train data from all languages into one file
combine_data('train_en-US.jsonl', 'train_sw-KE.jsonl', 'train_de-DE.jsonl')
