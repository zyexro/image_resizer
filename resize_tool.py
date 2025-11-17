import argparse
from PIL import Image
import os

def resize_image(input_path, output_path, width, height):
    """
    Resizes an image to the specified width and height and saves it.
    """
    try:
        # 1. Check if input file exists
        if not os.path.exists(input_path):
            print(f"Error: Input file not found at '{input_path}'")
            return

        # 2. Open the image
        img = Image.open(input_path)

        # 3. Resize the image
        print(f"Resizing image from {img.size} to ({width}, {height})...")
        resized_img = img.resize((width, height))

        # 4. Save the resized image
        resized_img.save(output_path)
        print(f"Success: Resized image saved to '{output_path}'")

    except Exception as e:
        print(f"An error occurred during resizing: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line tool to resize images."
    )
    parser.add_argument(
        "input_file",
        help="Path to the input image file."
    )
    parser.add_argument(
        "output_file",
        help="Path to save the resized output image file."
    )
    parser.add_argument(
        "--width",
        type=int,
        required=True,
        help="The desired width of the output image."
    )
    parser.add_argument(
        "--height",
        type=int,
        required=True,
        help="The desired height of the output image."
    )

    args = parser.parse_args()

    resize_image(args.input_file, args.output_file, args.width, args.height)

if __name__ == "__main__":
    main()
