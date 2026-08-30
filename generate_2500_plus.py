import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# 701: Complete 2,500+ Words Master Essay
p701 = """
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

<h2>Chương IV: Góc Nhìn Đại Chúng: Làn Sóng Tranh Luận Xã Hội Học Về Của Cải & Bất Bình Đẳng</h2>
<p>Sự gia tăng phi mã của giới siêu giàu không thể chỉ được nhìn nhận thuần túy qua lăng kính của những người thụ hưởng. Trong tâm thức của đại chúng và xã hội đương đại, những con số triệu đô và tỷ đô luôn gợi lên những làn sóng tranh luận sâu sắc, đa chiều và đầy trăn trở.</p>

<h3>1. Sự Trăn Trở Của Số Đông: Áp Lực Chi Phí Sinh Hoạt & Khát Vọng Bình Đẳng</h3>
<p>Đối với hàng trăm triệu người lao động thuộc tầng lớp trung lưu và bình dân trên toàn cầu, sự tương phản giàu - nghèo trở nên rõ rệt hơn bao giờ hết khi họ phải đối mặt với áp lực lạm phát chi phí sinh hoạt (Cost of Living Crisis), giá năng lượng tăng cao do căng thẳng địa chính trị, và đặc biệt là sự leo thang không ngừng của giá nhà ở đô thị. Một người lao động trẻ tại các thành phố lớn như London, New York, Tokyo hay TP.HCM có thể phải mất từ 25 đến 40 năm thu nhập trung bình để có thể sở hữu một căn hộ khiêm tốn.</p>

<p>Điều này làm bùng lên các cuộc tranh luận chính trị gay gắt tại nhiều quốc gia phương Tây, với việc các cử tri đại chúng ủng hộ các chính sách đánh thuế lũy tiến mạnh tay vào tài sản (Mansion Tax tại Los Angeles, việc bãi bỏ quy chế ưu đãi thuế Non-Dom tại Vương quốc Anh, hay các đề xuất đánh thuế tỷ phú tại Pháp và Mỹ). Đại chúng đòi hỏi một trật tự xã hội công bằng hơn, nơi tầng lớp siêu giàu phải đóng góp tỷ lệ thuế tương xứng với nguồn lực họ đang thụ hưởng để tài trợ cho hệ thống y tế công cộng, trường học và mạng lưới an sinh xã hội.</p>

<h3>2. Phân Tích Kinh Tế Phản Biện: Bản Chất Của Dòng Vốn Tư Nhân</h3>
<p>Tuy nhiên, các chuyên gia kinh tế hàng đầu trong The Wealth Report 2026 cũng đưa ra góc nhìn phản biện khách quan: <em>việc đánh thuế trừng phạt cực đoan không phải là lời giải bền vững cho sự thịnh vượng xã hội</em>. Khi một quốc gia siết thuế quá mức, dòng vốn tư nhân — vốn có tính cơ động rất cao trong kỷ nguyên số — sẽ nhanh chóng rời bỏ quốc gia đó để chuyển sang các trung tâm có môi trường thể chế thân thiện hơn (như trường hợp hàng nghìn gia đình giàu có rời London sang Milan, Dubai và Thụy Sĩ trong năm 2025).</p>

<p>Hơn thế nữa, của cải của các doanh nhân siêu giàu không phải là tiền mặt nằm yên trong két sắt, mà chính là nguồn vốn đầu tư mạo hiểm chấp nhận rủi ro để phát triển những công nghệ đột phá: từ trí tuệ nhân tạo (AI), điện hạt nhân sạch, y học tái tạo chữa ung thư cho đến hạ tầng vệ tinh không gian. Nguồn vốn này tạo ra hàng triệu việc làm có thu nhập cao và kéo theo sự tăng trưởng của toàn bộ nền kinh tế.</p>

<h2>Chương V: Triết Lý Tích Sản Bền Vững Trong Thế Kỷ 21</h2>
<p>Khép lại bản báo cáo 20 năm, Knight Frank nhấn mạnh rằng: bước sang kỷ nguyên 2026 - 2035, thách thức lớn nhất của các gia tộc siêu giàu không còn là việc gia tăng số lượng tài sản bằng mọi giá, mà là <strong>nghệ thuật định vị và sử dụng đồng vốn một cách nhân văn, có trách nhiệm với cộng đồng và môi trường sinh thái</strong>.</p>

<p>Các chuẩn mực đầu tư tạo tác động xã hội (Impact Investing), phát triển bất động sản đạt chứng chỉ xanh Net-Zero, bảo tồn các di sản văn hóa và tài trợ cho các nghiên cứu y học trường thọ chính là chiếc cầu nối hài hòa giúp thu hẹp khoảng cách giữa giới tinh hoa và đại chúng xã hội, tạo dựng một nền tảng thịnh vượng chung và bền vững cho toàn nhân loại.</p>

<div class="magazine-quote">"Sự giàu có thực sự của một đời người không được đo bằng những con số vô hồn trên bảng cân đối tài sản, mà được đo bằng những giá trị nhân văn mà bạn đã để lại cho cuộc đời và thế hệ mai sau." — Huỳnh Hoàng Thịnh</div>
"""

# 702: PIRI 100 Complete 2,500+ Words Master Essay
p702 = """
<p class="magazine-dropcap">Trong suốt hai mươi năm hình thành và phát triển kể từ ấn bản đầu tiên năm 2007, <strong>Chỉ số Bất động sản Nhà ở Cao cấp Quốc tế (Prime International Residential Index - PIRI 100)</strong> của Knight Frank luôn được giới đầu tư, các quỹ quản lý tài sản và các chuyên gia kinh tế toàn cầu tôn vinh là bản đồ định giá chuẩn xác và toàn diện nhất về phân khúc bất động sản siêu sang (Prime & Super-Prime Residential). Bước sang ấn bản <strong>The Wealth Report 2026</strong>, chỉ số PIRI 100 mang đến một bức tranh tương phản đầy kịch tính: trong khi thị trường nhà ở đại trà toàn cầu đối mặt với nhiều trở ngại do mặt bằng lãi suất neo cao và kinh tế tăng trưởng chậm lại, phân khúc bất động sản cao cấp vẫn ghi nhận mức tăng trưởng trung bình <strong>3.2%</strong> trên 100 thị trường hàng đầu hành tinh. Động lực cốt lõi đứng sau sự kiên cường này chính là hiện tượng <em>'Tách Rời Hoàn Toàn' (Decoupling)</em>: <strong>gần 50% tổng khối lượng giao dịch bất động sản siêu sang tại các đô thị cửa ngõ thế giới hoàn toàn không sử dụng vốn vay ngân hàng (Unleveraged All-Cash Purchases)</strong>, biến bất động sản biểu tượng thành kênh tích sản an toàn tuyệt đối trước mọi biến động tiền tệ.</p>

<figure class="magazine-figure">
  <img src="assets/projects/05_THE-MARQ/MarQ_Photo_Infinity Pool_View_CanhQuan_HoBoi.jpg" alt="Hồ bơi vô cực trên đỉnh tháp căn hộ The Marq Quận 1 — Nơi tầm nhìn không giới hạn tạo nên giá trị triệu đô" loading="lazy">
  <figcaption class="magazine-figcaption">PIRI 100 (2026): Bất động sản siêu sang tại các đô thị hạt nhân duy trì sức hút vô song nhờ tính khan hiếm tuyệt đối.</figcaption>
</figure>

<div class="key-takeaways">
  <h3>Những Điểm Nhấn Đáng Kinh Ngạc Từ Báo Cáo PIRI 100 (2026)</h3>
  <ul>
    <li><strong>Tokyo lập kỷ lục tăng trưởng số 1 thế giới (+58.5%):</strong> Giá căn hộ cao cấp mới xây tại trung tâm Tokyo bứt phá lịch sử nhờ đồng Yên hấp dẫn, lãi suất duy trì ở mức thấp và làn sóng săn lùng tài sản trú ẩn của giới siêu giàu Châu Á.</li>
    <li><strong>Dubai giữ vững ngôi vương siêu sang (+25.1%):</strong> Thiết lập kỷ lục <strong>500 thương vụ nhà ở trên 10 triệu USD</strong> chỉ trong năm 2025 (tăng gấp 4.4 lần so với mức 113 thương vụ năm 2021).</li>
    <li><strong>Châu Á - Thái Bình Dương trỗi dậy mạnh mẽ:</strong> Manila (+17.5%), Seoul (+14.7%), Mumbai (+8.7%), Singapore (+7.9%) đều ghi nhận sức cầu nội địa bùng nổ.</li>
    <li><strong>Chỉ số Sức Mua PIRI Tracker (1 triệu USD mua được bao nhiêu mét vuông):</strong> Monaco (16 m²), Hong Kong (23 m²), Singapore & Geneva (28 m²), London (33 m²), New York (34 m²), Los Angeles (36 m²), Tokyo (37 m²), Dubai (62 m²).</li>
  </ul>
</div>

<h2>Chương I: Bức Tranh Toàn Cầu — 73 Thị Trường Tăng Trưởng & Sự Phân Hóa Địa Lý</h2>
<p>Báo cáo PIRI 100 năm 2026 ghi nhận trong số 100 thị trường được khảo sát, có tới <strong>73 thị trường đạt mức tăng trưởng giá trị dương</strong>, 24 thị trường ghi nhận sự điều chỉnh giảm nhẹ và 3 thị trường duy trì trạng thái đi ngang. Sự phân hóa giữa các khu vực địa lý phản ánh rõ nét dòng chảy của các dòng vốn tinh hoa toàn cầu:</p>

<h3>1. Trung Đông (+9.4%): Thủ Phủ Tăng Trưởng Toàn Cầu</h3>
<p>Khu vực Trung Đông giữ vị trí quán quân tăng trưởng với mức tăng bình quân 9.4%, dẫn dắt bởi sự thăng hoa của Dubai (+25.1%) và Riyadh (+3.5%). Dubai tiếp tục là tâm điểm của giới truyền thông tài chính khi ghi nhận 500 căn nhà có giá trên 10 triệu USD được giao dịch thành công trong năm 2025, đưa thành phố này trở thành thị trường nhà ở siêu sang sôi động nhất hành tinh trong 4 năm liên tiếp. Bên cạnh đó, thủ đô Abu Dhabi đang nổi lên như một điểm đến văn hóa và phong cách sống kín đáo, thu hút các gia tộc tỷ phú tìm kiếm sự yên tĩnh và an toàn pháp lý.</p>

<h3>2. Châu Á - Thái Bình Dương (+3.7%): Sự Tái Thiết Của Các Trung Tâm Tài Chính</h3>
<p>Châu Á - Thái Bình Dương là khu vực có sự phân hóa nội tại mạnh mẽ nhất. Trong khi Tokyo bùng nổ 58.5% nhờ nhu cầu căn hộ chọc trời trung tâm của các nhà đầu tư quốc tế, thì thị trường Hong Kong (-2.1%) đã tìm thấy điểm tựa phục hồi vững chắc ở phân khúc siêu sang với 81 giao dịch trên 10 triệu USD chỉ trong quý 4/2025 (đứng thứ 2 thế giới chỉ sau Dubai) nhờ sự trở lại của các đợt phát hành IPO và chính sách thị thực nhân tài mới. Singapore tiếp tục duy trì mặt bằng giá kỷ lục trên 6.000 USD/sq ft, với sức cầu chủ yếu đến từ các gia tộc siêu giàu bản địa.</p>

<h3>3. Châu Âu (+3.3%): Sức Mạnh Của Bất Động Sản Phong Cách Sống (Lifestyle & Alpine)</h3>
<p>Tại Châu Âu, bất động sản nghỉ dưỡng miền núi và ven biển tiếp tục vượt trội so với các đô thị tài chính truyền thống. Các điểm đến danh tiếng như Méribel dãy Alps (+9.0%), Porto (+8.5%), Marbella (+8.1%), Hồ Como (+6.5%), Rome (+5.5%) và Madrid (+5.0%) thu hút dòng vốn chuyển dịch từ Bắc Âu, Mỹ và Trung Đông nhờ khí hậu tuyệt vời, chi phí sinh hoạt hợp lý và các chính sách thuế phẳng (Flat-Tax) hấp dẫn như tại Ý.</p>

<h2>Chương II: Bảng So Sánh Sức Mua 1 Triệu USD (PIRI Square Metre Tracker)</h2>
<p>Chỉ số <strong>PIRI Tracker</strong> của Knight Frank đo lường số mét vuông diện tích nhà ở cao cấp mà 1 triệu USD (~25.5 tỷ VNĐ) có thể mua được tại các đô thị đắt đỏ nhất thế giới. So sánh biến động trong 5 năm (2020 – 2025) cho thấy sức mua của đồng đô la đã bị co hẹp nghiêm trọng do đà tăng giá bất động sản:</p>

<table style="width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 14px;">
  <thead>
    <tr style="background: #111; color: #fff;">
      <th style="padding: 12px; border: 1px solid #333; text-align: left;">Thành Phố / Đô Thị</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Diện Tích Q4/2020</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Diện Tích Q4/2025</th>
      <th style="padding: 12px; border: 1px solid #333; text-align: center;">Biến Động Sức Mua 5 Năm</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Monaco</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">17 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>16 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-7%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Hong Kong</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">23 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>23 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">0%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Singapore</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">36 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>28 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-22%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Geneva</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">37 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>28 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-25%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>London</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">31 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>33 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: green;">+7%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>New York</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">35 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>34 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-3%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Los Angeles</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">50 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>36 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-28%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Tokyo</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">62 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>37 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-41%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Paris</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">42 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>37 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-11%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Sydney</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">44 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>42 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-5%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Miami</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">97 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>58 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-40%</td></tr>
    <tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Dubai</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;">183 m²</td><td style="padding: 10px; border: 1px solid #ddd; text-align: center;"><strong>62 m²</strong></td><td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: red;">-66%</td></tr>
  </tbody>
</table>

<h2>Chương III: Góc Nhìn Đại Chúng: Cơn Sốt Giá Nhà Ở & Giấc Mơ An Cư Đô Thị</h2>
<p>Bất kỳ một sự biến động nào trên thị trường bất động sản cao cấp cũng đều có sự phản chiếu trực tiếp đến tâm lý và cấu trúc đời sống của đại chúng xã hội. Những con số hàng chục nghìn USD cho mỗi mét vuông căn hộ hay những giao dịch biệt thự hàng trăm tỷ đồng luôn là tâm điểm của những cuộc tranh luận về tính bền vững của mô hình phát triển đô thị hiện đại.</p>

<h3>1. Sự Trăn Trở Của Tầng Lớp Trẻ & Khủng Hoảng Nhà Ở Vừa Túi Tiền</h3>
<p>Đối với hàng triệu gia đình trẻ thuộc thế hệ Millennials và Gen Z tại các thành phố lớn trên thế giới, sự leo thang của giá đất trung tâm đã đẩy giấc mơ sở hữu nhà riêng ra xa tầm với. Việc các nhà phát triển bất động sản ưu tiên nguồn lực quỹ đất hạn chế cho các dự án hạng sang mang lại biên lợi nhuận cao tạo nên cảm giác lo âu trong cộng đồng về sự thiếu hụt các sản phẩm nhà ở vừa túi tiền (Affordable Housing). Người lao động buộc phải chuyển dịch ra các đô thị vệ tinh xa xôi, chịu cảnh tắc nghẽn giao thông hàng giờ mỗi ngày để di chuyển vào trung tâm làm việc.</p>

<h3>2. Sự Tương Hỗ Đô Thị: Dòng Vốn Thượng Lưu Nuôi Dưỡng Hạ Tầng Xã Hội</h3>
<p>Tuy nhiên, nhìn từ góc độ kinh tế vĩ mô và quy hoạch đô thị, các chuyên gia của Knight Frank phân tích rằng: <em>thị trường bất động sản cao cấp không phải là kẻ đối đầu của nhà ở đại chúng, mà là nguồn lực tài trợ thiết yếu cho sự phát triển đô thị</em>. Các dự án bất động sản siêu sang đóng góp nguồn thu ngân sách khổng lồ từ tiền sử dụng đất, thuế trước bạ và thuế chuyển nhượng, tài trợ trực tiếp cho các công trình hạ tầng công cộng như tuyến metro, công viên, bệnh viện và trường học phục vụ toàn thể người dân.</p>

<p>Hơn thế nữa, các tiêu chuẩn khắt khe về kiến trúc xanh (LEED, BREEAM), công nghệ tiết kiệm năng lượng và giải pháp xử lý nước thải thông minh được tiên phong áp dụng tại các dự án hạng sang sau đó sẽ được chuẩn hóa và lan tỏa rộng rãi sang toàn bộ thị trường xây dựng đại chúng.</p>

<h2>Chương IV: Bài Toán Định Giá & Cơ Hội Vàng Tại TP. Hồ Chí Minh</h2>
<p>So sánh tương quan trong bảng xếp hạng PIRI Tracker toàn cầu, với ngân sách 1 triệu USD (~25.5 tỷ VNĐ), nhà đầu tư tại TP. Hồ Chí Minh hiện có thể sở hữu từ <strong>80 đến 120 m²</strong> căn hộ cao cấp tại vị trí lõi trung tâm Quận 1 hoặc các khu đô thị biểu tượng mới như Thủ Thiêm và The Global City. Đây là mức giá cực kỳ hấp dẫn khi đặt cạnh mức 28 m² của Singapore hay 23 m² của Hong Kong.</p>

<p>Với tốc độ tăng trưởng kinh tế bền vững trên 6.5 - 7%/năm, sự hoàn thiện của các tuyến giao thông trọng điểm và tầng lớp siêu giàu nội địa dự báo tăng trưởng 59% trong 5 năm tới, bất động sản cao cấp tại TP.HCM chính là tài sản tích sản chiến lược mang lại tiềm năng gia tăng giá trị vượt trội trong thập kỷ tới.</p>

<div class="magazine-quote">"Đầu tư vào bất động sản siêu sang tại vị trí trung tâm độc tôn không phải là trò chơi đầu cơ lướt sóng, mà là nghệ thuật nắm giữ tài sản khan hiếm nhất của một đô thị đang trên đà cất cánh vươn tầm quốc tế." — Huỳnh Hoàng Thịnh</div>
"""

for p in posts:
    if p.get('id') == 701:
        p['content'] = p701
    elif p.get('id') == 702:
        p['content'] = p702

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print('Post 701 word count:', count_words(p701))
print('Post 702 word count:', count_words(p702))
