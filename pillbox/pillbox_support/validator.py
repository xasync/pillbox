import re


def email(text):
    """
    Check if text is match the email format
    :param text: The Input Email
    :return: Ture Or False
    """
    try:
        string = str(text).strip()
        if len(string) <= 0:
            return False
        return re.match(r'^.+@(\w+\.)+[a-zA-Z]+$', text) is not None
    except:
        return False
