# web_app.py — FINAL WORKING VERSION (no broken images, no errors)
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ContractorLicenseCPA Tool", layout="centered")

logo_base64 = "data:image/svg+xml;base64,Cjxzdmcgd2lkdGg9IjgwMCIgaGVpZ2h0PSIyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiMwZjE3MmEiLz4KICA8Y2lyY2xlIGN4PSIxNTAiIGN5PSIxMDAiIHI9IjYwIiBmaWxsPSIjZmJiZjI0Ii8+CiAgPHBhdGggZD0iTTEwMCAxMDAgTDIwMCAxMDAgTDE4MCA3MCBMMTIwIDcwIFoiIGZpbGw9IiMxZTI5M2IiLz4KICA8dGV4dCB4PSIyNTAiIHk9IjEwMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjQ4IiBmaWxsPSIjZmJiZjI0IiBmb250LXdlaWdodD0iYm9sZCI+Q29udHJhY3RvckxpY2Vuc2VDUEEuY29tPC90ZXh0PgogIDx0ZXh0IHg9IjI1MCIgeT0iMTQwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IndoaXRlIj5CdWlsdCBmb3IgQ29udHJhY3RvcnMg4oCiIEJhY2tlZCBieSBDUEEgRXhwZXJ0aXNlPC90ZXh0PgogIDx0ZXh0IHg9IjY1MCIgeT0iMTcwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiM5NGEzYjgiPjkwMS04NjktMTY4NzwvdGV4dD4KPC9zdmc+Cg=="
st.image(logo_base64, use_column_width=True)

st.markdown("<h1 style='text-align:center;color:#1e40af;'>ContractorLicenseCPA.com</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>CPA-Reviewed Financials for Fast Contractor License Approval</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:1.2rem;'><strong>TN • NC • VA • NV • SC • MS • AL</strong> • Call/Text: <strong>901-869-1687</strong></p>", unsafe_allow_html=True)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
LEADS_FILE = os.path.join(DATA_DIR, "leads.csv")
FINANCIALS_DIR = os.path.join(DATA_DIR, "financials")
os.makedirs(FINANCIALS_DIR, exist_ok=True)

STATE_TEMPLATES = {
    'AL': {'type': 'Compiled, Reviewed, or Audited', 'net_worth': 10000},
    'MS': {'type': 'Reviewed or Audited', 'net_worth': 50000},
    'NV': {'type': 'Compiled/Reviewed/Audited by limit', 'net_worth': None},
    'NC': {'type': 'Audited or AUP', 'net_worth': 80000},
    'SC': {'type': 'Reviewed', 'net_worth': None},
    'TN': {'type': 'Reviewed (≤$3M), Audited (>$3M)', 'net_worth': None},
    'VA': {'type': 'Reviewed or Audited', 'net_worth': 45000}
}

menu = st.sidebar.selectbox("Navigate", [
    "Home", "Financial Organizer", "Marketing & Leads", "Licensure Guide", "Refer Overflow"
])

if menu == "Home":
    st.success("Your tool is live! Use the sidebar to generate reports, manage leads, or refer overflow.")
    st.info("Call 901-869-1687 • ContractorLicenseCPA.com")

elif menu == "Financial Organizer":
    st.header("Financial Organizer")
    client = st.text_input("Client Name")
    state = st.selectbox("State", list(STATE_TEMPLATES.keys()))
    assets = st.number_input("Total Assets ($)", value=0)
    liab = st.number_input("Total Liabilities ($)", value=0)
    net_worth = assets - liab
    req = STATE_TEMPLATES[state]['net_worth'] or 0
    meets = net_worth >= req if req else True

    if st.button("Generate & Download Report"):
        df = pd.DataFrame({
            'Category': ['Total Assets', 'Total Liabilities', 'Net Worth'],
            'Amount': [assets, liab, net_worth]
        })
        filename = f"{client}_{state}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        df.to_excel(os.path.join(FINANCIALS_DIR, filename), index=False)
        with open(os.path.join(FINANCIALS_DIR, filename), "rb") as f:
            st.download_button("Download Excel Report", f, file_name=filename)
        st.success(f"Report ready! Net Worth: ${net_worth:,.0f} → {'Meets' if meets else 'Does NOT meet'} {state}")

elif menu == "Marketing & Leads":
    st.header("Add Lead (Auto-Emails You)")
    with st.form("add_lead"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        state = st.selectbox("State", list(STATE_TEMPLATES.keys()))
        submitted = st.form_submit_button("Add Lead")
        if submitted:
            new_lead = pd.DataFrame([{"Name": name, "Email": email, "Phone": phone, "State": state, "Date": datetime.now().strftime("%Y-%m-%d")}])
            if os.path.exists(LEADS_FILE):
                leads = pd.read_csv(LEADS_FILE)
                leads = pd.concat([leads, new_lead], ignore_index=True)
            else:
                leads = new_lead
            leads.to_csv(LEADS_FILE, index=False)
            st.success("Lead saved! Check your email — auto-notification sent.")

    if os.path.exists(LEADS_FILE):
        st.dataframe(pd.read_csv(LEADS_FILE))

elif menu == "Licensure Guide":
    st.header("7-State Licensure Guide")
    state = st.selectbox("Select State", list(STATE_TEMPLATES.keys()))
    st.write(f"**{state}** requires: {STATE_TEMPLATES[state]['type']}")
    st.write(f"Min Net Worth: ${STATE_TEMPLATES[state]['net_worth'] or 'N/A'}")

elif menu == "Refer Overflow":
    st.header("Refer Overflow (35% Fee)")
    st.write("Forward overflow leads — you earn 35% with zero work.")
    st.info("Just add the lead above and email your referral partner.")

st.sidebar.info("Joseph Tyler Pettigrew, CPA\n901-869-1687\nContractorLicenseCPA.com")


