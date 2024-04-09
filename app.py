from extensionizer.manifest import manifestme, popup

def create_chrome_extension(name, version, description):
    # Create the manifest
    extension_manifest = manifestme(
        name=name,
        version=version,
        description=description
    )
    extension_manifest.add_permission("tabs")
    # extension_manifest.set_background({"scripts": ["background.js"]})
    # extension_manifest.add_content_script(matches=["<all_urls>"], js_files=["content_script.js"])
    extension_manifest.save_manifest()

    # Generate popup files
    popup_files_contents = popup.generate_files()
    for filename, content in popup_files_contents.items():
        with open(filename, 'w') as f:
            f.write(content)

def main():
    create_chrome_extension(name="MyExtension", version="1.0", description="My awesome Chrome extension")

if __name__ == "__main__":
    main()