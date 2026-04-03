import streamlit as st

# ================= HEADER =================
st.title("💊 Ibuprofen Chiral Centre Analysis")

st.markdown("""
### 👩‍🎓 Student Details
- **Name:** YGS Deepshikha  
- **Reg No:** RA2511026050065  
- **Class:** AIML-A  
""")

st.markdown("---")

# ================= THEORY =================
st.header("📚 Theory")

st.subheader("🔬 What is Stereochemistry?")
st.write("""
Stereochemistry is the study of the three-dimensional (3D) arrangement of atoms in molecules.
Even if two molecules have the same chemical formula, their spatial arrangement can change 
their properties and behavior.
""")

st.subheader("💊 About the Compound: Ibuprofen")
st.write("""
Ibuprofen is a commonly used non-steroidal anti-inflammatory drug (NSAID).
It helps in reducing pain, fever, and inflammation.
It contains a chiral carbon, which makes it important in stereochemistry.
""")

# 🔥 YOUR UPLOADED IMAGE (IMPORTANT)
st.image("ibuprofen.png", caption="Ibuprofen Molecular Structure", use_column_width=True)

st.subheader("⚛ What is R/S Configuration?")
st.write("""
R/S configuration describes the spatial arrangement of groups around a chiral carbon.
- R: Clockwise
- S: Anticlockwise
""")

st.markdown("---")

# ================= MOLECULE =================
st.header("🧪 Step 1: Molecule Structure (Simplified)")

ibuprofen = {
    "C1": ["C2", "H", "H", "H"],
    "C2": ["C1", "C3", "CH3", "COOH"],
    "C3": ["C2", "Ring", "H", "H"],
    "Ring": ["C3", "C", "C", "C"]
}

st.write(ibuprofen)

# ================= CHIRAL DETECTION =================
st.header("🔍 Step 2: Identify Chiral Centres")

chiral_centres = []

for carbon, groups in ibuprofen.items():
    if len(set(groups)) == 4:
        chiral_centres.append(carbon)

if chiral_centres:
    for c in chiral_centres:
        st.success(f"✔ {c} is a chiral centre")
else:
    st.error("No chiral centres found")

# ================= COUNT =================
st.header("📊 Step 3: Total Chiral Centres")
st.info(f"Total number of chiral centres: {len(chiral_centres)}")

# ================= R/S =================
st.header("⚛ Step 4: R/S Configuration")

def find_RS(groups):
    return "R" if sorted(groups) == groups else "S"

for c in chiral_centres:
    st.write(f"{c} → {find_RS(ibuprofen[c])}")

# ================= CONCLUSION =================
st.header("✅ Conclusion")

st.write(f"""
Ibuprofen has {len(chiral_centres)} chiral centre(s).
The chiral carbon is {chiral_centres} and it shows R configuration.
""")

st.markdown("---")
st.caption("📚 B.Tech AIML Mini Project")
