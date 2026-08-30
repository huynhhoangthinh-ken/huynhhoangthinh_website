import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Comprehensive texts for all 10 posts:

# 701: Wealth Report Global & Vietnam (2,500+ words)
p701_text = """
<p class="magazine-dropcap">Tròn hai mươi năm trước, vào năm 2007, khi ấn bản đầu tiên của <strong>The Wealth Report</strong> được công bố bởi tập đoàn tư vấn và nghiên cứu bất động sản quốc tế Knight Frank, nền kinh tế thế giới đang đắm chìm trong giai đoạn hoàng kim của toàn cầu hóa không biên giới, thanh khoản tài chính dồi dào và lãi suất rẻ. Bước sang năm 2026, kỷ niệm tròn 2 thập kỷ của báo cáo danh giá này, bối cảnh kinh tế vĩ mô toàn cầu đã chuyển biến sâu sắc sang một trạng thái hoàn toàn mới: <em>một trật tự kinh tế phân cực (Fractured Geopolitical Landscape)</em>, nơi các cú sốc địa chính trị, xung đột năng lượng và áp lực lạm phát diễn ra với tần suất ngày càng dày đặc. Tuy nhiên, giữa bức tranh đầy biến động đó, một quy luật kinh tế cốt lõi vẫn không ngừng bứt phá: <strong>tốc độ tạo lập tài sản của giới siêu giàu (UHNWI - Ultra High Net Worth Individuals) đang diễn ra với quy mô và vận tốc lớn nhất trong lịch sử nhân loại</strong>.</p>

<figure class="magazine-figure">
  <img src="assets/Index_asset/editorial_luxury_house_exterior_photo_0923_NgoaiThat_KienTruc_HoangHon_BanDem.jpg" alt="Kiến trúc dinh thự siêu sang — Biểu tượng của sự tích lũy tài sản tinh hoa trong kỷ nguyên mới" loading="lazy">
  <figcaption class="magazine-figcaption">The Wealth Report 2026: Dân số UHNWI toàn cầu đạt 713.626 người, phản ánh sự mở rộng của cải bất chấp biến động kinh tế vĩ mô.</figcaption>
</figure>

<div class="key-takeaways">
  <h3>Những Số Liệu Trọng Tâm Từ Mô Hình Định Lượng Tài Sản Wealth Sizing Model 2026</h3>
  <ul>
    <li><strong>Kỷ lục dân số UHNWI toàn cầu:</strong> Tổng số cá nhân có tài sản ròng từ 30 triệu USD trở lên đã chạm mốc <strong>713.626 người</strong> vào năm 2026 (tăng 29.4% từ 551.435 người năm 2021). Dự báo chạm ngưỡng <strong>948.241 người</strong> vào năm 2031 (+32.9%).</li>
    <li><strong>Mỗi ngày có 89 triệu phú UHNWI mới xuất hiện:</strong> Trong suốt 5 năm qua, trung bình cứ mỗi 24 giờ trôi qua, thế giới lại ghi nhận thêm 89 cá nhân vượt qua ngưỡng tài sản 30 triệu USD.</li>
    <li><strong>Sự thống trị tuyệt đối của nền kinh tế Mỹ:</strong> 41% trong tổng số người siêu giàu mới xuất hiện trong nửa thập kỷ qua thuộc về nước Mỹ, nâng tổng dân số UHNWI của Mỹ lên 251.352 người (chiếm 35.2% toàn cầu và dự báo đạt 40.8% vào 2031 với 387.422 người).</li>
    <li><strong>Việt Nam - Điểm sáng tăng trưởng hàng đầu Châu Á:</strong> Dân số siêu giàu tại Việt Nam dự báo tăng trưởng <strong>59.0% trong giai đoạn 2026 - 2031</strong>, từ 1.233 người lên 1.960 người, thuộc top 4 quốc gia tăng trưởng nhanh nhất thế giới.</li>
  </ul>
</div>

<h2>Chương I: Nhìn Lại Hai Thập Kỷ 'Plutonomy' (2007 – 2026)</h2>
<p>Thuật ngữ <strong>Plutonomy</strong> (nền kinh tế do tầng lớp siêu giàu dẫn dắt) lần đầu tiên được định nghĩa vào năm 2005 bởi nhà kinh tế học Ajay Kapur tại tập đoàn tài chính Citigroup. Luận điểm cốt lõi của Kapur khi đó vô cùng rõ ràng: khi của cải tập trung ngày càng lớn vào tay nhóm 1% chóp bu, các quy luật kinh tế học tiêu dùng truyền thống sẽ bị bẻ gãy. Nhu cầu của nhóm siêu giàu sẽ định hình toàn bộ các thị trường tài sản cao cấp, từ bất động sản biểu tượng, nghệ thuật kinh điển cho đến du thuyền và hàng không thương gia.</p>

<p>Nhà ngân hàng tư nhân kỳ cựu <strong>David Poole</strong> (cựu Giám đốc Citi Private Bank UK, người đã đồng hành cùng Knight Frank xuất bản 6 ấn bản đầu tiên của The Wealth Report) chia sẻ trong ấn phẩm 2026:</p>
<div class="magazine-quote">'Hai mươi năm qua đã chứng minh tính đúng đắn tuyệt đối của luận thuyết Plutonomy. Thế giới luôn tạo ra những cơ chế ưu tiên cho người có nhiều vốn hơn. Càng lên cao trên tháp tài sản, tốc độ tích lũy của cải biên (incremental wealth creation) lại càng tăng theo cấp số nhân.'</div>

<p>Sau cuộc khủng hoảng tài chính toàn cầu 2008, chính sách nới lỏng định lượng (QE) và kỷ nguyên lãi suất siêu thấp kéo dài đã tạo ra một lực đẩy vô tiền khoáng hậu. Giới siêu giàu dễ dàng tiếp cận các nguồn vốn vay ngân hàng với lãi suất đơn vị thấp (1-3%) để đòn bẩy tài sản, trong khi các danh mục đầu tư bất động sản và cổ phiếu mang lại lợi nhuận kép hai chữ số hàng năm. Điều này tạo nên một khoảng cách phân kỳ sâu sắc giữa những người sở hữu tài sản vốn (Capital Owners) và những người sống dựa vào thu nhập tiền lương thuần túy.</p>

<p>Đến năm 2026, sự kết hợp giữa công nghệ số, trí tuệ nhân tạo (AI) và các nền tảng thương mại toàn cầu hóa đã tiếp tục nhân rộng quy mô tài sản với tốc độ chóng mặt. Những người sáng lập công nghệ và các nhà đầu tư mạo hiểm chỉ mất từ 3 đến 5 năm để xây dựng một doanh nghiệp kỳ lân (Unicorn) trị giá hàng tỷ USD, so với mốc thời gian từ 20 đến 30 năm của các ngành công nghiệp truyền thống thế kỷ 20.</p>

<h2>Chương II: Phân Tích Chuyên Sâu Dữ Liệu Wealth Sizing Model 2026</h2>
<p>Mô hình định lượng tài sản <strong>Wealth Sizing Model</strong> do nhóm Khoa học Dữ liệu (Data Science) của Knight Frank xây dựng đã phác họa bức tranh toàn cảnh về sự phân bổ của 713.626 cá nhân UHNWI trên toàn cầu:</p>

<h3>1. Khu Vực Bắc Mỹ: Cỗ Máy Sản Sinh Tài Sản Công Nghệ</h3>
<p>Bắc Mỹ tiếp tục giữ vị thế đầu tàu thống trị với 264.272 người siêu giàu (chiếm 37.0% toàn cầu), và dự kiến sẽ tăng vọt lên 404.218 người vào năm 2031. Nền kinh tế Mỹ kết hợp hoàn hảo giữa quy mô thị trường khổng lồ, hệ thống pháp lý bảo vệ quyền sở hữu tư nhân chặt chẽ, và đặc biệt là hệ sinh thái công nghệ AI, bán dẫn và đầu tư mạo hiểm (Venture Capital). Các trung tâm như Silicon Valley, Austin, Miami và New York liên tục sản sinh ra những thế hệ triệu phú và tỷ phú công nghệ mới chỉ trong thời gian rất ngắn.</p>

<h3>2. Châu Á - Thái Bình Dương: Thủ Phủ Tỷ Phú Của Thế Giới</h3>
<p>Châu Á - Thái Bình Dương ghi nhận 219.310 cá nhân UHNWI vào năm 2026 và dự báo đạt 272.530 người vào năm 2031. Tuy nhiên, điểm đặc biệt nhất của khu vực này là sự tập trung của <strong>1.116 tỷ phú đô la (Billionaires)</strong> — chiếm tới 35.9% tổng số tỷ phú của toàn nhân loại, vượt xa Bắc Mỹ (965 tỷ phú) và Châu Âu (780 tỷ phú). Sự chuyển dịch trọng tâm của cải sang Châu Á phản ánh sự trỗi dậy của các chuỗi cung ứng công nghiệp toàn cầu, sự phát triển thần tốc của cơ sở hạ tầng đô thị và tốc độ gia tăng tầng lớp trung lưu và thượng lưu tại các quốc gia như Trung Quốc, Ấn Độ, Indonesia và Việt Nam.</p>

<h3>3. Châu Âu & Trung Đông: Hai Sắc Thái Đầu Tư Tương Phản</h3>
<p>Châu Âu hiện có 183.953 cá nhân siêu giàu, tăng trưởng ổn định ở mức +17.0% đến năm 2031. Mặc dù đối mặt với thách thức về già hóa dân số và chính sách thuế tài sản khắt khe, Châu Âu vẫn là trung tâm bảo tồn di sản gia tộc không thể thay thế. Ngược lại, khu vực Trung Đông (với 21.922 cá nhân UHNWI và 128 tỷ phú) đang nổi lên như một thỏi nam châm hút vốn toàn cầu nhờ các chiến lược chuyển đổi kinh tế phi dầu mỏ, chính sách thuế ưu đãi và sự phát triển vượt bậc của các đô thị quốc tế như Dubai và Abu Dhabi.</p>

<table style="width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 14px;">
  <thead>
    <tr style="background: #111; color: #fff;">
      <th style="padding: 12px; border: 1px solid #333; text-align: left;">Khu Vực Địa Lý</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Số Lượng UHNWI (2021)</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Số Lượng UHNWI (2026)</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Dự Báo UHNWI (2031)</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Tăng Trưởng 2026-2031</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Bắc Mỹ</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">195,089</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">264,272</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>404,218</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;"><strong>+53.0%</strong></td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Châu Á - TBD</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">175,776</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">219,310</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>272,530</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;"><strong>+24.3%</strong></td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Châu Âu</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">146,525</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">183,953</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>215,195</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;"><strong>+17.0%</strong></td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Trung Đông</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">13,486</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">21,922</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>28,956</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;"><strong>+32.1%</strong></td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Mỹ Latinh</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">14,284</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">16,847</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>18,930</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;"><strong>+12.4%</strong></td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Châu Phi</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">6,275</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">7,322</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>8,412</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;"><strong>+14.9%</strong></td></tr>
    <tr style="background: #f5f5f5; font-weight: bold;"><td style="padding: 10px; border: 1px solid #333;"><strong>TOÀN CẦU</strong></td><td style="padding: 10px; border: 1px solid #333; text-align: center;"><strong>551,435</strong></td><td style="padding: 10px; border: 1px solid #333; text-align: center;"><strong>713,626</strong></td><td style="padding: 10px; border: 1px solid #333; text-align: center;"><strong>948,241</strong></td><td style="padding: 10px; border: 1px solid #333; text-align: center; color: blue;"><strong>+32.9%</strong></td></tr>
  </tbody>
</table>

<h2>Chương III: Việt Nam Trên Bản Đồ Tích Sản Thế Giới — Tăng Trưởng 59% Đến 2031</h2>
<p>Báo cáo của Knight Frank dành sự quan tâm đặc biệt đến Việt Nam như một trong những thị trường mới nổi có tốc độ gia tăng người siêu giàu nhanh nhất thế giới. Từ mức 954 người năm 2021, số lượng UHNWI tại Việt Nam đã đạt 1.233 người năm 2026 (+29.2%), và được dự báo sẽ đạt mốc <strong>1.960 người vào năm 2031 (+59.0%)</strong>.</p>

<p>Sự tích lũy tài sản thần tốc tại Việt Nam gắn liền với sự chuyển dịch cơ cấu kinh tế mạnh mẽ:</p>
<ul>
  <li><strong>Vị thế mắt xích công nghiệp toàn cầu:</strong> Làn sóng FDI đổ vào các tổ hợp bán dẫn, linh kiện điện tử và sản xuất năng lượng tái tạo tạo ra giá trị gia tăng khổng lồ cho các doanh nghiệp phụ trợ nội địa.</li>
  <li><strong>Đô thị hóa và nâng tầm hạ tầng:</strong> Các đại dự án hạ tầng giao thông (sân bay quốc tế Long Thành, các tuyến đường vành đai 3, vành đai 4, các tuyến metro tại TP.HCM và Hà Nội) mở ra những chu kỳ tăng giá trị đất đai và bất động sản thương mại dài hạn.</li>
  <li><strong>Thế hệ doanh nhân kế nghiệp (Next-Gen Wealth):</strong> Sự chuyển giao tài sản từ thế hệ doanh nhân F1 (những người làm giàu từ sản xuất, thương mại truyền thống) sang thế hệ F2 (những người có tư duy tài chính toàn cầu, đầu tư công nghệ số, kinh tế xanh và bất động sản hàng hiệu).</li>
</ul>

<p>Sự gia tăng nhanh chóng của tầng lớp siêu giàu tại Việt Nam đang kéo theo sự hình thành của một thị trường tiêu dùng cao cấp hoàn toàn mới. Nhu cầu về các dinh thự ven sông biệt lập, căn hộ penthouse trung tâm thành phố, du thuyền tư nhân, đồng hồ haute horlogerie và các dịch vụ quản lý gia sản chuyên nghiệp (Family Office) đang bùng nổ, đưa Việt Nam trở thành một trong những thị trường xa xỉ năng động bậc nhất khu vực Đông Nam Á.</p>

<h2>Chương IV: Góc Nhìn Đại Chúng: Làn Sóng Tranh Luận Xã Hội Học Về Của Cải & Bất Bình Đẳng</h2>
<p>Sự gia tăng phi mã của giới siêu giàu không thể chỉ được nhìn nhận thuần túy qua lăng kính của những người thụ hưởng. Trong tâm thức của đại chúng và xã hội đương đại, những con số triệu đô và tỷ đô luôn gợi lên những làn sóng tranh luận sâu sắc, đa chiều và đầy trăn trở.</p>

<h3>1. Sự Trăn Trở Của Số Đông: Áp Lực Chi Phí Sinh Hoạt & Khát Vọng Bình Đẳng</h3>
<p>Đối với hàng trăm triệu người lao động thuộc tầng lớp trung lưu và bình dân trên toàn cầu, sự tương phản giàu - nghèo trở nên rõ rệt hơn bao giờ hết khi họ phải đối mặt với áp lực lạm phát chi phí sinh hoạt (Cost of Living Crisis), giá năng lượng tăng cao do căng thẳng địa chính trị, và đặc biệt là sự leo thang không ngừng của giá nhà ở đô thị. Một người lao động trẻ tại các thành phố lớn như London, New York, Tokyo hay TP.HCM có thể phải mất từ 25 đến 40 năm thu nhập trung bình để có thể sở hữu một căn hộ khiêm tốn.</p>

<p>Điều này làm bùng lên các cuộc tranh luận chính trị gay gắt tại nhiều quốc gia phương Tây, với việc các cử tri đại chúng ủng hộ các chính sách đánh thuế lũy tiến mạnh tay vào tài sản (Mansion Tax tại Los Angeles, việc bãi bỏ quy chế ưu đãi thuế Non-Dom tại Vương quốc Anh, hay các đề xuất đánh thuế tỷ phú tại Pháp và Mỹ). Đại chúng đòi hỏi một trật tự xã hội công bằng hơn, nơi tầng lớp siêu giàu phải đóng góp tỷ lệ thuế tương xứng với nguồn lực họ đang thụ hưởng để tài trợ cho hệ thống y tế công cộng, trường học và mạng lưới an sinh xã hội.</p>

<h3>2. Phân Tích Kinh Tế Phản Biện: Bản Chất Của Dòng Vốn Tư Nhân</h3>
<p>Tuy nhiên, các chuyên gia kinh tế hàng đầu trong The Wealth Report 2026 cũng đưa ra góc nhìn phản biện khách quan: <em>việc đánh thuế trừng phạt cực đoan không phải là lời giải bền vững cho sự thịnh vượng xã hội</em>. Khi một quốc gia siết thuế quá mức, dòng vốn tư nhân — vốn có tính cơ động rất cao trong kỷ nguyên số — sẽ nhanh chóng rời bỏ quốc gia đó để chuyển sang các trung tâm có môi trường thể chế thân thiện hơn (như trường hợp hàng nghìn gia đình giàu có rời London sang Milan, Dubai và Thụy Sĩ trong năm 2025).</p>

<p>Hơn thế nữa, của cải của các doanh nhân siêu giàu không phải là tiền mặt nằm yên trong két sắt, mà chính là nguồn vốn đầu tư mạo hiểm chấp nhận rủi ro để phát triển những công nghệ đột phá: từ trí tuệ nhân tạo (AI), điện hạt nhân sạch, y học tái tạo chữa ung thư cho đến hạ tầng vệ tinh không gian. Nguồn vốn này tạo ra hàng triệu việc làm có thu nhập cao và kéo theo sự tăng trưởng của toàn bộ nền kinh tế.</p>

<h2>Chương V: Chiến Lược Quản Trị Rủi Ro & Phân Bổ Danh Mục Trong Kỷ Nguyên Biến Động</h2>
<p>Đứng trước một thế giới phân cực và nhiều bất định, báo cáo của Knight Frank khuyến nghị 4 nguyên tắc cốt lõi giúp các gia tộc bảo vệ và phát triển tài sản bền vững:</p>
<ol>
  <li><strong>Đa dạng hóa địa lý (Geographic Diversification):</strong> Không bao giờ tập trung toàn bộ tài sản tại một quốc gia duy nhất. Thiết lập các trung tâm quản lý tài sản tại ít nhất 2 đến 3 trung tâm tài chính lớn (Bắc Mỹ, Châu Âu, Châu Á - Thái Bình Dương) để phân tán rủi ro chính trị và pháp lý.</li>
  <li><strong>Tăng tỷ trọng tài sản hữu hình có tính khan hiếm cao (Hard & Tangible Assets):</strong> Nắm giữ bất động sản biểu tượng tại trung tâm các đô thị di sản, các dinh thự ven sông, đất trồng nho Grand Cru và các tác phẩm nghệ thuật kinh điển. Đây là những tài sản không thể nhân bản và có khả năng bảo toàn giá trị vượt trội trước mọi chu kỳ lạm phát tiền tệ.</li>
  <li><strong>Đầu tư vào hạ tầng tương lai:</strong> Phân bổ vốn vào các lĩnh vực hạ tầng năng lượng tái tạo, trung tâm dữ liệu AI, logistics tự động hóa và y học công nghệ cao — những ngành có nhu cầu tăng trưởng cấu trúc không phụ thuộc vào chu kỳ kinh tế ngắn hạn.</li>
  <li><strong>Hoạch định chuyển giao thế hệ chuyên nghiệp:</strong> Xây dựng hiến pháp gia tộc (Family Constitution), thành lập các quỹ tín thác độc lập và đào tạo thế hệ kế thừa về đạo đức kinh doanh và quản trị rủi ro.</li>
</ol>

<h2>Chương VI: Tầm Nhìn Chiến Lược 2026 – 2035 & Giá Trị Di Sản Bền Vững</h2>
<p>Khép lại bản báo cáo 20 năm, Knight Frank nhấn mạnh rằng: bước sang kỷ nguyên 2026 - 2035, thách thức lớn nhất của các gia tộc siêu giàu không còn là việc gia tăng số lượng tài sản bằng mọi giá, mà là <strong>nghệ thuật định vị và sử dụng đồng vốn một cách nhân văn, có trách nhiệm với cộng đồng và môi trường sinh thái</strong>.</p>

<p>Các chuẩn mực đầu tư tạo tác động xã hội (Impact Investing), phát triển bất động sản đạt chứng chỉ xanh Net-Zero, bảo tồn các di sản văn hóa và tài trợ cho các nghiên cứu y học trường thọ chính là chiếc cầu nối hài hòa giúp thu hẹp khoảng cách giữa giới tinh hoa và đại chúng xã hội, tạo dựng một nền tảng thịnh vượng chung và bền vững cho toàn nhân loại.</p>

<div class="magazine-quote">"Sự giàu có thực sự của một đời người không được đo bằng những con số vô hồn trên bảng cân đối tài sản, mà được đo bằng những giá trị nhân văn mà bạn đã để lại cho cuộc đời và thế hệ mai sau." — Huỳnh Hoàng Thịnh</div>
"""

# Let's apply p701 to posts
for p in posts:
    if p.get('id') == 701:
        p['content'] = p701_text

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print('Post 701 Word Count:', count_words(p701_text))
