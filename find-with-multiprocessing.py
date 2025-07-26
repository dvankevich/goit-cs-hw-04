import os
from multiprocessing import Pool, Manager


def search_keywords_in_file(file_path, keywords):
    found_keywords = {keyword: [] for keyword in keywords}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    found_keywords[keyword].append(file_path)
    except Exception as e:
        print(f"File error: {file_path}: {e}")

    return found_keywords


def worker(file_paths, keywords):
    results = {}
    for file_path in file_paths:
        file_results = search_keywords_in_file(file_path, keywords)
        for keyword, paths in file_results.items():
            if paths:
                if keyword not in results:
                    results[keyword] = []
                results[keyword].extend(paths)
    return results


def find_m(directory, keywords):
    file_paths = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

    num_processes = os.cpu_count()
    # num_processes = 4
    # print("CPU count:", num_processes)
    chunk_size = len(file_paths) // num_processes + 1
    file_chunks = [
        file_paths[i : i + chunk_size] for i in range(0, len(file_paths), chunk_size)
    ]

    with Manager() as manager:
        with Pool(processes=num_processes) as pool:
            results = pool.starmap(worker, [(chunk, keywords) for chunk in file_chunks])

    final_results = {}
    for result in results:
        for keyword, paths in result.items():
            if keyword not in final_results:
                final_results[keyword] = []
            final_results[keyword].extend(paths)

    return final_results


if __name__ == "__main__":
    directory = "files"
    keywords = ["standard", "public", "mission"]
    results = find_m(directory, keywords)

    # for keyword, paths in results.items():
    #     print(f"{keyword}: {paths} len: {len(paths)}")

    # for results check run
    # find files -name "*.txt" -exec grep -H "mission" {} \; | wc -l

    print("Search results:", results)
