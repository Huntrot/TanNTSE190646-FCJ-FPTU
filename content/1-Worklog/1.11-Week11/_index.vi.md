---
title: "Worklog Tuần 11"
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---
### Mục tiêu tuần 11:

* Hoàn thiện project BE.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Tham gia sự kiện **AWS Cloud Mastery Series #2**. | 17/11/2025   | 17/11/2025      | <> |
| 3   | - Chỉnh sửa code BE: <br>&emsp; + chuyển hoàn toàn sang Serverless gồm aws-serverless-java-container-springboot2 và DynamoDB Enhanced Client. | 18/11/2025   | 18/11/2025      | <> |
| 4   | - Chỉnh sửa code BE: <br>&emsp; + Dùng phương pháp Adapter Layer để chuyển đổi mySQL của database sang DynamoDB. | 19/11/2025   | 19/11/2025      | <> |
| 5-6   | - Chỉnh sửa code BE: <br>&emsp; + bỏ Adapter Layer vì nó làm BE tăng gấp đôi dữ liệu. <br> + Dùng cloud-native chuyển đổi hoàn toàn thành DynamoDB. | 20/11/2025   | 23/11/2025      | <> |


### Kết quả đạt được tuần 11:

### Kết quả đạt được tuần 11:
- Hoàn tất việc tham gia sự kiện **Cloud Mastery Series #2**, nắm vững các nội dung quan trọng: DevOps Mindset, CI/CD Pipeline, Monitoring & Observability với **CloudWatch** và **AWS X-Ray**.  
- Hiểu rõ pipeline workflow thực tế từ phần trình bày của diễn giả, áp dụng trực tiếp cho dự án backend.  
- Triển khai thành công backend trên **AWS Lambda** thông qua `aws-serverless-java-container-springboot2`.  
- Chuyển toàn bộ database từ **MySQL → DynamoDB**, xử lý đầy đủ model, repository, service.  
- Loại bỏ Adapter Layer để tránh dư thừa dữ liệu, tiếp cận theo hướng **cloud-native**, giảm độ phức tạp và tăng hiệu năng.  
- Fix nhiều lỗi liên quan đến DynamoDB Enhanced Client, NumberFormatException, và sửa lại toàn bộ model cho phù hợp KeySchema.  
- Backend đã chạy ổn định trên serverless, chuẩn bị cho bước tối ưu hoá chi phí và tuning DynamoDB.