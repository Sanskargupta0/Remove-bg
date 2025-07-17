from flask import Flask, request, jsonify, send_file, render_template, after_this_request
from rembg import remove, new_session
import os
import zipfile
import tempfile
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max per file

UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

@app.route('/')
def index():
    backend_url = request.host_url.rstrip('/')
    return render_template('index.html', backend_url=backend_url)

@app.route('/get-random-images')
def get_random_images():
    try:
        url = f"https://api.unsplash.com/photos/random?query=headshot&count=4&client_id={UNSPLASH_ACCESS_KEY}"
        response = requests.get(url)
        response.raise_for_status()
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

    temp_dir = tempfile.mkdtemp()

    for file in files:
        if file.filename == '':
            continue

        try:
            input_image = file.read()
            output_image = remove(input_image, session=new_session(model_name='u2netp'))
            output_path = os.path.join(temp_dir, f"output_{os.path.splitext(file.filename)[0]}.png")
            with open(output_path, "wb") as f:
                f.write(output_image)
            output_files.append(output_path)
        except Exception as e:
            print(f"Error processing file {file.filename}: {e}")
            continue

    if len(output_files) == 0:
        return jsonify({"error": "No valid images processed"}), 400

    if len(output_files) == 1:
        @after_this_request
        def cleanup_single_file(response):
            try:
                os.remove(output_files[0])
                os.rmdir(temp_dir)
            except Exception as e:
                print(f"Cleanup error: {e}")
            return response
        return send_file(output_files[0], mimetype='image/png', as_attachment=True)

    zip_path = os.path.join(temp_dir, "processed_images.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for path in output_files:
            zipf.write(path, os.path.basename(path))
            os.remove(path)

    @after_this_request
    def cleanup_zip_file(response):
        try:
            os.remove(zip_path)
            os.rmdir(temp_dir)
        except Exception as e:
            print(f"Cleanup error: {e}")
        return response

    return send_file(zip_path, mimetype='application/zip', as_attachment=True)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
