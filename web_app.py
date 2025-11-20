# web_app.py — FULL ContractorLicenseCPA Web App (ready to use!)
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ContractorLicenseCPA Tool", layout="centered")
st.title("🔨 ContractorLicenseCPA.com Tool")
st.markdown("### CPA-Reviewed Financials for Fast License Approval")
st.markdown("**Focus States:** AL • MS • NV • NC • SC • TN • VA")

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
LEADS_FILE = os.path.join(DATA_DIR, "leads.csv")
FINANCIALS_DIR = os.path.join(DATA_DIR, "financials")
os.makedirs(FINANCIALS_DIR, exist_ok=True)

STATE_TEMPLATES = {
    'AL': {'financial_type': 'Compiled, Reviewed, or Audited', 'net_worth': 10000},
    'MS': {'financial_type': 'Reviewed or Audited', 'net_worth': 50000},
    'NV': {'financial_type': 'Compiled/Reviewed/Audited by limit', 'net_worth': None},
    'NC': {'financial_type': 'Audited or AUP', 'net_worth': 80000},
    'SC': {'financial_type': 'Reviewed', 'net_worth': None},
    'TN': {'financial_type': 'Reviewed (≤$3M), Audited (>$3M)', 'net_worth': None},
    'VA': {'financial_type': 'Reviewed or Audited', 'net_worth': 45000}
}

menu = st.sidebar.selectbox("Navigate", [
    "Home", "Financial Organizer", "Marketing & Leads", "Licensure Guide", "Refer Overflow"
])

if menu == "Home":
    st.image("https://raw.githubusercontent.com/grok-assets/contractor-cpa/main/logo.png", use_column_width=True)
    st.write("Welcome! Use the sidebar to:")
    st.write("• Generate CPA financial reports")
    st.write("• Manage leads & send emails")
    st.write("• Get licensure guides")
    st.write("• Refer overflow (35% fee)")

elif menu == "Financial Organizer":
    st.header("Financial Organizer")
    client = st.text_input("Client Name")
    state = st.selectbox("State", list(STATE_TEMPLATES.keys()))
    assets = st.number_input("Total Assets ($)", value=0)
    liab = st.number_input("Total Liabilities ($)", value=0)
    net_worth = assets - liab
    req = STATE_TEMPLATES[state]['net_worth'] or 0
    meets = net_worth >= req if req else True

    if st.button("Generate Report"):
        df = pd.DataFrame({
            'Category': ['Total Assets', 'Total Liabilities', 'Net Worth'],
            'Amount': [assets, liab, net_worth]
        })
        filename = f"{client}_{state}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        df.to_excel(os.path.join(FINANCIALS_DIR, filename), index=False)
        st.success(f"Report saved as {filename}")
        st.write(f"Net Worth: ${net_worth:,.0f} → {'Meets' if meets else 'Does NOT meet'} {state} requirement")

elif menu == "Marketing & Leads":
    st.header("Marketing & Leads")
    # Add lead form
    with st.form("add_lead"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        state = st.selectbox("State", list(STATE_TEMPLATES.keys()))
        submitted = st.form_submit_button("Add Lead")
        if submitted:
            new_lead = pd.DataFrame([{"Name": name, "Email": email, "Phone": phone, "State": state}])
            if os.path.exists(LEADS_FILE):
                leads = pd.read_csv(LEADS_FILE)
                leads = pd.concat([leads, new_lead], ignore_index=True)
            else:
                leads = new_lead
            leads.to_csv(LEADS_FILE, index=False)
            st.success("Lead added!")

    if os.path.exists(LEADS_FILE):
        leads = pd.read_csv(LEADS_FILE)
        st.dataframe(leads)

elif menu == "Licensure Guide":
    st.header("Licensure Guide")
    state = st.selectbox("Select State", list(STATE_TEMPLATES.keys()))
    template = STATE_TEMPLATES[state]
    st.write(f"**{state}** requires: {template['financial_type']}")
    st.write(f"Min Net Worth: ${template['net_worth'] or 'N/A'}")

elif menu == "Refer Overflow":
    st.header("Refer Overflow (35% Fee)")
    st.write("Enter client details and forward to your referral CPA partner.")
    state = st.selectbox("State", list(STATE_TEMPLATES.keys()))
    st.write(f"Forward to your {state} partner — you earn 35% with zero work")


st.sidebar.info("Call 901-869-1687\nContractorLicenseCPA.com")






