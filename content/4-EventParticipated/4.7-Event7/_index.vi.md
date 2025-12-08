---
title: "Event 7"
weight: 1
chapter: false
pre: " <b> 4.7. </b> "
---

## Báo cáo sự kiện AWS Cloud Club – Security & Data Protection Workshop

### Mục đích của sự kiện
- Hiểu rõ tư duy **Incident Response** trong môi trường AWS.  
- Nắm các khái niệm cốt lõi về **Data Protection**, gồm mã hóa, quản lý khóa và giám sát truy cập.  
- Thực hành bảo mật dữ liệu với **AWS KMS** và theo dõi hoạt động bằng **AWS CloudTrail**.  
- Cải thiện kỹ năng làm việc nhóm thông qua hoạt động theo mô hình GameDay.  

---

### Danh sách diễn giả
- **Le Vu Xuan An** - AWS Cloud Club Captain HCMUTE, First Cloud Al Journey
- **Tran Duc Anh** - AWS Cloud Club Captain SGU, First Cloud Al Journey
- **Tran Doan Cong Ly** - AWS Cloud Club Captain PTIT, First Cloud Al Journey
- **Danh Hoang Hieu Nghi** - AWS Cloud Club Captain HUFLIT, First Cloud Al Journey
- **Nguyen Tuan Thinh** - Cloud Engineer Trainee, First Cloud Al Journey
- **Nguyen Do Thanh Dat** - Cloud Engineer Trainee, First Cloud Al Journey
- **Kha Van** - Cloud Security Engineer, AWS Community Builders
- **Thịnh Lâm** – FCJ Cloud Engineer  
- **Việt Nguyễn** – FCJ Cloud Engineer  
- **Mendel Grabski (Long)** – ex Head of Security & DevOps, Cloud Security Solutions Architect  
- **Tinh Truong** – AWS Community Builder, Platform Engineer tại TymeX  

---

### Nội dung nổi bật

#### Incident Response trong môi trường AWS
- Quy trình xử lý sự cố gồm các bước: **Detect → Analyze → Contain → Eradicate → Recover → Lessons Learned**.  
- Nhấn mạnh tầm quan trọng của phối hợp nhóm và phân công trách nhiệm.  
- Các ví dụ thực tế giúp hiểu rõ cách phát hiện và cô lập sự cố nhanh chóng.

#### Data Protection – Encryption & Key Governance
- Giải thích các hình thức mã hóa: **Encryption at Rest**, **Encryption in Transit**, và cách chúng được triển khai trong AWS.  
- Thực hành với **AWS Key Management Service (KMS)**:  
  - AWS owned CMK  
  - AWS managed CMK  
  - Customer managed CMK  
- Học cách thiết lập **Customer Managed Key** để kiểm soát lifecycle, rotation và giới hạn quyền truy cập.

#### KMS cho DynamoDB (phần tôi học được nhiều nhất)
- DynamoDB được mã hóa mặc định bằng AES-256.  
- So sánh sự khác biệt giữa các loại Key và lý do nên dùng Customer Managed Key cho sản phẩm thực tế.  
- Minh họa cách mỗi lần DynamoDB dùng key để “Decrypt” đều được ghi lại, giúp theo dõi được hoạt động nghi ngờ.

#### CloudTrail – Theo dõi & điều tra sự cố
- CloudTrail ghi lại mọi **AWS API Call** trong tài khoản.  
- Các tình huống demo giúp hiểu cách dùng CloudTrail để:  
  - theo dõi hành vi liên quan đến KMS,  
  - kiểm tra quyền truy cập IAM,  
  - phân tích truy cập vào dữ liệu trong S3 hoặc DynamoDB.  

---

### Trải nghiệm & Bài học cá nhân
- Đây là **lần đầu tiên tôi tham gia một sự kiện dạng GameDay**, và tôi học được rất nhiều điều mới.  
- Hoạt động nhóm giúp tôi hiểu rõ cách **phân chia nhiệm vụ theo độ khó**, đồng thời hỗ trợ lẫn nhau để giải quyết thử thách.  
- Nhờ workshop thực tế, tôi hiểu sâu hơn về cách mã hóa dữ liệu với KMS và truy vết hành vi bằng CloudTrail.  
- Nhận ra tầm quan trọng của teamwork trong bảo mật – một cá nhân không thể xử lý toàn bộ sự cố một mình.

---

### Kết quả đạt được
- Nắm rõ quy trình **Incident Response Framework** áp dụng trong dự án thật.  
- Thành thạo cách dùng **KMS cho DynamoDB** và quản lý khóa theo chuẩn bảo mật.  
- Có khả năng đọc và phân tích **CloudTrail logs** để điều tra sự cố.  
- Cải thiện kỹ năng làm việc nhóm, xử lý tình huống và tư duy phản ứng nhanh.  
- Tự tin hơn khi triển khai các biện pháp bảo vệ dữ liệu trong hệ thống thực tế.  

---

### Hình ảnh sự kiện
![Event7 Photo 1](/images/4-Events/Event7/1.jpg)  
![Event7 Photo 2](/images/4-Events/Event7/2.jng)  
![Event7 Photo 3](/images/4-Events/Event7/3.jpg)

> **Tóm tắt:** Sự kiện Security & Data Protection Workshop giúp tôi hiểu sâu hơn về bảo mật dữ liệu trên AWS—đặc biệt là KMS, CloudTrail và Incident Response. Đồng thời, đây là cơ hội tuyệt vời để rèn luyện làm việc nhóm thông qua mô hình GameDay và áp dụng kiến thức bảo mật vào thực tế.
