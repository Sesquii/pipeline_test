
=====
PROMPT1: 
Write a complete, self-contained Python program that implements a "Procedural Dungeon Generator".

Requirements:

- The script should use a "cellular automata" algorithm to generate a text-based dungeon map.
- The map should be a grid of characters, where `#` represents a wall and `.` represents a floor.
- The script must be saved as `BATCH6_PROMPT1_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT2: 
Write a complete, self-contained Python program that implements a "Procedural Dungeon Generator".

Requirements:

- The script should generate a dungeon using a "drunkard's walk" algorithm.
- The script should take the number of steps for the walk and the size of the map as command-line arguments.
- The map should be printed as a grid of `+` (walls) and ` ` (floors).
- The program must be saved as `BATCH6_PROMPT2_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT3: 
Write a complete, self-contained Python program that implements a "Procedural Dungeon Generator".

Requirements:

- The script should use a "binary space partitioning" (BSP) algorithm to generate a simple, tree-structured dungeon layout.
- The output should be a text-based visualization of the split rooms, with connections marked by `~`.
- The program must be saved as `BATCH6_PROMPT3_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT4: 
Write a complete, self-contained Python program that implements a "Procedural Dungeon Generator".

Requirements:

- The script should generate a dungeon based on a "growing tree" algorithm, with a focus on creating long, winding corridors.
- The dungeon should be represented as a grid of characters, with walls (`#`) and floors (`.`).
- The program must be saved as `BATCH6_PROMPT4_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT5: 
Write a complete, self-contained Python program that implements a "Procedural Dungeon Generator".

Requirements:

- The script should create a dungeon by randomly placing rooms of different sizes on a grid and then connecting them with corridors.
- The output should be a text-based map.
- The program must be saved as `BATCH6_PROMPT5_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT6: 
Write a complete, self-contained Python program that implements a "Glitchy Image Compressor".

Requirements:

- The script should use the `Pillow` library.
- The script should take a JPG image file path as input.
- It should compress the image by selectively corrupting a random number of a random pixel's RGB values to 0.
- The output file must be saved as `<input_filename>_corrupt.jpg`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT7: 
Write a complete, self-contained Python program that implements a "Glitchy Image Compressor".

Requirements:

- The script should use the `imageio` library.
- The script should take a GIF file path as input.
- It should create a new GIF where every fifth frame is replaced with a single, solid-color frame (e.g., black or white).
- The output file must be saved as `<input_filename>_glitchy.gif`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT8: 
Write a complete, self-contained Python program that implements a "Glitchy Image Compressor".

Requirements:

- The script should use the `opencv-python` library.
- The script should take a video file path as a command-line argument.
- It should process the video frame-by-frame, and for every 50th frame, it should "glitch" it by shifting a random portion of the frame's pixels.
- The output file must be a new video saved as `<input_filename>_video_glitch.avi`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT9: 
Write a complete, self-contained Python program that implements a "Glitchy Image Compressor".

Requirements:

- The script should use the `Pillow` library.
- The script should take a PNG file path as input.
- It should "dither" the image by reducing its color palette to only 2-3 colors and then randomly swapping pixels with a different color from the reduced palette.
- The output file must be saved as `<input_filename>_dithered.png`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT10: 
Write a complete, self-contained Python program that implements a "Glitchy Image Compressor".

Requirements:

- The script should use `numpy` and `Pillow`.
- The script should take an image file path as input.
- It should convert the image to a NumPy array and then "glitch" it by randomly transposing or flipping 10% of the array's rows or columns.
- The output file must be saved as `<input_filename>_np_glitch.png`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT11: 
Write a complete, self-contained Python program that implements an "Unreliable API Simulator".

Requirements:

- The script should use the `aiohttp` library to create a flaky asynchronous API.
- It should have an endpoint `/data` that, 70% of the time, returns a valid JSON response and 30% of the time, raises a `TimeoutError`.
- The program must be saved as `BATCH6_PROMPT11_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT12: 
Write a complete, self-contained Python program that implements an "Unreliable API Simulator".

Requirements:

- The script should use a simple `socket` server to simulate a flaky, non-HTTP API.
- It should accept connections and, with a 40% chance, close the connection immediately without sending any data.
- 60% of the time, it should send back a random string of nonsensical data.
- The program must be saved as `BATCH6_PROMPT12_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT13: 
Write a complete, self-contained Python program that implements an "Unreliable API Simulator".

Requirements:

- The script should use the `Flask` library.
- It should have an endpoint `/status` that, with a 50% chance, returns a 200 OK with a random quote, and with a 50% chance, returns a 403 Forbidden with a brief, cryptic error message.
- The program must be saved as `BATCH6_PROMPT13_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT14: 
Write a complete, self-contained Python program that implements an "Unreliable API Simulator".

Requirements:

- The script should use the `FastAPI` library.
- It should have a single endpoint that accepts a POST request with a JSON payload.
- With a 30% chance, the API should respond successfully and echo the payload back.
- With a 70% chance, it should return a 422 Unprocessable Entity error, regardless of the input.
- The program must be saved as `BATCH6_PROMPT14_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT15: 
Write a complete, self-contained Python program that implements an "Unreliable API Simulator".

Requirements:

- The script should use a simple `http.server` from the standard library.
- It should have one endpoint that, with a 60% chance, returns an empty 200 OK response and, with a 40% chance, returns a 503 Service Unavailable error after a random delay of 1-5 seconds.
- The program must be saved as `BATCH6_PROMPT15_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT16: 
Write a complete, self-contained Python program that implements a "Fictional Language Encoder".

Requirements:

- The script should use a Vigenère cipher with a hard-coded key of `'GIBBERISH'` to encode a string of English text.
- The program must be saved as `BATCH6_PROMPT16_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT17: 
Write a complete, self-contained Python program that implements a "Fictional Language Encoder".

Requirements:

- The script should take a string of English text and encode it into a new "language" by replacing every vowel with the next consonant in the alphabet (e.g., 'a' -> 'b', 'e' -> 'f').
- The program must be saved as `BATCH6_PROMPT17_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT18: 
Write a complete, self-contained Python program that implements a "Fictional Language Encoder".

Requirements:

- The script should take a string of English text.
- It should encode the text into a binary representation where each character's ASCII value is written in a block of 8 bits, and then every third bit is randomly flipped.
- The program must be saved as `BATCH6_PROMPT18_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT19: 
Write a complete, self-contained Python program that implements a "Fictional Language Encoder".

Requirements:

- The script should take a string of English text as input.
- It should "encode" the text by translating it into Morse code but with a random delay between each character, and with a 10% chance of a random, incorrect dot or dash being added.
- The program must be saved as `BATCH6_PROMPT19_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT20: 
Write a complete, self-contained Python program that implements a "Fictional Language Encoder".

Requirements:

- The script should implement a substitution cipher where each letter is replaced by a corresponding emoji from a hard-coded dictionary.
- The program must be saved as `BATCH6_PROMPT20_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT21: 
Write a complete, self-contained Python program that implements a "Conversational Command Line Interface".

Requirements:

- The script should use the `Click` library to create a simple CLI.
- It should have a command that, when called, provides an overly enthusiastic welcome message and then asks the user a series of personal, unrelated questions.
- The program must be saved as `BATCH6_PROMPT21_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT22: 
Write a complete, self-contained Python program that implements a "Conversational Command Line Interface".

Requirements:

- The script should use a simple `input()` loop.
- The program should respond to user input by generating a random insult from a predefined list, regardless of what the user types.
- The program must be saved as `BATCH6_PROMPT22_{{model_name}}.py`.
- Ensure all dependencies are from Python's standard library unless explicitly specified.
- The code must be clean, well-commented, and include a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT23: 
Write a complete, self-contained Python program that implements a "Conversational Command Line Interface".

Requirements:

- The script should use the `cmd` module from the standard library to create a basic interpreter.
- It should have a few hard-coded commands (e.g., `greet`, `status`) that provide overly verbose, chatty, and unhelpful responses.
- The program must be saved as `BATCH6_PROMPT23_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT24: 
Write a complete, self-contained Python program that implements a "Conversational Command Line Interface".

Requirements:

- The script should use the `rich` library to create a CLI that uses colorful, verbose, and visually distracting output (e.g., progress bars that never finish, spinners that just spin forever).
- The program must be saved as `BATCH6_PROMPT24_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT25: 
Write a complete, self-contained Python program that implements a "Conversational Command Line Interface".

Requirements:

- The script should use `argparse` to define a single command-line argument.
- When the user provides the argument, the script should print a detailed, overly-complex help message that is completely unrelated to the argument itself.
- The program must be saved as `BATCH6_PROMPT25_{{model_name}}.py`.
- Ensure the code is self-contained, well-commented, and has a clear entry point.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
