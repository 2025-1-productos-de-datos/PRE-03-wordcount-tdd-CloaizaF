import os

def write_word_counts(output_folder, word_count):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in word_count.items():
            f.write(f"{key}\t{value}\n")
