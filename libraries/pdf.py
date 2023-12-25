from PyPDF2 import PdfReader, PdfWriter
import shutil
import os


# TODO implement support for scanned pdfs
def read_pdf(path):
    """Loads a pdf file

    Args
        path: The path to the file.
    Returns
        A list of paragraphs/documents and title (initial 100 words considred as title of document)
    """
    pages_list = []
    with open(path,"rb") as pdfFileObj:
        reader = PdfReader(path)
        page = reader.pages[0]
        pages_list.append(page.extract_text())
    return pages_list


# def load_data(path):
#     """
#     Input  : path and file_name
#     Purpose: loading text file
#     Output : list of paragraphs/documents and 
#              title(initial 100 words considred as title of document)
#     """
#     documents_list = []
#     titles=[]
#     with open(path,"r", encoding="utf8") as fin:
#         for line in fin.readlines():
#             text = line.strip()
#             documents_list.append(text)
#     print("Total Number of Documents:",len(documents_list))
#     titles.append( text[0:min(len(text),100)] )
#     return documents_list,titles


def add_pics_to_pdf(path, pictures):
    """Creates a new pdf file that merges text and pictures.

    Args
        path: The path to the file.
    Returns
        A pdf file containing the original text pages as well as the newly generated pictures.
    Raises:
        IOError: An error occured creating a copy of the file specified in path
    """
    name, ext = os.path.splitext(path)
    dst = "{name}_picture_book{ext}".format(name=name, ext=ext)
    try:
        shutil.copyfile(path, dst)
    except IOError:
        print("Error: Failed to create copy of current file at {dst}. Directory not writable.").format(dst=dst)

    with open(dst, "rb") as pdfFile:
        reader = PdfReader(pdfFile)
        numPages = len(reader.pages)
        output = PdfWriter()
        for page_number in range(numPages):
            pgObj = reader.pages[page_number]
            if pgObj.extract_text() != "":
                if page_number % 2 == 0:
                    output.append_pages_from_reader(reader)
                    output.add_blank_page()
                    outputStream=open('samples/Amended.pdf','wb')
                    output.write(outputStream)
                    outputStream.close()


add_pics_to_pdf("samples/sample_2_page.pdf", [])