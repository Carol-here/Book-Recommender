
input_file = "tagged_description.txt"
output_file = "tagged_description_clean.txt"

with open(input_file, "r", encoding="cp1252", errors="ignore") as f:
    text = f.read()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ File converted to UTF-8 as tagged_description_clean.txt")
