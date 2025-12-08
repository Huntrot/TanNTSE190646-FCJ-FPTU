---
title: "Worklog Tuần 6"
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---



### Mục tiêu tuần 6:

* Hoàn thành lab của module 6, 7.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - **Thực hành:** <br>&emsp; + Module 06-lab5: Amazon Relational Database Service (Amazon RDS) account <br>&emsp; + Module 06-lab43 (bị lỗi không thể thực hành)                                                                                            | 14/10/2025   | 14/10/2025      | <https://000005.awsstudygroup.com/> |
| 3   |- Nghiên cứu chuyển đổi từ DynamoDB sang RDS (MySQL) cho proposal của nhóm. <br> - **Thực hành:** <br>&emsp; + Module 07-lab35: DataLake on AWS account                                            | 15/10/2025   | 15/10/2025      | <https://000035.awsstudygroup.com/> |
| 4   | - Tham gia sự kiện Data Science tại sảnh FPTU. <br> - Vẽ lại sơ đồ kiến trúc của project nhóm | 16/10/2025   | 16/10/2025      | <https://qhdn-hcmuni.fpt.edu.vn/2025/10/13/workshop-data-science-on-aws-mo-khoa-suc-manh-du-lieu-cung-dien-toan-dam-may/> |
| 5   | - Vẽ lại sơ đồ kiến trúc của nhóm again x7. <br> - **Thực hành:** <br>&emsp; + Module 07-lab40: Cost and performance analysis with AWS Glue and Amazon Athena| 17/10/2025   | 17/10/2025       | <https://000040.awsstudygroup.com/> |
| 6   | - Ôn tập cho thi giữa kỳ:<br>&emsp; + video "What is the AWS Well-Architected Framework?" <br>&emsp; + video "AWS re:Invent 2022 - AWS Well-Architected Framework security pillar: Cloud security @ scale (SUP309)"
" <br> - **Thực hành:** <br>&emsp; + Module 07-lab60: Work with Amazon DynamoDB| 18/10/2025   | 19/10/2025      | <https://www.youtube.com/watch?v=MpDJ6TCWKjk&t=1s> <br> <https://www.youtube.com/watch?v=nMxqziAibKk&t=3s> <br> <https://000060.awsstudygroup.com/> |

### Kết quả đạt được tuần 6:

- **Hoàn thành các bài thực hành của Module 6 và 7:**
  + Module 06-lab05: Nắm vững cách **tạo và quản lý Amazon RDS (MySQL)**, hiểu quy trình cấu hình subnet group, security group, và endpoint kết nối.  
  + Gặp lỗi kỹ thuật với Module 06-lab43, đã ghi nhận và tạm hoãn thực hành.  
  + Module 07-lab35: Thực hành **xây dựng Data Lake trên AWS** sử dụng S3, Glue, và Athena để quản lý và truy vấn dữ liệu phi cấu trúc.  
  + Module 07-lab40: Phân tích **chi phí và hiệu năng** thông qua AWS Glue và Athena; áp dụng bộ lọc để tối ưu hóa truy vấn dữ liệu.  
  + Module 07-lab60: Làm việc với **Amazon DynamoDB**, thực hành CRUD operation, Global Secondary Index (GSI) và auto-scaling.

- **Nghiên cứu kỹ thuật chuyển đổi từ DynamoDB sang RDS (MySQL)** cho proposal nhóm:
  + So sánh ưu – nhược điểm giữa NoSQL và Relational Database trong môi trường AWS.  
  + Đề xuất chiến lược migration: dùng AWS DMS (Database Migration Service) và lưu ý về schema conversion.

- **Cập nhật sơ đồ kiến trúc hệ thống của project nhóm:**
  + Bổ sung luồng dữ liệu giữa tầng ứng dụng và cơ sở dữ liệu (RDS).  
  + Làm rõ mối liên kết giữa các dịch vụ: S3, Lambda, API Gateway, và CloudFront.  
  + Chuẩn hóa ký hiệu và màu sắc để dễ phân biệt vai trò từng thành phần trong kiến trúc.

- **Tham gia sự kiện [Data Science on AWS – Mở khóa sức mạnh dữ liệu cùng điện toán đám mây]** tại sảnh FPTU:
  + Nắm bắt tổng quan về cách **AWS hỗ trợ xử lý dữ liệu quy mô lớn (Data Lake, Machine Learning pipeline)**.  
  + Hiểu mối liên hệ giữa phân tích dữ liệu và các dịch vụ AI/ML như SageMaker.

- **Ôn tập giữa kỳ:**
  + Củng cố kiến thức qua hai video trọng tâm:  
    ▫️ *"What is the AWS Well-Architected Framework?"* – Giới thiệu 5 trụ cột thiết kế tốt của AWS.  
    ▫️ *"AWS re:Invent 2022 - Security Pillar @ Scale"* – Làm rõ nguyên tắc bảo mật khi vận hành hệ thống AWS quy mô lớn.  
  + Ghi chú các điểm chính để chuẩn bị cho bài thi giữa kỳ (Midterm Assessment).
