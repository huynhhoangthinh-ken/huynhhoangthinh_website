import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Dictionary of all 10 long-form texts (2500+ words each)
essays = {}

# 702: PIRI 100 Global Luxury Housing Index (2,500+ words)
essays[702] = """
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

<h2>Chương III: Sáu Động Lực Cốt Lõi Định Hình Bất Động Sản Siêu Sang 2026</h2>
<p>Knight Frank phân tích 6 xu hướng cấu trúc sâu sắc đang tái định hình thị trường nhà ở thượng lưu:</p>
<ol>
  <li><strong>Sự gia tốc của việc tạo lập tài sản (Rise of Wealth Creation):</strong> Tốc độ tích lũy của cải của tầng lớp UHNWI toàn cầu đạt 5.3%/năm, vượt xa mức tăng trưởng GDP thế giới (3.3%), tạo ra nguồn cầu dồi dào và bền bỉ cho bất động sản cao cấp.</li>
  <li><strong>Chính sách thuế thúc đẩy di chuyển tài sản (Tax & Wealth Migration):</strong> Các sắc thuế mới như Mansion Tax ở Los Angeles hay việc bãi bỏ Non-Dom tại Anh đang thúc đẩy dòng vốn di chuyển sang Monaco, Ý, UAE và Thụy Sĩ.</li>
  <li><strong>Lối sống siêu cơ động 'Dip-in, Dip-out':</strong> Giới siêu giàu không còn sống cố định tại một thành phố duy nhất mà tổ chức cuộc sống linh hoạt giữa 3 đến 5 căn hộ tại các trung tâm tài chính toàn cầu.</li>
  <li><strong>Sự cạnh tranh và kết nối giữa các trung tâm tài sản:</strong> Các cặp đô thị như Hong Kong - Singapore, London - Dubai, New York - Miami đang hình thành các mạng lưới kết nối dòng vốn tương hỗ.</li>
  <li><strong>Nguồn cung hoàn thiện khan hiếm nghiêm trọng (Scarcity of Turnkey Stock):</strong> Chi phí xây dựng leo thang và quy trình cấp phép kéo dài khiến các bất động sản chìa khóa trao tay (Move-in-ready) tại vị trí đắc địa luôn được giao dịch với mức giá chênh lệch kỷ lục.</li>
  <li><strong>Sự bùng nổ của Bất động sản hàng hiệu (Branded Residences):</strong> Dự báo thị trường sẽ vượt mốc 1.000 dự án vào năm 2030, mở rộng mạnh mẽ sang các thương hiệu thời trang, phong cách sống và siêu xe.</li>
</ol>

<h2>Chương IV: Góc Nhìn Đại Chúng: Cơn Sốt Giá Nhà Ở & Nỗi Trăn Trở Của Cộng Đồng</h2>
<p>Đối với hàng triệu cư dân đô thị trên toàn cầu, những con số tăng trưởng phi mã của chỉ số PIRI 100 không chỉ là những biểu đồ tài chính khô khan; chúng tác động trực tiếp đến tâm lý và cấu trúc đời sống xã hội.</p>

<h3>1. Sự Trăn Trở Của Tầng Lớp Trẻ & Khủng Hoảng Nhà Ở Vừa Túi Tiền</h3>
<p>Đối với hàng triệu gia đình trẻ thuộc thế hệ Millennials và Gen Z tại các thành phố lớn trên thế giới, sự leo thang của giá đất trung tâm đã đẩy giấc mơ sở hữu nhà riêng ra xa tầm với. Việc các nhà phát triển bất động sản ưu tiên nguồn lực quỹ đất hạn chế cho các dự án hạng sang mang lại biên lợi nhuận cao tạo nên cảm giác lo âu trong cộng đồng về sự thiếu hụt các sản phẩm nhà ở vừa túi tiền (Affordable Housing). Người lao động buộc phải chuyển dịch ra các đô thị vệ tinh xa xôi, chịu cảnh tắc nghẽn giao thông hàng giờ mỗi ngày để di chuyển vào trung tâm làm việc.</p>

<h3>2. Sự Tương Hỗ Đô Thị: Dòng Vốn Thượng Lưu Nuôi Dưỡng Hạ Tầng Xã Hội</h3>
<p>Tuy nhiên, nhìn từ góc độ kinh tế vĩ mô và quy hoạch đô thị, các chuyên gia của Knight Frank phân tích rằng: <em>thị trường bất động sản cao cấp không phải là kẻ đối đầu của nhà ở đại chúng, mà là nguồn lực tài trợ thiết yếu cho sự phát triển đô thị</em>. Các dự án bất động sản siêu sang đóng góp nguồn thu ngân sách khổng lồ từ tiền sử dụng đất, thuế trước bạ và thuế chuyển nhượng, tài trợ trực tiếp cho các công trình hạ tầng công cộng như tuyến metro, công viên, bệnh viện và trường học phục vụ toàn thể người dân.</p>

<p>Hơn thế nữa, các tiêu chuẩn khắt khe về kiến trúc xanh (LEED, BREEAM), công nghệ tiết kiệm năng lượng và giải pháp xử lý nước thải thông minh được tiên phong áp dụng tại các dự án hạng sang sau đó sẽ được chuẩn hóa và lan tỏa rộng rãi sang toàn bộ thị trường xây dựng đại chúng.</p>

<h2>Chương V: Chiến Lược Tích Sản Bất Động Sản Biểu Tượng Dành Cho Nhà Đầu Tư Việt Nam</h2>
<p>Đứng trước bức tranh PIRI 100 toàn cầu, các nhà đầu tư bất động sản Việt Nam có thể rút ra những nguyên tắc vàng để tối đa hóa lợi nhuận và bảo toàn tài sản:</p>
<ul>
  <li><strong>Ưu tiên vị trí độc tôn không thể sao chép:</strong> Các bất động sản có tầm nhìn trực diện mặt sông, công viên trung tâm hoặc tại các khu tài chính lõi luôn có biên độ tăng giá vượt trội và giữ giá tốt nhất trong các cuộc khủng hoảng kinh tế.</li>
  <li><strong>Lựa chọn sản phẩm chìa khóa trao tay và có đơn vị quản lý quốc tế:</strong> Nhu cầu của khách thuê cao cấp và thế hệ siêu giàu trẻ tuổi luôn hướng về những căn hộ được hoàn thiện đầy đủ nội thất cao cấp với dịch vụ quản gia 24/7.</li>
  <li><strong>Tận dụng biên độ định giá hấp dẫn của TP.HCM:</strong> Với mức giá bình quân từ 5.000 đến 12.000 USD/m² tại khu vực Thủ Thiêm, Quận 1 và Nam Sài Gòn, TP.HCM vẫn đang ở vùng trũng định giá so với Bangkok (15.000 USD/m²), Singapore (60.000 USD/m²) và Hong Kong (80.000 USD/m²).</li>
</ul>

<h2>Chương VI: Tầm Nhìn Chiến Lược 2026 – 2035</h2>
<p>Thị trường bất động sản cao cấp toàn cầu đang bước vào một kỷ nguyên phát triển mới nơi chất lượng sống, tiện ích sức khỏe và tính bền vững sinh thái trở thành thước đo giá trị tối thượng. Nắm giữ những bất động sản biểu tượng tại các đô thị đang trên đà phát triển vượt bậc chính là chiến lược tích sản thông minh nhất để bảo vệ và nhân rộng khối tài sản gia tộc qua các thế hệ.</p>

<div class="magazine-quote">"Đầu tư vào bất động sản siêu sang tại vị trí trung tâm độc tôn không phải là trò chơi đầu cơ lướt sóng, mà là nghệ thuật nắm giữ tài sản khan hiếm nhất của một đô thị đang trên đà cất cánh vươn tầm quốc tế." — Huỳnh Hoàng Thịnh</div>
"""

# Apply to posts
for p in posts:
    if p.get('id') in essays:
        p['content'] = essays[p.get('id')]

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print('Post 702 Word Count:', count_words(essays[702]))
