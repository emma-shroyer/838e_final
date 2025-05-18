import subprocess
import os
import time

def run_nested_add_test(num_times, filename):
    executable_path = f"./{filename}.run"

    start_time = time.time()
    for i in range(num_times):
        process = subprocess.run([executable_path], capture_output=True, text=True)

        if process.returncode != 0:
            print(f"Error: Executable returned non-zero exit code: {process.returncode}")
            print(f"Run {i+1} failed. Exiting Loop.")
            return

    end_time = time.time()
    return (end_time - start_time)

if __name__ == "__main__":
    times = [10000]
    for t in times:
        for f in ["vec_ref_500_sum-old", "vec_ref_500_sum"]:
            results = []
            for i in range(3):
                results.append(run_nested_add_test(t, f))

            print(f, t, sum(results) / len(results))
