import re

def is_valid_email(email):
    """
    Validates if the provided email address is correctly formatted.
    
    Parameters:
    - email (str): The email address to validate.
    
    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    # Define the regex pattern for a valid email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the pattern with the provided email
    return bool(re.match(email_pattern, email))
