import json
def get_sample(dataset, idx):
    with open(dataset) as filino:
        data = json.load(filino)

    return data[idx]

