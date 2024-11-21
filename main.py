from flask import Flask, request, jsonify, send_file, render_template, after_this_request
from rembg import remove
import io
import os
import zipfile
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Get Unsplash API key from environment variable
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

@app.route('/')
def index():
    backend_url = request.host_url.rstrip('/')  # Get the current host URL
    return render_template('index.html', backend_url=backend_url)

@app.route('/get-random-images')
def get_random_images():
    try:
        # Fetch random headshot images from Unsplash
        url = f"https://api.unsplash.com/photos/random?query=headshot&count=4&client_id={UNSPLASH_ACCESS_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Extract image URLs from the response
        images = response.json()
        image_urls = [img['urls']['regular'] for img in images]

        return jsonify(image_urls)
    except Exception as e:
        print(f"Error fetching images: {e}")
        return jsonify({"error": "Failed to fetch images"}), 500

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'images' not in request.files:
        return jsonify({"error": "No image(s) provided"}), 400

    files = request.files.getlist('images')
    output_files = []

    for file in files:
        if file.filename == '':
            continue

        input_image = file.read()
        output_image = remove(input_image)
        output_buffer = io.BytesIO(output_image)
        output_buffer.seek(0)

        output_filename = f"output_{os.path.splitext(file.filename)[0]}.png"
        with open(output_filename, "wb") as f:
            f.write(output_buffer.getvalue())
        output_files.append(output_filename)

    if len(output_files) == 1:
        @after_this_request
        def cleanup_single_file(response):
            try:
                os.remove(output_files[0])
            except Exception as e:
                print(f"Error removing file: {e}")
            return response
        return send_file(output_files[0], mimetype='image/png', as_attachment=True)

    zip_filename = "processed_images.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for output_file in output_files:
            zipf.write(output_file)
            os.remove(output_file)

    @after_this_request
    def cleanup_zip_file(response):
        try:
            os.remove(zip_filename)
        except Exception as e:
            print(f"Error removing file: {e}")
        return response

    return send_file(zip_filename, mimetype='application/zip', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)