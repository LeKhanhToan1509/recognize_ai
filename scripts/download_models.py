import os
import sys
import requests
from pathlib import Path
import shutil

# Get the absolute path to the project root
ROOT_DIR = Path(__file__).parent.parent

# Define paths for model weights - updated to match detector_config.py structure
WEIGHTS_DIR = ROOT_DIR / "backend" / "src" / "tasks" / "weights"

def download_file(url, dest_path):
    """
    Download a file from URL to destination path
    """
    print(f"Downloading {url} to {dest_path}...")
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Download with progress indication
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        block_size = 8192
        downloaded = 0
        
        with open(dest_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    done = int(50 * downloaded / total_size) if total_size > 0 else 0
                    sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {downloaded}/{total_size} bytes")
                    sys.stdout.flush()
    print("\nDownload complete!")

def main():
    # Create weights directory if it doesn't exist
    os.makedirs(WEIGHTS_DIR, exist_ok=True)
    
    print(f"Model weights will be downloaded to: {WEIGHTS_DIR}")
    
    # Download SCRFD model 
    scrfd_model_path = WEIGHTS_DIR / "scrfd_2.5g_bnkps.onnx"
    scrfd_model_url = "https://github.com/deepinsight/insightface/raw/master/detection/scrfd/models/scrfd_2.5g_bnkps.onnx"
    
    # Download ArcFace model
    arcface_model_path = WEIGHTS_DIR / "arcface_r100.pth"
    arcface_model_url = "https://github.com/deepinsight/insightface/raw/master/recognition/arcface_torch/ms1mv3_arcface_r100_fp16/backbone.pth"
    
    print("Starting download of face recognition models...")
    
    # Download SCRFD model
    if not os.path.exists(scrfd_model_path):
        try:
            download_file(scrfd_model_url, scrfd_model_path)
        except Exception as e:
            print(f"Failed to download SCRFD model: {e}")
            print("Please download it manually from the URL and place it in the weights directory.")
    else:
        print(f"SCRFD model already exists at {scrfd_model_path}")
    
    # Download ArcFace model
    if not os.path.exists(arcface_model_path):
        try:
            download_file(arcface_model_url, arcface_model_path)
        except Exception as e:
            print(f"Failed to download ArcFace model: {e}")
            print("Please download it manually from the URL and place it in the weights directory.")
    else:
        print(f"ArcFace model already exists at {arcface_model_path}")
    
    print("\nAll downloads complete!")
    print(f"Models are located at: {WEIGHTS_DIR}")
    print("If any downloads failed, please download the models manually from the URLs provided.")

if __name__ == "__main__":
    main()
