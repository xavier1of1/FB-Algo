import requests
from bs4 import BeautifulSoup
#import numpy as np
#import pandas as pd

#open facebook marketplace page
url = 'https://www.facebook.com/marketplace/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')