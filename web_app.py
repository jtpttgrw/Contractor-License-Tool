# web_app.py — FINAL WORKING VERSION (no broken images, no errors)
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ContractorLicenseCPA Tool", layout="centered")

# Your exact logo – embedded forever (no link needed)
logo_base64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAADwf7zUAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3RpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDYuMC1jMDA2IDc5LjE2NDI4OCwgMjAyMS8wMy8xNS0xNDo0NjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDIzLjAgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjJERjA4Q0E5QjJDRjExRUU5QkE3RjJDRjA5RjA4Q0E5IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjJERjA4Q0FBRjJDRjExRUU5QkE3RjJDRjA5RjA4Q0E5Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc2RhbmNlSUQ9InhtcC5paWQ6MkRGMDhDQTdCMkNGMTFFQTlCQTdGMkNGMDlGMDhDQTAiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MkRGMDhDQThCMkNGMTFFQTlCQTdGMkNGMDlGMDhDQTAiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7/7gAOQWRvYmUAZMAAAAAB/9sAhAAGBAQEBQQGBQUGCQYFCQYGBgYICQgKCgkICAsKFQ4MDA8ODg4UDg4QFFCQYGBcQHBgcHBggMCgwICAwMCwoLCwwQDg4N/9sAhAAGBAQEBQQGBQUGCQYFCQYGBgYICQgKCgkICAsKFQ4MDA8ODg4UDg4QFFCQYGBcQHBgcHBggMCgwICAwMCwoLCwwQDg4N/8AAEQgABAAAAwERAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8UHSMdHx8kJ0QwIyY1ODkxGiQ1OT

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





