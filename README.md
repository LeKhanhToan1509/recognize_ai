# AI_CN11

## Description
AI_CN11 is a project that includes face recognition capabilities with a FastAPI backend.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd AI_CN11
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Face Recognition Models Setup
The application requires pre-trained models for face detection and recognition. To set up the models:

1. Download the required model files using the provided script:
   ```bash
   python scripts/download_models.py
   ```
   This will download the SCRFD model and place it in the correct directory.

2. If you prefer to download the models manually:
   - Download the SCRFD model from [the official repository](https://github.com/deepinsight/insightface/tree/master/detection/scrfd)
   - Place the downloaded model file in: `backend/backend/src/tasks/weights/`

## Project Structure
- `/backend`: Contains the backend server code
- `/scripts`: Utility scripts for setup and maintenance
- `/backend/backend/src/tasks/weights`: Directory for model weights
- `/backend/backend/src/tasks/faceRecognization`: Face recognition modules

## Usage
1. Start the backend server:
   ```bash
   cd backend/backend/src
   python main.py
   ```
2. Access the API at `http://localhost:8000`

## API Endpoints
- `GET /`: Root endpoint
- `POST /add_persons/`: Upload face images and register a person
- `DELETE /delete_persons/`: Delete a person's records
- `POST /upload_video`: Upload video for processing

## Troubleshooting
If you encounter errors related to missing model files, run the model download script as described in the setup section.
