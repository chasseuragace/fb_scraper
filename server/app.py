# server/app.py

from flask import Flask, jsonify
from facebook_scraper import get_profile

app = Flask(__name__)

@app.route('/profile/<profile_id>', methods=['GET'])
def get_profile_info(profile_id):
    try:
        # Get profile information
        profile_info = get_profile(profile_id)

        # Return profile information as JSON
        return jsonify(profile_info)

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500)
