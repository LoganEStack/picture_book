<!-- INTRODUCTION -->
<h2 align="center">picture_book</h3>
  <p align="center">
    Adds relevant illustrations to pages in a pdf.
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

This program adds AI generated illustrations to books by using topic modeling 
(a part of natural language processing) to determine the central theme of each page. 
The central themes are condensed into keywords which are fed into [DeepAI]. 
This produces images that are then placed back into the pdf file. Really, this is just 
a small experiment with natural langauge processing with a fun and whimsical end product.

### Built With

[![Python][Python]][python-url]


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Requires Python3 to run.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/LoganEStack/picture_book.git
   ```
2. Install packages with pip
   ```sh
   pip install -r requirements.txt
   ```


<!-- Layout -->
## Layout

### main.py
The entry point to the program.

### generate_pictures.py
Manages requests with DeepAI API to retrieve AI generated illustrations.

### pdf.py
Handles all pdf operations.

### topic_modeling
Contains all logic related to the extraction and representation of a page's central theme.


<!-- USAGE EXAMPLES -->
## Usage

This project can be used to improve any novel or short story 
that you ever thought "needed more pictures."

### API Key

picture_book makes a REST API request to an AI image generator in order to produce each 
page's illustration. The file where this is handled (generate_pictures.py) is set up to 
call DeepAI and requires that the user enter a key for the software. If another image 
generator is preferred, the cURL command can easily be swapped out here for that of 
another API.

### Input

The input to the project is a call to the main python file followed by a parameter 
for the path to the file that you wish to add pictures to.  
```sh
   python main.py "my_book.pdf"
```

### Output

The output is a new file in the same directory as the file uploaded by the user 
with "_picture_book" attached to the end of the file name.

<!-- ROADMAP -->
## Roadmap

- [x] Basic topic modeling
- [x] API connection to DeepAI
- [x] Insertion of images into pdf
- [ ] Improve merging of pictures and pdf files
- [ ] Better topic modeling for more accurate images
- [ ] Better scanning of pdf files (currently does not work for scanned files, only text)
- [ ] Find a better free API for image generation (DeepAI isn't great for this purpose)


<!-- MARKDOWN LINKS & IMAGES -->
[DeepAI]: https://deepai.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/