import pandas as pd
import re
import pdfplumber
import os

email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def extract_emails_from_excel(file_path):

    df = pd.read_excel(file_path, engine="openpyxl")

    emails = []

    for column in df.columns:
        for value in df[column]:

            # Convertir cualquier valor a string
            value = str(value)

            found = re.findall(email_regex, value)
            emails.extend(found)

    return list(set(emails))


def extract_emails_from_csv(file_path):

    df = pd.read_csv(file_path)

    emails = []

    for column in df.columns:
        for value in df[column]:

            # Convertir cualquier valor a string
            value = str(value)

            found = re.findall(email_regex, value)
            emails.extend(found)

    return list(set(emails))


def extract_emails_from_pdf(file_path):

    emails = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:

            text = page.extract_text()

            if text:
                found = re.findall(email_regex, text)
                emails.extend(found)

    return list(set(emails))


def extract_emails(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".xlsx":
        return extract_emails_from_excel(file_path)

    if ext == ".csv":
        return extract_emails_from_csv(file_path)

    if ext == ".pdf":
        return extract_emails_from_pdf(file_path)

    raise ValueError("Unsupported file format")

def extract_companies_from_excel(file_path):

    df = pd.read_excel(file_path, engine="openpyxl")

    companies = []

    for _, row in df.iterrows():

        empresa = str(row.get("empresa", "")).strip()
        correo = str(row.get("correo", "")).strip()

        if empresa and correo:
            companies.append({
                "empresa": empresa,
                "correo": correo
            })

    return companies