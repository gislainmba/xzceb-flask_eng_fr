import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['rzQU50_N2tufIr97-AT3ktZtfHrQHdWWAZjaFBy9JDZP']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e384ba1e-7e98-4a4f-af72-26183562720c']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('url')

def englishToFrench(englishText):
    frenchText = language_translator.translate(
    text = englishText,
    model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
    text = frenchText,
    model_id='fr-en').get_result()
    return englishText
