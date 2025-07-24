import threading
import os


def search_keywords_in_files(files, keywords, results):
    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        if keyword not in results:
                            results[keyword] = []
                        results[keyword].append(file_path)
        except Exception as e:
            print(f"File error {file_path}: {e}")


def main(directory, keywords):
    # get files list
    files = [
        os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")
    ]

    # split file list
    num_threads = 4
    chunk_size = len(files) // num_threads
    threads = []
    results = {}

    for i in range(num_threads):
        # Defining a portion of files for a thread
        start_index = i * chunk_size
        end_index = None if i + 1 == num_threads else (i + 1) * chunk_size
        thread_files = files[start_index:end_index]

        # thread create and run
        thread = threading.Thread(
            target=search_keywords_in_files, args=(thread_files, keywords, results)
        )
        threads.append(thread)
        thread.start()

    # wait for threads execution
    for thread in threads:
        thread.join()

    return results


if __name__ == "__main__":
    keywords_to_search = ["Group", "stuff", "environment"]
    results = main("files", keywords_to_search)
    print("Результати пошуку:", results)
