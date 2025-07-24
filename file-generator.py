from faker import Faker
import os

fake = Faker()

num_files = 100
output_dir = "files"
os.makedirs(output_dir, exist_ok=True)

for i in range(num_files):
    random_text = fake.text()
    file_name = os.path.join(output_dir, f"file_{i + 1}.txt")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(random_text)

print(f'Згенеровано {num_files} текстових файлів у каталозі "{output_dir}".')
