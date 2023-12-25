<!-- INTRODUCTION -->
<h2 align="center">illustrate_me</h3>
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

[![Python][Python]][React-url]


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
3. Run the application
   ```sh
   python main.py
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


<!-- ROADMAP -->
## Roadmap

- [x] Basic topic modeling
- [x] API connection to DeepAI
- [x] Insertion of images into pdf
- [ ] Better topic modeling for more accurate images
- [ ] Better scanning of pdf files (currently does not work for scanned files)
- [ ] Find a better free API for image generation (DeepAI isn't great for this purpose)


<!-- MARKDOWN LINKS & IMAGES -->
[DeepAI]: https://deepai.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
