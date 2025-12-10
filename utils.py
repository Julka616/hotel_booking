from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print(" Wrong date format. Use YYYY-MM-DD.")
        return False
