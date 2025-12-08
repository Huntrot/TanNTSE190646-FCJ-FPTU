# Hướng dẫn Deploy Hugo lên GitHub Pages

## Bước 1: Cập nhật config.toml
Mở file `config.toml` và thay đổi baseURL:
```toml
baseURL = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/"
```

Ví dụ:
- Nếu repo là `https://github.com/john/my-workshop` → baseURL = `"https://john.github.io/my-workshop/"`
- Nếu repo là `https://github.com/john/john.github.io` → baseURL = `"https://john.github.io/"`

## Bước 2: Push code lên GitHub
```bash
git add .
git commit -m "Setup GitHub Pages deployment"
git push origin main
```

## Bước 3: Cấu hình GitHub Pages
1. Vào repository trên GitHub
2. Vào **Settings** → **Pages**
3. Tại **Source**, chọn **GitHub Actions**

![GitHub Pages Settings](https://docs.github.com/assets/cb-47267/mw-1440/images/help/pages/publishing-source-drop-down.webp)

## Bước 4: Chờ deployment hoàn tất
- Vào tab **Actions** để xem quá trình build
- Khi có dấu ✅ màu xanh là đã deploy thành công
- Truy cập website tại URL đã cấu hình trong baseURL

## Test local trước khi deploy
```bash
# Build site
hugo

# Chạy server local
hugo server -D

# Truy cập http://localhost:1313
```

## Lưu ý
- Branch mặc định phải là `main` (hoặc sửa trong file `.github/workflows/hugo.yml`)
- Đảm bảo theme `hugo-theme-learn` đã được cài đặt trong thư mục `themes/`
- Nếu dùng submodule cho theme: `git submodule update --init --recursive`
