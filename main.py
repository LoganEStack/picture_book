from libraries.pdf import read_pdf, add_pics_to_pdf
from libraries.topic_modeling import preprocess_data, create_lsa_model
from libraries.generate_pictures import generate_pictures

if __name__ == "__main__":
    PATH = "samples/sample.pdf"
    NUM_TOPICS = 7
    NUM_WORDS = 5

    # LSA Model
    page_list = read_pdf(PATH)
    preprocessed_text = preprocess_data(page_list)
    model = create_lsa_model(preprocessed_text, NUM_TOPICS, NUM_WORDS)

    # Extract topics and issue curl to generate pictures
    page_topics = model.print_topics(num_topics=NUM_TOPICS, num_words=NUM_WORDS)
    pictures = generate_pictures(page_topics)
    add_pics_to_pdf(PATH, pictures)
