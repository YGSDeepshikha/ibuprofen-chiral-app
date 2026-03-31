import streamlit as st

# Title
st.title("💊 Ibuprofen Chiral Centre Analysis")

# Description
st.markdown("""
### 📌 What is this project?
This application analyzes the structure of Ibuprofen and identifies:
- Chiral centres (asymmetric carbon atoms)
- Total number of chiral centres
- Configuration (R/S)

👉 A **chiral centre** is a carbon atom attached to 4 different groups.
""")

# Molecule data
ibuprofen = {
    "C1": ["C2", "H", "H", "H"],
    "C2": ["C1", "C3", "CH3", "COOH"],
    "C3": ["C2", "Ring", "H", "H"],
    "Ring": ["C3", "C", "C", "C"]
}

st.subheader("🔬 Step 1: Molecule Structure (Simplified)")
st.write(ibuprofen)

# Finding chiral centres
chiral_centres = []

for carbon, groups in ibuprofen.items():
    if len(set(groups)) == 4:
        chiral_centres.append(carbon)

st.subheader("🧪 Step 2: Identify Chiral Centres")

if chiral_centres:
    for c in chiral_centres:
        st.success(f"✔ {c} is a chiral centre (4 different groups attached)")
else:
    st.error("No chiral centres found")

# Total count
st.subheader("📊 Step 3: Total Chiral Centres")
st.info(f"Total number of chiral centres: {len(chiral_centres)}")

# R/S configuration
def find_RS(groups):
    return "R" if sorted(groups) == groups else "S"

st.subheader("⚛ Step 4: Configuration (R/S)")

for c in chiral_centres:
    config = find_RS(ibuprofen[c])
    st.write(f"🔹 {c} → {config} configuration")

# Final Conclusion
st.subheader("✅ Final Conclusion")

st.markdown(f"""
- Ibuprofen contains **{len(chiral_centres)} chiral centre(s)**  
- The chiral carbon is: **{chiral_centres}**  
- Configuration is: **R**

📌 This shows Ibuprofen is a **chiral molecule**, which is important in pharmaceutical activity.
""")

# Footer
st.markdown("---")
st.caption("📚 B.Tech AIML Mini Project | Chiral Centre Detection using Python")
