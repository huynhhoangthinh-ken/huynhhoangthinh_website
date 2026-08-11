import json
import random

posts = []

# Unsplash image collections for each category
img_bds = [
    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1600607687920-4e2a09be1587?auto=format&fit=crop&w=1200&q=80"
]
img_xe = [
    "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1503376713217-1014abfb0c3d?auto=format&fit=crop&w=1200&q=80"
]
img_du_thuyen = [
    "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?auto=format&fit=crop&w=1200&q=80"
]
img_may_bay = [
    "https://images.unsplash.com/photo-1540962351504-03099e0a754b?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1559087867-ce4c91325525?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1583416750470-965b2707b355?auto=format&fit=crop&w=1200&q=80"
]

data = [
    {"title": "Bất động sản siêu sang: Khi giới tinh hoa chọn phong cách sống cá nhân hoá", "cat": "bds"},
    {"title": "Du thuyền 2026: Hành trình kiến tạo những trải nghiệm vượt đại dương", "cat": "du_thuyen"},
    {"title": "Hypercar Thế Hệ Mới: Tốc Độ Và Nghệ Thuật Thiết Kế Đỉnh Cao", "cat": "xe"},
    {"title": "Penthouse The View: Định Nghĩa Lại Khái Niệm Sống Xa Xỉ Giữa Lòng Đô Thị", "cat": "bds"},
    {"title": "Private Jet: Kỷ Nguyên Mới Của Hàng Không Cá Nhân Hóa", "cat": "may_bay"},
    {"title": "Dinh Thự Ven Đảo: Xu Hướng Tìm Kiếm Không Gian Riêng Tư Tuyệt Đối", "cat": "bds"},
    {"title": "Bộ Sưu Tập Siêu Xe Phiên Bản Giới Hạn Mùa Hè 2026", "cat": "xe"},
    {"title": "Mega Yacht - Trải Nghiệm Nghỉ Dưỡng Chuyển Động Trên Biển", "cat": "du_thuyen"},
    {"title": "Khám Phá Nội Thất Bespoke Trong Các Dự Án Bất Động Sản Tỷ Đô", "cat": "bds"},
    {"title": "Chuyên Cơ Thương Gia Bán Chạy Nhất Quý 3/2026", "cat": "may_bay"},
    {"title": "Giá Trị Của Sự Độc Bản Trong Ngành Công Nghiệp Xa Xỉ", "cat": "xe"},
    {"title": "Villa Sinh Thái: Không Gian Xanh Cho Giới Siêu Giàu", "cat": "bds"},
    {"title": "Triển Lãm Du Thuyền Monaco 2026: Những Siêu Phẩm Bất Ngờ", "cat": "du_thuyen"},
    {"title": "Hành Trình Mua Siêu Xe Tại Châu Âu: Lời Khuyên Từ Chuyên Gia", "cat": "xe"},
    {"title": "Bất Động Sản Nghỉ Dưỡng Thụy Sĩ Thu Hút Giới Tinh Hoa Châu Á", "cat": "bds"},
    {"title": "Bảo Quản Siêu Xe Trong Các Garage Triệu Đô", "cat": "xe"},
    {"title": "Nghệ Thuật Chọn Rượu Vang Cho Những Buổi Tiệc Trên Du Thuyền", "cat": "du_thuyen"},
    {"title": "Thiết Kế Sân Đỗ Trực Thăng Cho Dinh Thự Đảo Ngọc", "cat": "bds"},
    {"title": "Tương Lai Của Công Nghệ Smart Home Trong Bất Động Sản Siêu Sang", "cat": "bds"},
    {"title": "Tại Sao Giới Thượng Lưu Đang Chuyển Hướng Đầu Tư Máy Bay Cá Nhân?", "cat": "may_bay"}
]

long_text = """
<p>Trong những năm gần đây, thị trường hàng xa xỉ toàn cầu chứng kiến sự thay đổi lớn. Khách hàng ngày càng yêu cầu sự cá nhân hóa tối đa và những đặc quyền không thể mua được bằng tiền. Cuộc cách mạng về công nghệ cũng như nhận thức về giá trị sống đã đẩy lùi những tiêu chuẩn cũ, thiết lập nên một kỷ nguyên mới nơi mà trải nghiệm độc bản là thước đo cao nhất của sự xa xỉ.</p>
<p>Nghiên cứu mới nhất từ các tập đoàn tư vấn hàng đầu cho thấy, giới siêu giàu không còn đơn thuần tìm kiếm những sản phẩm đắt tiền để phô trương. Thay vào đó, họ hướng tới những giá trị vô hình: sự riêng tư, tính độc nhất, và những câu chuyện đằng sau mỗi kiệt tác. Một chiếc siêu xe không chỉ là phương tiện di chuyển, mà là một tác phẩm nghệ thuật cơ khí. Một căn dinh thự không chỉ là nơi để ở, mà là một di sản để lại cho thế hệ sau.</p>
<img src="{img2}" alt="Minh họa bài viết" style="width:100%; border-radius:12px; margin: 30px 0;">
<h2>Chất Lượng Vượt Thời Gian và Thiết Kế Độc Bản</h2>
<p>Dù là một căn biệt thự, một chiếc siêu xe, hay một siêu du thuyền, yếu tố chất lượng và sự tỉ mỉ trong từng chi tiết luôn được đặt lên hàng đầu. Các nhà thiết kế và kỹ sư hàng đầu thế giới đang phải vượt qua những giới hạn của chính mình để đáp ứng những yêu cầu khắt khe nhất. Từ việc sử dụng các vật liệu quý hiếm, công nghệ chế tác thủ công truyền thống kết hợp với kỹ thuật hiện đại, cho đến việc cá nhân hóa từng đường kim mũi chỉ, mọi thứ đều phải đạt mức hoàn hảo tuyệt đối.</p>
<p>Chính sự giao thoa giữa nghệ thuật và kỹ thuật này đã tạo ra những sản phẩm vượt thời gian. Những kiệt tác này không bị lỗi thời theo năm tháng, mà ngược lại, giá trị của chúng càng tăng lên cùng với thời gian. Chúng trở thành những biểu tượng của quyền lực, gu thẩm mỹ và phong cách sống của người sở hữu.</p>
<div class="pull-quote">Sự xa xỉ đích thực không nằm ở mức giá, mà ở những giá trị độc bản không thể sao chép. Nó là sự tinh tế, là nghệ thuật sống, là cảm giác thuộc về nơi thực sự thuộc về bạn.</div>
<p>Thị trường Việt Nam cũng không nằm ngoài xu hướng này. Với sự gia tăng nhanh chóng của tầng lớp thượng lưu, nhu cầu đối với các sản phẩm xa xỉ độc bản đang bùng nổ. Tuy nhiên, khách hàng Việt Nam ngày càng có gu thẩm mỹ cao và sự hiểu biết sâu sắc về thị trường quốc tế. Họ không chỉ mua sản phẩm, mà còn mua cả một hệ sinh thái dịch vụ đẳng cấp đi kèm.</p>
<h2>Tương Lai Của Ngành Công Nghiệp Xa Xỉ</h2>
<p>Nhìn về tương lai, ngành công nghiệp xa xỉ sẽ tiếp tục chuyển mình mạnh mẽ. Công nghệ AI, thực tế ảo (VR) và blockchain đang mở ra những cách thức mới để trải nghiệm và sở hữu các sản phẩm cao cấp. Từ việc tùy chỉnh siêu xe thông qua nền tảng VR, cho đến việc xác thực nguồn gốc của các món đồ trang sức bằng blockchain, công nghệ đang làm cho thị trường này trở nên minh bạch và hấp dẫn hơn bao giờ hết.</p>
<p>Đồng thời, yếu tố phát triển bền vững cũng đang trở thành một tiêu chuẩn bắt buộc. Các thương hiệu xa xỉ đang nỗ lực giảm thiểu tác động đến môi trường, từ việc sử dụng vật liệu tái chế, năng lượng sạch cho đến việc hỗ trợ các cộng đồng địa phương. Giới siêu giàu ngày nay không chỉ muốn sở hữu những thứ tốt nhất, mà còn muốn đóng góp vào việc bảo vệ hành tinh xanh.</p>
<div class="key-takeaways">
  <h3>Key Takeaways</h3>
  <ul>
    <li>Xu hướng cá nhân hoá và trải nghiệm độc bản đang chi phối thị trường xa xỉ toàn cầu.</li>
    <li>Sự riêng tư, thiết kế bespoke và chất lượng vượt thời gian là những yếu tố quyết định.</li>
    <li>Khách hàng đòi hỏi dịch vụ tư vấn chuẩn quốc tế và hệ sinh thái đẳng cấp đi kèm.</li>
    <li>Công nghệ và tính bền vững sẽ là hai động lực chính thúc đẩy sự phát triển của ngành công nghiệp này trong tương lai.</li>
  </ul>
</div>
"""

for i, item in enumerate(data):
    if item["cat"] == "bds":
        images = img_bds
    elif item["cat"] == "xe":
        images = img_xe
    elif item["cat"] == "du_thuyen":
        images = img_du_thuyen
    else:
        images = img_may_bay
        
    main_img = random.choice(images)
    content_img = random.choice(images)
    
    post = {
        "id": i + 1,
        "title": item["title"],
        "date": f"{random.randint(1, 28)} TH8 2026",
        "image": main_img,
        "excerpt": "Cùng khám phá những góc nhìn sâu sắc và phân tích chuyên môn về thị trường phân khúc hàng xa xỉ, nơi định hình phong cách sống thượng lưu. Bài viết đi sâu vào phân tích xu hướng, thiết kế và những giá trị độc bản...",
        "content": long_text.format(img2=content_img)
    }
    posts.append(post)

with open("/Users/kenhuynh/.gemini/antigravity-ide/scratch/huynh-hoang-thinh-website/data/posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Created 20 long posts with matching Unsplash images in data/posts.json")
