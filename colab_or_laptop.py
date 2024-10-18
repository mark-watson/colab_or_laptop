# colab_or_laptop.py

def is_colab():
    """
    Determines if the code is running in a Google Colab environment.

    Returns:
        bool: True if running in Google Colab, False otherwise.
    """
    try:
        import google.colab
        return True
    except ImportError:
        return False

# Example usage:
if __name__ == "__main__":
    if is_colab():
        print("Running in Google Colab.")
    else:
        print("Not running in Google Colab.")

