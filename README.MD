
# KK-Tools Nodes for ComfyUI

This repository contains two custom nodes for ComfyUI: `KK-Tools 🎨 Prompt Blender` and `KK-Tools 🎨 StringSwitcher`. These nodes are designed to add flexibility and dynamic functionality to your prompts and string manipulation workflows.

## Table of Contents
- [KK-Tools 🎨 Prompt Blender](#kk-tools--prompt-blender)
  - [Installation](#installation)
  - [Usage](#usage)
- [KK-Tools 🎨 StringSwitcher](#kk-tools--stringswitcher)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## KK-Tools 🎨 Prompt Blender

### Installation
1. **Download/Clone the Repository** into your `custom_nodes` folder inside your ComfyUI directory.
2. Ensure the `styles.json` file is also placed alongside the `Prompt Blender` node for it to load style and artist data correctly.

### Usage
The `Prompt Blender` node allows you to dynamically blend styles into a prompt using a spintax format and style selection. 

1. **Inputs**:
   - `seed`: An integer value for reproducibility of random selections.
   - `prompt`: A spintax string, e.g. `{man,woman} {standing,sitting}, {holding,looking at} {dog,cat,flamingo}`.
   - `style_selection`: A dropdown with three options:
     - `Random`: Randomly selects a style and a random artist within that style.
     - `Off`: No style will be added.
     - A specific style: Allows you to select a specific art style, and a random artist from that style will be chosen.

2. **Output**:
   - Returns the spintax-processed prompt, optionally appended with a selected style and artist.

3. **Example**:
   If you input the prompt `{man,woman} {standing,sitting}, {holding,looking at} {dog,cat,flamingo}` and choose a specific style like `Impressionism`, the result might be:
   ```
   man standing, holding dog, Impressionism in the style of Claude Monet
   ```

---

## KK-Tools 🎨 StringSwitcher

### Installation
1. **Download/Clone the Repository** into your `custom_nodes` folder inside your ComfyUI directory.

### Usage
The `StringSwitcher` node is a powerful tool to map input strings to corresponding output strings based on defined pairs.

1. **Inputs**:
   - `input_string`: The string that will be checked against the defined input-output pairs.
   - `default_value`: The value returned if no match is found in the input-output pairs.
   - `input_1` to `input_10`: The input strings you want to match against.
   - `output_1` to `output_10`: The corresponding output strings for each input.

2. **Output**:
   - Returns the matched output string based on the provided input, or the default value if no match is found.

3. **Example**:
   If `input_1` is set to `apple` and `output_1` is set to `fruit`, and your `input_string` is `apple`, the result will be `fruit`.

---

## Contributing

Feel free to submit issues or pull requests if you have suggestions or want to improve the functionality of the nodes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
