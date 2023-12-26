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
    assert pages != ''
    return pages


def add_pics_to_pdf(path, pictures):
    """Creates a new pdf file that merges text and pictures.

    Args
        path: The path to the file.
        pictures: 
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
    pictures[0].save(
        "picture_book_images.pdf", save_all=True, append_images=pictures[1:]
    )

    with open(path, "rb") as pdf_book, open("picture_book_images.pdf", "rb") as pdf_pic:
        reader_book = PdfReader(pdf_book)
        reader_pic = PdfReader(pdf_pic)

        writer = PdfWriter()
        for page, pic in zip(reader_book.pages, reader_pic.pages):
            writer.add_page(page)
            background = writer.add_blank_page()
            background.merge_page(pic)

        # write everything in the writer to a file
        with open(new_path, "wb") as outFile:
            writer.write(outFile)