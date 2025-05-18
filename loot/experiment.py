import subprocess
import os
import time

def run_nested_add_test(num_times=1000):
    executable_path = "./nested-add-test.run"

    start_time = time.time()
    for i in range(num_times):
        # Run the executable using subprocess.run()
        process = subprocess.run([executable_path], capture_output=True, text=True)

        # Check for errors.  Non-zero return code indicates an error.
        if process.returncode != 0:
            print(f"Error: Executable returned non-zero exit code: {process.returncode}")
            print(f"Run {i+1} failed. Exiting Loop.")
            return # Exit the loop on the first error.  You might want to continue, though.

    end_time = time.time()
    return (end_time - start_time)

if __name__ == "__main__":
    # Run the test 1000 times
    print(run_nested_add_test(num_times=1000))
    print("Finished running nested-add-test 1000 times.")
