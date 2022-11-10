import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['rzQU50_N2tufIr97-AT3ktZtfHrQHdWWAZjaFBy9JDZP']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e384ba1e-7e98-4a4f-af72-26183562720c']

translator= Translator(from_lang="english",to_lang="french")
translation = translator.translate("Guten Morgen")
print translation