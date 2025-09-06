import json
from django import template
from django.templatetags.static import static
from pathlib import Path

register = template.Library()

@register.simple_tag
def vite_asset(filename):
    manifest_path = Path('static/react/.vite/manifest.json')  # Correct path to manifest.json
    if manifest_path.exists():
        with open(manifest_path) as f:
            manifest = json.load(f)
        
        if filename in manifest:
            file = manifest[filename]["file"]
            return static(f'react/{file}')
        
        # If it's an entry with CSS (like index.html), look in the 'css' array
        if 'css' in manifest['index.html'] and filename == 'index.css':
            css_file = manifest['index.html']['css'][0]  # Get the first CSS file
            return static(f'react/{css_file}')
    
    return static(f'react/{filename}')