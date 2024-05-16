import cv2
import os

def convert_images(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                png_path = os.path.join(root, file)
                jpg_path = os.path.splitext(png_path)[0] + '.jpg'

                # Read the image
                image = cv2.imread(png_path)
                if image is not None:
                    # Convert and save the image in JPG format
                    cv2.imwrite(jpg_path, image)
                    # Optionally remove the original PNG file
                    os.remove(png_path)
                    print(f'Converted {png_path} to {jpg_path}')
                else:
                    print(f'Failed to read {png_path}, skipped conversion.')

# Assuming the root directory is the current directory
root_directory = 'images'
convert_images(root_directory)
