import os
import json

def list_images_in_folder(folder_path):
    # Get a list of all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files

def create_json_file(image_names, output_file):
    # Create a dictionary with a key "images" containing the list of image names
    data = {"images": image_names}

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data, indent=2)

    # Write the JSON string to a file
    with open(output_file, "w") as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    # Replace 'your_folder_path' with the actual path to your image folder
    folder_path = "img"

    # Replace 'output.json' with the desired name of your JSON file
    output_file = "output.json"

    # List all image names in the folder
    image_names = list_images_in_folder(folder_path)

    # Create and save the JSON file
    create_json_file(image_names, output_file)

    print(f"JSON file '{output_file}' created successfully.")
