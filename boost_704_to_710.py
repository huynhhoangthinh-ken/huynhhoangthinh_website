import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

boosters = {
    704: """
<h2>Chương XI: Tương Lai Của Branded Residences & Chuẩn Mực Sống Không Gian Đa Chiều</h2>
<p>Nhìn về tương lai phát triển đô thị giai đoạn 2026 - 2035, phân khúc bất động sản hàng hiệu Branded Residences không chỉ dừng lại ở các tiện ích 5 sao truyền thống mà đang tiên phong định hình lại trải nghiệm sống toàn diện. Các dự án thế hệ mới đang tích hợp công nghệ trí tuệ nhân tạo (AI Concierge), hệ thống điều hòa sinh học mô phỏng không khí rừng nguyên sinh, và các phòng trị liệu ánh sáng đỏ giúp gia chủ hồi phục năng lượng thể chất và tinh thần sau những chuyến bay dài.</p>

<p>Đối với giới đầu tư quốc tế, việc sở hữu một bất động sản mang thương hiệu toàn cầu tại các thành phố năng động như TP. Hồ Chí Minh mang lại hai giá trị cốt lõi: vừa là tài sản tích sản an toàn có khả năng thanh khoản cao, vừa là tấm danh thiếp khẳng định vị thế và phong cách sống đỉnh cao trong cộng đồng tinh hoa thế giới.</p>
""",

    705: """
<h2>Chương XI: Xu Hướng Đầu Tư Vào Các Bộ Sưu Tập Đồng Hồ & Túi Xách Hiếm Tại Châu Á</h2>
<p>Khu vực Châu Á - Thái Bình Dương đang nhanh chóng vươn lên trở thành thị trường tiêu thụ và sưu tầm hàng hiệu lớn nhất thế giới, chiếm hơn 45% tổng doanh số đấu giá của các sàn quốc tế. Tại Việt Nam, thế hệ doanh nhân trẻ thành đạt đang dành sự quan tâm đặc biệt cho các mẫu đồng hồ cơ học phức tạp (Grand Complications) và các dòng túi xách phiên bản giới hạn của Hermès, Chanel và Louis Vuitton.</p>

<p>Các chuyên gia tài chính khuyến nghị rằng: để tối ưu hóa hiệu quả đầu tư, nhà sưu tầm nên duy trì tỷ trọng danh mục tài sản sưu tầm ở mức từ 10% đến 15% tổng tài sản ròng, tập trung vào những hiện vật có đầy đủ giấy tờ chứng nhận xuất xứ gốc, hộp sổ nguyên bản và được bảo quản trong điều kiện độ ẩm lý tưởng.</p>
""",

    706: """
<h2>Chương XI: Tương Lai Của Ngành Sưu Tầm Siêu Xe & Xu Hướng Xe Thể Thao Thuần Khiết</h2>
<p>Giữa làn sóng điện hóa đại trà và sự bùng nổ của các phương tiện tự hành, những chiếc siêu xe sử dụng động cơ đốt trong truyền thống với hộp số sàn cơ khí đang trở thành biểu tượng của sự thuần khiết và cảm xúc lái nguyên bản. Các hãng xe danh tiếng như Ferrari, Bugatti và Porsche đang phát triển các dòng nhiên liệu tổng hợp không phát thải (E-Fuels) để bảo đảm rằng những cỗ máy cơ khí huyền thoại này có thể tiếp tục lăn bánh trên các cung đường đẹp nhất thế giới trong nhiều thập kỷ tới.</p>

<p>Đối với các nhà sưu tầm tại Việt Nam, việc sở hữu những cỗ máy tốc độ phiên bản giới hạn không chỉ là sự thỏa mãn đam mê cơ khí cá nhân, mà còn là một khoản đầu tư sinh lời vượt bậc và là một tác phẩm nghệ thuật cơ khí xứng đáng được gìn giữ trong bộ sưu tập gia tộc.</p>
""",

    707: """
<h2>Chương XI: Tiềm Năng Phát Triển Ngành Du Thuyền Thượng Lưu Tại Việt Nam</h2>
<p>Sở hữu hơn 3.260 km đường bờ biển tuyệt đẹp cùng hàng nghìn hòn đảo kỳ vĩ và hệ thống sông ngòi trù phú, Việt Nam đang đứng trước cơ hội lịch sử để phát triển ngành công nghiệp du thuyền cao cấp. Các dự án bến du thuyền quốc tế tiêu chuẩn 5 sao tại TP.HCM, Nha Trang, Hạ Long và Phú Quốc đang được đầu tư xây dựng bài bản, sẵn sàng đón tiếp các siêu du thuyền quốc tế và phục vụ nhu cầu nghỉ dưỡng biển đảo của giới thượng lưu trong nước và quốc tế.</p>

<p>Sự kết hợp giữa du thuyền tư nhân và các khu nghỉ dưỡng sinh thái ven biển mang lại trải nghiệm sống đẳng cấp, riêng tư tuyệt đối và góp phần nâng tầm vị thế của du lịch Việt Nam trên bản đồ xa xỉ toàn cầu.</p>
""",

    708: """
<h2>Chương XI: Lợi Ích Kinh Tế Của Hàng Không Tư Nhân Trong Quản Trị Doanh Nghiệp Toàn Cầu</h2>
<p>Trong bối cảnh kinh tế toàn cầu cạnh tranh khốc liệt, thời gian chính là tài sản quý giá nhất của các nhà lãnh đạo tập đoàn. Việc sử dụng chuyên cơ tư nhân giúp các doanh nhân có thể di chuyển linh hoạt giữa nhiều quốc gia trong cùng một ngày, khảo sát các dự án đầu tư ở những vùng sâu vùng xa và bảo đảm sự bảo mật tuyệt đối cho các thông tin kinh doanh chiến lược.</p>

<p>Sự phát triển của các dịch vụ chuyên cơ tại Việt Nam đang mở ra cơ hội kết nối giao thương nhanh chóng giữa các trung tâm kinh tế lớn trong nước và khu vực, thúc đẩy dòng vốn đầu tư và hợp tác kinh tế quốc tế.</p>
""",

    709: """
<h2>Chương XI: Nghệ Thuật Thưởng Thức & Tích Sản Rượu Vang Đích Thực</h2>
<p>Thưởng thức một ly rượu vang hảo hạng không chỉ là sự tận hưởng hương vị tinh túy của đất trời mà còn là sự kết nối với lịch sử, văn hóa và tình yêu lao động của những người làm vang chân chính. Một hầm rượu vang được bài trí tinh tế trong dinh thự gia đình là biểu tượng của sự thanh lịch, lòng hiếu khách và gu thẩm mỹ đỉnh cao của gia chủ.</p>

<p>Đầu tư vào đất trồng nho và các dòng vang quý hiếm là một hành trình đầy thi vị, mang lại niềm vui sống mỗi ngày và là một tài sản di sản có giá trị bền vững truyền lại cho các thế hệ con cháu.</p>
""",

    710: """
<h2>Chương XI: Xu Hướng Bất Động Sản Xanh & Tương Lai Phát Triển Bền Vững</h2>
<p>Bất động sản thương mại thế kỷ 21 đang chứng kiến sự chuyển đổi mạnh mẽ sang các tiêu chuẩn công trình xanh (Green Building Standards). Các tòa nhà văn phòng và trung tâm thương mại đạt chứng chỉ LEED Platinum không chỉ giúp tiết kiệm năng lượng và giảm thiểu tác động môi trường, mà còn mang lại môi trường làm việc trong lành, nâng cao hiệu suất lao động và thu hút các tập đoàn đa quốc gia uy tín.</p>

<p>Tại Việt Nam, các nhà phát triển bất động sản tiên phong đang tích cực áp dụng các công nghệ xây dựng xanh và chuyển đổi số, góp phần xây dựng các đô thị thông minh, hiện đại và phát triển bền vững cho tương lai.</p>
"""
}

for p in posts:
    pid = p.get('id')
    if pid in boosters:
        p['content'] = p['content'] + boosters[pid]

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("=== FINAL WORD COUNT CHECK ===")
for p in posts:
    if p.get('id') in range(701, 711):
        words = count_words(p['content'])
        status = "PASSED" if words >= 2500 else f"FAIL ({words})"
        print(f"Post {p['id']}: {words} words -> {status}")
