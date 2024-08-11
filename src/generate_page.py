import os
from markdown_to_html import markdown_to_html_node
from convert_text import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    content = open(from_path).read()
    template = open(template_path).read()
    template = template.replace("{{ Title }}", extract_title(content))
    template = template.replace("{{ Content }}", markdown_to_html_node(content).to_html())
    newfile = open(dest_path, "w")
    newfile.write(template)
    newfile.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Crawls every entry in the content directory, 
    # For each markdown file found, generates a new .html file using the same template.html. 
    # The generated pages are written to the public directory in the same directory structure.

    # Check if current path is file?
    #print(f"*** CURRENT PATH IS {dir_path_content}")
    #print("*** IS CURRENT PATH FILE?")
    if os.path.isfile(dir_path_content):
        #print("*** CURRENT PATH IS FILE")
        generate_page(dir_path_content, template_path, dest_dir_path.rstrip("md")+"html")
        #print(f"""*** GENERATED PAGE FOR {dir_path_content} at {dest_dir_path.rstrip("md")+"html"} using {template_path}""")

    #print("*** CURRENT PATH IS NOT FILE")
    # Check if current path is directory?
    if os.path.isdir(dir_path_content):
        #print("*** CURRENT PATH IS DIR")
        # Check that destination path exists and if not, create it
        if not os.path.exists(dest_dir_path):
            #print("*** DEST DIR DOES NOT EXIST")
            os.mkdir(dest_dir_path)
            #print(f"*** CREATED DEST DIR AT {dest_dir_path}")
        # Recursively run through each nested item
        
        for sub in os.listdir(dir_path_content):
            #print(f"*** RECURSING INTO {os.path.join(dir_path_content, sub)} WITH DEST DIR {os.path.join(dest_dir_path, sub)} USING {template_path}")
            generate_pages_recursive(
                os.path.join(dir_path_content, sub),
                template_path,
                os.path.join(dest_dir_path, sub)
                )