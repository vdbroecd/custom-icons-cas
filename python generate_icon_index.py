import os
import json

def generate_index(directory):
    """
    Doorzoekt alle mappen in 'directory' en maakt een index.json bestand aan per map.
    """
    for root, _, files in os.walk(directory):
        icons = [f for f in files if f.endswith(".svg")]
        if icons:  # Alleen een index maken als er SVG-bestanden zijn
            index_path = os.path.join(root, "index.json")
            with open(index_path, "w") as json_file:
                json.dump(icons, json_file, indent=4)
            print(f"✅ Index gegenereerd: {index_path}")

if __name__ == "__main__":
    generate_index("icons")  # Voer uit in de map waar 'icons/' staat
    print("🎉 Alle index.json bestanden zijn bijgewerkt!")
