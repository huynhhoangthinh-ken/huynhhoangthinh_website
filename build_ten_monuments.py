import json, re

def count_words(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    return len(text.split())

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Titles, topics, images for 701-710
meta = [
    (701, "Báo Cáo Thịnh Vượng The Wealth Report 2026: Dân Số Siêu Giàu Toàn Cầu Đạt 713.626 Người & Xu Hướng Tăng Trưởng 59% Của Việt Nam", "bds", "BẤT ĐỘNG SẢN SIÊU SANG", "assets/Index_asset/editorial_luxury_house_exterior_photo_0923_NgoaiThat_KienTruc_HoangHon_BanDem.jpg", "Dân số UHNWI toàn cầu và sự trỗi dậy của giới siêu giàu Việt Nam."),
    (702, "Chỉ Số PIRI 100 (2026): Bất Động Sản Siêu Sang Toàn Cầu Tăng 3.2% — Tokyo (58.5%), Dubai (25.1%) & Sức Mua Của 1 Triệu USD", "bds", "BẤT ĐỘNG SẢN SIÊU SANG", "assets/projects/05_THE-MARQ/MarQ_Photo_Infinity Pool_View_CanhQuan_HoBoi.jpg", "Phân tích biến động 100 thị trường bất động sản cao cấp hàng đầu thế giới."),
    (703, "Chiến Lược Family Office 2026: 10.000 Văn Phòng Gia Tộc Tái Cấu Trúc Danh Mục — Bất Động Sản Trực Tiếp & AI Data Center Chiếm Ngôi Đầu", "bds", "BẤT ĐỘNG SẢN SIÊU SANG", "assets/Index_asset/editorial_contemporary_building_facade_photo_0130_NgoaiThat_KienTruc_HoangHon_BanDem.jpg", "Khảo sát chiến lược phân bổ tài sản của 10.000 Family Office toàn cầu."),
    (704, "Lối Sống Siêu Cơ Động 'Dip-In, Dip-Out' 2026: Khi Giới Tinh Hoa Chuyển Dịch Tài Sản & Sự Lên Ngôi Của Branded Residences", "bds", "BẤT ĐỘNG SẢN SIÊU SANG", "assets/projects/03_RIVUS/Thumbnail.jpg", "Mô hình sống đa địa điểm và sự bùng nổ của bất động sản hàng hiệu quốc tế."),
    (705, "Chỉ Số Đầu Tư Xa Xỉ KFLII 2026: Nghệ Thuật Ấn Tượng Tăng 13.6%, Đồng Hồ Xa Xỉ Tăng 5.1% & Kỷ Lục Đấu Giá Túi Hermès 10.1 Triệu USD", "luxury", "ĐỒNG HỒ & HÀNG HIỆU", "assets/Posts/Patek Philippe Grandmaster Chime & Nautilus/Patek Philippe Grandmaster Chime & Nautilus:6_thumbnail.avif", "Chỉ số đầu tư tài sản xa xỉ KFLII và xu hướng săn lùng tài sản độc bản."),
    (706, "Thị Trường Siêu Xe Cổ Điển & Halo Cars 2026: Kỷ Lục Đấu Giá Ferrari 250 GTO (38.5 Triệu USD) & Sức Hút Youngtimer", "supercar", "SIÊU XE & HYPERCAR", "assets/Posts/Bugatti_tourbillon_2026/Bugatti Tourbillon (2026)1.jpg", "Kỷ lục đấu giá siêu xe cổ điển và sự lên ngôi của các cỗ máy tốc độ thập niên 90 - 2000."),
    (707, "Thị Trường Siêu Du Thuyền Toàn Cầu 2026 Bùng Nổ 70%: Kỷ Nguyên Megayacht Hydrogen Feadship 821 & Cuộc Đổ Bộ Của Tỷ Phú Công Nghệ", "yacht-jet", "DU THUYỀN & CHUYÊN CƠ", "assets/Posts/Feadship_821_(Viva)_2026/Feadship_821_(Viva)_20261.webp", "Sự phục hồi ngoạn mục 8.5 tỷ USD của ngành công nghiệp siêu du thuyền."),
    (708, "Hàng Không Tư Nhân 2026 & Bản Đồ Sống Đa Điểm: Chuyên Cơ Siêu Tầm Xa Kết Nối Dinh Thự, Resort Đảo Và Trung Tâm Tài Chính", "yacht-jet", "DU THUYỀN & CHUYÊN CƠ", "assets/Posts/Gulfstream_G700/Gulfstream_G700_22_thumbnail.jpg", "Dữ liệu hàng không tư nhân VistaJet và lối sống đa trung tâm của giới thượng lưu."),
    (709, "Đầu Tư Vườn Nho Toàn Cầu Global Vineyard Index 2026: Nghệ Thuật Tích Sản Rượu Vang Tại Burgundy, Tuscany, Bordeaux & Napa Valley", "bds", "BẤT ĐỘNG SẢN SIÊU SANG", "assets/Index_asset/editorial_suburban_house_exterior_photo_0782_NgoaiThat_KienTruc_HoangHon_BanDem.jpg", "Bảng giá đất trồng nho Grand Cru Burgundy 70 triệu USD/ha và xu hướng vang sinh thái."),
    (710, "Bất Động Sản Thương Mại & Hạ Tầng Năng Lượng AI 2026: Làn Sóng 144 Tỷ USD Vốn Tổ Chức & Xu Hướng Tái Sinh Văn Phòng Hạng A", "bds", "BẤT ĐỘNG SẢN SIÊU SANG", "assets/Index_asset/editorial_modern_building_facade_photo_0404_NgoaiThat_KienTruc_BanNgay.jpg", "Khảo sát Active Capital Survey và sự phục hồi của các thương vụ bất động sản thương mại.")
]

# We will build extensive, multi-section essays that surpass 2500 words
