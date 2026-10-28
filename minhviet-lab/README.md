BÁO CÁO QUY TRÌNH THỰC HÀNH LAB 06: BẢO MẬT VỚI DEVSECOPS

1. GIỚI THIỆU TỔNG QUAN

Bài thực hành hướng dẫn xây dựng và triển khai một ứng dụng web tĩnh bằng Docusaurus thông qua quy trình tự động hóa CI/CD (DevSecOps). Báo cáo này bao gồm toàn bộ các bước thực hiện từ môi trường cục bộ đến việc tích hợp và đẩy mã nguồn lên nền tảng lưu trữ.

2. CÁC BƯỚC THỰC HIỆN

Bước 1: Khởi tạo ứng dụng Docusaurus

Tạo và truy cập vào thư mục dự án trên máy cục bộ:

cd D:\minhviet-lab


Khởi tạo cấu trúc dự án Docusaurus và cài đặt các phụ thuộc (dependencies):

npm init docusaurus@latest . classic
npm install


Bước 2: Cấu hình ứng dụng (docusaurus.config.js)

Mở tệp docusaurus.config.js tại thư mục gốc và cập nhật các tham số đường dẫn tương ứng với repository:

URL: Địa chỉ trang web sẽ được lưu trữ (ví dụ: https://<username>.gitlab.io/ hoặc https://<username>.github.io/).

baseUrl: Tên repository hoặc đường dẫn gốc (ví dụ: /minhviet-2387700075/ hoặc /minhviet-lab/).

Bước 3: Cấu hình CI/CD Pipeline

Phương án A: Triển khai với GitLab CI/CD (.gitlab-ci.yml)

Tạo tệp .gitlab-ci.yml tại thư mục gốc dự án với nội dung cấu hình 2 giai đoạn (build và deploy):

stages:
  - build
  - deploy

build-job:
  stage: build
  image: node:18
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - build/

pages:
  stage: deploy
  script:
    - mv build/ public/
  artifacts:
    paths:
      - public/
  only:
    - main


Phương án B: Triển khai với GitHub Actions (.github/workflows/deploy.yml)

Tạo tệp deploy.yml bên trong thư mục .github/workflows/ với nội dung:

name: Deploy Docusaurus to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Build website
        run: npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build


Bước 4: Khởi tạo Git và Đẩy Mã Nguồn (Push Code)

Khởi tạo kho lưu trữ Git cục bộ và tạo commit đầu tiên:

git init
git add .
git commit -m "Initial commit: Docusaurus project with CI/CD configuration"
git branch -M main


Tạo Personal Access Token (PAT) trên nền tảng (GitLab/GitHub) với quyền write_repository để sử dụng làm mật khẩu xác thực HTTP.

Kết nối Remote Repository và đẩy code:

Đối với GitLab:

git remote add origin https://gitlab.com/vietnguyen-group2/minhviet-2387700075.git
git push -u origin main


Đối với GitHub:

git remote add origin https://github.com/<username>/minhviet-lab.git
git push -u origin main


3. GIÁM SÁT VÀ KIỂM TRA KẾT QUẢ

Kiểm tra Pipeline:

GitLab: Truy cập menu Build > Pipelines để theo dõi các job build-job và pages thực thi cho đến khi đạt trạng thái passed (xanh).

GitHub: Truy cập tab Actions trên Repository để xem tiến trình công việc Deploy Docusaurus to GitHub Pages.

Truy cập ứng dụng:

Sau khi pipeline hoàn tất, truy cập mục Deploy > Pages (trên GitLab) hoặc Settings > Pages (trên GitHub) để mở liên kết trang web Docusaurus đã được đưa lên sóng tự động.