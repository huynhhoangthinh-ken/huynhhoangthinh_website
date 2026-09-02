# -*- coding: utf-8 -*-
"""
Master expansion for Post 609 (Gladia / Gladia Heights) to 2000+ words
and updating latest local images (Amanoi 804, Helicopter 18, Gladia galleries).
"""

import json
import os

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# 1. Update Post 804 (Amanoi Ninh Thuận)
for p in posts:
    if p.get('id') == 804:
        p['image'] = 'assets/Posts/amanoi/thumbnail_amanoi.avif'
        # Add gallery if not already present
        if 'assets/Posts/amanoi/' not in p.get('content', ''):
            amanoi_gallery = """
<div style="margin: 35px 0; text-align: center;">
    <img src="assets/Posts/amanoi/amanoi_1.avif" alt="Amanoi Ninh Thuận Vịnh Vĩnh Hy" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 8px;">Toàn cảnh khu nghỉ dưỡng Amanoi ẩn mình giữa thảm rừng nguyên sinh Vườn Quốc Gia Núi Chúa và bờ vịnh Vĩnh Hy</p>
</div>
<div style="margin: 30px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/Posts/amanoi/amanoi_7.avif" alt="Hồ bơi vách đá Cliff Pool Amanoi" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Cliff Pool ngoạn mục vươn ra biển trên độ cao 100m</p>
    </div>
    <div>
        <img src="assets/Posts/amanoi/amanoi_8.avif" alt="Biệt thự Pavilion Amanoi" style="width: 100%; height: 260px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Kiến trúc Pavilion truyền thống kết hợp chuẩn mực xa xỉ đương đại</p>
    </div>
</div>
"""
            if "<h2>Chương 1:" in p['content']:
                p['content'] = p['content'].replace("<h2>Chương 1:", amanoi_gallery + "\n<h2>Chương 1:")
            else:
                p['content'] = amanoi_gallery + p['content']

    # Fix broken image for Post 18
    if p.get('id') == 18:
        p['image'] = 'assets/Posts/Helicopter/thumbnail_Helicopter_3.jpg.webp'

# 2. Expand Post 609: Gladia / Gladia Heights to 2000+ words
gladia_content = """
<p class="lead" style="font-size: 1.25rem; line-height: 1.8; color: #333; margin-bottom: 30px; font-style: italic; border-left: 4px solid #b89b5e; padding-left: 20px;">
    Trong bức tranh phát triển sôi động của thị trường bất động sản hạng sang và siêu sang, <strong>Gladia (Gladia Heights)</strong> nổi lên như một biểu tượng kiêu hãnh của chuẩn mực sống tinh hoa đương đại. Không đơn thuần là một công trình nhà ở thông thường, Gladia được kiến tạo để trở thành chốn an cư độc bản – nơi sự xa xỉ kín đáo (Quiet Luxury), triết lý kiến trúc xanh nhiệt đới hòa quyện cùng hệ sinh thái tiện ích chuẩn resort 5 sao quốc tế, mang lại giá trị di sản vững bền truyền đời cho cộng đồng tinh hoa.
</p>

<div style="margin: 35px 0; text-align: center;">
    <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -54_NgoaiThat_KienTruc.jpg" alt="Kiến trúc tổng thể Gladia Heights" style="width: 100%; border-radius: 8px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 10px;">Diện mạo kiến trúc độc bản và đường nét hình khối thanh thoát của dự án Gladia</p>
</div>

<h2>Chương 1: Tầm Nhìn Định Vị & Triết Lý Sống Xa Xỉ Đương Đại</h2>
<p>
    Đối với giới siêu giàu (UHNWIs) và tầng lớp trí thức thượng lưu toàn cầu, định nghĩa về không gian sống xa xỉ trong kỷ nguyên mới đã vượt ra khỏi những hào nhoáng bề ngoài của đá cẩm thạch dát vàng hay các chi tiết chạm trổ phô trương. Thay vào đó, khái niệm "xa xỉ thực thụ" ngày nay được đo lường bằng chiều sâu của sự an yên, tính riêng tư tuyệt đối, chất lượng vi khí hậu và giá trị gắn kết bền vững của gia đình.
</p>
<p>
    <strong>Gladia Heights</strong> ra đời như một câu trả lời hoàn hảo cho khát vọng ấy. Được phát triển bởi đội ngũ tâm huyết của Đại Chúng Properties, dự án đặt mục tiêu xây dựng một "Sanctuary" – một thánh địa nghỉ dưỡng riêng tư giữa lòng phố thị, nơi chủ nhân có thể tái tạo năng lượng thể chất và tinh thần sau những giờ phút làm việc căng thẳng, đồng thời là không gian khẳng định vị thế kín đáo nhưng đầy kiêu hãnh của người sở hữu.
</p>
<p>
    Mỗi góc nhỏ tại Gladia đều được chăm chút dựa trên triết lý "Con người là tâm điểm của không gian sống". Từng luồng gió tự nhiên, từng tia nắng bình minh được tính toán khúc xạ qua hệ lam nhôm và thảm thực vật nhiệt đới, tạo nên một bản giao hưởng hài hòa giữa kiến trúc nhân tạo và thiên nhiên bản địa.
</p>

<div style="margin: 35px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -11_NgoaiThat_Flycam_TongThe.jpg" alt="Toàn cảnh Flycam dự án Gladia" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Tầm nhìn bao quát từ trên cao ôm trọn khuôn viên cảnh quan xanh</p>
    </div>
    <div>
        <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -27_NgoaiThat_KienTruc.jpg" alt="Đường nét ban công và hệ lam chắn nắng hiện đại" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Mặt đứng kính Low-E tràn viền kết hợp lam che nắng khí động học</p>
    </div>
</div>

<h2>Chương 2: Ngôn Ngữ Kiến Trúc Tropical Modernism & Tối Ưu Hóa Vi Khí Hậu</h2>
<p>
    Phong cách kiến trúc chủ đạo của Gladia là <strong>Tropical Modernism (Hiện Đại Nhiệt Đới)</strong> kết hợp tinh thần <strong>Biophilic Design (Thiết Kế Ưa Sinh Học)</strong>. Thay vì cô lập con người trong những khối bê tông kín mít và lạm dụng điều hòa nhiệt độ, các kiến trúc sư tại Gladia đã kiến tạo mặt bằng thông minh với các trục đối lưu không khí xuyên phòng (Cross-ventilation), giúp luồng gió mát tự nhiên luôn lưu chuyển nhẹ nhàng trong từng căn hộ và dinh thự.
</p>
<p>
    Điểm nhấn nổi bật nhất trong giải pháp kiến trúc mặt ngoài là hệ thống kính hộp Low-E 3 lớp dày dặn, vừa có khả năng ngăn chặn 99% tia cực tím (UV) có hại, vừa triệt tiêu bức xạ nhiệt mặt trời nhưng vẫn đảm bảo độ truyền sáng tự nhiên đạt mức tối ưu. Nhờ đó, không gian bên trong luôn tràn ngập ánh sáng tự nhiên tinh khiết mà không gây cảm giác chói chang hay nóng bức.
</p>
<p>
    Hệ thống loggia rộng lớn, ban công giật cấp và bồn cây âm sàn tạo nên một lớp vỏ cách nhiệt sinh học tự nhiên. Màu sắc ngoại thất được tinh tuyển với các gam màu trung tính sang trọng như màu xám ghi thanh lịch, màu be đá tự nhiên và màu nâu trầm ấm của gỗ nhân tạo siêu bền ngoài trời, giúp công trình giữ mãi vẻ đẹp trường tồn cùng thời gian mà không lo ngại sự phai mòn của khí hậu nhiệt đới gió mùa.
</p>

<div style="margin: 35px 0; text-align: center;">
    <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -23_CanhQuan_HoBoi.jpg" alt="Hồ bơi resort trung tâm tại Gladia" style="width: 100%; border-radius: 8px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 10px;">Hồ bơi phong cách resort vô cực với hệ thống lọc nước muối khoáng điện phân không hóa chất</p>
</div>

<h2>Chương 3: Tuyệt Tác Cảnh Quan Đa Tầng, Hồ Bơi Vô Cực & Vườn Thiền Zen Garden</h2>
<p>
    Bước chân vào Gladia, cư dân và khách quý như lạc bước vào một khu nghỉ dưỡng sinh thái cao cấp biệt lập hoàn toàn khỏi sự ồn ào, khói bụi của nhịp sống đô thị. Cảnh quan của dự án được quy hoạch theo mô hình <strong>Đa Tầng Sinh Thái (Multi-layered Ecosystem)</strong>:
</p>
<ul style="line-height: 2; margin-left: 24px; color: #444; margin-bottom: 25px;">
    <li><strong>Tầng Cây Bóng Mát:</strong> Những gốc cây cổ thụ tỏa bóng xanh mát, tạo bóng râm tự nhiên che phủ cho các trục đường nội khu và đường dạo bộ.</li>
    <li><strong>Tầng Bụi Trung & Hoa Cảnh:</strong> Sự phối trộn tinh tế của các loài hoa hương sắc nhiệt đới thay đổi theo mùa, mang lại cảm xúc thư thái và tràn đầy sinh khí.</li>
    <li><strong>Tầng Thảm Cỏ & Thủy Sinh:</strong> Thảm cỏ nhung xanh mướt trải dài, kết nối liền mạch với các tiểu cảnh mặt nước và đài phun nước róc rách suốt ngày đêm.</li>
</ul>
<p>
    Trái tim của hệ sinh thái cảnh quan chính là cụm <strong>Hồ Bơi Vô Cực Sinh Thái (Infinity Resort Pool)</strong>. Ứng dụng công nghệ điện phân muối khoáng tự nhiên nhập khẩu từ châu Âu, nguồn nước tại hồ bơi Gladia luôn trong vắt như pha lê, hoàn toàn không có mùi clo khó chịu, bảo vệ an toàn tuyệt đối cho làn da và đôi mắt của trẻ nhỏ và người cao tuổi. Xung quanh hồ bơi là các chòi nghỉ Cabana sang trọng lấy cảm hứng từ các resort danh tiếng tại Bali và Maldives, nơi chủ nhân có thể nằm thưởng thức ly cocktail thượng hạng trong tiếng nhạc du dương.
</p>

<div style="margin: 35px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -12_CanhQuan_SanVuon.jpg" alt="Lối dạo bộ nội khu lát đá tự nhiên" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Đường dạo bộ lát đá granite tự nhiên rợp bóng mát cây xanh</p>
    </div>
    <div>
        <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -35_CanhQuan_SanVuon.jpg" alt="Vườn thiền và tiểu cảnh tĩnh tâm" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Vườn thiền Zen Garden yên ắng dành riêng cho phút giây tĩnh tại</p>
    </div>
</div>

<h2>Chương 4: Nghệ Thuật Bài Trí Nội Thất May Đo (Bespoke Interior) & Vật Liệu Tự Nhiên</h2>
<p>
    Tiến vào không gian sống bên trong của Gladia, người trải nghiệm sẽ lập tức ấn tượng trước vẻ đẹp tinh tế của phong cách thiết kế nội thất "May Đo" (Bespoke). Mỗi căn hộ và dinh thự được thiết kế với trần cao thoáng đạt từ 3.4m đến 3.8m, tạo cảm giác mở rộng biên độ không gian tối đa.
</p>
<p>
    Khu vực phòng khách và phòng ăn được thiết kế liên thông theo trường phái mở (Open-plan Concept), tạo nên một đại sảnh tiếp khách bề thế và đầm ấm. Sàn nhà được lát bằng đá cẩm thạch Marble tự nhiên nguyên khối nhập khẩu từ Ý và Tây Ban Nha với những đường vân sống động độc bản không bao giờ trùng lặp. Các mảng tường ốp gỗ sồi tự nhiên, nhấn nhá bởi các chi tiết nẹp đồng mạ vàng Champagne tinh xảo mang lại nét sang trọng quyến rũ khó cưỡng.
</p>

<div style="margin: 35px 0; text-align: center;">
    <img src="assets/projects/12_GLADIA/Gladia Web Dai Chung50_NoiThat_PhongKhach.jpg" alt="Nội thất phòng khách sang trọng Gladia" style="width: 100%; border-radius: 8px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 10px;">Phòng khách rộng lớn với thiết kế thông tầng, đón trọn ánh sáng tự nhiên và view sân vườn xanh ngát</p>
</div>

<p>
    Gian bếp tại Gladia được ví như trái tim kết nối tổ ấm. Khu bếp khô và ướt được bố trí tách biệt chuẩn mực phong cách sống thượng lưu. Toàn bộ thiết bị bếp từ bếp từ, lò nướng, máy hút mùi âm trần cho đến tủ lạnh âm tủ đều đến từ các thương hiệu danh giá hàng đầu thế giới như Miele, Bosch, và Gaggenau. Mặt bàn bếp bằng đá thạch anh nhân tạo chống trầy xước và chống ố hoàn hảo, kết hợp bàn đảo dài sang trọng biến nơi nấu nướng thành sàn diễn ẩm thực đẳng cấp của gia chủ.
</p>

<div style="margin: 35px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/projects/12_GLADIA/Gladia Web Dai Chung1_NoiThat_NhaBep.jpg" alt="Không gian bếp chuẩn quốc tế" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Khu vực bếp sang trọng trang bị bàn đảo tiện nghi và tủ rượu chuyên dụng</p>
    </div>
    <div>
        <img src="assets/projects/12_GLADIA/Gladia Web Dai Chung21_NoiThat_PhongNgu.jpg" alt="Phòng ngủ Master Suite ấm cúng" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Phòng ngủ Master Suite sàn gỗ engineered êm ái cùng tủ quần áo Walk-in Closet</p>
    </div>
</div>

<p>
    Không gian phòng ngủ Master Suite là chốn riêng tư chuẩn mực với diện tích rộng rãi, tích hợp phòng thay đồ (Walk-in Closet) bằng kính mờ nghệ thuật và đèn LED cảm ứng thông minh. Phòng tắm Master được trang bị bồn tắm nằm ngâm mình hướng ra ban công xanh, sen tắm đứng mạ crom của Hansgrohe hoặc Axor, cùng thiết bị vệ sinh thông minh Duravit mạ men kháng khuẩn cao cấp, biến mỗi phút giây tắm gội thành trải nghiệm spa trị liệu đích thực ngay tại nhà.
</p>

<div style="margin: 35px 0; text-align: center;">
    <img src="assets/projects/12_GLADIA/Gladia Web Dai Chung10_NoiThat_VeSinh.jpg" alt="Phòng tắm spa cao cấp tại Gladia" style="width: 100%; max-width: 800px; margin: 0 auto; border-radius: 8px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);" />
    <p style="font-size: 0.85rem; color: #777; font-style: italic; margin-top: 10px;">Phòng tắm chuẩn spa sang trọng với bồn tắm độc lập và vật liệu đá cẩm thạch tự nhiên</p>
</div>

<h2>Chương 5: Tổ Hợp Tiện Ích Đặc Quyền Club House Chuẩn Khách Sạn 5 Sao Quốc Tế</h2>
<p>
    Đẳng cấp của một cộng đồng bất động sản siêu sang nằm ở hệ giá trị tiện ích độc quyền mà những dự án thông thường không thể có được. Tại Gladia, cư dân được tận hưởng một hệ sinh thái sống - làm việc - giải trí hoàn chỉnh khép kín bên trong khuôn viên:
</p>
<ul style="line-height: 2; margin-left: 24px; color: #444; margin-bottom: 25px;">
    <li><strong>The Gladia Club House:</strong> Không gian tiếp đón đối tác và bạn bè trang trọng, tích hợp quầy bar Lounge rượu vang và phòng thưởng thức xì gà Cigar Lounge riêng tư chuẩn thượng lưu.</li>
    <li><strong>Phòng Gym & Yoga Panorama:</strong> Trang bị 100% dàn máy tập thế hệ mới nhất của Technogym kết nối màn hình thông minh, hướng trọn tầm nhìn ra hồ bơi xanh mát.</li>
    <li><strong>Khu Vực BBQ Ngoài Trời & Tiệc Riêng:</strong> Bố trí tách biệt trong khuôn viên vườn hoa rực rỡ, sẵn sàng phục vụ các bữa tiệc gia đình ấm cúng dưới sự hỗ trợ của đội ngũ đầu bếp đối tác khi có yêu cầu.</li>
    <li><strong>Sân Chơi Sáng Tạo Trẻ Em (Kids Zone):</strong> Thiết kế bằng vật liệu cao su hạt EPDM đạt chuẩn an toàn quốc tế, giúp con trẻ thỏa sức vui đùa và phát triển thể chất toàn diện giữa thiên nhiên.</li>
</ul>

<div style="margin: 35px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
    <div>
        <img src="assets/projects/12_GLADIA/Gladia_Website_Photo -20_TienIch_DichVu.jpg" alt="Khu dịch vụ và sảnh tiếp đón cư dân" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Sảnh đón tiếp sang trọng và lễ tân chuyên nghiệp phục vụ 24/7</p>
    </div>
    <div>
        <img src="assets/projects/12_GLADIA/Gladia Web Dai Chung25_TienIch_DichVu.jpg" alt="Không gian giải trí và thư giãn đặc quyền" style="width: 100%; height: 270px; object-fit: cover; border-radius: 6px;" />
        <p style="font-size: 0.8rem; color: #777; font-style: italic; margin-top: 6px; text-align: center;">Không gian lounge thư giãn giao lưu dành riêng cho cư dân thượng lưu</p>
    </div>
</div>

<h2>Chương 6: Tiêu Chuẩn Quản Lý Vận Hành & An Ninh Bảo Mật Đa Lớp Tuyệt Đối</h2>
<p>
    Đối với những chủ nhân danh giá, sự an toàn và tính riêng tư của đời sống cá nhân là ưu tiên tối thượng. Thấu hiểu sâu sắc điều đó, Gladia thiết lập hệ thống an ninh 4 lớp ứng dụng công nghệ trí tuệ nhân tạo (AI):
</p>
<ol style="line-height: 2; margin-left: 24px; color: #444; margin-bottom: 25px;">
    <li><strong>Lớp 1 - Vành đai ngoại vi:</strong> Hệ thống cảm biến nhiệt và hàng rào điện tử hồng ngoại 24/7, kết hợp đội ngũ bảo vệ tuần tra liên tục tại các chốt kiểm soát cổng vào.</li>
    <li><strong>Lớp 2 - Kiểm soát ra vào nội khu:</strong> Nhận diện khuôn mặt FaceID không chạm và camera đọc biển số xe tự động, ngăn chặn tuyệt đối mọi trường hợp xâm nhập không phép.</li>
    <li><strong>Lớp 3 - Kiểm soát tầng và thang máy:</strong> Thẻ từ phân tầng thông minh và thang máy riêng biệt cho từng phân khu, đảm bảo không ai có thể tiếp cận tầng nhà bạn ngoài chính gia đình bạn.</li>
    <li><strong>Lớp 4 - Cửa thông minh Smart Lock:</strong> Tích hợp mở khóa đa phương thức (vân tay, mã số, chìa cơ và ứng dụng điện thoại mã hóa bảo mật cấp ngân hàng).</li>
</ol>
<p>
    Bên cạnh đó, dịch vụ quản gia cá nhân (Concierge Service) chuẩn phong cách khách sạn 5 sao quốc tế luôn sẵn sàng hỗ trợ cư dân từ việc đặt vé máy bay, xe đưa đón hạng sang, dịch vụ giặt ủi cao cấp cho đến quản lý căn hộ khi gia chủ vắng nhà dài ngày du lịch hoặc công tác nước ngoài.
</p>

<h2>Chương 7: Giá Trị Di Sản Bền Vững & Tiềm Năng Gia Tăng Bất Động Sản</h2>
<p>
    Không chỉ là một tổ ấm lý tưởng để tận hưởng cuộc sống mỗi ngày, sở hữu một sản phẩm tại Gladia Heights còn là một quyết định đầu tư tích sản chiến lược đầy thông minh. Bất động sản tại các vị trí đắc địa với số lượng giới hạn, chất lượng thi công đỉnh cao và cộng đồng cư dân văn minh luôn là kênh trú ẩn an toàn và có tốc độ tăng trưởng vốn vượt trội nhất qua mọi chu kỳ kinh tế.
</p>
<p>
    Gladia không đơn thuần là một tài sản có thể định giá bằng tiền bạc, mà là một "Tài Sản Di Sản" (Legacy Asset) mang niềm tự hào truyền đời cho thế hệ con cháu tương lai. Nơi nuôi dưỡng những kỷ niệm gia đình vô giá, nơi ươm mầm cho những thế hệ tinh hoa tiếp nối được lớn lên trong một môi trường trong lành, an toàn và ngập tràn cảm hứng thẩm mỹ.
</p>

<div style="margin: 40px 0; background: #faf8f5; border: 1px solid #e8e2d5; border-radius: 8px; padding: 30px;">
    <h3 style="margin-top: 0; color: #b89b5e; font-family: var(--font-serif); font-size: 1.5rem; text-align: center; margin-bottom: 20px;">
        BẢNG TỔNG QUAN THÔNG TIN DỰ ÁN GLADIA
    </h3>
    <table style="width: 100%; border-collapse: collapse; line-height: 1.8; font-size: 0.95rem;">
        <tr style="border-bottom: 1px solid #e0d8c8;">
            <td style="padding: 10px 0; font-weight: bold; width: 35%; color: #333;">Tên thương mại:</td>
            <td style="padding: 10px 0; color: #555;">Gladia / Gladia Heights</td>
        </tr>
        <tr style="border-bottom: 1px solid #e0d8c8;">
            <td style="padding: 10px 0; font-weight: bold; color: #333;">Đơn vị phát triển:</td>
            <td style="padding: 10px 0; color: #555;">Đại Chúng Properties</td>
        </tr>
        <tr style="border-bottom: 1px solid #e0d8c8;">
            <td style="padding: 10px 0; font-weight: bold; color: #333;">Phong cách kiến trúc:</td>
            <td style="padding: 10px 0; color: #555;">Hiện đại nhiệt đới (Tropical Modernism) & Biophilic Design</td>
        </tr>
        <tr style="border-bottom: 1px solid #e0d8c8;">
            <td style="padding: 10px 0; font-weight: bold; color: #333;">Loại hình sản phẩm:</td>
            <td style="padding: 10px 0; color: #555;">Dinh thự vườn, Căn hộ hạng sang & Duplex / Penthouse</td>
        </tr>
        <tr style="border-bottom: 1px solid #e0d8c8;">
            <td style="padding: 10px 0; font-weight: bold; color: #333;">Tiêu chuẩn bàn giao:</td>
            <td style="padding: 10px 0; color: #555;">Hoàn thiện nội thất cao cấp (Miele, Bosch, Duravit, Hansgrohe, Daikin)</td>
        </tr>
        <tr style="border-bottom: 1px solid #e0d8c8;">
            <td style="padding: 10px 0; font-weight: bold; color: #333;">Tiện ích nội khu:</td>
            <td style="padding: 10px 0; color: #555;">Hồ bơi vô cực điện phân muối, Clubhouse, Gym Panorama, Zen Garden, BBQ Garden</td>
        </tr>
        <tr>
            <td style="padding: 10px 0; font-weight: bold; color: #333;">Hình thức sở hữu:</td>
            <td style="padding: 10px 0; color: #555;">Sổ hồng lâu dài đối với người Việt Nam, 50 năm đối với cá nhân nước ngoài</td>
        </tr>
    </table>
</div>

<div style="margin: 40px 0; padding: 25px; background: #fff; border-left: 4px solid #b89b5e; box-shadow: 0 4px 15px rgba(0,0,0,0.06);">
    <h4 style="margin-top: 0; color: #111; font-size: 1.2rem;">LIÊN HỆ TƯ VẤN & TRẢI NGHIỆM THỰC TẾ DỰ ÁN GLADIA</h4>
    <p style="margin-bottom: 15px; color: #555; line-height: 1.6;">
        Để đăng ký tham quan thực tế không gian nhà mẫu và nhận trọn bộ tài liệu chi tiết mặt bằng, chính sách ưu đãi đặc quyền cho cư dân đầu tiên, quý khách vui lòng liên hệ trực tiếp chuyên viên tư vấn chiến lược:
    </p>
    <p style="margin-bottom: 5px; font-weight: bold; color: #111;">
        📞 Hotline / Zalo: <a href="https://zalo.me/0906060036" target="_blank" style="color: #b89b5e; text-decoration: none;">0906 060 036</a> (Huỳnh Hoàng Thịnh)
    </p>
    <p style="margin: 0; color: #555;">
        🌐 Website: <a href="https://huynhhoangthinh.com" style="color: #b89b5e; text-decoration: none;">huynhhoangthinh.com</a>
    </p>
</div>
"""

for p in posts:
    if p.get('id') == 609:
        p['content'] = gladia_content.strip()
        p['lead'] = "Khám phá Gladia (Gladia Heights) – Tuyệt tác không gian sống hiện đại chuẩn resort tại Đại Chúng Properties, nơi sự chỉn chu về kiến trúc Tropical Modernism hòa quyện hoàn hảo với cảnh quan thiên nhiên đa tầng và hệ tiện ích 5 sao đặc quyền."

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("SUCCESS: Updated posts.json successfully!")

# Check word count
for p in posts:
    if p.get('id') == 609:
        words = len(p['content'].split())
        print(f"Gladia Post 609 word count: {words} words")
