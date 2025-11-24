import os
import shutil
import json

with open("config.json", "r", encoding="utf-8") as f:
	categories = json.load(f)

def get_category(ext: str):
	ext = ext.lower()
	for category, extensions in categories.items():
		if ext in extensions:
			return category
	return "other"

def sort_folder(path: str):
	if not os.path.exists(path):
		print("Папка не найдена:", path)
		return

	for file in os.listdir(path):
		full_path = os.path.join(path, file)

		if os.path.isdir(full_path):
			continue

		ext = os.path.splitext(file)[1].replace(".", "")
		category = get_category(ext)

		target_dir = os.path.join(path, category)
		os.makedirs(target_dir, exist_ok=True)

		shutil.move(full_path, os.path.join(target_dir, file))
		print(f"Перемещено: {file} → {category}/")

print("Введите путь к папке:")
folder = input("> ")
sort_folder(folder)
