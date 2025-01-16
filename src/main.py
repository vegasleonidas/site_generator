import os
import shutil

from page_generation import generate_page


def delete_public_directory(public_dir):
    """
    Deletes everything in the public directory.
    
    Args:
        public_dir (str): Path to the public directory.
    """
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.makedirs(public_dir)

def copy_static_to_public(static_dir, public_dir):
    """
    Copies all static files from the static directory to the public directory.
    
    Args:
        static_dir (str): Path to the static directory.
        public_dir (str): Path to the public directory.
    """
    if not os.path.exists(static_dir):
        raise ValueError(f"Static directory '{static_dir}' does not exist.")
    shutil.copytree(static_dir, public_dir, dirs_exist_ok=True)

def main():
    public_dir = "./public"
    static_dir = "./static"
    content_file = "/home/vegasleonidas/site_generator/Content/index.md"
    template_file = "/home/vegasleonidas/site_generator/template.html"
    output_file = os.path.join(public_dir, "index.html")

    # Step 1: Delete anything in the public directory
    print(f"Deleting contents of {public_dir}...")
    delete_public_directory(public_dir)

    # Step 2: Copy static files to the public directory
    print(f"Copying static files from {static_dir} to {public_dir}...")
    copy_static_to_public(static_dir, public_dir)

    # Step 3: Generate a page from content/index.md using template.html
    print(f"Generating page from {content_file} to {output_file} using {template_file}...")
    generate_page(content_file, template_file, output_file)

    print("Website generation completed!")

main()