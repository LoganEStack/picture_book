import requests
import re
from PIL import Image
from fpdf import FPDF

def generate_pictures(page_topics):
    """Generate an image based on keywords for each page.

    I use DeepAI for image generation because it's generous with its free API limits.
    This function can be modified to use any selection of image generation programs.
    
    Args
        page_topics: A list of keywords that define each page.
    Returns
        A PIL image for each page.
    """
    API_KEY = ''
    images = []
    for page in page_topics:
        if page:
            topics = ', '.join(re.findall(r'(?<=\*").*?(?=")', page[1]))
            # r = requests.post(
            #     "https://api.deepai.org/api/text2img",
            #     files = {
            #         'text': (None, 'Illustrated drawing of the following themes: ' + topics),
            #         'grid_size': (None, '1'),
            #     },
            #     headers={'api-key': API_KEY}
            # )
            try:
                # image_url = r.json()['output_url']
                image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/SNice.svg/1200px-SNice.svg.png"
                img_data = requests.get(image_url, stream=True)

                base_width= 300
                img = Image.open(img_data.raw)
                wpercent = (base_width / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)

                images.append(img)
            except KeyError as e:
                print("There was an issue with the API call.", e)
            # with open(f'images/image_{count}.jpg', 'wb') as handler:
            #     handler.write(img_data)
    return images
