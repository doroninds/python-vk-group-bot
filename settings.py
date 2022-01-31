# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATABASE = os.environ.get("DATABASE")
VK_API_TOKEN = os.environ.get("VK_API_TOKEN")
VK_BOT_GROUP_ID = os.environ.get("VK_BOT_GROUP_ID")
