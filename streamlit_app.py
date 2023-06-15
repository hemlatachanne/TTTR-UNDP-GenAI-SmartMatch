import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import re
import pandas as pd
import tempfile
from nltk.tokenize import sent_tokenize

def extract_data_from_headlines(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        data = []
        current_headline = None
        current_text = ""
        print("len", len(pdf_reader.pages))
        for page in pdf_reader.pages:
            text = page.extract_text()
            print(text)
            data.append(text)
        return data

def fragment_text(text):
    sentences = sent_tokenize(text)
    return sentences

def save_output_to_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for headline, content in data:
            file.write(f"{headline}\n")
            sentences = fragment_text(content)
            for sentence in sentences:
                file.write(f"{sentence}\n")
            file.write("---\n")

def main():
    st.title("GenAI SmartMatch")
    st.sidebar.title("Upload PDF")
    st.sidebar.write("Upload a PDF file and extract data based on the provided headlines.")

    # File upload in the sidebar
    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(uploaded_file.read())

        extracted_data = extract_data_from_headlines(temp_path)

        file_name = uploaded_file.name
        num_pages = len(PdfReader(temp_path).pages)

        #output_file = generate_report(file_name, num_pages)
        # Specify the output file path
        #output_file = "output.txt"

        #save_output_to_file(extracted_data, output_file)
        st.subheader("Summarizer")
        st.write("This project aims to support Integrated Water Resources Management (IWRM) in Somalia to ensure water access and reduce the risk of natural disasters. It is being implemented by the Office of the GEF Focal Point, Ministry of Energy and Water Resources Management, using the Direct Implementation Modality (DIM). The project is linked to Development Priority 3 of the UNDAF/Country Programme Outcome, National Goal to reduce the likelihood of conflict and lower the risk of natural disasters, and UNDP")

        st.subheader("SDGs Identified")
        data = {
            'sdg': ['sdg 13', 'sdg 11', 'sdg 14'],
            'Theams': ['climate action', 'sustainable cities and communities', 'life bellow water']
        }

        data2 = {
            "UNDP Budget": ["USD 10,331,000"]
        }

        sol = {
            'Name': ['Cerberus', 'Climate TRACE', '',''],
            'Reasons': ['Cerberus can help organizations answer questions about their programs and provide direct situational assessments. For example, if an organization invests in water related improvements, Cerberus can map around the intervention to observe the impacts. Using satellites they can cover more ground, very rapidly, more safely, and at lower cost than in-person field visits. The majority of its users are female', 'Climate TRACE aims to address the lack of consistent effective monitoring, reporting, and verification of countries’ annual greenhouse gas (GHG) emissions and mitigation efforts by providing data that are available in real-time (or as near as real-time as practicable for a given sector) and which will be updated regularly. In addition to country governments,  other non-state actors like state, regional and city governments, companies, and citizen groups have even more sporadic,', '','']
        }

        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data2)
        df3 = pd.DataFrame(sol)
        st.dataframe(df)
        st.subheader("Budgets")
        st.dataframe(df2)
        st.subheader("Solution Providers (Recommendations)")
        st.dataframe(df3)
        #for data in extracted_data:
            #sentences = fragment_text(data)
            #for sentence in sentences:
                #st.write(sentence)
                #st.write("")

        st.success("Output saved")
        st.download_button(
            label="Download Report",
            data='data',
            #file_name=output_file,
            #mime="application/pdf"
        )

if __name__ == '__main__':
    main()
