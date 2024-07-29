dataset = {"desease":['Iron Deficiency Anaemia', 'Megaloblastic Anemia'],
 'causes':['lack of iron in the body mainly due to nutritional deficiency, chronic blood loss malabsorption and hookworm infestations', 'to inadequate intake or malabsorption of vitamin B12 or folate.'], 
 'gender':['ALL', 'ALL'], 
 'age':['ALL', 'ALL'], 
 'most group':['pregnancy', 'ALL']}

import pandas as pd
import numpy as np
import nltk
import re
import random
import string
import warnings
warnings.simplefilter("ignore")
from PyPDF2 import PdfReader