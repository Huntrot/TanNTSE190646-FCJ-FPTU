---
title: "Blog 1"
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

### **Thu nhận và làm giàu các phát hiện bảo mật được phân phối qua Amazon EventBridge với Dynatrace**

Tác giả: Shashiraj Jeripotula 

Ngày đăng: 06/05/2025 

Danh mục:  [Amazon Elastic Container Registry](https://aws.amazon.com/blogs/apn/category/compute/amazon-elastic-container-registry/), [Amazon EventBridge](https://aws.amazon.com/blogs/apn/category/application-integration/amazon-eventbridge/), [APN Launches](https://aws.amazon.com/blogs/apn/category/apn-launches/), [AWS Security Hub](https://aws.amazon.com/blogs/apn/category/security-identity-compliance/aws-security-hub/), [Partner solutions](https://aws.amazon.com/blogs/apn/category/post-types/partner-solutions/), [Technical How-to](https://aws.amazon.com/blogs/apn/category/post-types/technical-how-to/), [Thought Leadership](https://aws.amazon.com/blogs/apn/category/post-types/thought-leadership/)

Đồng tác giả:

Valeriy Leykin – Senior Product Manager, Dynatrace

Erick Leon – Senior Manager, Global Tech Alliances, Dynatrace

Shashiraj Jeripotula – Principal Partner Solutions Architect, AWS

Trong các môi trường điện toán đám mây phức tạp, các phát hiện bảo mật thường bị chia cắt (siloed) giữa các công cụ ở giai đoạn xây dựng (build-time) và giai đoạn chạy (runtime), đồng thời trải rộng trên nhiều môi trường khác nhau. Do vậy, việc đạt được một cái nhìn toàn diện về tư thế bảo mật (security posture) và các nguy cơ tiềm ẩn (risks) ngày càng trở nên khó khăn. Tuy nhiên, theo nghiên cứu của Gartner ([Gartner research](https://www.gartner.com/doc/reprints?id=1-2J3U8GY7&ct=241017&st=sb)), chưa đến 15% khách hàng doanh nghiệp lớn đã triển khai ít nhất một giải pháp nền tảng bảo mật (security platform solution).

Hệ quả có thể nhận thấy rõ ở các khía cạnh sau:

* **Truy cập dữ liệu (Data access):** Các nhóm bảo mật và kỹ sư phải truy cập và điều hướng qua nhiều sản phẩm khác nhau để thu thập dữ liệu bảo mật liên quan.

* **Ưu tiên xử lý (Prioritization)**: Các nhóm phát triển và vận hành rốt cuộc lại có cách ưu tiên khác nhau đối với các phát hiện bảo mật từ những công cụ DevSecOps rời rạc.

* **Bao phủ bảo mật (Security coverage):** Kiến trúc sư bảo mật không thể nhận diện rõ ràng những khoảng trống (gaps) trong phạm vi bao phủ công cụ của môi trường họ.

* **Công việc thủ công (Manual effort):** Việc thông báo đến các bên liên quan về **các** phát hiện bảo mật nghiêm trọng (critical security findings) đòi hỏi nhiều bước xử lý và điều phối thủ công.

* **Khắc phục (Remediation):** Các nhóm chịu trách nhiệm (owner teams) thường mất nhiều thời gian hơn để xử lý các vấn đề bảo mật quan trọng do tình trạng quá tải cảnh báo (alert fatigue), làm gia tăng thời gian khắc phục trung bình (Mean Time to Remediation – MTTR).

Hơn nữa, số lượng lớn các phát hiện bảo mật có thể khiến các nhóm DevSecOps bị quá tải, dẫn đến việc bỏ sót những vấn đề thực sự quan trọng có ảnh hưởng trực tiếp đến các dịch vụ và ứng dụng đang chạy trong môi trường sản xuất. Một ví dụ điển hình là lỗ hổng có mức độ nghiêm trọng cao được phát hiện trong một tạo phẩm ở giai đoạn build (build-time artifact), chẳng hạn như một container image chưa được triển khai và do đó không ảnh hưởng đến runtime. Những phát hiện dạng này không nên làm phân tán sự chú ý của nhóm DevSecOps. Thay vào đó, họ cần tập trung vào những lỗ hổng tồn tại trong các ứng dụng đang chạy trên môi trường sản xuất, vốn được phơi bày trực tiếp ra internet và mang lại rủi ro thực sự.

### **Làm thế nào một nền tảng quan sát và bảo mật hợp nhất có thể hỗ trợ**

Để giải quyết thách thức này, nền tảng quan sát và bảo mật hợp nhất [Dynatrace](https://www.dynatrace.com/) được tích hợp với  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) nhằm phá vỡ sự chia cắt (silos) giữa các nhóm DevSecOps, hợp nhất các phát hiện bảo mật xuyên suốt vòng đời phát triển phần mềm (Software Development Lifecycle – SDLC) và làm giàu chúng bằng bối cảnh vận hành thực tế (runtime context). Với công nghệ  [Dynatrace’s OpenPipeline](https://www.dynatrace.com/platform/openpipeline/), nền tảng này cho phép các nhóm thu nhận (ingest), trực quan hóa (visualize), ưu tiên xử lý (prioritize) và tự động hóa (automate) các phát hiện bảo mật, từ đó giảm thiểu “nhiễu” cảnh báo và tập trung vào việc khắc phục những vấn đề có ý nghĩa quan trọng đối với các môi trường sản xuất trọng yếu.

Nền tảng Dynatrace kết hợp giữa khả năng quan sát rộng và sâu cùng bảo mật ứng dụng liên tục với AIOps tiên tiến nhất, nhằm cung cấp câu trả lời và tự động hóa thông minh từ dữ liệu ở quy mô doanh nghiệp. Điều này cho phép các tổ chức đổi mới có thể hiện đại hóa và tự động hóa vận hành đám mây, triển khai phần mềm nhanh hơn và an toàn hơn, đồng thời mang lại trải nghiệm số hoàn hảo cho người dùng.

### **Tiếp nhận dữ liệu Amazon EventBridge vào nền tảng Dynatrace**

Dynatrace hợp tác với AWS ([Dynatrace partners with AWS](https://partners.amazonaws.com/partners/001E000000texmiIAA/Dynatrace)) và cung cấp nền tảng Dynatrace như một điểm đích (destination) cho các quy tắc (rules) của [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html#api-destination-dynatrace) . Tùy thuộc vào từng trường hợp sử dụng cụ thể, các phát hiện (findings) và nhật ký (logs) có thể được chuyển tiếp tới các điểm cuối OpenPipeline chuyên dụng (dedicated OpenPipeline endpoints) và được tiếp nhận (ingested) vào hồ dữ liệu [Grail](https://www.dynatrace.com/platform/grail/) (Dynatrace Grail data lake).

![image1](/images/3-BlogsTranslated/blog1/1.png)*Hình 1 – Tiếp nhận dữ liệu từ Amazon EventBridge*

Nền tảng Dynatrace hỗ trợ các phát hiện bảo mật được chuyển tiếp qua Amazon EventBridge trong những kịch bản (scenarios) sau:

* Chuyển tiếp từ công cụ bên thứ ba dưới dạng sự kiện thô (*raw events*) hoặc theo một định dạng dữ liệu tiêu chuẩn chung (generic standard data format) được hỗ trợ, chẳng hạn như [Open Cybersecurity Schema Framework](https://schema.ocsf.io/) (OCSF) hoặc [Amazon Security Findings Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) (ASFF).

* Chuyển tiếp từ  [AWS Security Hub](https://aws.amazon.com/security-hub/), bao gồm các sự kiện về lỗ hổng (vulnerability), phát hiện (detection) và tuân thủ (compliance).

* Chuyển tiếp dưới dạng phát hiện bảo mật container từ [Amazon ECR](https://aws.amazon.com/ecr/) (bao gồm cả quét cơ bản và nâng cao).

* Chuyển tiếp dưới dạng các phát hiện (detection findings) từ [Amazon GuardDuty](https://aws.amazon.com/guardduty/).

Là một phần của từng thiết lập tích hợp riêng lẻ (individual integration setup), nền tảng Dynatrace cung cấp các [CloudFormation templates](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws) cùng hướng dẫn chi tiết để hướng dẫn người dùng thực hiện các bước cấu hình.

Quy tắc Amazon EventBridge sẽ lắng nghe các sự kiện và kích hoạt hàm (function) AWS Lambda tương ứng để tiền xử lý (pre-process) và gửi chúng đến nền tảng Dynatrace, thông qua OpenPipeline.

Nền tảng Dynatrace sẽ ánh xạ (map) các sự kiện đã tiếp nhận sang các quy ước của Semantic Dictionary (Semantic Dictionary conventions) dành cho các sản phẩm và định dạng dữ liệu được hỗ trợ ( [supported products and data formats](https://dt-url.net/1d63p0v)). Bạn có thể khai thác (consume) các sự kiện theo cách thống nhất để trực quan hóa và phân tích trong dashboards và notebooks, cũng như cho các trường hợp tự động hóa (automation use cases) trong workflows.

Trong quá trình khai thác sự kiện (event consumption), người dùng có thể làm giàu (enrich) chúng bằng bối cảnh runtime do Dynatrace cung cấp. Điều này giúp người dùng hiểu rõ hơn về cách các sự kiện đó ảnh hưởng đến môi trường vận hành đang được giám sát, đồng thời hỗ trợ thúc đẩy việc ưu tiên thông minh (intelligent prioritization).

![image2](/images/3-BlogsTranslated/blog1/2.png)*Hình 2: Dashboard Bối cảnh hóa Runtime (Runtime Contextualization) của Dynatrace*

### **Tóm tắt**

Bằng việc tích hợp Amazon EventBridge với nền tảng Dynatrace, các nhóm DevSecOps có thể truy cập cả các phát hiện bảo mật (security findings) và bối cảnh vận hành (runtime context) trên một nền tảng duy nhất cho phép ưu tiên các phát hiện trên một nền tảng duy nhất, cho phép ưu tiên các phát hiện (detections) khác nhau đến từ nhiều môi trường và sản phẩm một cách hiệu quả hơn.

Các khả năng/tính năng gốc (native capabilities) bổ sung của nền tảng Dynatrace — chẳng hạn như  [Workflows](https://docs.dynatrace.com/docs/shortlink/workflows), [Dashboards](https://docs.dynatrace.com/docs/shortlink/dashboards), và [Security Investigator](https://docs.dynatrace.com/docs/shortlink/security-investigator) — hỗ trợ người dùng trong việc trực quan hóa, phân tích và tự động hóa các phát hiện bảo mật. Nhờ đó, người dùng có thể tiến gần hơn đến việc vận hành hóa (operationalizing) các phát hiện này, đồng thời giảm tải tình trạng quá tải cảnh báo (alert fatigue).

Để tìm hiểu thêm về từng tích hợp AWS và các trường hợp sử dụng tương ứng trong nền tảng Dynatrace, bạn có thể tham khảo tài liệu chính thức của Dynatrace:

* [Tiếp nhận các phát hiện lỗ hổng và sự kiện quét từ Amazon ECR](https://dt-url.net/tz03pa8)

* [Tiếp nhận các phát hiện bảo mật từ AWS Security Hub](https://dt-url.net/bl23u9i)

* [Tiếp nhận các phát hiện bảo mật từ Amazon GuardDuty](https://dt-url.net/jv03zhm)

Để theo dõi các cập nhật sản phẩm và các năng lực mới của Dynatrace, vui lòng tham khảo thêm các blog:

* [Làm giàu phát hiện lỗ hổng của AWS ECR bằng bối cảnh runtime](https://dt-url.net/9763wjo)

* [Tiếp nhận và làm giàu các phát hiện bảo mật được phân phối qua Amazon EventBridge với Dynatrace](https://dt-url.net/xn03wga)

* [Tiếp nhận và làm giàu các phát hiện từ AWS Security Hub với Dynatrace](https://dt-url.net/t703wux)

![image3](/images/3-BlogsTranslated/blog1/3.png)

### **Dynatrace – AWS Partner Spotlight**

Dynatrace là một AWS Advanced Technology Partner và AWS Competency Partner, cung cấp giải pháp trí tuệ phần mềm (software intelligence) nhằm đơn giản hóa sự phức tạp của điện toán đám mây và thúc đẩy quá trình chuyển đổi số (digital transformation). Với khả năng quan sát nâng cao (advanced observability), trí tuệ nhân tạo (AI) và tự động hóa toàn diện, nền tảng “tất cả trong một” (all-in-one platform) của chúng tôi (our) mang đến những câu trả lời (answers) — không chỉ là dữ liệu (data) — về hiệu năng của ứng dụng, hạ tầng cơ sở (underlying infrastructure), và trải nghiệm của mọi người dùng.

[Contact Dynatrace](https://partnercentral.awspartner.com/PartnerConnect?id=001E000000texmiIAA&source=Blog&campaign=)|[Partner Overview](https://partners.amazonaws.com/partners/001E000000texmiIAA/Dynatrace)|[AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=1422b3b0-b081-4af9-9d2b-34e6eb924f05)

TAGS: [APN Programs](https://aws.amazon.com/blogs/apn/tag/apn-programs/), [AWS Competency Partners](https://aws.amazon.com/blogs/apn/tag/aws-competency-program/), [AWS Marketplace](https://aws.amazon.com/blogs/apn/tag/aws-marketplace/)
