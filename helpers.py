import os




def get_from_env(var_name: str) -> str:

    
    """
    Get a value from an environment variable. Used in CI for testing.
    """
    val = os.getenv(var_name, "")
    if val == "":
        print(f"Error: Missing environment variable {var_name}.")
        exit(1)

    return val