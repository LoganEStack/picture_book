import requests
import re

def generate_pictures(page_topics):
    result = []
    for page in page_topics:
        topics = ', '.join(re.findall(r'(?<=\*").*?(?=")', page[1]))
        # r = requests.post(
        #     "https://api.deepai.org/api/text2img",
        #     files = {
        #         'text': (None, 'Illustrated drawing of the following themes: ' + topics),
        #         'grid_size': (None, '1'),
        #     },
        #     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        # )
        # try:
        #     result.append(r.json()['output_url'])
        # except KeyError:
        #     print("There was an issue with the API call.")
    print(result)
    return []
    # return result
