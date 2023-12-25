from pypdf import PdfReader, PdfWriter
import os


def read_pdf(path):
    """Loads a pdf file

    Args
        path: The path to the file.
    Returns
        A list of paragraphs/documents and title (initial 100 words considred as title of document)
    """
    pages = []
    try:
        f = open(path,"rb")
    except FileNotFoundError:
        print('Could not locate', path)
    else:
        with f:
            reader = PdfReader(path)
            for page in reader.pages:
                pages.append(page.extract_text())
    return pages


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
    new_path = "{name}_picture_book{ext}".format(name=name, ext=ext)
    if os.path.isfile(new_path):
        raise FileExistsError("A file with the name", new_path, "already exists. "
                              "Please move this file out of the specified directory " 
                              "so that it does not get overwritten.")
    
    with open(path, "rb") as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)
            writer.add_blank_page()

        with open(new_path,'wb') as output_pdf:
            writer.write(output_pdf)

# add_pics_to_pdf("samples/sample_2_page.pdf", [])