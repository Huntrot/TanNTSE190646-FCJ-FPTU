---
title: "Blog 3"
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---
### **Tối đa hóa Tác động Tiếp thị với Composable CDP được hỗ trợ bởi AI (AI-Driven) trên nền tảng GrowthLoop và AWS**

**Tác giả:** Harmeet Nandrey và Jas Singh  

**Ngày đăng:** Ngày 13 tháng 5, 2025

**Danh mục:**  [AWS Partner Network](https://aws.amazon.com/blogs/apn/category/aws-partner-network/), [Marketing & Advertising](https://aws.amazon.com/blogs/apn/category/industries/marketing-and-advertising/), [Partner solutions](https://aws.amazon.com/blogs/apn/category/post-types/partner-solutions/), [Thought Leadership](https://aws.amazon.com/blogs/apn/category/post-types/thought-leadership/)

**Đồng tác giả:**

Harmeet Nandrey – Global Partner Solutions Architect, AdTech/MarTech, AWS

Jas Singh – Enterprise Solutions Architect, AWS

Dakota Lovins – Partner Marketing Manager, GrowthLoop

Khai thác dữ liệu khách hàng (customer data) một cách hiệu quả là điều cần thiết cho sự thành công của tiếp thị (marketing) hiện đại. Việc này giúp các nhà tiếp thị hiểu rõ đối tượng khách hàng của họ, điều chỉnh thông điệp và ưu đãi, cũng như cải thiện trải nghiệm khách hàng. Bằng cách có được một cái nhìn duy nhất (single view), toàn diện và chính xác về dữ liệu khách hàng, các nhà tiếp thị có thể tạo ra những chiến dịch thực sự được cá nhân hóa (personalized), thúc đẩy doanh thu (revenue-driving). Tuy nhiên, việc tạo ra một cái nhìn dữ liệu thống nhất để hỗ trợ các nhà tiếp thị không hề dễ dàng.

![image1](/images/3-BlogsTranslated/blog3/1.png)

Theo truyền thống, các tổ chức thường dựa vào nền tảng dữ liệu khách hàng đóng gói  ([packaged customer data platforms (CDPs)](https://www.growthloop.com/university/article/customer-data-platform-cdp#what-is-a-customer-data-platform-cdp?utm_campaign=AWS&utm_source=AWS_Blog)) để quản lý dữ liệu khách hàng phục vụ cho nhu cầu tiếp thị. Tuy nhiên, các giải pháp này thường khó triển khai và có chi phí cao. Hơn nữa, các nền tảng này thường yêu cầu dữ liệu khách hàng phải được nhập vào hệ thống trước khi có thể sử dụng cho các chiến dịch và phân tích. Quy trình này vừa tốn thời gian, kém an toàn, lại dễ tạo ra sai lệch dữ liệu và các kho dữ liệu biệt lập (data silos).

Các tổ chức hiện nay đang tìm cách áp dụng một phương pháp tiếp thị hiệu quả và hiệu suất hơn (efficient and effective) bằng cách kích hoạt dữ liệu (activating data) trực tiếp từ Amazon Web Services (AWS), sử dụng phương pháp [composable CDP (Composable CDP approach)](https://www.growthloop.com/university/article/composable-cdp?utm_campaign=AWS&utm_source=AWS_Blog) cho phép các nhà tiếp thị:

*  Kích hoạt (Activate) dữ liệu khách hàng của họ thông qua phân khúc đối tượng mục tiêu ( [targeted audience segments](https://www.growthloop.com/products/audience-segmentation?utm_campaign=AWS&utm_source=AWS_Blog)) và điều phối hành trình đa kênh (cross-channel journey orchestration).

* Đo lường kết quả theo thời gian thực và điều chỉnh chiến lược dựa trên sự thay đổi của thị trường.

* Tận dụng công nghệ *vận hành bằng AI (AI-powered)* để *tối ưu hóa hiệu suất liên tục (continuous performance optimization)*.

Bài viết này sẽ khám phá (explore) Composable CDP là gì và lý do các tổ chức đang áp dụng (embracing) phương pháp mới này cho việc kích hoạt dữ liệu (data activation). Đồng thời, bài viết cũng giải thích cách các tổ chức có thể tích hợp nền tảng Composable CDP của GrowthLoop với hạ tầng AWS hiện có để cho phép một vòng phản hồi (feedback loop) vận hành bằng AI (AI-powered), giúp kích hoạt chiến dịch (campaign activation) thông minh hơn.

GrowthLoop là một Đối tác AWS ([AWS partner](https://partners.amazonaws.com/partners/0018W00002YjyApQAJ/Growthloop?utm_campaign=AWS&utm_source=AWS_Blog)) và Nhà bán hàng trên [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=889b5b80-e61e-402f-8779-224c4b0006a7&utm_campaign=AWS&utm_source=AWS_Blog) (AWS Marketplace Seller), kết hợp sức mạnh của đám mây dữ liệu Amazon Redshift (Amazon Redshift data cloud) với AI để chuyển đổi cách các doanh nghiệp xây dựng phân khúc đối tượng (audience segments), điều phối hành trình đa kênh (cross-channel journeys) và lặp lại/làm mới dựa trên kết quả chiến dịch (iterate on campaign results).

### **Những hạn chế của CDPs truyền thống**

Hơn hai phần ba số người trả lời (respondents) trong [Khảo sát Công nghệ Tiếp thị Gartner 2023](https://www.gartner.com/en/documents/5197663) (2023 Gartner Marketing Technology Survey) cho biết họ đã áp dụng một nền tảng dữ liệu khách hàng (customer data platform). Mặc dù được sử dụng rộng rãi, các CDP đóng gói truyền thống vẫn gặp phải nhiều thách thức, bao gồm:

* Dữ liệu được sao chép (replicated) trên CDP, kho dữ liệu (data warehouse) và các nền tảng tiếp thị (marketing platforms) khác mà tổ chức sử dụng. Điều này tạo thêm các kho dữ liệu biệt lập (data silos), dẫn đến dữ liệu không đầy đủ hoặc không nhất quán giữa các nguồn, hạn chế khả năng cung cấp thông điệp thống nhất.

* Việc sao chép dữ liệu (duplication of data) sang các nguồn bên ngoài (external sources) có thể dẫn đến (result in) rủi ro bảo mật (security risks) và các thách thức về tuân thủ dữ liệu (data compliance challenges) tiềm ẩn (potential).

* Thiếu khả năng mở rộng và linh hoạt, gây cản trở cho việc thử nghiệm.

* Chi phí cao và quy trình triển khai kéo dài, làm chậm đáng kể **việc thu hồi lợi tức đầu tư (ROI).**

* Sự phụ thuộc (reliance) của đội ngũ tiếp thị (marketing team) vào nhóm kỹ thuật (engineering teams) để trích xuất (pull) dữ liệu khách hàng liên quan (relevant customer data). Quy trình này làm chậm tiến độ của các nhà tiếp thị (slows marketers) và khiến kỹ sư bị phân tán (diverts) khỏi việc giải quyết các vấn đề phức tạp và mang tính sống còn với doanh nghiệp (business-critical).

Những giải pháp truyền thống này làm giảm (reduce) hiệu quả tiếp thị (marketing efficiency), tính cá nhân hóa (personalization) và hiệu suất (performance) Khi không có cái nhìn khách hàng hợp nhất và toàn diện, các tổ chức buộc phải thiết kế chiến dịch dựa trên dữ liệu phân mảnh từ nhiều nguồn khác nhau.

Để giải quyết (resolve) các thách thức trên, các tổ chức đang thúc đẩy (pushing for) những giải pháp mới giúp đơn giản hóa (simplify) vận hành (operations), giảm chi phí (decrease costs) và cung cấp quyền truy cập đầy đủ (complete access) vào dữ liệu sở hữu trực tiếp ([first-party data](https://www.growthloop.com/university/article/first-party-data?utm_campaign=AWS&utm_source=AWS_Blog)).

### **Composable CDP của GrowthLoop trên Amazon Redshift**

GrowthLoop là một [Composable CDP](https://www.growthloop.com/post/aws-customer-data-platform-guide?utm_campaign=AWS&utm_source=AWS_Blog) **được hỗ trợ bởi** Amazon Redshift. Nền tảng của GrowthLoop hoạt động trực tiếp trên dữ liệu của Amazon Redshift, sử dụng một **nguồn chân lý duy nhất (single source of truth)**, loại bỏ các thách thức về quản lý dữ liệu vốn tồn tại trong CDP truyền thống. Giải pháp này cũng cho phép các nhóm tiếp thị tận dụng toàn bộ dữ liệu khách hàng thông qua một giao diện trực quan, không cần viết code (no-code interface) – tất cả mà không cần dữ liệu rời khỏi kho dữ liệu đám mây (cloud data warehouse) Amazon Redshift của họ.

Tính dễ sử dụng (ease of use) của nền tảng Composable CDP của GrowthLoop cho phép các nhà tiếp thị tự phục vụ dữ liệu (self-serve data) và giúp họ diễn giải (interpret) kết quả từ các chiến dịch mà không cần dựa vào (relying on) kỹ sư dữ liệu (data engineers) hoặc các truy vấn SQL (SQL queries) phức tạp (intricate). Nhờ vậy, đội ngũ tiếp thị có thể **phân khúc đối tượng** (segment audiences) và kích hoạt các hành trình đa kênh phức tạp chỉ trong vài giờ, thay vì phải mất vài tuần hoặc vài tháng như trước.

Tiếp thị đầu cuối (End-to-end Marketing) trên đám mây dữ liệu của bạn để xây dựng đối tượng và điều phối hành trình khách hàng trên mọi nền tảng tiếp thị trong một giao diện người dùng duy nhất

![image2](/images/3-BlogsTranslated/blog3/2.png)*Hình 1: GrowthLoop composable CDP on Amazon Redshift*

Amazon Redshift giúp các tổ chức tập trung toàn bộ dữ liệu liên quan đến tiếp thị tại một nơi duy nhất, đồng thời cung cấp khả năng mở rộng (scalability) và hiệu suất (performance) cần thiết để thích ứng với nhu cầu kinh doanh luôn thay đổi. Sau đó, Composable CDP của GrowthLoop đóng vai trò như một lớp kích hoạt ([activation layer](https://www.growthloop.com/university/article/customer-data-activation?utm_campaign=AWS&utm_source=AWS_Blog)) trên Amazon Redshift, mang lại những lợi thế vượt trội so với các CDP đóng gói truyền thống.

Các tổ chức áp dụng Composable CDP có thể nhận được nhiều lợi ích, bao gồm:

* **Rút ngắn thời gian tạo ra giá trị (Accelerated time-to-value):** Nếu dữ liệu của công ty đã có trong Amazon Redshift, bạn có thể kích hoạt nền tảng GrowthLoop chỉ trong vài phút, tạo ra **ROI tức thì**.

* **Nguồn chân lý duy nhất (Single source of truth)**: Vì nền tảng GrowthLoop hoạt động trực tiếp trên Amazon Redshift, các tổ chức không cần thêm bộ nhớ dữ liệu hoặc sao chép bổ sung. Điều này tạo ra một bộ dữ liệu toàn diện, chính xác mà bất kỳ ai trong tổ chức cũng có thể khai thác.

* **Xây dựng đối tượng và điều phối hành trình tự phục vụ (Self-service audience building and journey orchestration**): Giao diện không cần mã (no-code), dễ sử dụng của GrowthLoop dân chủ hóa (democratizes) việc truy cập vào toàn bộ dữ liệu tiếp thị của bạn. Điều này có nghĩa là đội ngũ **tiếp thị** có thể nhanh chóng xây dựng đối tượng mục tiêu cho bất kỳ kênh tiếp thị nào và khởi chạy chiến dịch chỉ trong vài phút. Bên cạnh đó, bạn có thể tối đa hóa hiệu suất của các công cụ tiếp thị ưa thích bằng cách điều phối liền mạch [hành trình khách hàng đa kênh](https://www.growthloop.com/products/journeys?utm_campaign=AWS&utm_source=AWS_Blog) ([cross-channel customer journeys](https://www.growthloop.com/products/journeys?utm_campaign=AWS&utm_source=AWS_Blog)) tại mọi điểm đến.

GrowthLoop giúp các tổ chức khai thác toàn bộ tiềm năng dữ liệu khách hàng thông qua một Composable CDP năng động. Các tổ chức có thể dễ dàng tích hợp thông tin chi tiết của khách hàng (customer insights) trên nhiều điểm chạm (touchpoints), tự động hóa các luồng công việc (workflows) chính và mang lại các trải nghiệm siêu nhắm mục tiêu (hyper-targeted experiences).

### **Khai mở thành công với GrowthLoop**

Hãy cùng khám phá một số tính năng nổi bật khác của nền tảng GrowthLoop có thể nâng cao hiệu quả tiếp thị:

**Tận dụng sức mạnh của tiếp thị hợp nhất và tối đa hóa ROI với The Loop**

**Đội ngũ tiếp thị (Marketing teams)** cần có khả năng đo lường chính xác cách nỗ lực của họ thúc đẩy kết quả kinh doanh, bao gồm kênh nào và chiến thuật cá nhân hóa nào hoạt động hiệu quả nhất. Tuy nhiên, để đạt được điều này, các tổ chức phải có khả năng kết hợp dữ liệu kênh, dữ liệu khách hàng và dữ liệu mua hàng trên nền tảng đám mây để thực hiện phân tích toàn cảnh (“full-picture analysis”).

[**Tính năng The Loop** của GrowthLoop](https://www.growthloop.com/post/growthloop-launches-the-loop?utm_campaign=AWS&utm_source=AWS_Blog)tận dụng dữ liệu theo một cách hoàn toàn mới, đồng thời cho phép bạn giữ lại và tích hợp các khoản đầu tư công nghệ hiện có mà không cần phải đại tu hoàn toàn (overhaul). Tiếp thị dựa trên vòng lặp hợp nhất ([Unified-loop marketing](https://www.growthloop.com/post/closed-loop-marketing-vs-unified-loop-marketing?utm_campaign=AWS&utm_source=AWS_Blog)) trao quyền cho các nhóm sử dụng các công cụ ưa thích miễn là đáp ứng hai điều kiện:

1. Một lớp dữ liệu khách hàng thống nhất duy nhất trong kho dữ liệu đám mây (cloud data warehouse)

2. Một Composable CDP với khả năng đưa kết quả chiến dịch quay trở lại kho dữ liệu đám mây

Với dữ liệu được lưu trữ trên Amazon Redshift và Composable CDP của GrowthLoop, các nhà tiếp thị (marketers) của bạn có thể kích hoạt các chiến dịch mục tiêu trên tất cả kênh và hiểu được cách hiệu suất tiếp thị thúc đẩy kết quả kinh doanh. Họ cũng có thể tăng tốc tác động tiếp thị bằng các [insight](https://www.growthloop.com/products/measurement-and-insights?utm_campaign=AWS&utm_source=AWS_Blog) và gợi ý từ AI. Vòng lặp tiếp thị hợp nhất này giúp đội ngũ hiểu rõ cách từng kênh và từng nhóm khách hàng ảnh hưởng trực tiếp đến kết quả kinh doanh, từ đó họ có thể xây dựng chiến lược, xoay trục (pivot), và cải tiến (iterate) để đạt lợi tức đầu tư (ROI) tối đa.

![image3](/images/3-BlogsTranslated/blog3/3.png)

*Hình 2: Vòng lặp The Loop giúp tăng cường tác động tiếp thị*

Tiếp thị theo vòng lặp hợp nhất (Unified-loop marketing) cho phép các nhóm bắt đầu xây dựng phân khúc đối tượng (audiences) dựa trên nguồn chân lý duy nhất (single source of truth) của họ trên nhiều kênh, đồng thời học hỏi từ các chiến dịch này để cải tiến (iteration) nhanh hơn và có thông tin đầy đủ hơn (more informed). Những thông tin chi tiết (insights) này — khi được gửi trở lại kho dữ liệu đám mây (data cloud) Amazon Redshift — sẽ mở khóa tiềm năng to lớn cho AI trong việc khuếch đại (amplify) các nỗ lực tiếp thị của bạn.

Với quyền truy cập vào bộ sưu tập dữ liệu cụ thể của tổ chức, bao gồm thông tin đối tượng (audience information), dữ liệu mua hàng (purchase data), và phản hồi của từng nhóm đối tượng đối với các chiến dịch theo kênh trong Amazon Redshift, AI của GrowthLoop có thể cung cấp một loạt (suite) khuyến nghị – từ việc cải thiện chiến lược phân khúc, đến lựa chọn kênh (channel selection) trong tương lai, đến phân tích dự đoán (predictive analysis) để xác định những chiến dịch có khả năng đạt hiệu quả cao.

### **Phân khúc đối tượng bằng ngôn ngữ tự nhiên, được hỗ trợ bởi Amazon Bedrock**

Tính năng [**Computed Attributes**](https://www.growthloop.com/post/growthloop-launches-computed-attributes-generative-ai-feature-powered-by-aws?utm_campaign=AWS&utm_source=AWS_Blog) nâng cao của GrowthLoop — được cung cấp năng lực bởi AWS (powered by AWS) và xây dựng trên [Amazon Bedrock](https://aws.amazon.com/bedrock?utm_campaign=AWS&utm_source=AWS_Blog) — cho phép các nhà tiếp thị sử dụng ngôn ngữ tự nhiên để tạo phân khúc đối tượng (audience segments). Một nhà tiếp thị chỉ cần nhập (types out) các thuộc tính họ muốn sử dụng cho phân khúc hoặc cá nhân hóa đối tượng, và hệ thống sẽ sử dụng Amazon Bedrock để tự động tạo ra các trường tính toán (computed fields) chính xác.

![image4](/images/3-BlogsTranslated/blog3/4.png)

*Hình 3: Tính năng Computed Attributes sử dụng Amazon Bedrock*

Hãy xem xét một ví dụ: một nhà tiếp thị cần nhắm mục tiêu đến những khách hàng đã thực hiện từ một đến năm lần mua hàng trong năm vừa qua. Việc tạo phân khúc đối tượng phù hợp từ dữ liệu sở hữu trực tiếp (first-party data) có thể là một thách thức nếu không dành thời gian và nguồn lực để viết các truy vấn SQL tùy chỉnh. Tuy nhiên, với **tính năng [Computed Attributes](https://www.growthloop.com/post/growthloop-launches-computed-attributes-generative-ai-feature-powered-by-aws?utm_campaign=AWS&utm_source=AWS_Blog)** được **hỗ trợ bởi AI tạo sinh (generative AI)**, nhà tiếp thị chỉ cần nhập vào, “has between 2 and 10 purchases over the last 12 months” và trình xây dựng đối tượng (audience builder) của GrowthLoop sẽ ngay lập tức tạo ra các trường được tính toán (computed fields) để sử dụng trong phân khúc đối tượng hoặc hành trình khách hàng (customer journey) của chiến dịch. Cách tiếp cận này giúp các nhà tiếp thị triển khai các chiến dịch tiếp thị được cá nhân hóa cao, dựa trên dữ liệu, trong thời gian ngắn hơn đáng kể và với chi phí vận hành (overhead) thấp hơn đáng kể. Bên cạnh đó, toàn bộ thông tin về đối tượng (audience information) đều được đưa trở lại vòng lặp hợp nhất (unified loop), giúp kết quả tiếp thị liên tục được cải thiện theo thời gian.

**Kết luận**

Trong thế giới số phát triển nhanh chóng ngày nay, các tổ chức cần nắm toàn quyền kiểm soát đối với dữ liệu bên thứ nhất (first-party data) của mình để tối đa hóa giá trị dữ liệu. Các giải pháp truyền thống thường khiến việc tiếp nhận (ingest), lưu trữ (store) và kích hoạt dữ liệu (activate data) trên Amazon Redshift ở quy mô lớn trở nên khó khăn. Tuy nhiên, với Composable CDP của GrowthLoop *được xếp lớp (layered on top)* trên dữ liệu của bạn trong Amazon Redshift, các nhà tiếp thị có thể dễ dàng kích hoạt chiến dịch và hành trình khách hàng (campaigns and journeys). Họ có thể đo lường kết quả, liên tục tối ưu hóa chiến lược với AI, và mang lại hiệu quả cùng kết quả vượt trội. GrowthLoop tích hợp liền mạch với hạ tầng AWS hiện có và các công cụ tiếp thị khác, cho phép tổ chức nhanh chóng **hiện thực hóa (realize)** giá trị và tạo ra một vòng lặp hợp nhất (unified loop) liên tục (constantly) học hỏi và cải tiến.

Để bắt đầu với GrowthLoop, hãy [yêu cầu bản demo ngay hôm nay](https://www.growthloop.com/contact-us?utm_campaign=AWS&utm_source=AWS_Blog).

![image5](/images/3-BlogsTranslated/blog3/5.png)

### **GrowthLoop – AWS Partner Spotlight**

**GrowthLoop** là một **Đối tác AWS (AWS Partner)**, kết hợp sức mạnh của đám mây dữ liệu Amazon Redshift (Amazon Redshift data cloud) với trí tuệ nhân tạo (AI) nhằm chuyển đổi cách các doanh nghiệp xây dựng phân khúc khách hàng (audience segments), điều phối hành trình đa kênh (cross-channel journeys) và cải tiến dựa trên kết quả chiến dịch (iterate on campaign results).

[Contact GrowthLoop](https://partners.amazonaws.com/contactpartner?partnerId=0018W00002YjyApQAJ&partnerName=Growthloop) | [Partner Overview](https://partners.amazonaws.com/partners/0018W00002YjyApQAJ/Growthloop) | [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=889b5b80-e61e-402f-8779-224c4b0006a7&utm_campaign=AWS&utm_source=AWS_Blog)

**TAGS:** [Amazon Redshift](https://aws.amazon.com/blogs/apn/tag/amazon-redshift/), [Analytics](https://aws.amazon.com/blogs/apn/tag/analytics/), [AWS Partner Solution](https://aws.amazon.com/blogs/apn/tag/aws-partner-solution/), [Customer 360](https://aws.amazon.com/blogs/apn/tag/customer-360/), [Customer Data Platform](https://aws.amazon.com/blogs/apn/tag/customer-data-platform/)
