import random
import json
import os

class StyleBlenderNode:
    @classmethod
    def INPUT_TYPES(cls):
        # Add a dropdown selector for style, with "Random" and "Off" options
        return {
            "required": {
                "seed": ("INT", {"default": 42}),
                "prompt": ("STRING", {"multiline": True, "default": "{man,woman} {standing,sitting}, {holding,looking at} {dog,cat,flamingo}"}),
                "style_selection": (["Random", "Off"] + list(cls.load_style_names()), {"default": "Random"}),  # Style selector with Random, Off, and specific styles
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    OUTPUT_NODE = True

    @staticmethod
    def load_styles():
        # Load styles from styles.json
        styles_file = os.path.join(os.path.dirname(__file__), 'styles.json')
        try:
            with open(styles_file, 'r', encoding='utf-8') as f:  # Explicitly using UTF-8 encoding
                styles = json.load(f)
            return styles
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            return {"Error": [f"JSON decode error: {e}"]}

    @classmethod
    def load_style_names(cls):
        # Get style names from the styles.json file for dropdown selection
        styles = cls.load_styles()
        if "Error" in styles:
            return ["Error"]
        return list(styles.keys())

    def process(self, seed, prompt, style_selection):
        # Use the provided seed for style selection
        random.seed(seed)

        # Process the spintax in the prompt
        prompt = self.process_spintax(prompt)

        # Load the styles from JSON
        styles = self.load_styles()
        if "Error" in styles:
            return (f"Error loading styles: {styles['Error'][0]}",)

        # Handle style selection logic
        if style_selection == "Random":
            # Select a random style using the provided seed
            random_style_name = random.choice(list(styles.keys()))

            # Modify the seed by multiplying it by 2 for artist selection
            random.seed(seed * 2)

            # Select a random artist from the selected style
            random_artist = random.choice(styles[random_style_name])

            # Generate the result string with random style and artist
            generated_style = f"{random_style_name} in the style of {random_artist}"
            result = f"{prompt}, {generated_style}"

        elif style_selection == "Off":
            # No style selected, only return the spintax-processed prompt
            result = prompt

        else:
            # Specific style selected, use that style
            if style_selection in styles:
                random_artist = random.choice(styles[style_selection])
                generated_style = f"{style_selection} in the style of {random_artist}"
                result = f"{prompt}, {generated_style}"
            else:
                result = f"Error: Style {style_selection} not found."

        return (result,)

    def process_spintax(self, text):
        """
        Process spintax in the form of {option1,option2,option3}.
        """
        while True:
            start = text.find("{")
            end = text.find("}", start)
            if start == -1 or end == -1:
                break
            options = text[start + 1:end].split(",")
            chosen = random.choice(options)
            text = text[:start] + chosen + text[end + 1:]
        return text


# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "KK-Tools 🎨 Prompt Blender": StyleBlenderNode
}
