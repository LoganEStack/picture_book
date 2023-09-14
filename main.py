from libraries.load import load_data_pdf
from libraries.topic_modeling import preprocess_data, create_gensim_lsa_model
from libraries.generate_pictures import generate_pictures


if __name__ == "__main__":
    PATH = "sample.pdf"

    # LSA Model
    number_of_topics = 7
    words = 5
    page_list = load_data_pdf(PATH)
    clean_text = preprocess_data(page_list)
    model = create_gensim_lsa_model(clean_text,number_of_topics,words)

    # Extract topics and issue curl
    page_topics = model.print_topics(num_topics=number_of_topics, num_words=words)
    # pictures = generate_pictures(page_topics)

# TODO take resulting image and place it on a new page in pdf
