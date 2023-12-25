import requests
import re

def generate_pictures(page_topics):
    """Generate an image based on keywords for each page.

    I use DeepAI for image generation because it's generous with its free API limits.
    This function can be modified to use any selection of image generation programs.
    
    Args
        page_topics: A list of keywords that define each page.
    Returns
        An image for each page.
    """
    API_KEY = ''
    result = []
    for page in page_topics:
        if page:
            topics = ', '.join(re.findall(r'(?<=\*").*?(?=")', page[1]))
            r = requests.post(
                "https://api.deepai.org/api/text2img",
                files = {
                    'text': (None, 'Illustrated drawing of the following themes: ' + topics),
                    'grid_size': (None, '1'),
                },
                headers={'api-key': API_KEY}
            )
            try:
                result.append(r.json()['output_url'])
            except KeyError:
                print("There was an issue with the API call.")
    print(result)
    return result
