import os
from typing import List
import requests

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Updated import: Assumes FAQEngine and the FAQ text are in 'rag_app.py'
from rag_app import FAQEngine, PYTHON_FAQ_TEXT


# Load environment variables from .env file
load_dotenv()

# Configuration constants
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "python_faq_collection"  # Using a new collection for the Python data
HOST = "127.0.0.1"
PORT = 8080
