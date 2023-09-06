import streamlit as st
from utils import get_sample
import string
import random
import csv

reference_dataset = "llama-7b-hf-saferpaca-Instructions-2000.json"
key_in_dataset = reference_dataset.replace(".json", "")

your_name = "Fede"

with st.sidebar:
    st.write("Annotation")

# using random.choices()
# generating random strings
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=18))
if 'key' not in st.session_state:
    st.session_state['key'] = f"{reference_dataset}_{your_name}_{key}"

if 'number' not in st.session_state:
    st.session_state['number'] = 0

data = get_sample(reference_dataset, st.session_state['number'])

options = [(reference_dataset, data[key_in_dataset]), ("alpaca", data["alpaca"])]

random.shuffle(options)

question = data["question"]
typ = data["type"]

st.write(f"# Welcome!")
st.write(f"## Annotation Guidelines")
st.write("* You are presented with two columns that contains answers from two different models. Each column contains a text. Your task is to decide which column contains the better answer to the question.")
st.write("* You can also decide that both columns are equally good or equally bad.")
st.write("* Columns are randomly shuffled.")

percentage = round(st.session_state['number']/100*100, 2)
st.write(f"## You are at {st.session_state['number']} out of 100. That is {percentage}% of the dataset.")


st.write(f"# Question:\n### {question}")

col1, col2 = st.columns(2)

with col1:
    st.write("#### Column A")
    st.write(options[0][1])
with col2:
    st.write("#### Column B")
    st.write(options[1][1])


def on_clicker(internal_state):

    def on_click():
        with open(f"{st.session_state['key']}.csv", "a") as f:
            fcsv = csv.writer(f, delimiter=',')
            fcsv.writerow([question, options[0][0], options[0][1], options[1][0], options[1][1], internal_state, typ])
            st.session_state['number'] = st.session_state['number'] + 1

    return on_click


st.write("#### Evaluation: Which column contains the best answer?")

col1, col2, col3, col4 = st.columns([1,1,1,1])


with col2:
    st.button("Column A", on_click=on_clicker(options[0][0]))
with col3:
    st.button("Column B", on_click=on_clicker(options[1][0]))
with col1:
    st.button("Equally Bad", on_click=on_clicker("Equally Bad"))
with col4:
    st.button("Equally Good", on_click=on_clicker("Equally Good"))


