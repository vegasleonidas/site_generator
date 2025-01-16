import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    """
    Extracts the h1 header from the given markdown text.
    
    Args:
        markdown (str): The markdown content.
        
    Returns:
        str: The text of the h1 header without the leading # and extra whitespace.
        
    Raises:
        ValueError: If no h1 header is found in the markdown content.
    """
    for line in markdown.splitlines():
        line = line.strip()  # Remove leading and trailing whitespace
        if line.startswith("# "):  # Check if it's an h1 header
            return line[2:].strip()  # Remove '# ' and any additional whitespace
    raise ValueError("No h1 header found in the markdown content.")

def generate_page(from_path, template_path, dest_path):
    """
    Generates an HTML page from a markdown file and a template.
    
    Args:
        from_path (str): Path to the markdown file.
        template_path (str): Path to the template file.
        dest_path (str): Path to save the generated HTML file.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown content
    with open(from_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    # Read the template content
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract the title
    title = extract_title(markdown_content)
    
    # Replace placeholders in the template
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Write the generated HTML to the destination file
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generates HTML pages from markdown files in a directory structure.
    
    Args:
        dir_path_content (str): Path to the root content directory containing markdown files.
        template_path (str): Path to the template file.
        dest_dir_path (str): Path to the root directory where generated HTML files will be saved.
    """
    # Walk through the content directory
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            # Process only markdown files
            if file.endswith('.md'):
                # Construct full paths
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, dir_path_content)
                dest_sub_dir = os.path.join(dest_dir_path, relative_path)
                
                # Ensure destination subdirectory exists
                os.makedirs(dest_sub_dir, exist_ok=True)
                
                # Construct destination file path with .html extension
                dest_file_name = f"{os.path.splitext(file)[0]}.html"
                dest_path = os.path.join(dest_sub_dir, dest_file_name)
                
                # Generate the HTML page
                generate_page(from_path, template_path, dest_path)


