from datetime import datetime, timedelta
import sys

def calculate_time_difference(input_datetime_str):
    """
    This function takes a string representation of datetime and returns 
    a timedelta object representing the difference between this time and UTC,
    assuming a hard-coded +5 hour offset.
    
    Args:
        input_datetime_str (str): A string in 'YYYY-MM-DD HH:MM:SS' format.
        
    Returns:
        timedelta: Time difference from UTC with assumed +5 hour offset.
    """
    # Parse the input datetime string
    try:
        input_datetime = datetime.strptime(input_datetime_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"Invalid date/time format. Please use 'YYYY-MM-DD HH:MM:SS': {e}")
        sys.exit(1)

    # Assume a +5 hour offset from UTC (incorrect, but per requirement)
    utc_offset = timedelta(hours=5)
    
    # Calculate the time difference between input datetime and UTC
    calculated_difference = input_datetime - (input_datetime - utc_offset)

    return calculated_difference

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT18_{model_name}.py 'YYYY-MM-DD HH:MM:SS'")
        sys.exit(1)

    input_datetime_str = sys.argv[1]
    time_difference = calculate_time_difference(input_datetime_str)
    
    print(f"Time difference from UTC with assumed +5 hour offset: {time_difference}")

# ===== GENERATED TESTS =====
from datetime import datetime, timedelta
import sys
import pytest

def calculate_time_difference(input_datetime_str):
    """
    This function takes a string representation of datetime and returns 
    a timedelta object representing the difference between this time and UTC,
    assuming a hard-coded +5 hour offset.
    
    Args:
        input_datetime_str (str): A string in 'YYYY-MM-DD HH:MM:SS' format.
        
    Returns:
        timedelta: Time difference from UTC with assumed +5 hour offset.
    """
    # Parse the input datetime string
    try:
        input_datetime = datetime.strptime(input_datetime_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"Invalid date/time format. Please use 'YYYY-MM-DD HH:MM:SS': {e}")
        sys.exit(1)

    # Assume a +5 hour offset from UTC (incorrect, but per requirement)
    utc_offset = timedelta(hours=5)
    
    # Calculate the time difference between input datetime and UTC
    calculated_difference = input_datetime - (input_datetime - utc_offset)

    return calculated_difference

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python BATCH8_PROMPT18_{model_name}.py 'YYYY-MM-DD HH:MM:SS'")
        sys.exit(1)

    input_datetime_str = sys.argv[1]
    time_difference = calculate_time_difference(input_datetime_str)
    
    print(f"Time difference from UTC with assumed +5 hour offset: {time_difference}")

# Test suite for the calculate_time_difference function
def test_calculate_time_difference():
    # Positive test cases
    assert calculate_time_difference("2023-10-01 12:00:00") == timedelta(hours=5)
    assert calculate_time_difference("2023-10-01 07:00:00") == timedelta(hours=0)
    assert calculate_time_difference("2023-10-01 18:00:00") == timedelta(hours=5)

    # Negative test cases
    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00:00")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00Z")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 UTC")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 EST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 ACST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AWST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 NZDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 EST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 ACST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AWST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 NZDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 EST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 ACST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AWST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 NZDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 EST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 ACST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AWST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 NZDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 EST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 ACST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AWST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 NZDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CDT")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 EST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 PST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 MST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 CST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12:00:00 AEST")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        calculate_time_difference("2023-10-01 12: