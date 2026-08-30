import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Domain-specific long-form content expansions for Posts 703-710
domain_expansions = {
    703: """
<h2>Chương III: Cấu Trúc Vận Hành Của Family Office Hiện Đại & Bài Học Quản Trị Gia Sản</h2>
<p>Một văn phòng gia tộc (Family Office) tiêu chuẩn năm 2026 không còn là một phòng làm việc nhỏ với một vài luật sư và kế toán gia đình. Các tổ chức này đã phát triển thành những cỗ máy đầu tư tinh vi với đầy đủ các ban bệ chuyên trách:</p>
<ul>
  <li><strong>Ban Đầu tư Trực tiếp (Direct Investment Team):</strong> Chịu trách nhiệm săn lùng, thẩm định và đàm phán các thương vụ mua lại bất động sản thương mại, thâu tóm doanh nghiệp chưa niêm yết (Private Equity) và đầu tư vốn mạo hiểm vào các startup công nghệ đột phá.</li>
  <li><strong>Ban Quản trị Rủi ro & Pháp lý Quốc tế:</strong> Theo dõi biến động chính sách thuế xuyên biên giới, luật thừa kế, cơ chế bảo mật thông tin và tuân thủ các quy định phòng chống rửa tiền (AML) quốc tế.</li>
  <li><strong>Ban Quản trị Phong cách sống & Dịch vụ Gia đình (Concierge & Lifestyle Services):</strong> Quản lý danh mục du thuyền, chuyên cơ, bộ sưu tập nghệ thuật, trường học cho thế hệ kế cận và an ninh cá nhân đa tầng.</li>
</ul>

<h2>Chương IV: Cuộc Đua Giữa Các Trung Tâm Quản Lý Tài Sản: London, Dubai, Singapore & Hong Kong</h2>
<p>Báo cáo của Knight Frank phác họa sự cạnh tranh khốc liệt nhưng mang tính bổ trợ giữa các 'Hub' quản lý tài sản lớn nhất hành tinh:</p>
<ul>
  <li><strong>London:</strong> Dù đối mặt với sự thay đổi về chính sách thuế Non-Dom, London vẫn là trung tâm tài chính có hệ sinh thái cố vấn, luật pháp và ngân hàng đầu tư sâu rộng nhất thế giới. Các gia tộc vẫn giữ văn phòng tại London vì 'đây là nơi các thương vụ lớn diễn ra'.</li>
  <li><strong>Dubai & Abu Dhabi:</strong> Tăng trưởng vượt bậc với chính sách thuế 0%, thủ tục cấp phép nhanh chóng và vị trí địa lý đắc địa kết nối giữa Châu Âu, Châu Á và Châu Phi. Hàng loạt quỹ đầu tư khổng lồ như Bridgewater Associates, KKR và Partners Group đã mở văn phòng tại đây.</li>
  <li><strong>Singapore & Hong Kong:</strong> Singapore tiếp tục là điểm đến an toàn tuyệt đối cho dòng vốn Đông Nam Á; trong khi Hong Kong đang hồi sinh mạnh mẽ nhờ làn sóng phát hành IPO và sự hỗ trợ mạnh mẽ của dòng vốn từ Trung Quốc đại lục.</li>
</ul>

<h2>Chương V: Góc Nhìn Đại Chúng: Sự Kín Tiếng, Trách Nhiệm Xã Hội & Đầu Tư Tạo Tác Động (Impact Investing)</h2>
<p>Đối với xã hội và đại chúng, sự tồn tại của hơn 10.000 Family Office quản lý hàng nghìn tỷ USD luôn gợi lên câu hỏi về trách nhiệm xã hội của các gia tộc siêu giàu. Đại chúng ngày càng đòi hỏi các gia đình tỷ phú phải có sự đóng góp rõ ràng hơn vào việc giải quyết các cuộc khủng hoảng chung của nhân loại.</p>

<p>Thấu hiểu điều này, thế hệ thừa kế trẻ (Next-Gen) của các Family Office đang dẫn đầu làn sóng <strong>Đầu tư Tạo Tác Động (Impact Investing)</strong>. Thay vì chỉ tối đa hóa lợi nhuận tài chính thuần túy, họ phân bổ ít nhất 15 - 25% danh mục vào các dự án giảm phát thải carbon, nông nghiệp tái sinh, năng lượng mặt trời cho vùng sâu vùng xa, và các quỹ nghiên cứu y học miễn phí. Đây là bước tiến quan trọng giúp hài hòa lợi ích giữa sự thịnh vượng gia tộc và sự tiến bộ của toàn thể cộng đồng.</p>

<h2>Chương VI: Lời Khuyên Xây Dựng Cấu Trúc Quản Trị Gia Tộc Cho Doanh Nhân Việt Nam</h2>
<p>Đối với các doanh nhân hàng đầu tại Việt Nam đang bước vào giai đoạn chuyển giao thế hệ, việc sớm thiết lập mô hình Family Office chuyên nghiệp là điều kiện tiên quyết để tránh nguy cơ 'không ai giàu ba họ'. Cần tách bạch rõ ràng giữa tài sản doanh nghiệp kinh doanh và tài sản tích sản gia đình, xây dựng quy chế gia tộc minh bạch và đào tạo thế hệ con cháu về đạo đức kinh doanh, lòng trắc ẩn và tư duy phụng sự xã hội.</p>
""",

    704: """
<h2>Chương III: Giải Mã Cơn Sốt Branded Residences — Sự Giao Thoa Giữa Bất Động Sản & Thương Hiệu Xa Xỉ</h2>
<p>Thị trường bất động sản hàng hiệu (Branded Residences) đang trải qua giai đoạn bùng nổ mạnh mẽ nhất trong lịch sử, với dự báo của Knight Frank sẽ vượt qua <strong>1.000 dự án đang hoạt động vào năm 2030</strong>. Sự phát triển này không còn giới hạn ở các tập đoàn khách sạn danh tiếng (như Four Seasons, Ritz-Carlton, Mandarin Oriental, Aman) mà đã mở rộng sang:</p>
<ul>
  <li><strong>Các nhà mốt thời trang Haute Couture:</strong> Elie Saab, Armani/Casa, Fendi Casa, Missoni mang đến ngôn ngữ thiết kế may đo tinh xảo và vật liệu nội thất độc quyền.</li>
  <li><strong>Các thánh địa siêu xe:</strong> Porsche Design Tower, Bugatti Residences, Aston Martin Residences đưa thang máy nâng siêu xe lên tận phòng khách của gia chủ tại tầng 50.</li>
  <li><strong>Các thương hiệu chăm sóc sức khỏe & nghỉ dưỡng:</strong> Six Senses, SHA Wellness Clinic, Clinique La Prairie tích hợp trung tâm y tế tế bào và phục hồi năng lượng ngay trong khuôn viên tòa nhà.</li>
</ul>

<h2>Chương IV: Dịch Vụ Quản Gia 24/7 & Yêu Cầu 'Turnkey Perfection' Của Giới Tinh Hoa</h2>
<p>Paddy Dring, Giám đốc Khối Khách hàng Tư nhân của Knight Frank, nhấn mạnh: <em>'Khách hàng siêu giàu ngày nay không muốn lãng phí thời gian vào việc quản lý vận hành hay sửa chữa nhà cửa. Họ yêu cầu sự hoàn hảo chìa khóa trao tay.'</em></p>

<p>Khi chủ nhân đáp chuyến bay đêm xuống thành phố, căn hộ Branded Residence của họ phải ở trạng thái sẵn sàng 100%: nhiệt độ phòng tự động điều chỉnh theo nhịp sinh học gia chủ, tủ lạnh chứa đầy các loại thực phẩm hữu cơ và rượu vang theo thực đơn yêu thích, hoa tươi được cắm mới và nhân viên quản gia túc trực để phục vụ bữa tối nóng sốt do đầu bếp riêng chuẩn bị.</p>

<h2>Chương V: Góc Nhìn Đại Chúng: Lối Sống Siêu Cơ Động & Văn Hóa Đô Thị Bản Địa</h2>
<p>Sự gia tăng của tầng lớp cư dân 'bán thời gian' (Part-time Residents) tại các đô thị lớn như London hay New York đôi khi tạo nên những phản ứng trái chiều từ người dân địa phương. Một số ý kiến lo ngại rằng các khu phố trung tâm với những căn hộ cao cấp bỏ trống phần lớn thời gian trong năm có thể làm giảm sức sống cộng đồng truyền thống (hiện tượng 'Lights-Out London').</p>

<p>Để khắc phục điều này, các nhà phát triển bất động sản hàng hiệu thế hệ mới đang tích hợp các không gian thương mại mở, phòng trưng bày nghệ thuật công cộng và các tuyến phố đi bộ ẩm thực tại khối đế tòa nhà, vừa phục vụ cư dân tòa tháp, vừa tạo nên điểm đến văn hóa sôi động cho toàn bộ cư dân khu vực xung quanh.</p>

<h2>Chương VI: Tiềm Năng Dẫn Đầu Của Bất Động Sản Hàng Hiệu Tại Việt Nam</h2>
<p>Việt Nam đang nổi lên là một trong những thị trường Branded Residences tăng trưởng nhanh nhất thế giới. Các dự án biểu tượng như The Rivus Elie Saab hay Grand Marina Saigon chứng minh rằng tầng lớp thượng lưu Việt Nam hoàn toàn sẵn sàng chi trả mức giá cao để sở hữu những không gian sống đạt chuẩn mực khắt khe nhất của các thương hiệu huyền thoại thế giới.</p>
""",

    705: """
<h2>Chương III: Phân Tích Chuyên Sâu Các Danh Mục Đầu Tư Xa Xỉ Trọng Điểm 2026</h2>
<p>Báo cáo KFLII 2026 phân tích chi tiết biến động của 10 danh mục tài sản sưu tầm được giới siêu giàu ưa chuộng nhất:</p>
<ul>
  <li><strong>Nghệ thuật Ấn tượng & Hiện đại (+13.6%):</strong> Dẫn đầu sự phục hồi toàn thị trường, được thúc đẩy bởi các bộ sưu tập di sản hiếm có của các danh họa Gustav Klimt, Monet, Van Gogh và Munch.</li>
  <li><strong>Đồng hồ Haute Horlogerie (+5.1%):</strong> Patek Philippe (+12.1%) và Rolex (+4.6%) tiếp tục giữ vững vị thế 'tiền tệ vạn năng'. Các mẫu đồng hồ thép thể thao kinh điển như Patek Philippe Aquanaut 5167A và Nautilus 5711 giữ kỷ lục thanh khoản nhanh nhất trên thị trường thứ cấp.</li>
  <li><strong>Túi xách Hermès Birkin & Kelly (-0.2%):</strong> Hoạt động như một tài sản phòng hộ chống lạm phát tương tự vàng vật chất. Giá trị của những chiếc túi da cá sấu Porosus hay da thuộc Himalaya nguyên bản tiếp tục tăng trưởng ổn định trên các sàn đấu giá quốc tế.</li>
  <li><strong>Rượu vang cao cấp Fine Wine (-2.5%):</strong> Dù thị trường chung chịu tác động bởi thuế quan, các dòng vang siêu thượng hạng như Domaine de la Romanée-Conti hay Domaine Leroy Musigny Grand Cru (590.000 USD/thùng) vẫn tăng giá mạnh mẽ.</li>
</ul>

<h2>Chương IV: Sự Trỗi Dậy Của Thế Hệ Sưu Tầm Gen Z & Khái Niệm 'Conspicuous Taste'</h2>
<p>Chuyên gia Lee Bofkin, nhà sưu tầm nghệ thuật danh tiếng tại London, đúc kết trong ấn phẩm The Wealth Report: <em>'Sưu tầm trong thế kỷ 21 không còn là phô trương tiêu dùng (Conspicuous Consumption) — đó là phô trương gu thẩm mỹ và tri thức văn hóa (Conspicuous Taste).'</em></p>

<p>Thế hệ trẻ giàu có ngày nay không sưu tầm để khoe khoang sự giàu sang bề nổi. Họ tìm kiếm những món đồ có câu chuyện lịch sử độc bản, những vật phẩm mang tính kết nối cảm xúc sâu sắc và tôn vinh bàn tay tài hoa của các nghệ nhân thủ công truyền thống.</p>

<h2>Chương V: Góc Nhìn Đại Chúng: Nghệ Thuật Trong Đời Sống & Giá Trị Văn Hóa Đại Chúng</h2>
<p>Trong mắt công chúng, các cuộc đấu giá hàng chục triệu USD tại Christie's hay Sotheby's thường được theo dõi như những sự kiện văn hóa nghệ thuật hấp dẫn. Sự lan tỏa của các hình ảnh tác phẩm nghệ thuật, đồng hồ kiệt tác và thời trang cao cấp trên mạng xã hội đã truyền cảm hứng mạnh mẽ cho cộng đồng về tình yêu cái đẹp và sự trân trọng đối với các di sản văn hóa nhân loại.</p>

<h2>Chương VI: Nguyên Tắc Xây Dựng Bộ Sưu Tập Tích Sản Cho Nhà Đầu Tư Tinh Hoa</h2>
<p>Để xây dựng một bộ sưu tập tài sản xa xỉ vừa thỏa mãn đam mê cá nhân vừa đảm bảo khả năng sinh lời và bảo toàn vốn, nhà đầu tư cần tuân thủ 3 nguyên tắc vàng: <strong>Ưu tiên tính độc bản (Rarity), Xác thực nguồn gốc lịch sử minh bạch (Provenance) và Bảo quản trong điều kiện môi trường đạt chuẩn viện bảo tàng (Preservation)</strong>.</p>
""",

    706: """
<h2>Chương III: Phân Tích Các Phiên Đấu Giá Kỷ Lục Tại Monterey & Kissimmee</h2>
<p>Tuần lễ xe hơi Monterey Car Week tại California và phiên đấu giá Mecum Kissimmee đầu năm 2026 đã chứng minh rằng dòng tiền của giới sưu tầm siêu xe luôn tìm đến những tác phẩm mang tính biểu tượng lịch sử:</p>
<ul>
  <li><strong>Ferrari 250 GTO (1962):</strong> Mức giá 38.5 triệu USD tái khẳng định vị thế 'Chén Thánh' của làng xe cổ thế giới, với động cơ V12 Colombo 3.0L và lịch sử đua xe huyền thoại.</li>
  <li><strong>Ferrari F50 (1995):</strong> Mức giá 9.2 triệu USD tại Monterey và 12 triệu USD tại Kissimmee cho thấy sự trỗi dậy mạnh mẽ của các siêu xe sử dụng động cơ F1 gắn thẳng vào khung gầm carbon.</li>
  <li><strong>Ferrari Enzo (2003):</strong> Mức giá 18 triệu USD thiết lập kỷ lục mới cho thế hệ Hypercar đầu thế kỷ 21 do huyền thoại Michael Schumacher trực tiếp tham gia phát triển.</li>
</ul>

<h2>Chương IV: Trào Lưu Sưu Tầm Xe 'Youngtimer' Thập Niên 90 – 2000</h2>
<p>Báo cáo của HAGI ghi nhận sự bùng nổ của thế hệ xe thể thao Youngtimer. Các mẫu xe poster gắn liền với tuổi thơ của thế hệ doanh nhân 8X, 9X như <strong>BMW E30 M3 (+22.3%)</strong>, <strong>Porsche Carrera GT</strong>, <strong>Lamborghini Countach, Miura và Diablo</strong> đang trở thành tâm điểm săn lùng với giá trị tăng trưởng gấp đôi chỉ trong vòng 3 năm qua.</p>

<h2>Chương V: Góc Nhìn Đại Chúng: Giữa Đam Mê Tốc Độ & Ý Thức Bảo Vệ Môi Trường</h2>
<p>Công chúng luôn dành một tình cảm đặc biệt cho những cỗ máy tốc độ tuyệt đẹp. Tiếng gầm của khối động cơ đốt trong thuần khiết và thiết kế khí động học điêu khắc luôn là nguồn cảm hứng bất tận cho những người yêu thích kỹ thuật cơ khí và thiết kế công nghiệp trên toàn thế giới.</p>

<p>Đồng thời, ý thức về môi trường cũng thúc đẩy các nhà sưu tập siêu xe hàng đầu chuyển hướng sang sử dụng nhiên liệu sinh học tổng hợp (E-Fuels) và ủng hộ các công nghệ phục chế xe cổ tích hợp hệ thống kiểm soát khí thải hiện đại, giúp gìn giữ những tuyệt tác cơ khí di sản mà không gây ảnh hưởng đến môi trường.</p>

<h2>Chương VI: Nghệ Thuật Bảo Quản & Lưu Giữ Siêu Xe Chuẩn Bảo Tàng</h2>
<p>Một chiếc siêu xe triệu đô chỉ có thể duy trì và gia tăng giá trị khi được bảo quản trong hệ thống garage chuyên dụng đạt chuẩn: nhiệt độ kiểm soát 20 - 22°C, độ ẩm 45 - 50%, hệ thống sạc bù ắc quy thông minh và chế độ bảo dưỡng định kỳ bởi chính các kỹ sư trưởng của nhà sản xuất.</p>
""",

    707: """
<h2>Chương III: Công Nghệ Đóng Tàu Xanh & Sự Đột Phá Của Năng Lượng Hydrogen 2026</h2>
<p>Ngành đóng tàu siêu du thuyền đang tiên phong trong cuộc cách mạng năng lượng xanh của ngành hàng hải toàn cầu:</p>
<ul>
  <li><strong>Feadship 821 (119m):</strong> Siêu du thuyền chạy bằng pin nhiên liệu Hydrogen đầu tiên trên thế giới, có khả năng vận hành hoàn toàn không phát thải khí CO2 và triệt tiêu 100% tiếng ồn động cơ khi di chuyển qua các vùng bảo tồn biển nhạy cảm.</li>
  <li><strong>Hệ thống ổn định con quay hồi chuyển (Gyroscopic Stabilizers):</strong> Giúp thân tàu giữ thăng bằng tuyệt đối ngay cả giữa những đợt sóng biển cấp 6, mang lại trải nghiệm nghỉ dưỡng êm ái như trên đất liền.</li>
  <li><strong>Vật liệu Composite sợi carbon siêu nhẹ:</strong> Giảm trọng lượng thân tàu tới 30%, tối ưu hóa hiệu suất nhiên liệu và tăng tầm hải trình lên trên 6.000 hải lý.</li>
</ul>

<h2>Chương IV: Bản Đồ Hải Trình Mới: Từ Địa Trung Hải Đến Biển Đỏ & Đông Nam Á</h2>
<p>Bên cạnh các hải trình truyền thống tại Monaco, Cannes, Amalfi và Caribbean, các tỷ phú du thuyền đang mở rộng hải trình sang các vùng biển mới:</p>
<ul>
  <li><strong>Biển Đỏ (Saudi Arabia):</strong> Đại dự án Amaala và đảo Sindalah với các bến du thuyền 7 sao được trang bị cơ sở hạ tầng hiện đại bậc nhất hành tinh.</li>
  <li><strong>Quần đảo Indonesia & Vịnh Thái Lan:</strong> Hơn 17.000 hòn đảo hoang sơ với các rạn san hô kỳ vĩ đang trở thành điểm đến khám phá yêu thích của các siêu du thuyền thám hiểm (Expedition Yachts).</li>
  <li><strong>Vịnh Hạ Long & Vịnh Nha Trang (Việt Nam):</strong> Với cảnh quan thiên nhiên kỳ vĩ được UNESCO công nhận, Việt Nam sở hữu tiềm năng khổng lồ để trở thành trung tâm du thuyền quốc tế của khu vực Đông Nam Á trong thập kỷ tới.</li>
</ul>

<h2>Chương V: Góc Nhìn Đại Chúng: Lối Sống Biển Khơi & Bảo Tồn Đại Dương</h2>
<p>Hình ảnh những chiếc siêu du thuyền nguy nga thả neo giữa vịnh biển luôn gợi lên sự ngưỡng mộ về một phong cách sống tự do và phóng khoáng. Đại chúng ngày nay cũng đánh giá rất cao các chủ tàu tích cực tham gia vào các chiến dịch làm sạch rác thải nhựa đại dương, hỗ trợ các nhà khoa học hải dương học nghiên cứu bảo tồn san hô và thúc đẩy du lịch sinh thái bền vững tại các cộng đồng cư dân ven biển.</p>

<h2>Chương VI: Chiến Lược Khai Thác & Quản Lý Du Thuyền Dành Cho Chủ Sở Hữu</h2>
<p>Sở hữu một siêu du thuyền đòi hỏi kế hoạch tài chính và vận hành chuyên nghiệp. Mô hình kết hợp giữa sử dụng cá nhân (6 tháng) và khai thác cho thuê cao cấp (Charter Market - 500.000 USD/tuần) là giải pháp tài chính thông minh giúp bù đắp chi phí bảo trì và phi hành đoàn hàng năm, đồng thời duy trì giá trị thanh khoản cao cho con tàu.</p>
""",

    708: """
<h2>Chương III: Phân Tích Các Cỗ Máy Chuyên Cơ Dẫn Đầu Kỷ Nguyên 2026</h2>
<p>Thế hệ chuyên cơ siêu tầm xa mới nhất mang đến những bước tiến vượt bậc về công nghệ hàng không và tiện nghi khoang khách:</p>
<ul>
  <li><strong>Gulfstream G700:</strong> Tầm bay 7.500 hải lý, tốc độ Mach 0.925, 20 cửa sổ bầu dục toàn cảnh lớn nhất phân khúc và hệ thống chiếu sáng theo nhịp sinh học Circadian Lighting giúp triệt tiêu hoàn toàn cảm giác lệch múi giờ (Jet Lag).</li>
  <li><strong>Bombardier Global 8000:</strong> Mẫu phản lực thương gia dân dụng nhanh nhất thế giới với vận tốc chạm ngưỡng Mach 0.94 và tầm bay kỷ lục 8.000 hải lý (14.800 km), kết nối thẳng New York - Singapore mà không cần tiếp nhiên liệu.</li>
  <li><strong>Dassault Falcon 10X:</strong> Được ví như 'Penthouse giữa tầng mây' với chiều rộng cabin lên tới 2.77m và tích hợp công nghệ an toàn Smart Recovery thừa hưởng từ tiêm kích quân sự Rafale.</li>
  <li><strong>Pilatus PC-24:</strong> Dòng phản lực siêu đa năng độc nhất thế giới có khả năng hạ cánh trên đường băng sỏi đá ngắn dưới 893m, mở ra khả năng tiếp cận hơn 20.000 sân bay nhỏ trên toàn cầu.</li>
</ul>

<h2>Chương IV: Dữ Liệu VistaJet Về Sự Thay Đổi Nhân Khẩu Học Của Khách Bay Chuyên Cơ</h2>
<p>Báo cáo của VistaJet công bố trong The Wealth Report 2026 ghi nhận kỷ lục chưa từng có: <strong>47% khách hàng bay chuyên cơ lần đầu tiên trong quý 1/2026 thuộc độ tuổi dưới 45</strong>. Đây là thế hệ doanh nhân công nghệ, các nhà quản lý quỹ đầu cơ và nhà sáng lập trẻ tuổi coi chuyên cơ là công cụ tối ưu hóa thời gian và năng suất làm việc thay vì một món đồ xa xỉ thụ động.</p>

<h2>Chương V: Góc Nhìn Đại Chúng: Hàng Không Tư Nhân & Thách Thức Chuyển Đổi Xanh</h2>
<p>Mặc dù chuyên cơ tư nhân mang lại hiệu quả làm việc vượt trội cho các nhà lãnh đạo tập đoàn toàn cầu, ngành hàng không tư nhân cũng đang đối mặt với những phản biện xã hội về lượng khí thải carbon trên mỗi hành khách. Để đáp ứng kỳ vọng của công chúng và bảo vệ môi trường, các hãng sản xuất chuyên cơ đang dẫn đầu trong việc thử nghiệm 100% nhiên liệu hàng không bền vững (SAF) và nghiên cứu động cơ hybrid điện trong tương lai gần.</p>

<h2>Chương VI: Giải Pháp Tối Ưu Hóa Chi Phí: Jet Card & Sở Hữu Cổ Phần (Fractional Ownership)</h2>
<p>Đối với các doanh nhân có nhu cầu bay từ 50 đến 150 giờ mỗi năm, các chương trình Thẻ giờ bay (Jet Card) hoặc sở hữu cổ phần chuyên cơ từ các đơn vị uy tín như VistaJet, NetJets là giải pháp phân bổ dòng vốn hiệu quả nhất, giúp tiếp cận các dòng chuyên cơ tối tân mà không cần gánh chịu chi phí sở hữu và bảo trì trọn gói hàng năm.</p>
""",

    709: """
<h2>Chương III: Bảng Giá Đất Vườn Nho Toàn Cầu & Sự Khan Hiếm Của Grand Cru</h2>
<p>Chỉ số <strong>Knight Frank Global Vineyard Index 2026</strong> công bố mức giá tham chiếu cho 1 hecta đất trồng nho tại các vùng danh tiếng nhất hành tinh:</p>
<ul>
  <li><strong>Burgundy Grand Cru (Côte de Nuits - Pháp):</strong> Lên tới <strong>55 - 70 triệu USD/ha</strong> (với ngân sách 1 triệu USD, nhà đầu tư chỉ mua được một mảnh đất nhỏ 200 m² - tương đương 14m x 14m).</li>
  <li><strong>Barolo & Barbaresco (Piedmont - Ý):</strong> <strong>2.7 triệu USD/ha</strong> (+15% trong 12 tháng qua).</li>
  <li><strong>Champagne (Côte des Blancs - Pháp):</strong> <strong>1.9 triệu USD/ha</strong>.</li>
  <li><strong>Bordeaux (Margaux - Pháp):</strong> <strong>1.65 triệu USD/ha</strong>.</li>
  <li><strong>Tuscany (Bolgheri & Brunello di Montalcino - Ý):</strong> <strong>1.2 triệu USD/ha</strong>.</li>
  <li><strong>Napa Valley (Rutherford - Mỹ):</strong> <strong>1.17 triệu USD/ha</strong>.</li>
  <li><strong>Úc (Barossa Valley) & Nam Phi (Stellenbosch):</strong> <strong>55.000 - 60.000 USD/ha</strong> (với 1 triệu USD có thể sở hữu điền trang rộng 16 - 18 hecta).</li>
</ul>

<h2>Chương IV: Biến Đổi Khí Hậu & Sự Dịch Chuyển Của Bản Đồ Rượu Vang Thế Giới</h2>
<p>Nhiệt độ tăng cao tại các vùng truyền thống đang mở ra cơ hội vàng cho các vùng đất trồng nho có khí hậu mát mẻ (Cool-Climate Regions): Thung lũng Loire và Limoux (Pháp), Alto Adige và Friuli (Ý), Thung lũng Willamette Oregon (Mỹ), Tasmania và Central Otago (New Zealand), cùng sự trỗi dậy ngoạn mục của các dòng vang sủi cao cấp tại miền Nam nước Anh (Sussex, Kent, Essex).</p>

<h2>Chương V: Góc Nhìn Đại Chúng: Nghệ Thuật Ẩm Thực, Vang Hữu Cơ & Lối Sống Điền Trang</h2>
<p>Trong tâm thức của đại chúng, hình ảnh một điền trang rượu vang cổ kính giữa vùng quê châu Âu luôn là biểu tượng của cuộc sống an nhiên, hòa mình vào thiên nhiên và gìn giữ văn hóa gia đình. Sự chuyển đổi sang phương pháp làm vang hữu cơ và sinh học năng động (Biodynamic) đang nhận được sự ủng hộ nhiệt liệt từ thế hệ người tiêu dùng có ý thức bảo vệ môi trường trên khắp thế giới.</p>

<h2>Chương VI: Khuyến Nghị Đầu Tư Bất Động Sản Vườn Nho Cho Giới Tinh Hoa</h2>
<p>Đầu tư vào bất động sản vườn nho không chỉ là bài toán sản xuất rượu vang thương mại mà là chiến lược tích sản di sản kết hợp du lịch nghỉ dưỡng cao cấp (Wine Hospitality & Cellar-Door Tourism). Một điền trang sở hữu thương hiệu uy tín, kiến trúc đẹp và dịch vụ đón tiếp 5 sao luôn có khả năng tạo ra dòng tiền bền vững và gia tăng giá trị vượt trội theo thời gian.</p>
""",

    710: """
<h2>Chương III: Sự Tái Xuất Của Các Đại Thương Vụ Văn Phòng Hạng A (Big-Ticket Office Deals)</h2>
<p>Bất chấp những dự đoán bi quan thời kỳ hậu Covid, thị trường văn phòng hạng A tại các trung tâm tài chính toàn cầu đã chứng kiến sự trở lại ngoạn mục với tổng vốn tư nhân giải ngân đạt <strong>18.9 tỷ USD</strong> tại Châu Âu năm 2025. Tiêu biểu nhất là thương vụ tập đoàn <strong>Blackstone mua lại tòa nhà văn phòng Trocadéro tại Paris với giá 820 triệu USD</strong> — thương vụ lớn nhất của Blackstone tại Pháp kể từ năm 2018.</p>

<h2>Chương IV: Cơn Sốt Trung Tâm Dữ Liệu (Data Centres) & An Ninh Năng Lượng Cho Trí Tuệ Nhân Tạo AI</h2>
<p>Theo báo cáo của Cơ quan Năng lượng Quốc tế (IEA) và Knight Frank, cuộc cách mạng AI đang tạo ra một cơn khát điện năng chưa từng thấy. Mức tiêu thụ điện của các trung tâm dữ liệu dự báo sẽ <strong>tăng 127% vào năm 2030</strong>, đưa tỷ trọng tiêu thụ điện của Data Center tại Mỹ từ 4.5% lên gần 9% tổng sản lượng điện quốc gia. Bất động sản hạ tầng công nghệ kết hợp các dự án năng lượng tái tạo độc lập đang trở thành phân khúc đầu tư có tỷ suất sinh lời hấp dẫn nhất cho các định chế tài chính toàn cầu.</p>

<h2>Chương V: Góc Nhìn Đại Chúng: Tương Lai Không Gian Làm Việc & Đô Thị Bền Vững</h2>
<p>Đối với hàng triệu nhân viên văn phòng và cư dân đô thị, việc các doanh nghiệp quay trở lại mô hình làm việc trực tiếp tại văn phòng 4 ngày/tuần đang tiếp thêm sinh khí mới cho các khu phố trung tâm, các nhà hàng, quán cà phê và dịch vụ thương mại. Đại chúng đánh giá cao các tòa nhà văn phòng hiện đại đạt chứng chỉ xanh ESG, có không gian mở, nhiều cây xanh và ứng dụng công nghệ lọc khí tươi bảo vệ sức khỏe người lao động.</p>

<h2>Chương VI: Chiến Lược Phân Bổ Vốn Bất Động Sản Thương Mại Năm 2026</h2>
<p>Các nhà đầu tư bất động sản thương mại năm 2026 cần tập trung vào 2 chiến lược cốt lõi: <strong>Thâu tóm các bất động sản văn phòng hạng A tại vị trí trung tâm lõi (Core CBD) đạt chuẩn xanh ESG</strong>, và <strong>Đầu tư đón đầu vào các cụm trung tâm dữ liệu AI và logistics tự động hóa</strong> để nắm bắt cơ hội tăng trưởng vượt bậc trong kỷ nguyên kinh tế số.</p>
"""
}

# Apply domain expansions to posts 703 to 710
for p in posts:
    pid = p.get('id')
    if pid in domain_expansions:
        p['content'] = p.get('content', '') + domain_expansions[pid]

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("=== FINAL WORD COUNTS FOR ALL 10 MASTER ARTICLES ===")
for p in posts:
    if p.get('id') in range(701, 711):
        print(f"Post {p['id']}: {count_words(p['content'])} words")
