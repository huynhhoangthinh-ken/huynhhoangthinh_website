const fs = require('fs');
const file = '/Users/kenhuynh/Desktop/huynh-hoang-thinh-website/data/posts.json';
const data = JSON.parse(fs.readFileSync(file, 'utf8'));

const articles = {
  1: {
    excerpt: "Khám phá cách giới tinh hoa biến những không gian sống thành những tác phẩm nghệ thuật mang đậm dấu ấn cá nhân, vượt xa mọi chuẩn mực thông thường.",
    content: "<p>Bất động sản siêu sang hiện nay không chỉ là nơi trú ngụ, mà đã trở thành một tuyên ngôn về phong cách sống. Những chủ nhân giới tinh hoa không còn hài lòng với những thiết kế rập khuôn; họ yêu cầu những đặc quyền cá nhân hóa tuyệt đối.</p>\n<p>Từ việc lựa chọn vật liệu quý hiếm, thiết kế cảnh quan độc quyền, đến hệ thống thông minh tinh chỉnh theo thói quen sinh hoạt, mọi chi tiết đều được đo ni đóng giày. Sự xa xỉ giờ đây nằm ở những giá trị độc bản không thể sao chép, tạo nên một di sản trường tồn cho các thế hệ sau.</p>"
  },
  2: {
    excerpt: "Du thuyền năm 2026 không chỉ là phương tiện di chuyển trên biển mà đã trở thành những resort di động xa hoa bậc nhất thế giới.",
    content: "<p>Thị trường siêu du thuyền năm 2026 đang chứng kiến sự bùng nổ của những công nghệ tiên tiến và thiết kế đột phá. Giới siêu giàu không chỉ mua du thuyền, họ đang đầu tư vào một lối sống tự do không giới hạn trên những đại dương bao la.</p>\n<p>Các thiết kế mới nhất tích hợp công nghệ xanh giảm phát thải, kết hợp cùng nội thất xa xỉ từ các thương hiệu thời trang hàng đầu thế giới. Những chiếc Mega Yacht giờ đây sở hữu đầy đủ từ bãi đỗ trực thăng, rạp chiếu phim, đến phòng thí nghiệm khám phá đại dương, mang lại trải nghiệm nghỉ dưỡng hoàn hảo nhất.</p>"
  },
  3: {
    excerpt: "Sự trỗi dậy của những chiếc Hypercar không chỉ phá vỡ giới hạn tốc độ mà còn định nghĩa lại nghệ thuật cơ khí đương đại.",
    content: "<p>Hypercar thế hệ mới là sự kết tinh hoàn hảo giữa kỹ thuật hàng không vũ trụ và đam mê tốc độ. Với mức giá hàng triệu đô, mỗi chiếc xe là một tác phẩm nghệ thuật cơ khí mang tính biểu tượng.</p>\n<p>Năm 2026, các hãng xe như Bugatti, Koenigsegg hay Pagani không chỉ chạy đua về mã lực mà còn tập trung vào tính khí động học và cá nhân hóa. Sợi carbon, hợp kim siêu nhẹ và động cơ hybrid mạnh mẽ đang thống trị, biến mỗi cú đạp ga thành một bản giao hưởng của sức mạnh và sự phấn khích.</p>"
  },
  4: {
    excerpt: "Penthouse The View mang đến góc nhìn ngoạn mục và định nghĩa lại sự xa xỉ với những tiện ích đặc quyền ngay trên đỉnh thành phố.",
    content: "<p>Nằm ở vị trí đắc địa nhất giữa lòng đô thị phồn hoa, Penthouse The View là đỉnh cao của sự sang trọng. Tầm nhìn 360 độ bao quát toàn cảnh thành phố cùng thiết kế thông tầng mang đến không gian vô tận.</p>\n<p>Nội thất được chăm chút tỉ mỉ với các tác phẩm nghệ thuật đương đại, hồ bơi vô cực riêng tư và hệ thống an ninh đa lớp. Đây không chỉ là một không gian sống, mà là một pháo đài bình yên giữa bầu trời, nơi chủ nhân có thể tận hưởng sự riêng tư tuyệt đối ngay giữa trung tâm náo nhiệt.</p>"
  },
  5: {
    excerpt: "Khi thời gian là tài sản quý giá nhất, Private Jet mở ra kỷ nguyên di chuyển linh hoạt, an toàn và riêng tư tuyệt đối.",
    content: "<p>Sở hữu một chiếc chuyên cơ cá nhân không còn chỉ là biểu tượng của sự giàu có, mà là công cụ tối ưu hóa thời gian và hiệu suất làm việc. Năm 2026, kỷ nguyên hàng không cá nhân hóa đã đạt đến những đỉnh cao mới.</p>\n<p>Nội thất chuyên cơ được thiết kế bởi các kiến trúc sư danh tiếng, tích hợp phòng họp trực tuyến, phòng ngủ chuẩn 5 sao và hệ thống thanh lọc không khí y tế. Khả năng bay thẳng không dừng (non-stop) xuyên lục địa giúp giới thượng lưu làm chủ hoàn toàn lịch trình của mình.</p>"
  },
  6: {
    excerpt: "Các dinh thự ven đảo đang trở thành lựa chọn hàng đầu cho những ai tìm kiếm sự bình yên và tách biệt hoàn toàn khỏi thế giới.",
    content: "<p>Nhu cầu tìm kiếm không gian sống tách biệt đang đẩy giá trị của các dinh thự ven đảo lên mức kỷ lục. Giới tinh hoa khao khát một chốn ẩn náu an toàn, nơi thiên nhiên hòa quyện cùng kiến trúc nhân tạo.</p>\n<p>Được bao bọc bởi biển xanh, những dinh thự này mang lại quyền riêng tư tuyệt đối. Các tiện ích đi kèm như bến du thuyền cá nhân, sân golf tư nhân và hệ thống năng lượng tự cung tự cấp đang trở thành tiêu chuẩn mới cho lối sống ẩn danh thượng lưu.</p>"
  },
  7: {
    excerpt: "Mùa hè 2026 chứng kiến sự ra mắt của bộ sưu tập siêu xe phiên bản giới hạn, làm say lòng những nhà sưu tập khó tính nhất.",
    content: "<p>Thị trường sưu tầm xe đang nóng hơn bao giờ hết với sự xuất hiện của bộ sưu tập mùa hè 2026. Chỉ có vài chục chiếc được sản xuất trên toàn cầu, khiến chúng trở thành những viên kim cương trên bốn bánh.</p>\n<p>Mỗi chiếc xe mang một mã số độc nhất, được chế tác thủ công với thời gian lên tới hàng nghìn giờ. Đối với các nhà sưu tập, việc sở hữu không chỉ mang lại niềm vui cầm lái mà còn là một khoản đầu tư sinh lời vượt trội, miễn nhiễm với mọi biến động kinh tế.</p>"
  },
  8: {
    excerpt: "Mega Yacht không chỉ là biểu tượng của quyền lực mà còn là những kỳ quan kiến trúc trôi nổi trên đại dương.",
    content: "<p>Quy mô của những chiếc Mega Yacht ngày càng khiến thế giới kinh ngạc. Vượt qua giới hạn của một phương tiện hàng hải, chúng được thiết kế như những siêu đô thị thu nhỏ với hàng loạt tiện ích không tưởng.</p>\n<p>Từ những khu vườn sinh thái nhiệt đới trên boong, thác nước nhân tạo, đến tàu ngầm thám hiểm đi kèm, giới siêu giàu đang mang toàn bộ tiện nghi của đất liền ra giữa biển khơi. Đây là cách họ tận hưởng sự tự do tuyệt đối và khẳng định vị thế độc tôn.</p>"
  },
  9: {
    excerpt: "Nội thất Bespoke trong các dự án tỷ đô phản ánh gu thẩm mỹ độc đáo và sự tinh tế vượt bậc của những chủ nhân danh giá.",
    content: "<p>Bespoke (chế tác độc bản) đang là từ khóa dẫn dắt xu hướng nội thất siêu sang. Không có chỗ cho sự sản xuất hàng loạt, mọi chi tiết trong một căn dinh thự tỷ đô đều phải kể một câu chuyện riêng.</p>\n<p>Từ những bộ sofa bọc da khâu tay từ Ý, đèn chùm pha lê chế tác theo họa tiết gia huy, đến những tấm thảm dệt tay quý hiếm. Sự kết hợp giữa nghệ thuật thủ công truyền thống và ý tưởng táo bạo của chủ nhân tạo nên những không gian sống đậm chất nghệ thuật và không thể sao chép.</p>"
  },
  10: {
    excerpt: "Điểm mặt những mẫu chuyên cơ thương gia đang làm mưa làm gió trong quý 3 năm 2026 nhờ tầm bay và hiệu suất vượt trội.",
    content: "<p>Quý 3/2026 ghi nhận doanh số kỷ lục của phân khúc chuyên cơ tầm xa. Các nhà tài phiệt và CEO toàn cầu đang săn lùng những mẫu máy bay có thể bay thẳng từ Á sang Mỹ mà không cần tiếp nhiên liệu.</p>\n<p>Những mẫu máy bay bán chạy nhất không chỉ đáp ứng về tốc độ và hiệu suất, mà còn sở hữu không gian cabin rộng rãi bậc nhất. Công nghệ chống ồn chủ động và ánh sáng sinh học giúp giảm thiểu mệt mỏi sau những chuyến bay dài, đảm bảo chủ nhân luôn trong trạng thái tốt nhất.</p>"
  },
  11: {
    excerpt: "Sự độc bản đang là thước đo cao nhất của sự xa xỉ, nơi giới tinh hoa sẵn sàng chi hàng triệu đô để sở hữu thứ không ai khác có.",
    content: "<p>Trong một thế giới nơi hàng hiệu dễ dàng được tiếp cận bởi số đông, giới siêu giàu đang tái định nghĩa lại khái niệm xa xỉ. Sự xa xỉ đích thực giờ đây nằm ở tính độc bản (One-of-a-kind).</p>\n<p>Dù là một chiếc đồng hồ tùy chỉnh cỗ máy, một siêu xe với màu sơn được phát triển riêng biệt, hay một căn hộ có thiết kế duy nhất trên thế giới. Giá trị của sự độc bản không nằm ở vật chất, mà nằm ở cảm giác quyền lực và đặc quyền tối cao của người sở hữu.</p>"
  },
  12: {
    excerpt: "Villa Sinh Thái đang vươn lên thành xu hướng mới, kết hợp hài hòa giữa sự xa hoa và trách nhiệm bảo vệ môi trường.",
    content: "<p>Lối sống thượng lưu đang dần chuyển dịch theo hướng phát triển bền vững. Villa sinh thái (Eco-Luxury Villa) ra đời để đáp ứng nhu cầu sống xanh nhưng không làm giảm đi sự sang trọng.</p>\n<p>Được xây dựng từ các vật liệu tự nhiên, sử dụng năng lượng mặt trời và hệ thống thu gom nước mưa thông minh, những căn villa này hòa mình hoàn toàn vào thiên nhiên. Giới tinh hoa hiện đại hiểu rằng, bảo vệ môi trường cũng chính là bảo vệ sức khỏe và di sản của chính họ.</p>"
  },
  13: {
    excerpt: "Monaco Yacht Show 2026 mang đến những thiết kế tương lai và các công nghệ hàng hải tối tân nhất chưa từng được công bố.",
    content: "<p>Triển lãm du thuyền lớn nhất thế giới tại Monaco năm nay tiếp tục làm mãn nhãn giới mộ điệu. Hàng chục siêu phẩm mới lần đầu tiên được hạ thủy, mang theo những tinh hoa của kỹ thuật đóng tàu hiện đại.</p>\n<p>Điểm nhấn của năm nay là sự lên ngôi của các mẫu du thuyền thám hiểm (Explorer Yachts) với khả năng phá băng và hoạt động độc lập nhiều tháng trên biển. Bên cạnh đó, xu hướng sử dụng động cơ hydro và năng lượng tái tạo cũng được các xưởng đóng tàu hàng đầu lăng xê mạnh mẽ.</p>"
  },
  14: {
    excerpt: "Hành trình đặt mua và tùy chỉnh một chiếc siêu xe tại các nhà máy danh tiếng ở Châu Âu là một trải nghiệm đậm chất thượng lưu.",
    content: "<p>Việc mua một chiếc siêu xe không chỉ đơn thuần là thanh toán và nhận chìa khóa. Nó là một hành trình nghệ thuật kéo dài hàng tháng, thậm chí hàng năm trời, bắt đầu từ những chuyến thăm nhà máy tại Ý hay Anh.</p>\n<p>Khách hàng VIP sẽ được làm việc trực tiếp với giám đốc thiết kế, tham gia vào quá trình chọn lựa từng loại da, màu chỉ khâu và thậm chí là tinh chỉnh âm thanh ống xả. Trải nghiệm này mang tính cá nhân hóa cao độ, biến chủ nhân thành một người đồng sáng tạo ra kiệt tác của riêng mình.</p>"
  },
  15: {
    excerpt: "Thụy Sĩ tiếp tục giữ vững vị thế là thiên đường nghỉ dưỡng và trú ẩn tài sản an toàn nhất cho giới siêu giàu Châu Á.",
    content: "<p>Bất động sản Thụy Sĩ luôn có một sức hút mãnh liệt nhờ cảnh quan thiên nhiên tuyệt mỹ, sự riêng tư tuyệt đối và nền tảng kinh tế ổn định. Giới tinh hoa Châu Á đang xem đây là điểm đến lý tưởng để đa dạng hóa danh mục đầu tư.</p>\n<p>Những căn Chalet nằm nép mình bên dãy Alps phủ tuyết, trang bị nội thất xa xỉ và hầm rượu vang trăm năm, mang đến trải nghiệm nghỉ dưỡng mùa đông đẳng cấp. Sự khan hiếm quỹ đất và các quy định nghiêm ngặt càng đẩy giá trị bất động sản nơi đây lên cao.</p>"
  },
  16: {
    excerpt: "Garage siêu xe giờ đây không chỉ là bãi đỗ, mà là những không gian trưng bày nghệ thuật với công nghệ bảo quản tối tân.",
    content: "<p>Sở hữu một bộ sưu tập xe hàng triệu đô đòi hỏi một không gian lưu trữ và bảo quản tương xứng. Các Garage triệu đô đang trở thành một phần không thể thiếu trong các dinh thự siêu sang.</p>\n<p>Chúng được trang bị hệ thống kiểm soát nhiệt độ, độ ẩm chính xác, sàn epoxy chịu lực và ánh sáng thiết kế riêng để tôn lên đường nét của từng chiếc xe. Nhiều chủ nhân còn tích hợp quầy bar, phòng lounge ngay trong garage để chiêm ngưỡng những 'đứa con cưng' của mình cùng đối tác.</p>"
  },
  17: {
    excerpt: "Thưởng thức rượu vang trên siêu du thuyền đòi hỏi sự am hiểu sâu sắc về cách lưu trữ và lựa chọn hương vị trên biển.",
    content: "<p>Trải nghiệm ẩm thực trên siêu du thuyền không thể trọn vẹn nếu thiếu đi những chai rượu vang hảo hạng. Tuy nhiên, việc bảo quản và thưởng thức vang trên môi trường biển đầy sóng gió lại là một nghệ thuật.</p>\n<p>Các siêu du thuyền hiện đại đều được trang bị hầm rượu (Wine Cellar) chống rung lắc chuyên dụng. Việc kết hợp vang với các món hải sản tươi sống được chế biến bởi đầu bếp Michelin ngay giữa đại dương mang đến những cung bậc cảm xúc ẩm thực thăng hoa nhất.</p>"
  },
  18: {
    excerpt: "Sân đỗ trực thăng cá nhân là mảnh ghép hoàn hảo, mang lại sự linh hoạt tối đa cho các chủ nhân dinh thự trên đảo.",
    content: "<p>Thời gian là vàng, và đối với giới siêu giàu, việc di chuyển phải luôn nhanh chóng và thuận tiện nhất. Thiết kế sân đỗ trực thăng (Helipad) ngay trong khuôn viên dinh thự ven đảo đang trở thành tiêu chuẩn bắt buộc.</p>\n<p>Không chỉ đòi hỏi tính toán kỹ lưỡng về cấu trúc và khí động học, sân đỗ còn phải hòa hợp với cảnh quan tổng thể. Nó mở ra đặc quyền di chuyển bay thẳng từ sân bay quốc tế hoặc du thuyền cá nhân về thẳng dinh thự chỉ trong vài phút.</p>"
  },
  19: {
    excerpt: "Công nghệ nhà thông minh (Smart Home) đang tiến một bước dài, mang lại trải nghiệm sống vô hình nhưng đầy thấu hiểu.",
    content: "<p>Bất động sản siêu sang không còn chỉ dựa vào kiến trúc vật lý, mà đang được thổi hồn bởi công nghệ AI và IoT. Kỷ nguyên Smart Home mới tập trung vào trải nghiệm 'vô hình' - khi công nghệ tự động thấu hiểu và phục vụ chủ nhân.</p>\n<p>Từ việc nhận diện khuôn mặt để mở khóa, phân tích cảm xúc để điều chỉnh ánh sáng và âm nhạc, đến hệ thống lọc nước và không khí tự động giám sát chất lượng. Ngôi nhà giờ đây trở thành một người quản gia ảo mẫn cán, chăm sóc từng khía cạnh của cuộc sống.</p>"
  },
  20: {
    excerpt: "Máy bay cá nhân không chỉ là phương tiện di chuyển, mà đang trở thành một kênh đầu tư chiến lược mang lại nhiều đặc quyền.",
    content: "<p>Thị trường hàng không cá nhân đang chứng kiến sự chuyển dịch từ việc 'thuê chuyến' sang 'sở hữu hoàn toàn'. Giới thượng lưu nhận ra rằng việc đầu tư vào máy bay cá nhân mang lại nhiều giá trị hơn họ tưởng.</p>\n<p>Bên cạnh việc làm chủ thời gian và không gian làm việc an toàn, máy bay cá nhân còn là một tài sản có thể cho thuê lại (charter) khi không sử dụng, giúp tối ưu hóa chi phí vận hành. Đồng thời, nó là một công cụ ngoại giao xuất sắc trong các thương vụ làm ăn quốc tế.</p>"
  }
};

data.forEach(p => {
  if (articles[p.id]) {
    // Extract existing image tag to keep the picture
    const imgMatch = p.content.match(/<img[^>]+>/);
    const imgTag = imgMatch ? imgMatch[0] : '';
    
    // Replace content
    p.excerpt = articles[p.id].excerpt;
    p.content = '\n' + articles[p.id].content + '\n' + imgTag + '\n';
  }
});

fs.writeFileSync(file, JSON.stringify(data, null, 2));
console.log('Successfully updated 20 articles.');
