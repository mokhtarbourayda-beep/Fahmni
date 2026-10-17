import os, shutil, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("FAHMNI_DB", "/tmp/fahmni.db")
os.environ.setdefault("FAHMNI_SECRET", "/tmp/fahmni.secret")
os.environ.setdefault("FAHMNI_TTSCACHE", "/tmp/tts_cache")
if not os.path.exists("/tmp/fahmni.db"):
    shutil.copy(os.path.join(ROOT, "fahmni.db"), "/tmp/fahmni.db")
from app import app as application
