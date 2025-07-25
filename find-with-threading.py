import threading
import os
import logging

# debug_mode = True
debug_mode = False

if debug_mode:
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
else:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def search_keywords_in_files(files, keywords, results):
    logging.debug(f"thread work with files: {files}")

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
            logging.error(f"File error {file_path}: {e}")


def find_t(directory, keywords):
    # get file list
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

        # create and run thread
        thread = threading.Thread(
            target=search_keywords_in_files, args=(thread_files, keywords, results)
        )
        threads.append(thread)
        thread.start()

    # wait for all threads complete
    for thread in threads:
        thread.join()

    return results


if __name__ == "__main__":
    keywords_to_search = ["standard", "public", "mission"]
    results = find_t("files", keywords_to_search)

    for keyword, paths in results.items():
        print(f"{keyword}: {paths}")
    # print("Search results:", results)
