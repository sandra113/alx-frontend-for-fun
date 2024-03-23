import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    # Check if Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    
    # Convert Markdown to HTML
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown.markdown(markdown_content)
    
    # Write HTML content to output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)

