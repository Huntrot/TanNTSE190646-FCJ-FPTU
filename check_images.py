import os
import re
from pathlib import Path

# Đường dẫn gốc
root_dir = Path(__file__).parent
content_dir = root_dir / "content" / "5-Workshop"
static_dir = root_dir / "static"

# Tìm tất cả file markdown
md_files = list(content_dir.rglob("*.md"))

missing_images = []
found_images = []

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Tìm tất cả đường dẫn hình ảnh
    image_pattern = r'!\[.*?\]\((.*?)\)'
    images = re.findall(image_pattern, content)
    
    for img_path in images:
        # Bỏ qua URL external
        if img_path.startswith('http'):
            continue
            
        # Chuyển đường dẫn tương đối thành tuyệt đối
        if img_path.startswith('/'):
            full_path = static_dir / img_path.lstrip('/')
        else:
            full_path = md_file.parent / img_path
            
        # Kiểm tra file có tồn tại không
        if not full_path.exists():
            missing_images.append({
                'markdown': str(md_file.relative_to(root_dir)),
                'image': img_path,
                'expected': str(full_path.relative_to(root_dir))
            })
        else:
            found_images.append(img_path)

# In kết quả
with open('image_check_report.txt', 'w', encoding='utf-8') as report:
    report.write("=" * 80 + "\n")
    report.write(f"TOTAL MARKDOWN FILES: {len(md_files)}\n")
    report.write(f"TOTAL IMAGES FOUND: {len(found_images)}\n")
    report.write(f"TOTAL MISSING IMAGES: {len(missing_images)}\n")
    report.write("=" * 80 + "\n\n")
    
    if missing_images:
        report.write("MISSING IMAGES:\n\n")
        for item in missing_images:
            report.write(f"File: {item['markdown']}\n")
            report.write(f"  -> Reference: {item['image']}\n")
            report.write(f"  -> Expected path: {item['expected']}\n\n")
    else:
        report.write("ALL IMAGES EXIST!\n")

print(f"Report saved to: image_check_report.txt")
print(f"Total markdown files: {len(md_files)}")
print(f"Total images found: {len(found_images)}")
print(f"Total missing images: {len(missing_images)}")
