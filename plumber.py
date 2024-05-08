import pdfplumber

with pdfplumber.open("/Users/samnagourney/Downloads/AMERICAN_COASTAL_INSURANCE_CORP_10K_20230417.pdf") as pdf:
    result = pdf.pages[79].extract_text()
    print(result)
    
    
    # for page in :
    #     text = page.extract_text()
    #     print(text)


# with pdfplumber.open("/Users/samnagourney/Downloads/AMERICAN_COASTAL_INSURANCE_CORP_10K_20230417.pdf") as pdf:
#     result = pdf.pages[65].extract_tables()
#     print(result)
