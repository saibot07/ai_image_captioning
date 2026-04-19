# AI Image Captioning

AI Image Captioning is a Python tool that generates captions for images using OpenAI's CLIP and GPT models. It combines the power of computer vision and natural language processing to produce descriptive sentences for input images.

## Features
- Generates human-readable captions for images.
- Uses OpenAI's CLIP for image understanding and GPT for text generation.
- Simple and lightweight implementation.

## Requirements
- Python 3.9+
- Required Libraries:
  - OpenAI's `openai` library
  - `torch`
  - `Pillow`
- You must have an OpenAI API Key.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai_image_captioning.git
   cd ai_image_captioning
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage
To generate captions for an image, simply run:
```bash
python main.py --image_path path/to/your/image.jpg
```

## License
This project is licensed under the MIT License.