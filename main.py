import argparse
import openai
from PIL import Image
import torch
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel

# Initialize model and processor
def initialize_model():
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    return model, processor

# Generate image embeddings
def get_image_features(image_path, model, processor):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    return image_features

# Generate caption using GPT
def generate_caption(image_features):
    description = f"This image contains: {str(image_features)}"
    prompt = f"Describe this image content:\n{description}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    caption = response.choices[0].text.strip()
    return caption

# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', required=True, help='Path to the input image')
    args = parser.parse_args()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set!")

    model, processor = initialize_model()
    image_features = get_image_features(args.image_path, model, processor)
    caption = generate_caption(image_features)
    print(f"Generated Caption: {caption}")

if __name__ == "__main__":
    main()