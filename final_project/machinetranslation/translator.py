"""Translation en-fr and fr-en"""

import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
language_translator.set_service_url('url')

def english_to_french(english_text):
    """Translate from English to French"""
    en_2_fr = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = en_2_fr['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate from French to English"""
    fr_2_en = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = fr_2_en['translations'][0]['translation']
    return english_text
