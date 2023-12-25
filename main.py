from libraries.pdf import read_pdf, add_pics_to_pdf
from libraries.topic_modeling import preprocess_data, create_lsa_model
from libraries.generate_pictures import generate_pictures
import sys


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     raise IndexError("picture_book takes exactly 1 argument. "
    #                      "The proper syntax is:\npython main.py <file path>")
    # path = sys.argv[1]
    path = "samples/sample_2_page.pdf"
    NUM_TOPICS = 7
    NUM_WORDS = 5

    # LSA Model
    pages = read_pdf(path)
    preprocessed_pages = preprocess_data(pages)
    model = create_lsa_model(preprocessed_pages, NUM_TOPICS, NUM_WORDS)

    # Extract topics and issue curl to generate pictures
    page_topics = model.print_topics(num_topics=NUM_TOPICS, num_words=NUM_WORDS)
    print(page_topics)
    pictures = generate_pictures(page_topics)
    add_pics_to_pdf(path, pictures)
