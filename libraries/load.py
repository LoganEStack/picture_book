from PyPDF2 import PdfReader

# TODO implement support for scanned pdfs
def load_data_pdf(path):
    """
    Input  : path to file
    Purpose: loading text file
    Output : list of paragraphs/documents and 
             title(initial 100 words considred as title of document)
    """
    pages_list = []
    with open(path,"rb") as pdfFileObj:
        reader = PdfReader(path)
        page = reader.pages[0]
        pages_list.append(page.extract_text())
    return pages_list


def load_data(path):
    """
    Input  : path and file_name
    Purpose: loading text file
    Output : list of paragraphs/documents and 
             title(initial 100 words considred as title of document)
    """
    documents_list = []
    titles=[]
    with open(path,"r", encoding="utf8") as fin:
        for line in fin.readlines():
            text = line.strip()
            documents_list.append(text)
    print("Total Number of Documents:",len(documents_list))
    titles.append( text[0:min(len(text),100)] )
    return documents_list,titles