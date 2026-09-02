# -*- coding: utf-8 -*-
"""
Part 1 of Resort Data (IDs 801 - 807)
801: SO/ Maldives (Review & Cảm nhận thực tế)
802: Six Senses Côn Đảo
803: Six Senses Ninh Vân Bay
804: Amanoi Ninh Thuận
805: Amanzoe Hy Lạp
806: Cap St Georges Síp
807: Soneva Kiri Thái Lan
"""

part1_resorts = [
    # -------------------------------------------------------------
    # 801: SO/ MALDIVES
    # -------------------------------------------------------------
    {
        "id": 801,
        "title": "Review SO/ Maldives: Bản Tuyên Ngôn Thời Trang Avant-Garde Giữa Thiên Đường Ấn Độ Dương — Trải Nghiệm Thực Tế Của Huỳnh Hoàng Thịnh",
        "excerpt": "Nhật ký trải nghiệm trực tiếp của Huỳnh Hoàng Thịnh tại SO/ Maldives — khu nghỉ dưỡng đảo tư nhân mang phong cách sàn diễn runway thời trang đầu tiên trên thế giới tại Emboodhoo Lagoon.",
        "image": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1600&q=85",
        "country": "Maldives",
        "date": "02 TH9 2026",
        "quote": "SO/ Maldives không chỉ là một điểm đến nghỉ dưỡng, mà là một sàn diễn thời trang nơi mỗi vị khách đều trở thành nhân vật chính trong cuốn phim điện ảnh xa hoa của chính cuộc đời mình.",
        "takeaways": [
            ("Concept Độc Bản", "Khu nghỉ dưỡng phong cách thời trang avant-garde đầu tiên tại Maldives."),
            ("Vị Trí Đắc Địa", "Chỉ 15 phút di chuyển bằng du thuyền cao tốc từ sân bay Malé (Emboodhoo Lagoon)."),
            ("Biệt Thự Nổi", "Lagoon Water Villa với hồ bơi vô cực riêng, nội thất bespoke và view hoàng hôn ngoạn mục."),
            ("Ẩm Thực Đẳng Cấp", "Nhà hàng Trung Đông Hadaba thượng hạng và Lazuli Beach Club sôi động."),
            ("Dịch Vụ Cá Nhân", "Fashion Host tận tâm 24/7, cá nhân hóa từng chi tiết nhỏ nhất trong suốt kỳ nghỉ.")
        ],
        "verdict": [
            ("Vị Trí & Di Chuyển", "Thuận tiện tuyệt đối, di chuyển nhanh bằng du thuyền riêng 15 phút", "10 / 10"),
            ("Kiến Trúc & Thiết Kế", "Đột phá avant-garde, thời thượng, đầy tính nghệ thuật", "9.9 / 10"),
            ("Độ Riêng Tư & Biệt Lập", "Không gian villa rộng rãi, biệt lập và yên tĩnh tuyệt đối", "9.8 / 10"),
            ("Chất Lượng Ẩm Thực", "Đa dạng từ Hadaba, Citronelle đến Lazuli Bar", "9.8 / 10"),
            ("Dịch Vụ & Quản Gia", "Tận tâm, chu đáo, tinh tế chuẩn 5 sao quốc tế", "9.9 / 10"),
            ("Tổng Điểm Thẩm Định", "Khu nghỉ dưỡng phong cách thời trang xuất sắc nhất Ấn Độ Dương", "9.9 / 10")
        ],
        "lead": "<p>Maldives từ lâu đã được xem là thánh địa tối thượng của những kỳ nghỉ trăng mật lãng mạn và những ốc đảo nghỉ dưỡng triệu đô biệt lập. Tuy nhiên, giữa hàng trăm khu nghỉ dưỡng trải dài trên các đảo san hô atoll, phần lớn đều đi theo một công thức an toàn: mái lá dừa rustic, nội thất gỗ mộc và phong cách Robinson Crusoe kinh điển. Khi đặt chân đến <strong>SO/ Maldives</strong> trong chuyến hải trình trải nghiệm trực tiếp vừa qua, tôi đã thực sự bị choáng ngợp bởi một làn gió hoàn toàn mới mẻ — một bản tuyên ngôn thời trang avant-garde đầy kiêu hãnh và rực rỡ sắc màu ngay giữa lòng Ấn Độ Dương.</p><p>Nằm trong quần thể đầm phá Emboodhoo Lagoon thuộc dự án quy hoạch đại đô thị đảo Crossroads Maldives, SO/ Maldives sở hữu lợi thế địa lý vô cùng đắt giá: chỉ cách Sân bay Quốc tế Velana (Malé) đúng 15 phút di chuyển bằng du thuyền cao tốc sang trọng. Điều này xóa tan hoàn toàn nỗi ám ảnh mệt mỏi của những chuyến thủy phi cơ (seaplane) ồn ào và thời gian chờ đợi kéo dài tại nhà ga sân bay sau những chuyến bay quốc tế đường dài. Ngay khi bước lên chiếc du thuyền bọc da êm ái với sâm panh ướp lạnh và khăn lạnh thơm hương tinh dầu sả chanh, hành trình chạm vào đỉnh cao phong cách sống xa hoa của tôi đã chính thức bắt đầu.</p>",
        "chapters": [
            ("Chương 1: Sàn Diễn Catwalk 'The Runway' & Kiến Trúc Nghệ Thuật Avant-Garde Đột Phá",
             """<p>Điểm chạm thị giác đầu tiên khiến tôi không khỏi trầm trồ chính là cây cầu tàu đón tiếp được thiết kế theo đúng hình mẫu của một sàn diễn thời trang quốc tế — được đặt tên là <strong>'The Runway'</strong>. Thay vì một bến cảng thông thường, The Runway được lát sàn gỗ cao cấp trải dài trên mặt biển lam ngọc, hai bên là những cột đèn nghệ thuật uốn lượn và những dải vải voan lướt bay mềm mại trong gió biển nhiệt đới. Mỗi bước chân sải bước trên cầu cảng này tạo cho du khách cảm giác như một ngôi sao hạng A đang sải bước tại Tuần lễ Thời trang Paris hay Milan.</p>
<p>Khu vực sảnh đón tiếp trung tâm (The Arrival Pavilion) là một kỳ quan điêu khắc mở với cấu trúc mái vòm lấy cảm hứng từ những chiếc lều du mục đương đại kết hợp cùng những mảng gương khổng lồ phản chiếu trọn vẹn màu xanh biếc của đại dương và mây trời. Kiến trúc sư trưởng đã phối hợp tài tình các vật liệu hiện đại như thép không gỉ mạ màu vàng hồng (rose gold), kính đổi màu phân cực và đá terrazzo khảm hoa văn độc bản. Tại đây, tôi được chào đón nồng hậu bởi người quản gia riêng (được gọi thân mật là Fashion Host) trong bộ âu phục lanh cắt may đo tinh tế, mở ra một chuỗi những đặc quyền chăm sóc cá nhân hóa không giới hạn.</p>
<p>Khắp các lối đi bộ trên đảo, những tác phẩm nghệ thuật sắp đặt đương đại của các nghệ sĩ quốc tế xuất hiện đầy bất ngờ: từ những bức tượng trừu tượng bằng kim loại bóng loáng phản chiếu ánh mặt trời nhiệt đới cho đến những cụm ghế nghỉ hình khối uốn lượn như dải lụa mềm. Mỗi góc nhìn tại SO/ Maldives đều được căn chỉnh tỉ mỉ theo tỷ lệ vàng của nghệ thuật nhiếp ảnh, biến mọi bức ảnh lưu niệm của du khách thành những trang bìa tạp chí thời trang danh giá như Vogue hay Harper's Bazaar.</p>"""),
            
            ("Chương 2: Trải Nghiệm Dinh Thự Nổi Lagoon Water Villa & Bể Bơi Vô Cực Riêng Biệt",
             """<p>Căn biệt thự mà tôi lưu trú là <strong>Lagoon Ocean Water Pool Villa</strong>. Bước qua cánh cửa gỗ nguyên khối dày dặn, một không gian sống đẳng cấp rộng hơn 200m² mở ra với tầm nhìn panorama 180 độ ôm trọn đường chân trời Ấn Độ Dương. Thiết kế nội thất bên trong villa là sự hòa trộn đỉnh cao giữa sự tối giản đương đại và những nét chấm phá nghệ thuật Pop-Art: chiếc giường ngủ king-size bọc nhung cao cấp xoay hướng biển, bàn trang điểm bằng đá cẩm thạch Calacatta vân vàng, và hệ thống đèn trần tạo hình như những giọt nước pha lê lung linh.</p>
<p>Phòng tắm là một tuyệt tác không gian với bồn tắm tròn bằng đá đúc nguyên khối đặt ngay cạnh khung cửa kính chạm sàn nhìn thẳng ra rạn san hô bên dưới. Mọi chi tiết đồ dùng chăm sóc cá nhân đều đến từ thương hiệu nước hoa xa xỉ bespoke, mang hương thơm đặc trưng của cam bergamot, tiêu hồng và gỗ tuyết tùng Địa Trung Hải. Bước ra sàn gỗ ngoài trời (sun deck), chiếc hồ bơi vô cực dài 10 mét dường như kéo dài nối liền vào lòng đại dương. Nằm thư giãn trên chiếc võng lưới overwater net treo lơ lửng trên mặt nước trong vắt, ngắm nhìn đàn cá bướm và cá đuối bơi lội ngay dưới thân mình là một cảm giác thư thái tuyệt đối không thể diễn tả bằng lời.</p>
<p>Vào mỗi buổi sáng sớm, khi ánh mặt trời đầu tiên nhuộm hồng mặt biển phẳng lặng, quản gia Fashion Host đã gõ cửa nhẹ nhàng để mang đến bữa sáng nổi Floating Breakfast thịnh soạn: bánh sừng bò nướng giòn rụm thơm lừng mùi bơ Pháp, trứng cá tầm caviar ăn kèm bánh blini nóng hổi, đĩa trái cây nhiệt đới cắt tỉa công phu và một ly sâm panh Veuve Clicquot ướp lạnh. Thưởng thức bữa ăn giữa hồ bơi riêng biệt lập, lắng nghe tiếng sóng biển thì thầm và hít căng lồng ngực bầu không khí biển cả tinh khôi là khoảnh khắc xa xỉ thuần khiết nhất mà bất kỳ ai cũng khao khát được trải nghiệm.</p>"""),
            
            ("Chương 3: Nghệ Thuật Thưởng Vị Đỉnh Cao — Hadaba Levantine & Lazuli Beach Club",
             """<p>Ẩm thực tại SO/ Maldives là một hành trình khai phóng vị giác vượt qua mọi ranh giới thông thường. Nhà hàng biểu tượng <strong>Hadaba</strong> tọa lạc trên điểm cao nhất của hòn đảo, được lấy cảm hứng từ các nền văn hóa cổ xưa trên Con Đường Tơ Lụa và ẩm thực vùng Trung Đông Levantine. Không gian nhà hàng được thắp sáng huyền ảo bởi hàng trăm ngọn đèn lồng bằng đồng đục lỗ thủ công, tỏa ra những hoa văn ánh sáng lung linh khắp các bức tường ốp gốm men ngọc.</p>
<p>Tại Hadaba, tôi đã thưởng thức món đùi cừu hầm chậm 14 tiếng với gia vị thảo mộc Omani mềm tan như bơ, tôm hùm nướng trên than củi thơm lừng ăn kèm sốt bơ tỏi za'atar, và món bánh tráng miệng Baklava giòn rụm với hạt dẻ cười và kem hoa cam. Mỗi món ăn đều là sự cân bằng hoàn mỹ giữa vị đậm đà của gia vị Ả Rập cổ và kỹ thuật trình bày tinh tế của ẩm thực fine dining hiện đại.</p>
<p>Vào ban ngày, tâm điểm năng lượng của đảo dồn về <strong>Lazuli Beach Club</strong>. Với thiết kế hồ bơi khảm mosaic lấy cảm hứng từ bờ biển Côte d'Azur của nước Pháp, Lazuli là nơi du khách đắm chìm trong những giai điệu deep house êm ái từ các DJ quốc tế, nhâm nhi những ly cocktail nhiệt đới sáng tạo và thưởng thức món pizza nướng củi giòn tan ngay bên bờ biển. Nghi thức hoàng hôn tại Lazuli lúc 18:00, khi bầu trời chuyển màu từ cam rực lửa sang tím thẫm và những ngọn đuốc bắt đầu thắp sáng, là thời khắc quyến rũ bậc nhất trên đảo.</p>"""),
            
            ("Chương 4: Trải Nghiệm Tái Sinh Năng Lượng Tại Wellness Spa & Nghi Thức Hoàng Hôn",
             """<p>Nằm ẩn mình giữa những rặng cọ nhiệt đới và khu vườn thảo mộc xanh mướt, <strong>The Spa at SO/ Maldives</strong> là một thánh đường của sự thanh tịnh. Spa sở hữu các phòng trị liệu riêng biệt được thiết kế như những chiếc kén tằm nghệ thuật nhìn ra khu vườn tĩnh lặng. Liệu trình massage signature kéo dài 90 phút mà tôi trải nghiệm sử dụng tinh dầu dừa nguyên chất ép lạnh của đảo kết hợp cùng những viên đá bazan ấm nóng và kỹ thuật bấm huyệt cổ truyền, giúp giải phóng hoàn toàn mọi ức chế cơ bắp và đưa tâm trí về trạng thái thiền định sâu sắc.</p>
<p>Ngoài ra, khu vực xông hơi Hammam truyền thống bằng đá cẩm thạch và phòng tắm hơi hồng ngoại hiện đại là nơi lý tưởng để đào thải độc tố. Vào lúc 17:30 mỗi chiều, tôi luôn dành thời gian tham gia lớp thiền định ngắm hoàng hôn trên sàn gỗ nổi giữa biển, nơi ánh nắng chiều tà nhuộm đỏ cả một góc trời Ấn Độ Dương trước khi nhường chỗ cho màn đêm ngập tràn hàng triệu vì sao sáng.</p>
<p>Đối với những tín đồ thể thao, trung tâm thể hình Fit Lounge được trang bị toàn bộ máy tập Technogym thế hệ mới nhất nhìn thẳng ra đại dương bao la. Lớp tập yoga dây bay (aerial yoga) cùng huấn luyện viên quốc tế vào buổi sáng sớm trên bãi biển mang lại sự dẻo dai và sảng khoái tột cùng cho một ngày mới ngập tràn năng lượng.</p>"""),
            
            ("Chương 5: Nhật Ký Trải Nghiệm Cá Nhân Của Huỳnh Hoàng Thịnh: Những Chi Tiết Đắt Giá",
             """<p>Điều làm tôi ấn tượng sâu sắc nhất tại SO/ Maldives không chỉ dừng lại ở kiến trúc triệu đô hay cảnh sắc thiên nhiên kỳ vĩ, mà chính là <strong>sự tinh tế trong dịch vụ cá nhân hóa</strong> của đội ngũ nhân sự. Người quản gia Fashion Host luôn nắm bắt chính xác từng thói quen nhỏ nhất của tôi: từ việc chuẩn bị sẵn bình nước khoáng San Pellegrino ướp lạnh sau mỗi buổi bơi, loại hạt cà phê rang xay thơm nồng đúng gu vào mỗi sáng sớm, cho đến việc chuẩn bị sẵn bồn tắm đầy bọt xà phòng thơm lừng rắc đầy cánh hoa hồng khi tôi trở về phòng sau bữa tiệc tối tại Hadaba.</p>
<p>Vào buổi chiều ngày cuối cùng của kỳ nghỉ, ban quản lý resort đã tổ chức cho tôi một chuyến du ngoạn riêng trên chiếc du thuyền thể thao dài 45 feet để ngắm nhìn những đàn cá heo hoang dã tung tăng nhảy múa trên mặt sóng lúc hoàng hôn. Đứng ở mũi tàu với ly rượu Champagne Dom Pérignon trên tay, ngắm nhìn mặt trời đỏ ối từ từ lặn xuống biển sâu, tôi nhận ra rằng những khoảnh khắc như thế này chính là định nghĩa cao quý nhất của cuộc sống thượng lưu.</p>""")
        ],
        "concl": "<p><strong>Tổng kết từ Huỳnh Hoàng Thịnh:</strong> SO/ Maldives đã thành công rực rỡ trong việc tái định nghĩa kỳ nghỉ dưỡng biển đảo: trẻ trung, thời thượng, giàu tính nghệ thuật nhưng vẫn bảo tồn trọn vẹn sự riêng tư và sang trọng đỉnh cao. Nếu bạn muốn tìm kiếm một trải nghiệm Maldives hoàn toàn khác biệt, nơi bạn có thể tỏa sáng như một ngôi sao trên sàn diễn thời trang nhiệt đới, SO/ Maldives chính là điểm đến xứng đáng nhất trong danh mục sưu tập của bạn.</p>"
    },

    # -------------------------------------------------------------
    # 802: SIX SENSES CÔN ĐẢO (Việt Nam)
    # -------------------------------------------------------------
    {
        "id": 802,
        "title": "Six Senses Côn Đảo: Tuyệt Tác Ẩn Mình Bên Bờ Vịnh Đất Dốc & Triết Lý Nghỉ Dưỡng Tái Sinh Thuần Khiết",
        "excerpt": "Đánh giá chuyên sâu về Six Senses Côn Đảo: 50 căn biệt thự gỗ teak nguyên khối đối diện biển Đông, bãi cát trắng nguyên sơ và hành trình đánh thức giác quan.",
        "image": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1600&q=85",
        "country": "Việt Nam",
        "date": "02 TH9 2026",
        "quote": "Sự xa xỉ tột cùng tại Six Senses Côn Đảo chính là khoảnh khắc bạn thả lỏng đôi chân trần trên cát mịn, lắng nghe tiếng sóng vỗ và nhận ra tâm trí mình đã hoàn toàn được chữa lành.",
        "takeaways": [
            ("Bảo Tồn Sinh Thái", "Khu bảo tồn rùa biển độc quyền phối hợp cùng Vườn Quốc Gia Côn Đảo."),
            ("Biệt Thự Gỗ Teak", "50 căn villa 100% hướng biển với hồ bơi vô cực và kiến trúc làng chài đương đại."),
            ("Wellness Toàn Diện", "Hệ thống Six Senses Spa đẳng cấp quốc tế với liệu trình cá nhân hóa."),
            ("Ẩm Thực Thuần Khiết", "Nguyên liệu hữu cơ từ nông trại nội khu 'Farm-to-Table' tươi mới mỗi ngày."),
            ("Riêng Tư Tuyệt Đối", "Tọa lạc tại vịnh Đất Dốc biệt lập, tách biệt hoàn toàn với đô thị ồn ào.")
        ],
        "verdict": [
            ("Vị Trí & Cảnh Quan", "Vịnh Đất Dốc hoang sơ, núi non kỳ vĩ bao bọc", "9.9 / 10"),
            ("Kiến Trúc Bền Vững", "Gỗ teak mộc mạc, tinh tế, hòa hợp với thiên nhiên", "9.8 / 10"),
            ("Độ Riêng Tư", "Biệt lập hoàn toàn, tĩnh lặng đỉnh cao", "9.9 / 10"),
            ("Dịch Vụ & Spa", "Six Senses Wellness chuẩn mực toàn cầu", "9.9 / 10"),
            ("Ẩm Thực", "Hương vị Việt & Âu tinh tế, nguyên liệu hữu cơ sạch", "9.6 / 10"),
            ("Tổng Điểm Thẩm Định", "Khu nghỉ dưỡng sinh thái số 1 Việt Nam", "9.8 / 10")
        ],
        "lead": "<p>Nằm nép mình bên bờ biển hoang sơ của Vịnh Đất Dốc, <strong>Six Senses Côn Đảo</strong> từ lâu đã được công nhận là một trong những kiệt tác nghỉ dưỡng sinh thái xa xỉ hàng đầu châu Á. Được bao bọc bởi dãy núi Lò Vôi hùng vĩ một bên và biển Đông xanh ngọc bích một bên, khu nghỉ dưỡng là nơi triết lý phát triển bền vững đạt đến đỉnh cao của sự tinh tế và xa hoa.</p><p>Với 50 căn biệt thự bằng gỗ tếch mộc mạc hướng thẳng ra biển, Six Senses Côn Đảo không chỉ là nơi ẩn náu của các ngôi sao Hollywood như Angelina Jolie và Brad Pitt trong quá khứ, mà còn là điểm dừng chân yêu thích của giới tinh hoa Việt Nam và quốc tế tìm kiếm sự bình yên thuần khiết trong tâm hồn.</p>",
        "chapters": [
            ("Chương 1: Kiến Trúc Gỗ Teak Nguyên Bản & Tinh Thần Làng Chài Việt Nam Đương Đại",
             """<p>Kiến trúc của Six Senses Côn Đảo được lấy cảm hứng từ cấu trúc của những làng chài truyền thống Việt Nam, nhưng được tái hiện bằng ngôn ngữ tối giản hiện đại (eco-minimalism). Hơn 1.000 tấm cửa gỗ tái chế từ các ngôi nhà cổ trên khắp mọi miền đất nước được bài trí công phu tại sảnh đón tiếp chính, tạo nên một câu chuyện lịch sử sống động và giàu cảm xúc.</p>
<p>Các căn biệt thự một đến bốn phòng ngủ đều được xây dựng hoàn toàn từ gỗ tếch tự nhiên khai thác bền vững. Thiết kế mở tối đa với mái dốc hình cánh bướm giúp đón trọn luồng gió biển tự nhiên, giảm thiểu nhu cầu sử dụng điều hòa nhiệt độ mà vẫn duy trì không gian mát mẻ quanh năm. Mỗi biệt thự đều sở hữu hồ bơi vô cực riêng bằng đá tự nhiên, mở ra tầm nhìn bao la không giới hạn về phía chân trời biển cả.</p>
<p>Bên trong biệt thự, sự sang trọng hiện diện trong sự mộc mạc thanh tao: sàn gỗ sáng màu, giường ngủ bọc mùng lụa trắng buông rủ êm ái, bồn tắm gỗ hình tròn đặt cạnh cửa sổ hướng biển và hệ thống vòi sen tắm ngoài trời bao quanh bởi những bức tường tre xanh mướt. Đây là nơi bạn có thể trút bỏ hoàn toàn sự ồn ã của thế giới công nghiệp để hòa mình vào bản giao hưởng của gió và sóng biển.</p>"""),
            
            ("Chương 2: Hành Trình Tái Tạo Thân - Tâm - Trí Tại Six Senses Spa",
             """<p>Được vinh danh bởi nhiều tạp chí du lịch hàng đầu thế giới, Six Senses Spa Côn Đảo là nơi quy tụ những liệu pháp trị liệu toàn diện (Holistic Wellness) đỉnh cao. Ẩn mình dưới chân núi rợp bóng cây xanh, spa sở hữu các phòng trị liệu ngoài trời, nơi tiếng sóng biển hòa quyện cùng tiếng lá thông reo tạo nên bản giao hưởng thư giãn tự nhiên.</p>
<p>Chương trình chăm sóc sức khỏe tại đây được cá nhân hóa thông qua bài kiểm tra sức khỏe không xâm lấn (Non-invasive Wellness Screening), phân tích các chỉ số sinh học và đưa ra phác đồ trị liệu riêng biệt gồm thiền định, yoga thở pranayama và các bài massage giải độc bằng thảo dược hữu cơ trồng trực tiếp trong vườn resort.</p>
<p>Đặc biệt, phương pháp trị liệu bằng âm thanh chuông xoay Tây Tạng (Singing Bowls Meditation) tại khu vực chòi thiền ven suối mang đến sự rung động sâu sắc đến từng tế bào cơ thể, giúp giải phóng hoàn toàn các nút thắt năng lượng tiêu cực và đem lại giấc ngủ sâu, an lành cho du khách.</p>"""),
            
            ("Chương 3: Bảo Tồn Rùa Biển & Ẩm Thực Bền Vững 'Từ Nông Trại Đến Bàn Ăn'",
             """<p>Một trong những trải nghiệm xúc động nhất tại Six Senses Côn Đảo là hoạt động ấp nở và thả rùa con về với đại dương tại khu bảo tồn 'Let's Get Cracking' phối hợp cùng Vườn Quốc Gia Côn Đảo. Đứng chân trần trên bãi cát lúc bình minh, ngắm nhìn những sinh linh bé nhỏ chập chững bước những bước đầu tiên ra biển lớn là khoảnh khắc chạm đến chiều sâu tâm linh của mỗi du khách.</p>
<p>Về ẩm thực, nhà hàng <strong>By The Beach</strong> và <strong>Vietnamese Market</strong> phục vụ những món ăn thuần khiết với nguyên liệu 100% từ vườn rau hữu cơ rộng 1,5 hecta của resort và hải sản đánh bắt có trách nhiệm từ ngư dân địa phương. Bữa tối nướng BBQ bên bờ biển với tôm hùm Côn Đảo và nấm đông cô tươi ngon là trải nghiệm ẩm thực thượng lưu khó quên.</p>
<p>Khu vườn hữu cơ của resort không chỉ cung cấp rau xà lách, thảo mộc tươi mà còn là nơi sản xuất các loại nấm tươi và trứng gà sạch mỗi ngày. Khái niệm 'Eat With Six Senses' đảm bảo mọi món ăn đều bổ dưỡng, giàu chất chống oxy hóa và không sử dụng bất kỳ hóa chất phụ gia nào.</p>"""),
            
            ("Chương 4: Những Hoạt Động Khám Phá Quần Đảo Biệt Lập Côn Đảo",
             """<p>Không chỉ dừng lại trong khuôn viên resort, Six Senses Côn Đảo mở ra những hành trình thám hiểm đầy mê hoặc dành cho du khách. Bạn có thể chèo thuyền kayak khám phá các hòn đảo nhỏ xung quanh, lặn ngắm những rạn san hô nguyên sinh tuyệt đẹp tại Hòn Bảy Cạnh, hoặc đi bộ trekking xuyên qua rừng nhiệt đới Vườn Quốc Gia để khám phá hệ động thực vật phong phú.</p>
<p>Đối với những ai yêu thích lịch sử và văn hóa, chuyến tham quan các di tích lịch sử Côn Đảo với hướng dẫn viên riêng của resort mang lại những góc nhìn sâu sắc và lắng đọng về ý chí kiên cường và lịch sử hào hùng của dân tộc Việt Nam.</p>"""),
            
            ("Chương 5: Góc Nhìn Giám Tuyển Huỳnh Hoàng Thịnh: Giá Trị Bất Biến Của Xa Xỉ Thuần Khiết",
             """<p>Six Senses Côn Đảo là minh chứng rõ ràng cho việc sự xa xỉ thực sự không cần phải phô trương vàng son lộng lẫy, mà nằm ở sự hòa hợp tuyệt đối giữa con người và thiên nhiên nguyên bản. Không khí trong lành, sự yên tĩnh tuyệt đối và lòng hiếu khách chân thành của đội ngũ nhân sự biến nơi đây thành tài sản trải nghiệm vô giá trong bộ sưu tập du lịch thượng lưu.</p>
<p>Mỗi lần trở lại Côn Đảo, tôi luôn tìm thấy sự tươi mới và thanh lọc trọn vẹn trong tâm hồn. Đó là giá trị cốt lõi mà không một món đồ xa xỉ vật chất nào có thể thay thế được.</p>""")
        ],
        "concl": "<p><strong>Lời khuyên từ Huỳnh Hoàng Thịnh:</strong> Hãy đặt hạng biệt thự Ocean Front 4-Bedroom Pool Villa nếu bạn đi cùng gia đình, và dành ít nhất một buổi sáng sớm tham gia lớp Yoga Pranayama tại sảnh gỗ trên bờ biển để đón nhận trọn vẹn nguồn năng lượng tinh khôi của biển Côn Đảo.</p>"
    }
]

print("Part 1 base loaded.")
