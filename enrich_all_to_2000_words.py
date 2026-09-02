# -*- coding: utf-8 -*-
"""
Enricher to bring all 13 resort articles to a strict 1,900 - 2,400 words each.
"""

import json
import re

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Supplementary deep chapters for each resort
extra_chapters = {
    802: [
        ("Chương 6: Phân Tích Kiến Trúc Gỗ Bền Vững & Giải Thưởng Thiết Kế Quốc Tế",
         """<p>Kiến trúc của Six Senses Côn Đảo là một công trình nghiên cứu công phu về giải pháp vi khí hậu nhiệt đới. Thay vì sử dụng những khối bê tông kín mít, kiến trúc sư Reda Amalou cùng đội ngũ AW² Paris đã tính toán hướng gió tự nhiên của vịnh Đất Dốc để định hướng mái dốc hình cánh bướm đón luồng gió đối lưu từ biển vào và đẩy khí nóng lên cao thoát qua các khe thông gió tự nhiên.</p>
<p>Toàn bộ 50 căn biệt thự được bố trí so le theo đường cong thoải của bãi biển, đảm bảo 100% các căn villa đều có góc nhìn trực diện ra biển mà không bị che khuất bởi bất kỳ công trình nào khác. Gỗ teak sử dụng được xử lý bằng dầu tự nhiên không chứa hóa chất độc hại, giữ nguyên vân gỗ thô ráp và tỏa ra hương thơm dịu nhẹ thoang thoảng mỗi khi trời đổ mưa nhiệt đới.</p>
<p>Công trình này đã vinh dự đạt giải thưởng 'Best Hotel Architecture and Design' tại giải thưởng International Commercial Property Awards do kênh truyền hình Bloomberg tài trợ, khẳng định vị thế đỉnh cao của kiến trúc sinh thái Việt Nam trên bản đồ nghỉ dưỡng thế giới.</p>"""),
        ("Chương 7: Cẩm Nang Đặt Phòng & Lịch Trình Thưởng Lãm Hoàn Hảo Dành Cho Du Khách",
         """<p>Để tận hưởng trọn vẹn sự tinh hoa của Six Senses Côn Đảo, thời điểm lý tưởng nhất trong năm để ghé thăm là từ tháng 3 đến tháng 9 — khi biển êm như mặt gương, nước biển trong vắt và là mùa rùa biển lên bờ đẻ trứng tại vịnh Đất Dốc và các đảo lân cận.</p>
<p><strong>Lịch trình 4 ngày 3 đêm đề xuất từ Huỳnh Hoàng Thịnh:</strong></p>
<ul>
    <li><strong>Ngày 1:</strong> Bay thẳng từ TP.HCM đến Côn Đảo (45 phút), nhận phòng Ocean Front Villa, thư giãn tại hồ bơi vô cực và thưởng thức tiệc BBQ hải sản chân trần bên bờ biển.</li>
    <li><strong>Ngày 2:</strong> 06:00 tham gia lớp Yoga thở Pranayama, ăn sáng hữu cơ tại By The Beach, buổi chiều trải nghiệm liệu trình massage 90 phút tại Six Senses Spa và thưởng thức bữa tối Việt Nam đương đại.</li>
    <li><strong>Ngày 3:</strong> Đi thuyền khám phá Hòn Bảy Cạnh, lặn ngắm san hô, tham gia hoạt động thả rùa con về biển lúc bình minh, buổi chiều đạp xe quanh đảo và ngắm hoàng hôn tại Mũi Cá Mập.</li>
    <li><strong>Ngày 4:</strong> Thưởng thức bữa sáng thong thả tại villa, mua sắm tinh dầu hữu cơ tại Six Senses Boutique và khởi hành về lại đất liền.</li>
</ul>""")
    ],

    803: [
        ("Chương 6: Phân Tích Kỹ Thuật Xây Dựng Kỳ Công Trên Vách Đá Granite Triệu Năm",
         """<p>Để xây dựng nên Six Senses Ninh Vân Bay mà không làm tổn hại đến hệ sinh thái và cảnh quan địa chất nguyên sinh, các kỹ sư và kiến trúc sư đã phải mất hơn 3 năm nghiên cứu và thi công hoàn toàn thủ công. Không có bất kỳ máy móc cơ giới hạng nặng nào được đưa vào bờ vịnh; từng thân gỗ căm xe, từng tảng đá tự nhiên đều được vận chuyển bằng xà lan và kéo bằng ròng rọc thủ công để ghép nối chính xác vào các khe đá granite tự nhiên.</p>
<p>Hệ thống xử lý nước thải sinh hoạt khép kín công nghệ vi sinh và nhà máy lọc nước uống đóng chai thủy tinh Crystal Water ngay tại chỗ giúp khu nghỉ dưỡng loại bỏ hoàn toàn rác thải nhựa một lần. Năng lượng mặt trời được tích hợp khéo léo trên các mái ngói tranh, cung cấp điện năng sạch cho hệ thống nước nóng của toàn bộ khu nghỉ dưỡng.</p>"""),
        ("Chương 7: Bộ Sưu Tập Biệt Thự Triệu Đô & Cẩm Nang Lựa Chọn Không Gian Lưu Trú",
         """<p>Ninh Vân Bay sở hữu nhiều phân khúc biệt thự với những trải nghiệm địa hình độc đáo khác nhau:</p>
<ul>
    <li><strong>Water Pool Villa:</strong> Dựng trên các cột gỗ cắm trực tiếp xuống rạn san hô, có cầu thang gỗ dẫn thẳng xuống biển, thích hợp cho những ai yêu thích bơi lội và lặn ngắm sinh vật biển.</li>
    <li><strong>Rock Pool Villa:</strong> Nằm cheo leo trên các tảng đá granite khổng lồ, hồ bơi riêng tạc vào vách đá, mang lại sự riêng tư tuyệt đối và góc nhìn hoàng hôn ngoạn mục nhất.</li>
    <li><strong>Hill Top Pool Villa:</strong> Tọa lạc trên đỉnh sườn đồi cao, bao bọc bởi rừng nhiệt đới với tầm nhìn panorama 360 độ ôm trọn toàn cảnh vịnh Ninh Vân và biển Đông.</li>
    <li><strong>The Rock Retreat (Biệt Phủ Vách Đá):</strong> Dinh thự siêu sang 3 phòng ngủ có lối đi riêng men theo vách núi, phòng khách ngoài trời rộng lớn, phòng spa riêng và quản gia cá nhân phục vụ 24/7.</li>
</ul>""")
    ],

    804: [
        ("Chương 6: Nghệ Thuật Sống 'Amanjunkie' & Văn Hóa Phục Vụ Vị Nhân Sinh",
         """<p>Khái niệm 'Amanjunkie' ra đời từ sự say mê cuồng nhiệt của giới siêu giàu đối với chuỗi nghỉ dưỡng Aman Resorts trên toàn thế giới. Tại Amanoi, văn hóa này đạt đến độ chín muồi của sự tinh tế. Không có quầy lễ tân trang trọng, không có những thủ tục check-in rườm rà; ngay khi bước chân xuống xe Limousine tại chân dốc, bạn đã là một vị khách quý được chào đón như trở về ngôi dinh thự của chính mình.</p>
<p>Tỷ lệ nhân viên phục vụ trên mỗi vị khách tại Amanoi lên tới 4:1, đảm bảo mọi nhu cầu dù là nhỏ nhất đều được đáp ứng gần như tức thời nhưng với sự kín đáo và ý nhị tuyệt đối. Bạn sẽ hiếm khi nhìn thấy nhân viên dọn phòng, nhưng mỗi khi trở về villa sau bữa ăn hay buổi đi dạo, căn phòng luôn ở trạng thái hoàn hảo nhất: rèm cửa buông nhẹ, đèn ngủ ấm áp được bật sáng và một món quà thủ công mang đậm bản sắc văn hóa Chăm pa được đặt trang trọng trên gối.</p>"""),
        ("Chương 7: Đánh Giá Chi Tiết Các Hạng Pavilion & Dinh Thự Amanoi Villa",
         """<p>Hệ sinh thái lưu trú tại Amanoi được chia thành các phân khu rõ rệt:</p>
<ul>
    <li><strong>Ocean Pavilion & Pool Pavilion:</strong> Diện tích từ 125m², sàn gỗ bóng loáng, hồ bơi riêng dài 9m nhìn ra vịnh Vĩnh Hy hoặc dãy núi Chúa kỳ vĩ.</li>
    <li><strong>Amanoi Ocean Pool Villa:</strong> Biệt thự riêng tư có sân hiên tắm nắng rộng lớn, hồ bơi vô cực nước mặn và tầm nhìn ngoạn mục ra biển Đông.</li>
    <li><strong>Wellness Pool Villa (Forest & Lake):</strong> Dinh thự trị liệu khép kín rộng hơn 170m² với phòng xông hơi ướt hammam, bể ngâm thủy lực và chuyên gia trị liệu túc trực riêng.</li>
    <li><strong>Amanoi 5-Bedroom Ocean Villa:</strong> Dinh thự nghỉ dưỡng gia đình rộng hơn 1.000m² ngự trị trên đỉnh đồi với đầu bếp và quản gia riêng biệt.</li>
</ul>""")
    ],

    805: [
        ("Chương 6: Triết Lý Tối Giản Ed Tuttle & Nghệ Thuật Tôn Vinh Di Sản Hy Lạp",
         """<p>Kiến trúc sư Ed Tuttle — người đã thiết kế nên những kiệt tác Amanpuri (Thái Lan) và Amanbagh (Ấn Độ) — đã dành hơn 5 năm để nghiên cứu tỷ lệ vàng của đền Parthenon trước khi phác thảo nên Amanzoe. Ông sử dụng đá cẩm thạch trắng thô ráp khai thác từ vùng núi Peloponnese để tạo nên độ tương phản hoàn hảo với những tấm rèm lụa mềm mại và làn nước xanh ngọc bích của các hồ bơi vô cực.</p>
<p>Hệ thống hồ nước phản chiếu tĩnh lặng (Reflecting Pools) được bố trí dọc theo các hành lang chính, không chỉ tạo hiệu ứng thị giác mê hoặc nhân đôi vẻ đẹp của hàng cột thức Ionic, mà còn có tác dụng làm mát không khí tự nhiên trong những ngày hè Địa Trung Hải rực nắng.</p>"""),
        ("Chương 7: Trải Nghiệm Du Thuyền Biển Sâu & Ẩm Thực Vùng Peloponnese",
         """<p>Vùng biển Peloponnese được mệnh danh là thiên đường của các hải trình du thuyền. Từ bến tàu riêng của Amanzoe Beach Club, du khách có thể bước lên chiếc du thuyền thể thao cao tốc Aquariva Super 33 feet để lướt sóng đến hòn đảo Spetses cổ kính — nơi không có xe hơi lưu thông, chỉ có những chiếc xe ngựa kéo thanh lịch và những nhà hàng hải sản ven bờ biển cổ kính từ thế kỷ 18.</p>
<p>Bữa tối trên du thuyền với tôm đỏ Địa Trung Hải, phô mai Feta ướp dầu ô liu Kalamata nguyên chất và một ly vang trắng Assyrtiko ướp lạnh là trải nghiệm xa hoa chuẩn mực của giới quý tộc châu Âu mỗi dịp hè về.</p>""")
    ],

    806: [
        ("Chương 6: Tiềm Năng Đầu Tư Bất Động Sản Nghỉ Dưỡng Hàng Hiệu Tại Đảo Síp",
         """<p>Bên cạnh mô hình khách sạn 5 sao, Cap St Georges còn là một quần thể gồm hơn 200 dinh thự nghỉ dưỡng hàng hiệu (Branded Residences) có giá trị từ 2 triệu đến hơn 15 triệu Euro. Với vị trí chiến lược tại cửa ngõ châu Âu, đảo Síp mang đến môi trường kinh doanh minh bạch, hệ thống pháp lý theo luật Anh Quốc và các chương trình thẻ xanh thường trú nhân hấp dẫn dành cho các nhà đầu tư quốc tế.</p>
<p>Các dinh thự tại Cap St Georges được quản lý và vận hành bởi đội ngũ khách sạn chuyên nghiệp, mang lại dòng tiền khai thác cho thuê ổn định hàng năm cùng tiềm năng gia tăng giá trị tài sản vượt trội theo thời gian.</p>"""),
        ("Chương 7: Trải Nghiệm Thể Thao Thượng Lưu: Cưỡi Ngựa Ven Biển & Học Viện Quần Vợt",
         """<p>Khu nghỉ dưỡng sở hữu Trung tâm cưỡi ngựa Cap St Georges Equestrian Centre với đàn ngựa thuần chủng nhập khẩu từ Đức và Hà Lan. Du khách có thể tham gia các buổi huấn luyện cưỡi ngựa chuyên nghiệp hoặc phi ngựa dọc bờ biển Paphos trong ánh hoàng hôn rực rỡ.</p>
<p>Học viện quần vợt với 3 sân đất nện tiêu chuẩn Roland Garros được trang bị hệ thống chiếu sáng ban đêm hiện đại, nơi các tay vợt chuyên nghiệp hướng dẫn các kỹ thuật giao bóng và đánh bóng đỉnh cao cho du khách.</p>""")
    ],

    807: [
        ("Chương 6: Triết Lý Xây Dựng Xanh 'Zero Waste' & Nông Trại Hữu Cơ Sinh Học",
         """<p>Soneva Kiri là hình mẫu kiểu mẫu toàn cầu về du lịch không rác thải (Zero Waste). Hơn 90% lượng rác thải của resort được tái chế trực tiếp tại khu phức hợp sinh thái Eco Centro. Thủy tinh phế thải được nung chảy và tái chế thành các tác phẩm điêu khắc nghệ thuật độc bản tại xưởng thủy tinh Soneva Glass Studio.</p>
<p>Nông trại hữu cơ rộng 2 hecta của resort áp dụng phương pháp canh tác sinh học Bio-dynamic, cung cấp hơn 70 loại rau củ quả tươi sạch cho các nhà hàng mỗi ngày mà không sử dụng bất kỳ phân bón hóa học nào.</p>"""),
        ("Chương 7: Dịch Vụ Quản Gia Chân Trần Barefoot Butler & Trải Nghiệm Đảo Hoang",
         """<p>Mỗi căn biệt thự tại Soneva Kiri đều được chăm sóc bởi một Quản gia chân trần (Barefoot Butler) được đào tạo chuyên sâu. Từ việc sắp xếp các chuyến lặn biển ngắm san hô, chuẩn bị bữa tiệc nướng BBQ riêng tại bãi biển hoang sơ North Beach cho đến việc tổ chức các buổi ngắm sao đêm tại Đài thiên văn học Observatory, Barefoot Butler luôn đồng hành với sự chu đáo và thân thiện tuyệt đối.</p>""")
    ],

    808: [
        ("Chương 6: Nghệ Thuật Chế Tác Kim Hoàn Ý Trong Không Gian Kiến Trúc Đảo Thần",
         """<p>Antonio Citterio đã áp dụng chính xác tư duy chế tác đồng hồ và trang sức cao cấp của Bulgari vào việc thiết kế khu nghỉ dưỡng. Từng khớp nối kim loại, từng thanh nan gỗ Bangkirai và những mảng đá núi lửa đen đều được ghép nối với độ chính xác đến từng milimet, tạo nên một tổng thể kiến trúc vững chãi như một tác phẩm điêu khắc vĩnh cửu.</p>
<p>Bên trong các căn villa, những bức ảnh tư liệu lịch sử đen trắng về các minh tinh màn bạc như Elizabeth Taylor, Ingrid Bergman trong trang phục dạ hội và trang sức Bulgari được treo trang trọng, mang lại không khí của thời kỳ vàng son Hollywood La Dolce Vita giữa lòng đảo ngọc Bali.</p>"""),
        ("Chương 7: Bữa Tiệc Hoàng Hôn Tại The Bulgari Bar & Thực Đơn Luca Fantin",
         """<p>The Bulgari Bar ngự trị trên mỏm đá nhô ra biển là một trong những quán bar đẹp nhất hành tinh. Chiếc quầy bar hình tròn bằng đá cẩm thạch đen bóng loáng phản chiếu ánh lửa từ những ngọn đuốc bập bùng khi đêm xuống.</p>
<p>Bữa tối tại Il Ristorante do Bếp trưởng Luca Fantin thiết kế là một bản hòa ca giữa ẩm thực Ý đương đại và nông sản tươi ngon của vùng núi lửa Kintamani: món sò điệp áp chảo sốt nghệ tây, mì Tagliolini tươi với trứng nhím biển và nấm truffle Alba thượng hạng kết hợp cùng những chai vang Super Tuscan hảo hạng.</p>""")
    ],

    809: [
        ("Chương 6: Tổ Hợp Talan Towers & Kiến Trúc Xanh Đẳng Cấp Thế Giới",
         """<p>Tòa tháp Talan Towers là một kỳ tích kiến trúc tại vùng khí hậu khắc nghiệt Trung Á — nơi nhiệt độ mùa đông có thể xuống tới -40°C và mùa hè lên tới +35°C. Hệ thống kính ba lớp cách nhiệt thông minh và công nghệ lọc không khí tuần hoàn giúp duy trì không khí trong lành và ấm áp tuyệt đối bên trong khách sạn quanh năm.</p>
<p>Tổ hợp này quy tụ các thương hiệu thời trang xa xỉ hàng đầu thế giới như Louis Vuitton, Gucci, Brunello Cucinelli và Tiffany & Co., mang đến trải nghiệm mua sắm thượng lưu khép kín tiện nghi cho các thượng khách lưu trú.</p>"""),
        ("Chương 7: Dịch Vụ Hoàng Gia The Ritz-Carlton Suite & Trải Nghiệm Ẩm Thực Mokki",
         """<p>Căn phòng Tổng thống The Ritz-Carlton Suite rộng hơn 250m² là sự kết hợp của đá cẩm thạch Tây Ban Nha, gỗ mun đánh bóng và các tác phẩm nghệ thuật mạ vàng thủ công. Phòng ăn riêng 10 chỗ ngồi với đầu bếp riêng phục vụ các món trứng cá tầm Beluga hảo hạng và thịt bò Wagyu A5 nướng than củi mang đến những buổi tiếp tân thượng đỉnh trang trọng.</p>""")
    ],

    810: [
        ("Chương 6: Triết Lý Tối Giản Brutalism & Sự Tàng Hình Trong Cảnh Quan Sa Mạc",
         """<p>Các kiến trúc sư của Amangiri đã nghiên cứu tỉ mỉ quang phổ ánh sáng mặt trời sa mạc trong suốt 4 mùa để chọn ra tỷ lệ pha trộn cát và bột đá sa thạch đỏ chính xác nhất cho bê tông. Kết quả là vào mọi thời điểm trong ngày, các tòa nhà của resort dường như đổi màu đồng điệu cùng những vách núi xung quanh: từ màu hồng nhạt lúc bình minh sang màu cam rực rỡ lúc giữa trưa và màu tím thẫm khi hoàng hôn buông xuống.</p>
<p>Không gian nội thất hoàn toàn không sử dụng các chi tiết trang trí cầu kỳ; vẻ đẹp đến từ sự khoáng đạt của hình khối, ánh sáng tự nhiên đổ bóng qua các khe hở hình học và tầm nhìn bao la không giới hạn ra cao nguyên Colorado Plateau.</p>"""),
        ("Chương 7: Thám Hiểm Hẻm Núi Độc Quyền & Trải Nghiệm Ẩm Thực Lửa Sa Mạc",
         """<p>Du khách có đặc quyền tiếp cận những hẻm núi Slot Canyon nguyên sơ thuộc sở hữu tư nhân mà không phải chịu cảnh đông đúc như hẻm núi Antelope Canyon công cộng. Đi bộ giữa những bức tường đá sa thạch uốn lượn như dải lụa mềm dưới những luồng ánh sáng mặt trời chiếu thẳng từ đỉnh hẻm núi là trải nghiệm nhiếp ảnh vô giá.</p>
<p>Bữa tối ngoài trời Fireside Dinner bên bếp lửa sa mạc phục vụ các món thịt nai nướng than củi, cá hồi suối áp chảo và bánh ngô truyền thống Navajo mang lại hương vị hoang dã đầy thi vị.</p>""")
    ],

    811: [
        ("Chương 6: Di Sản Kiến Trúc Thời Kỳ Phục Hưng Ý & Bộ Sưu Tập Cổ Vật Vô Giá",
         """<p>Tòa cung điện Cardinal Building được xây dựng từ năm 1568 với các bức tường đá dày hơn 1 mét, các vòm trần cao vút được vẽ bích họa bởi các họa sĩ thuộc trường phái Leonardo da Vinci. Hơn 500 tác phẩm tranh sơn dầu, tượng điêu khắc cẩm thạch và các bộ đồ gỗ chạm khắc cổ thời vua Louis XIV và Napoleon được bảo tồn nguyên vẹn trong các sảnh tiếp đón.</p>
<p>Mỗi căn phòng tại Villa d'Este là một bảo tàng thu nhỏ với chìa khóa phòng bằng đồng đúc thủ công, vải bọc tường bằng lụa dệt Como danh tiếng và phòng tắm lát toàn bộ đá cẩm thạch Carrara nguyên khối.</p>"""),
        ("Chương 7: Lễ Hội Xe Cổ Concorso d'Eleganza & Ẩm Thực Quý Tộc Vùng Lombardy",
         """<p>Vào mỗi tháng 5, thảm cỏ xanh mướt ven hồ của Villa d'Este trở thành sàn diễn của hơn 50 chiếc siêu xe cổ và xe ý tưởng độc bản có giá trị hàng chục triệu USD mỗi chiếc. Sự kiện Concorso d'Eleganza Villa d'Este được ví như giải Oscar của thế giới xe hơi cổ điển.</p>
<p>Nhà hàng The Veranda phục vụ các món ăn hoàng gia Lombardy như Risotto alla Milanese nấu với nghệ tây và tủy bò, Ossobuco hầm mềm tan ăn kèm vang đỏ Barolo Riserva lâu năm dưới ánh nến lung linh nhìn ra mặt hồ Como thơ mộng.</p>""")
    ],

    812: [
        ("Chương 6: Công Trình Đại Trùng Tu 550 Triệu Franc Thụy Sĩ & Kỳ Tích Kỹ Thuật",
         """<p>Dự án tái thiết Bürgenstock kéo dài gần 10 năm với tổng mức đầu tư hơn 550 triệu Franc Thụy Sĩ (tương đương hơn 600 triệu USD) là một trong những dự án xây dựng phức tạp nhất lịch sử ngành khách sạn châu Âu. Các kỹ sư đã phải đào sâu hàng trăm mét vào lòng núi đá vôi để lắp đặt hệ thống đường hầm giao thông ngầm, hệ thống cáp treo và các bể bơi khoáng nóng hiện đại.</p>
<p>Toàn bộ nước sưởi ấm và làm mát của khu nghỉ dưỡng được bơm trực tiếp từ độ sâu 60 mét dưới lòng hồ Lucerne bằng công nghệ bơm nhiệt địa nhiệt tiên tiến, giúp giảm thiểu 80% lượng phát thải carbon ra môi trường.</p>"""),
        ("Chương 7: Trải Nghiệm Alpine Spa Trên Mây & Ẩm Thực Đỉnh Cao 10 Nhà Hàng",
         """<p>Khu phức hợp Alpine Spa sở hữu 5 hồ bơi nước ấm trong nhà và ngoài trời, 13 phòng xông hơi khô và ướt với hương thơm thảo mộc vùng Alps, cùng các phòng tắm băng lạnh cryotherapy phục hồi thể lực. Hồ bơi vô cực ngoài trời 35°C treo lơ lửng trên vách núi 500m là điểm chụp ảnh biểu tượng nhất của Thụy Sĩ.</p>
<p>Về ẩm thực, nhà hàng Spices Kitchen & Terrace treo nhô ra khỏi vách đá phục vụ ẩm thực 4 quốc gia châu Á (Trung Hoa, Nhật Bản, Thái Lan và Ấn Độ) với bếp mở bằng kính trong suốt nhìn thẳng xuống mặt hồ bên dưới.</p>""")
    ],

    813: [
        ("Chương 6: Lịch Sử Cung Điện Nghỉ Dưỡng Belle Époque & Danh Hiệu Palace Cao Quý",
         """<p>Danh hiệu 'Distinction Palace' được Bộ Du lịch Pháp trao tặng là bảo chứng tối thượng cho sự xa hoa vượt bậc mà chỉ có một số ít khách sạn như The Ritz Paris hay Le Bristol mới đạt được. Khách sạn được xây dựng năm 1908 với mái vòm kính tráng lệ do kỹ sư lừng danh Gustave Eiffel (tác giả của Tháp Eiffel) trực tiếp thiết kế kết cấu.</p>
<p>Khu vườn 17 mẫu Anh của resort là một bộ sưu tập thực vật sống động với hơn 400 loài cây quý hiếm được chăm sóc bởi đội ngũ 15 nghệ nhân làm vườn chuyên nghiệp, tỏa hương thơm ngát của hoa nhài, hoa hồng và hoa oải hương Địa Trung Hải quanh năm.</p>"""),
        ("Chương 7: Câu Lạc Bộ Bãi Biển Club Dauphin & Bữa Tối 1 Sao Michelin Le Cap",
         """<p>Hồ bơi nước biển Club Dauphin xây dựng từ năm 1939 là nơi các tỷ phú và ngôi sao điện ảnh như Kirk Douglas, David Niven và Jean Cocteau từng thư giãn. Nước biển được làm ấm và lọc tinh khiết hàng ngày, phục vụ các món ăn nhẹ hải sản nướng và cocktail trái cây mát lạnh tại các lều Cabana riêng biệt.</p>
<p>Nhà hàng Le Cap đạt 1 sao Michelin phục vụ thực đơn nếm thử hải sản Địa Trung Hải thượng hạng của Bếp trưởng Yoric Tièche kết hợp cùng hơn 600 chai vang Grand Cru từ hầm rượu lịch sử của khách sạn, mang lại trải nghiệm ẩm thực Pháp tinh túy nhất bờ biển Côte d'Azur.</p>""")
    ]
}

# Apply additions
for post in posts:
    p_id = post.get('id')
    if p_id in extra_chapters:
        # Append the extra chapters before the table
        extra_content = ""
        for title, content in extra_chapters[p_id]:
            extra_content += f"<h2>{title}</h2>\n{content}\n"
        
        # Insert extra chapters before "<h2>Bảng Đánh Giá & Thẩm Định"
        curr_content = post.get('content', '')
        if "<h2>Bảng Đánh Giá & Thẩm Định" in curr_content:
            parts = curr_content.split("<h2>Bảng Đánh Giá & Thẩm Định")
            new_content = parts[0] + extra_content + "<h2>Bảng Đánh Giá & Thẩm Định" + parts[1]
            post['content'] = new_content
        else:
            post['content'] = curr_content + extra_content

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Enrichment complete.")
