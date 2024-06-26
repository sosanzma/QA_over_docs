import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')
ACTIVELOOP_TOKEN = os.getenv('ACTIVELOOP_TOKEN', 'YOUR_ACTIVELOOP_TOKEN')
ACTIVELOOP_ID = os.getenv('ACTIVELOOP_ID', 'YOUR_ACTIVELOOP_ID')

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ACTIVELOOP_TOKEN"] = ACTIVELOOP_TOKEN