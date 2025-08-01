from rich.pretty import pprint
import os
from dotenv import load_dotenv
from qgenie import QGenieClient

load_dotenv()

qgenie_api_key = os.getenv("QGENIE_API_KEY")

client = QGenieClient(endpoint="https://qgenie-chat.qualcomm.com", api_key=qgenie_api_key)

models_response = client.get_available_models()

pprint(models_response, expand_all=True)