import os

# Paths (adjust to your setup)
SCRIPTS_DIR = "C:\Users\rudol\OneDrive\Documents\PIF\pipeline_test\Script_Factory\Script_Factory_Runs"
TESTS_DIR = "C:\Users\rudol\OneDrive\Documents\PIF\pipeline_test\Script_Factory\Tests"

# Your pytest-generation prompt template
PYTEST_PROMPT_TEMPLATE = """
You are a professional Python software engineer specializing in writing comprehensive unit tests using the pytest framework.
Your task is to generate a pytest test suite for the following Python script.

- Ensure every function has at least one test.
- Include a test for normal, expected inputs.
- Include at least one test for an edge case (e.g., empty lists, zero, negative numbers, null values).
- Include tests for any expected error handling or exceptions.
- Add clear comments explaining the purpose of each test.

Do not include any other text in your response, just the Python code for the test suite.

Here is the script to test:


"""

def main():
    # Ensure output directory exists
    os.makedirs(TESTS_DIR, exist_ok=True)

    for filename in os.listdir(SCRIPTS_DIR):
        if filename.endswith(".py"):
            filepath = os.path.join(SCRIPTS_DIR, filename)

            # Read the script content
            with open(filepath, "r", encoding="utf-8") as f:
                script_code = f.read()

            # Insert script into pytest prompt
            pytest_prompt = PYTEST_PROMPT_TEMPLATE.format(script_code=script_code)

            # Save prompt to file (you’ll paste into LM Studio / ChatGPT)
            test_filename = f"test_{filename}"
            test_filepath = os.path.join(TESTS_DIR, test_filename + ".prompt.txt")
            with open(test_filepath, "w", encoding="utf-8") as f:
                f.write(pytest_prompt)

            print(f"[+] Generated pytest prompt for {filename} → {test_filepath}")

if __name__ == "__main__":
    main()
