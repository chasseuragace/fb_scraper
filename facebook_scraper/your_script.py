# your_script.py

from facebook_scraper import get_profile

# Function to get and print profile information
def get_and_print_profile_information(profile_name):
    try:
        # Get profile information
        profile_info = get_profile(profile_name)

        # Print profile information
        print("Profile Information:")
        for key, value in profile_info.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
profile_name = "naskrzydlachfundacja"
get_and_print_profile_information(profile_name)
