def main():
    # Get complete file name.
    file = input("File name: ").strip().lower().split(".")

    file_len = len(file)
    # Look for no extension.
    if file_len == 1:
        print("application/octet-stream")
        return

    else:
        # Handle cases where extension of form " .foo" and files having multiple extensions.
        extension = file[file_len-1].strip()
        mime(extension)


# Print MIME type.
def mime(extension):
    match extension:
        case "gif" | "jpeg" | "jpg" | "png":
            print(f"image/{extension}") if extension != "jpg" else print(f"image/jpeg")

        case "pdf" | "zip":
            print(f"application/{extension}")

        case "txt":
            print("text/plain")

        # Any other file extension.
        case _:
            print("application/octet-stream")


if __name__ == "__main__":
    main()
