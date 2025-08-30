🧠 LLM Code Generation & Evaluation Pipeline

This README provides an overview of a Python-based pipeline designed to evaluate the code generation capabilities of Large Language Models (LLMs). The project systematically generates, processes, and tests Python scripts to measure the success rate of code and unit test creation.

⚙️ Pipeline Components & Workflow

The pipeline is organized into a series of interconnected scripts, with a primary flow as follows:

    Code Generation (promptrunner.py)

        Purpose: The entry point of the pipeline. It reads a list of prompts from a batch of Markdown files, connects to a local LLM server (like LM Studio), and generates raw Python scripts based on these prompts.

        Functionality: Handles batch processing for multiple LLMs and organizes the raw output into a structured all_runs directory for subsequent processing.

    Preprocessing (preprocess_scripts.py)

        Purpose: Prepares the raw, generated scripts for test generation.

        Functionality:

            Copies and renames the generated scripts from the all_runs directory into a cleaner Script_Factory/Preprocessing folder.

            Fixes potential import issues and performs other minor, preliminary cleanups.

            This script ensures that the file paths and names are consistent for the next step.

    Test Generation (generate_tests_enhanced.py)

        Purpose: Automatically generates pytest unit tests for the preprocessed scripts.

        Functionality:

            Reads each preprocessed script.

            Crafts a new prompt that includes the original script and a request to generate unit tests for it.

            Sends this prompt to a designated "testing" LLM.

            Appends the newly generated test code to the original script, creating a single, comprehensive file.

            Saves the resulting file to the pytest_scripts directory.

    Cleanup (basic_cleanup.py & clean_test_files.py)

        Purpose: To remove extraneous, non-code text that LLMs often include in their output (e.g., conversational filler, code block markers).

        Functionality: These scripts use rule-based logic to "clean" the files so they are syntactically valid and can be executed without errors. This step is a critical bottleneck, and successful cleanup is essential for the rest of the pipeline to function.

    Test Execution & Aggregation (run_pytest_aggregator.py)

        Purpose: Runs the pytest framework on all the cleaned and tested scripts and aggregates the results into a final report.

        Functionality:

            Iterates through the files in the pytest_scripts directory.

            Executes pytest on each file, with a timeout to prevent infinite loops.

            Collects detailed metrics: number of scripts processed, passed tests, failed tests, and scripts with syntax errors or timeouts.

            Generates a final, comprehensive report saved to the misc_pytest_outputs folder, which includes a summary of performance by model and batch.

📈 Key Metrics & Project Goals

The primary goal of this pipeline is to answer the following questions:

    Which LLMs are most effective at generating usable, syntactically correct Python scripts?

    Which LLMs are best at generating robust, passing pytest unit tests for a given script?

    How do different prompts and models affect the final success rate of a generated script?

The pipeline measures success not just by a pytest pass rate but also by the percentage of generated scripts that can be successfully cleaned and run without syntax errors.

🚧 Future Improvements

    Enhanced Cleanup: The current cleanup scripts are a known weakness. A future improvement would be to use an LLM itself to perform the cleanup, providing it with syntax errors and asking it to correct the file.

    Automated Feedback Loop: Implement a system to automatically send files that fail the cleanup or testing stage back to an LLM with a debugging prompt, and then retry the process.

    Expanded Test Coverage: Broaden the scope of the generated prompts to include more standard programming tasks to get a more comprehensive evaluation of each LLM's general coding ability.