import json
def get_sample(idx):
    with open("500.json") as filino:
        data = json.load(filino)

    return data[idx]

