# importing required modules
from PyPDF2 import PdfReader
from gensim import corpora
from gensim.models import LsiModel
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim.models.coherencemodel import CoherenceModel
# import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
import requests
import re

PATH = "test/d.pdf"

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


def preprocess_data(doc_set):
    """
    Input  : document list
    Purpose: preprocess text (tokenize, removing stopwords, and stemming)
    Output : preprocessed text
    """
    # initialize regex tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    # create English stop words list
    en_stop = set(stopwords.words('english'))
    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # list for tokenized documents in loop
    texts = []
    # loop through document list
    for i in doc_set:
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]
        # stem tokens
        # stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        # lematize tokens
        lemmatized_tokens = [lemmatizer.lemmatize(i) for i in stopped_tokens]
        # add tokens to list
        texts.append(lemmatized_tokens)
    return texts
    

def prepare_corpus(doc_clean):
    """
    Input  : clean document
    Purpose: create term dictionary of our courpus and Converting list of documents (corpus) into Document Term Matrix
    Output : term dictionary and Document Term Matrix
    """
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
    dictionary = corpora.Dictionary(doc_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # generate LDA model
    return dictionary,doc_term_matrix


def create_gensim_lsa_model(doc_clean,number_of_topics,words): 
    """
    Input  : clean document, number of topics and number of words associated with each topic
    Purpose: create LSA model using gensim
    Output : return LSA model
    """
    dictionary,doc_term_matrix=prepare_corpus(doc_clean)
    # model_list, coherence_values = compute_coherence_values(dictionary, doc_term_matrix, doc_clean,
    #                                                         stop=6, start=1, step=1)
    # generate LSA model
    lsamodel = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary)  # train model
    print(lsamodel.print_topics(num_topics=number_of_topics, num_words=words))
    return lsamodel


def compute_coherence_values(dictionary, doc_term_matrix, doc_clean, stop, start=2, step=3):
    """
    Input   : dictionary : Gensim dictionary
              corpus : Gensim corpus
              texts : List of input texts
              stop : Max num of topics
    purpose : Compute c_v coherence for various number of topics
    Output  : model_list : List of LSA topic models
              coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, stop, step):
        # generate LSA model
        model = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary)  # train model
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=doc_clean, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())
    return model_list, coherence_values

# def plot_graph(doc_clean,start, stop, step):
#     dictionary,doc_term_matrix=prepare_corpus(doc_clean)
#     model_list, coherence_values = compute_coherence_values(dictionary, doc_term_matrix,doc_clean,
#                                                             stop=2, start=12, step=1)
    # Show graph
#     x = range(start, stop, step)
#     plt.plot(x, coherence_values)
#     plt.xlabel("Number of Topics")
#     plt.ylabel("Coherence score")
#     plt.legend(("coherence_values"), loc='best')
#     plt.show()
# start,stop,step=2,12,1
# plot_graph(clean_text,start,stop,step)

# LSA Model
number_of_topics = 7
words = 5
page_list = load_data_pdf(PATH)
clean_text=preprocess_data(page_list)
model=create_gensim_lsa_model(clean_text,number_of_topics,words)

# Extract topics and issue curl
page_topics = model.print_topics(num_topics=number_of_topics, num_words=words)
result = []
for page in page_topics:
    topics = ', '.join(re.findall(r'(?<=\*").*?(?=")', page[1]))
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': 'Illustrated drawing of the following themes: ' + topics,
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    try:
        result.append(r.json()['output_url'])
    except KeyError:
        print("API didn't like that call.")
print(result)

# TODO take resulting image and place it on a new page in pdf