import os
from dotenv import load_dotenv
from qgenie import QGenieClient, ChatMessage

load_dotenv()

qgenie_api_key = os.getenv("QGENIE_API_KEY")

client = QGenieClient(endpoint="https://qgenie-chat.qualcomm.com", api_key=qgenie_api_key)




