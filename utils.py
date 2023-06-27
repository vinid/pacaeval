import json
def get_sample(idx):
    with open("2500.json") as filino:
        data = json.load(filino)

    return data[idx]

