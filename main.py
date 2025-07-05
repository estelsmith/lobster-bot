import fire

def scrape():
    """
    Scrape a URL and clean its content for analyzing with an LLM.
    """
    print('Hello world!')

if __name__ == '__main__':
    fire.Fire({'scrape': scrape})
