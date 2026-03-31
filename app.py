import streamlit as st

st.title("Ibuprofen Chiral Centre Finder")

ibuprofen = {
    "C1": ["C2", "H", "H", "H"],
    "C2": ["C1", "C3", "CH3", "COOH"],
    "C3": ["C2", "Ring", "H", "H"],
    "Ring": ["C3", "C", "C", "C"]
}

chiral_centres = []

for carbon, groups in ibuprofen.items():
    if len(set(groups)) == 4:
        chiral_centres.append(carbon)

st.write("Chiral Centres:", chiral_centres)
st.write("Total:", len(chiral_centres))

def find_RS(groups):
    return "R" if sorted(groups) == groups else "S"

for c in chiral_centres:
    st.write(f"{c} → {find_RS(ibuprofen[c])}")
