import os

from dotenv import load_dotenv

from convex import ConvexClient

#load_dotenv(".env.local")
#load_dotenv()
#os.getenv("CONVEX_URL")

client = ConvexClient("https://uncommon-goldfish-647.convex.cloud")
client.set_auth("token-from-authetication-flow")
from pprint import pprint
pprint(client.query("task"))