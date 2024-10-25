class StringSwitcherNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_string": ("STRING", {"forceInput": True}),  # Connection point
                "default_value": ("STRING", {"multiline": True, "max_height": 100}),  # Control height of multiline
                "input_1": ("STRING",),  # Single-line input
                "output_1": ("STRING", {"multiline": True, "max_height": 100}),  # Control height of multiline
                "input_2": ("STRING",),
                "output_2": ("STRING", {"multiline": True, "max_height": 100}),
                "input_3": ("STRING",),
                "output_3": ("STRING", {"multiline": True, "max_height": 100}),
                "input_4": ("STRING",),
                "output_4": ("STRING", {"multiline": True, "max_height": 100}),
                "input_5": ("STRING",),
                "output_5": ("STRING", {"multiline": True, "max_height": 100}),
                "input_6": ("STRING",),
                "output_6": ("STRING", {"multiline": True, "max_height": 100}),
                "input_7": ("STRING",),
                "output_7": ("STRING", {"multiline": True, "max_height": 100}),
                "input_8": ("STRING",),
                "output_8": ("STRING", {"multiline": True, "max_height": 100}),
                "input_9": ("STRING",),
                "output_9": ("STRING", {"multiline": True, "max_height": 100}),
                "input_10": ("STRING",),
                "output_10": ("STRING", {"multiline": True, "max_height": 100}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"

    def process(self, input_string, default_value, input_1, output_1, input_2, output_2, input_3, output_3, input_4, output_4,
                input_5, output_5, input_6, output_6, input_7, output_7, input_8, output_8, input_9, output_9, input_10, output_10):
        # Define the input-output pairs
        input_output_pairs = [
            (input_1, output_1),
            (input_2, output_2),
            (input_3, output_3),
            (input_4, output_4),
            (input_5, output_5),
            (input_6, output_6),
            (input_7, output_7),
            (input_8, output_8),
            (input_9, output_9),
            (input_10, output_10)
        ]

        # Check if the input matches any of the defined inputs
        for in_val, out_val in input_output_pairs:
            if input_string == in_val:
                return (out_val,)

        # If no match, return the default value
        return (default_value,)


# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "KK-Tools 🎨 String Switcher": StringSwitcherNode
}
