from gensim import corpora
from gensim.models import LsiModel
from gensim.models.coherencemodel import CoherenceModel
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#from nltk.stem.porter import PorterStemmer


def preprocess_data(documents):
    """Pre-processes text to clean it up.

    This involves:
        - tokenizing (placing individual words into a list)
        - removing stopwords (deleting insignificant words not relevant to the topic)
        - lemmatization (reducing a word to its root meaning (ex. creative -> create))
    
    Args
        documents: List of documents to pre-process.
    Returns
        Text that has been cleaned up and simplified.
    """
    tokenizer = RegexpTokenizer(r'\w+')
    stop_list = set(stopwords.words('english'))
    # Could use a stemmer if we wanted, which is a more brute-ish, codeified lemmatizer
    # stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    preprocessed_text = []
    for doc in documents:
        tokens = tokenizer.tokenize(doc.lower())
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in stop_list]
        # stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        lemmatized_tokens = [lemmatizer.lemmatize(i) for i in stopped_tokens]
        preprocessed_text.append(lemmatized_tokens)
    return preprocessed_text
    

def prepare_corpus(preprocessed_text):
    """Create term dictionary of our courpus and Converting list of documents (corpus) into Document Term Matrix.

    Args
        preprocessed_text: clean document
    Returns
        term dictionary and Document Term Matrix
    """
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. 
    # dictionary = corpora.Dictionary(preprocessed_text)
    dictionary = corpora.Dictionary(preprocessed_text)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in preprocessed_text]
    # generate LDA model
    return dictionary,doc_term_matrix


def create_lsa_model(preprocessed_text, num_topics, num_words):
    """Create LSA (Latent Semantic Analysis) model

    Args
        preprocessed_text: Cleaned up text.
        num_topics: Number of topics.
        num_words: Number of words associated with each topic.
    Returns
        The LSA model.
    """
    dictionary, doc_term_matrix = prepare_corpus(preprocessed_text)
    # model_list, coherence_values = compute_coherence_values(dictionary, doc_term_matrix, preprocessed_text,
    #                                                         stop=6, start=1, step=1)
    # generate LSA model
    lsa_model = LsiModel(doc_term_matrix, num_topics=num_topics, id2word = dictionary)
    print(lsa_model.print_topics(num_topics=num_topics, num_words=num_words))
    return lsa_model


def compute_coherence_values(dictionary, doc_term_matrix, preprocessed_text, stop, start=2, step=3):
    """Compute c_v coherence for various number of topics

    Args
        dictionary : Gensim dictionary
        corpus : Gensim corpus
        texts : List of input texts
        stop : Max num of topics
    Returns
        List of LSA topic models and list of coherence values corresponding 
        to the LDA model with respective number of topics.
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, stop, step):
        # generate LSA model
        model = LsiModel(doc_term_matrix, num_topics=num_topics, id2word = dictionary)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=preprocessed_text, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())
    return model_list, coherence_values