from datetime import datetime
import pytz

def get_current_ist():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist).strftime("%I:%M:%S %p")