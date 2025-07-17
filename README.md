# [Remove Background](https://remove-bg-rv88.onrender.com/) &middot; [![Author Sanskar Gupta](https://img.shields.io/badge/Author-Sanskar-%3C%3E)](https://www.linkedin.com/in/sanskar-gupta-12476423b/)  
[![GitHub](https://img.shields.io/badge/GitHub-%3C%3E)](https://github.com/Sanskargupta0/Remove-bg)  
[![Flask](https://img.shields.io/badge/Flask-%3C%3E)](https://flask.palletsprojects.com/)  
[![Docker](https://img.shields.io/badge/Docker-%3C%3E)](https://hub.docker.com/r/sanskargupta0/remove-bg)  
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-%3C%3E)](https://tailwindcss.com/)

## 📝 Project Description

Remove Background is a powerful web-based image processing application that uses AI to automatically remove backgrounds from images. Built with Flask and powered by the rembg library using state-of-the-art U2-Net deep learning models, this application provides instant background removal for both single and multiple images. The platform features a modern responsive interface, drag-and-drop functionality, batch processing capabilities, and seamless file download management for professional image editing workflows.

## ⚙️ Tech Stack

- **Backend Framework**: Flask 3.1.0
- **AI/ML Library**: rembg 2.0.59 (U2-Net model)
- **Image Processing**: OpenCV 4.10.0.84, Pillow 11.0.0
- **Deep Learning**: ONNX Runtime 1.20.0, NumPy 2.0.2
- **Frontend**: TailwindCSS, Vanilla JavaScript, HTML5
- **API Integration**: Unsplash API for sample images
- **Web Server**: Gunicorn 23.0.0
- **Containerization**: Docker
- **Deployment**: Render.com
- **Environment**: Python 3.12+

## 🔋 Features

👉 **AI-Powered Background Removal**: Advanced U2-Net deep learning model (U2netp) for precise background removal with professional quality results, handling complex edges and fine details automatically.

👉 **Multiple Image Processing**: 
- Batch processing of multiple images simultaneously
- Automatic ZIP file generation for multiple outputs
- Support for various image formats (JPG, PNG, WEBP)
- Intelligent file size validation and optimization
- Progress tracking for batch operations

👉 **Modern User Interface**: 
- Responsive design optimized for all devices (mobile, tablet, desktop)
- Dark/Light mode compatibility with system preferences
- Drag-and-drop file upload with visual feedback
- Real-time image preview with grid layout
- Professional gradient styling and glass effect animations

👉 **Sample Image Integration**: 
- Unsplash API integration for random headshot samples
- Interactive sample processing with one-click testing
- Automatic image fetching with loading states
- Error handling and retry functionality for API failures

👉 **Advanced File Management**: 
- 2MB maximum file size per image for optimal performance
- Temporary file handling with automatic cleanup
- Secure file processing in isolated temporary directories
- Multi-format output support (PNG for transparency)
- Memory-efficient processing for large batches

👉 **Production-Ready Architecture**: 
- Docker containerization for consistent deployment
- Gunicorn WSGI server for production scalability
- Environment variable configuration management
- Error handling and logging for debugging
- CORS support for API integration

👉 **Download & Export System**: 
- Instant download links for processed images
- Automatic filename generation with prefixes
- ZIP compression for multiple image downloads
- Download progress indicators and status updates
- Clean URL handling and memory management

👉 **Performance Optimization**: 
- Pre-loaded AI model caching for faster processing
- Efficient memory management for large images
- Asynchronous file processing capabilities
- Optimized image compression and quality settings
- Background cleanup processes for server maintenance

## 🏗️ System Architecture

### Application Architecture

The application follows a microservice-oriented Flask architecture with:

1. **Single-File Flask Application**: Streamlined `app.py` with all endpoints and logic
2. **AI Model Integration**: rembg library with U2-Net model for background removal
3. **Template-Based Frontend**: Jinja2 templating with TailwindCSS styling
4. **API Integration**: External Unsplash API for sample image generation

### AI Processing Pipeline

The background removal process follows this workflow:

1. **Image Upload**: Multi-file upload with validation and size checking
2. **AI Processing**: rembg library with U2netp session for background removal
3. **Output Generation**: PNG format with transparency preservation
4. **File Management**: Temporary storage with automatic cleanup
5. **Download Delivery**: Direct file serving or ZIP compression for batches

### Deployment Architecture

```
Frontend (TailwindCSS) ← HTTP → Flask App ← AI Processing → rembg (U2-Net)
         ↓                      ↓                    ↓
   User Interface        File Management      Background Removal
         ↓                      ↓                    ↓
   Docker Container ←  Environment Config  →  Model Loading
         ↓                      ↓                    ↓
   Render.com Platform    Gunicorn Server     Temporary Storage
```

## 🚀 Quick Start

Follow these steps to set up the project locally on your machine.

### Prerequisites

Make sure you have the following installed:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [Docker](https://www.docker.com/get-started) (optional, for containerized deployment)

### Cloning the Repository

```bash
git clone https://github.com/Sanskargupta0/Remove-bg.git
cd Remove-bg
```

### Installation

1. **Create a virtual environment**:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Download the AI Model** (Optional - will auto-download on first use):

```bash
# The U2-Net model will be automatically downloaded to ~/.u2net/
# Or manually download from: https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
```

### Environment Configuration

Create a `.env` file in the root directory:

```env
# Unsplash API key for sample images (optional)
UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here

# Port configuration (optional, defaults to 5000)
PORT=5000
```

### Running the Application

1. **Start the Flask development server**:

```bash
# Direct Python execution
python app.py

# Or using Flask CLI
set FLASK_APP=app.py  # Windows
export FLASK_APP=app.py  # macOS/Linux
flask run
```

2. Open your browser and navigate to `http://localhost:5000`

## 🐳 Docker Deployment

### Using Pre-built Docker Image

```bash
# Pull the official Docker image
docker pull sanskargupta0/remove-bg:remove-bg

# Run the container
docker run -p 5000:5000 -e UNSPLASH_ACCESS_KEY=your_key sanskargupta0/remove-bg:remove-bg
```

### Building from Source

```bash
# Build the Docker image
docker build -t remove-bg .

# Run the container
docker run -p 5000:5000 -e UNSPLASH_ACCESS_KEY=your_key  remove-bg
```

### Docker Compose (Optional)

Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  remove-bg:
    image: sanskargupta0/remove-bg:remove-bg
    ports:
      - "5000:5000"
    environment:
      - UNSPLASH_ACCESS_KEY=${UNSPLASH_ACCESS_KEY}
      - PORT=5000
    restart: unless-stopped
```

Run with: `docker-compose up -d`

## 🔐 Environment Configuration

### Application Settings

The application can be configured using environment variables:

```python
# Maximum file size per image (default: 2MB)
MAX_CONTENT_LENGTH = 2 * 1024 * 1024

# Unsplash API integration (optional)
UNSPLASH_ACCESS_KEY = "your_api_key_here"

# Server port configuration
PORT = 5000  # Default port
```

### File Processing Configuration

- **Maximum file size**: 2MB per image
- **Supported formats**: JPG, PNG, WEBP, and other PIL-supported formats
- **Output format**: PNG with transparency
- **Temporary storage**: System temp directory with automatic cleanup
- **AI Model**: U2netp (lightweight version of U2-Net)

## 🎯 Usage Guide

### Basic Usage

1. **Single Image Processing**:
   - Drag and drop an image or click to browse
   - Click "Upload & Process Image(s)" button
   - Download the processed image with transparent background

2. **Batch Processing**:
   - Select multiple images (up to system memory limits)
   - Process all images simultaneously
   - Download a ZIP file containing all processed images

3. **Sample Testing**:
   - Use the provided sample headshot images
   - Click any sample image for instant processing
   - Test the AI capabilities before uploading your own images

### Advanced Features

1. **API Integration**:
   - Direct API endpoint: `POST /remove-bg`
   - Multi-part form data with `images` field
   - Returns processed image or ZIP for multiple files

2. **Error Handling**:
   - File size validation with user feedback
   - Processing error recovery and retry
   - Network error handling for sample images

## 🏗️ Project Structure

```
Remove-bg/
├── app.py                        # Main Flask application
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
├── render.yaml                  # Render.com deployment config
├── README.md                    # Project documentation
├── .env                         # Environment variables (create manually)
├── templates/                   # Jinja2 templates
│   └── index.html              # Main application interface
└── u2net.onnx                  # AI model (downloaded automatically)
```

### Key Files Description

- **app.py**: Main Flask application with all routes and AI processing logic
- **templates/index.html**: Modern responsive frontend with TailwindCSS
- **Dockerfile**: Multi-stage Docker build with model pre-loading
- **requirements.txt**: Complete Python dependency list with versions
- **render.yaml**: Production deployment configuration for Render.com

## 🔄 Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py

# Run with debug mode
FLASK_ENV=development python app.py

# Build Docker image
docker build -t remove-bg .

# Run Docker container
docker run -p 5000:5000 remove-bg

# Check Python dependencies
pip list

# Update requirements
pip freeze > requirements.txt
```

## 🌐 Production Deployment

### Render.com Deployment

The application is configured for one-click deployment on Render.com:

1. **Connect your GitHub repository** to Render
2. **Use the provided render.yaml** for automatic configuration
3. **Set environment variables** in Render dashboard
4. **Deploy automatically** on code push

### Manual Production Deployment

1. **Prepare the environment**:
```bash
pip install -r requirements.txt
gunicorn -b 0.0.0.0:5000 app:app
```

2. **Configure environment variables**:
   - Set `UNSPLASH_ACCESS_KEY` for sample images
   - Configure `PORT` for custom port binding
   - Set production Flask settings

3. **Set up reverse proxy** (Nginx recommended):
```nginx
location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### Scaling and Performance

- **Horizontal Scaling**: Deploy multiple instances behind load balancer
- **Memory Management**: Monitor RAM usage during batch processing
- **Storage**: Implement persistent storage for large-scale deployments
- **CDN**: Use CDN for static assets and model files

## 🔒 Security Features

- **File Validation**: Strict file type and size checking
- **Temporary Storage**: Automatic cleanup of processed files
- **Memory Management**: Efficient handling of large image batches
- **Error Boundaries**: Graceful error handling and recovery
- **API Rate Limiting**: Protection against abuse (configure as needed)
- **CORS Configuration**: Secure cross-origin request handling

## 🎨 UI/UX Features

- **Responsive Design**: TailwindCSS framework for all screen sizes
- **Modern Interface**: Gradient backgrounds and glass effects
- **Interactive Elements**: Hover animations and loading states
- **Dark Mode Support**: Automatic system preference detection
- **Mobile Optimization**: Touch-friendly controls and layouts
- **Accessibility**: ARIA labels and keyboard navigation support

## 🔧 API Endpoints

### Main Endpoints:

- **`GET /`** - Main application interface
- **`POST /remove-bg`** - Background removal processing
- **`GET /get-random-images`** - Fetch sample images from Unsplash

### API Usage Examples:

```bash
# Single image processing
curl -X POST -F "images=@image.jpg" http://localhost:5000/remove-bg -o output.png

# Multiple images
curl -X POST -F "images=@image1.jpg" -F "images=@image2.jpg" http://localhost:5000/remove-bg -o output.zip
```

### Response Formats:

- **Single image**: PNG file with transparency
- **Multiple images**: ZIP file containing all processed images
- **Error responses**: JSON with error details and status codes

## 🚦 Troubleshooting

### Common Issues

1. **Model Download Issues**:
   - Check internet connection for initial model download
   - Verify sufficient disk space (~176MB for U2-Net model)
   - Manually download model to `~/.u2net/u2net.onnx` if needed

2. **Memory Issues**:
   - Reduce image sizes before processing
   - Process fewer images simultaneously
   - Increase system RAM or swap space

3. **File Upload Problems**:
   - Check file size limits (2MB per image)
   - Verify supported file formats
   - Ensure stable network connection

4. **Docker Issues**:
   - Verify Docker daemon is running
   - Check port availability (5000)
   - Ensure sufficient system resources

### Performance Optimization

- **Image Preprocessing**: Resize large images before upload
- **Batch Size**: Process 3-5 images simultaneously for optimal performance
- **Memory Monitoring**: Monitor system RAM during processing
- **Cache Management**: Clear browser cache if UI issues occur

## 📱 Browser Compatibility

The application is compatible with:
- **Chrome**: Version 80+
- **Firefox**: Version 75+
- **Safari**: Version 13+
- **Edge**: Version 80+

### Mobile Support:
- **iOS Safari**: Full functionality with touch support
- **Android Chrome**: Optimized for mobile processing
- **Responsive Design**: Adaptive layout for all screen sizes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 for Python code formatting
- Use meaningful variable and function names
- Add error handling for all file operations
- Ensure proper resource cleanup (temp files, memory)
- Test with various image formats and sizes

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Verify your environment meets the prerequisites
3. Review application logs for error details
4. Open an issue on GitHub with detailed error information

## 🔗 Live Demo & Resources

**Live Application**: [https://remove-bg-rv88.onrender.com/](https://remove-bg-rv88.onrender.com/)

**Docker Image**: `docker pull sanskargupta0/remove-bg:remove-bg`

**GitHub Repository**: [https://github.com/Sanskargupta0/Remove-bg](https://github.com/Sanskargupta0/Remove-bg)

### Quick Test Commands:

```bash
# Test the live application
curl -X POST -F "images=@test.jpg" https://remove-bg-rv88.onrender.com/remove-bg -o result.png

# Run locally with Docker
docker run -p 5000:5000 sanskargupta0/remove-bg:remove-bg
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🖼️ Use Cases & Applications

This application is perfect for:

- **E-commerce**: Product photography with clean backgrounds
- **Social Media**: Profile pictures and content creation
- **Marketing**: Professional headshots and promotional materials
- **Design**: Graphic design workflows and image composition
- **Photography**: Portrait enhancement and background replacement
- **Web Development**: Creating transparent images for websites

## 🔬 Technical Specifications

### AI Model Details:
- **Architecture**: U2-Net (U-Square Net)
- **Model Variant**: U2netp (lightweight version)
- **Input Resolution**: Variable (maintains aspect ratio)
- **Processing Time**: ~2-5 seconds per image
- **Model Size**: ~176MB
- **Accuracy**: High precision for human subjects and objects

### System Requirements:
- **RAM**: Minimum 2GB, Recommended 4GB+
- **Storage**: 1GB free space (for model and temp files)
- **CPU**: Multi-core processor recommended
- **Network**: Internet connection for model download and sample images

### 📸 Screenshots

#### Home Page
![Home Page](/screenshots/home-page.png)

#### Upload Interface
![Upload Interface](/screenshots/upload-interface.png)

#### Before Processing
![Before Processing](/screenshots/before-processing.png)

#### After Processing - Background Removed
![After Processing](/screenshots/after-processing.png)

#### Batch Processing with Multiple Images
![Batch Processing](/screenshots/batch-processing.png)

#### Sample Images Feature
![Sample Images](/screenshots/sample-images.png)

#### Mobile Responsive View
![Mobile View](/screenshots/mobile-view.png)


---

Built with ❤️ by [Sanskar Gupta](https://www.linkedin.com/in/sanskar-gupta-12476423b/) for AI-Powered Image Processing
