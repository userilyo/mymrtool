import streamlit as st
import re

# Define more efficient regular expressions for different PII detection and anonymization using given example
regex_patterns = {
    "uk_ss_id": re.compile(r'\b[A-Z]{2}\s\d{6}\s[A-Z]\b'),  # e.g. AB 123456 A
    "uk_phone_number": re.compile(r'\+44\d{10}|0\d{10}'),  # e.g. +447444647712 or 07444647712 oldreg=\+44\d{10}|0\d{10} new=^(?:\+44\d{10}|0\d{10})$
    "uk_postcode": re.compile(r'\b[A-Z]{1,2}\d{1,2}[A-Z]?\s*\d[A-Z]{2}\b', re.IGNORECASE), # e.g. RG12BD or RG1 2BD or EC1N 2MN or 
    "email_address": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')  # e.g. abc_def@google.com
}

# Risk classification
risk_levels = {
    "uk_ss_id": "high",
    "uk_phone_number": "medium",
    "uk_postcode": "medium",
    "email_address": "low"
}

# Data anonymization mappings
anonymized_mappings = {
    "uk_ss_id": "SS_ID_ANONYMIZED",
    "uk_phone_number": "PHONENUMBER_ANONYMIZED",
    "uk_postcode": "POSTCODE_ANONYMIZED",
    "email_address": "EMAILADDRESS_ANONYMIZED"
}


def process_text(text, document_title):
    output_data = []
    # Use regex for pattern-based matching
    for pii_category, pattern in regex_patterns.items():
        for match in pattern.findall(text):
            risk_level = risk_levels[pii_category]
            anonymized_text = anonymized_mappings[pii_category]
            output_data.append({'document_title': document_title, 'source_PII': match, 'risk_level': risk_level, 'anonymized_PII': anonymized_text})
            # Anonymize the text
            text = text.replace(match, anonymized_text)
    return output_data, text


# Streamlit app
st.title("MYMRT PII Anonymizer")
uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode()
    document_title = uploaded_file.name
    output_data, anonymized_text = process_text(text, document_title)

    st.subheader("Anonymized Text:")
    st.text_area("", anonymized_text, height=300)
