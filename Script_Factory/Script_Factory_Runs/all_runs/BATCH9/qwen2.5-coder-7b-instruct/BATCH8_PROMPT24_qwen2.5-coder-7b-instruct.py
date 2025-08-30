# BATCH8_PROMPT24_qwen.py

import datetime
from pytz import timezone

def main():
    # Define a datetime object for Tokyo
    tokyo_time = datetime.datetime.now(timezone('Asia/Tokyo'))
    
    # Attempt to convert the time to another timezone (e.g., UTC)
    try:
        utc_time = tokyo_time.astimezone(timezone('UTC'))
    except Exception as e:
        # Print a humorous error message
        print("Error: Timezone conversion is futile. It's like trying to change the color of a sunset.")
    else:
        print(f"Tokyo time: {tokyo_time}")
        print(f"UTC time: {utc_time}")

if __name__ == "__main__":
    main()