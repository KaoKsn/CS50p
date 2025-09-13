from PIL import Image, ImageOps
import sys
import os


def main():

    # Handle invalid command-line arguments.
    validate_command_line_args()

    image = open_img_file(sys.argv[1], sys.argv[2])

    process_image(image)

    # Close the image.
    image.close()


def validate_command_line_args():
    length = len(sys.argv)

    if length in [1, 2]:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")


def open_img_file(input_img, output_image):
    extensions = ['.jpeg', '.jpg', '.png']

    # Standardize extensions: foo.bar.JpeG
    input_file_ext = os.path.splitext(input_img)[1].lower()
    output_file_ext = os.path.splitext(output_image)[1].lower()

    # Handle invalid extensions.
    if input_file_ext != output_file_ext:
        sys.exit("Input and Output have different extensions!")

    elif not input_file_ext in extensions :
        sys.exit("Invalid file extension! Choose one of [JPEG, JPG, PNG]")

    # Check if file exists.
    try:
        return Image.open(input_img)
    except FileNotFoundError:
        sys.exit("Image does not exist")
    # Handle permission errors.
    except PermissionError:
        sys.exit("Can't open image, Permission Denied")


def process_image(img):
    #real_size = img.size

    with Image.open("shirt.png") as shirt:
        # Resize img to shirt.size
        img = ImageOps.fit(img, shirt.size)

        # Overlap the shirt onto the image.{Second shirt is the mask - what pixels to replace overlap with image in 'img'.}
        img.paste(shirt, shirt)

        # Resize to the original size.
        # img = ImageOps.fit(img, real_size)

        # Save the final image as a new image.
        try:
            img.save(sys.argv[2])
        except OSError:
            sys.exit("Problem encountered while saving the image :)")


if __name__ == "__main__":
    main()
