FROM python:3.12.7

# download this https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
# copy model to avoid unnecessary download
COPY u2net.onnx /root/.u2net/u2net.onnx

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py

COPY templates templates

EXPOSE 5000

CMD ["python", "app.py"]