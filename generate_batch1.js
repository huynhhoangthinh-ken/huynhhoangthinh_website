const fs = require('fs');
const file = '/Users/kenhuynh/Desktop/huynh-hoang-thinh-website/data/posts.json';
let data = JSON.parse(fs.readFileSync(file, 'utf8'));

// Utility to generate image HTML
function getImgHtml(prompt, caption) {
  const url = `https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=1200&height=800&nologo=true`;
  return `
    <figure class="magazine-figure">
      <img src="${url}" alt="${caption}">
      <figcaption class="magazine-figcaption">${caption}</figcaption>
    </figure>
  `;
}

const articles = {
  1: {
    excerpt: "Khám phá cách giới tinh hoa biến những không gian sống thành những tác phẩm nghệ thuật mang đậm dấu ấn cá nhân, vượt xa mọi chuẩn mực thông thường về bất động sản.",
    content: `
      <p class="magazine-dropcap">Bất động sản siêu sang hiện nay không chỉ là nơi trú ngụ, mà đã trở thành một tuyên ngôn về phong cách sống. Những chủ nhân giới tinh hoa không còn hài lòng với những thiết kế rập khuôn; họ yêu cầu những đặc quyền cá nhân hóa tuyệt đối từ kiến trúc tổng thể cho đến từng chi tiết nội thất nhỏ nhất.</p>
      
      ${getImgHtml('ultra luxury villa interior with panoramic ocean view modern design', 'Không gian phòng khách mở hướng trọn tầm nhìn ra đại dương')}

      <p>Từ việc lựa chọn vật liệu quý hiếm, thiết kế cảnh quan độc quyền, đến hệ thống thông minh tinh chỉnh theo thói quen sinh hoạt, mọi chi tiết đều được "đo ni đóng giày". Sự xa xỉ giờ đây nằm ở những giá trị độc bản không thể sao chép. Khách hàng không mua một ngôi nhà, họ mua một trải nghiệm sống độc nhất vô nhị. Họ làm việc trực tiếp với các kiến trúc sư hàng đầu thế giới để tạo ra những không gian phản ánh chính xác bản ngã và thành tựu của mình.</p>
      
      <div class="magazine-quote">Sự xa xỉ đích thực không nằm ở mức giá, mà nằm ở tính độc bản và câu chuyện đằng sau mỗi thiết kế.</div>
      
      <p>Bên cạnh kiến trúc, các tiện ích nội khu cũng được nâng tầm đáng kể. Không còn là những tiện ích chung chung, các dinh thự hiện đại tích hợp sẵn hầm rượu vang bảo quản hàng nghìn chai, phòng chiếu phim IMAX riêng tư, bến du thuyền cá nhân, và thậm chí là những trung tâm chăm sóc sức khỏe, spa tiêu chuẩn 6 sao ngay tại nhà.</p>
      
      ${getImgHtml('bespoke luxury wine cellar in modern mansion', 'Hầm rượu vang bespoke lưu trữ hàng ngàn chai vang quý hiếm')}
      
      <p>Yếu tố công nghệ cũng đóng vai trò cốt lõi. Hệ thống Smart Home không chỉ dừng lại ở việc bật tắt đèn, mà tiến xa hơn bằng cách phân tích thói quen, tự động điều chỉnh ánh sáng sinh học (circadian lighting), nhiệt độ và mùi hương để tối ưu hóa sức khỏe của gia chủ. Cùng với đó là hệ thống an ninh đa lớp vô hình, đảm bảo sự riêng tư và an toàn tuyệt đối mà không phá vỡ cảnh quan thẩm mỹ của ngôi nhà.</p>
      
      <p>Tựu trung lại, sự cá nhân hóa trong bất động sản siêu sang không chỉ là một xu hướng nhất thời, mà là một bước tiến tất yếu của thị trường khi nhu cầu thể hiện đẳng cấp của giới siêu giàu ngày càng tinh tế và sâu sắc hơn. Đó là nghệ thuật của việc biến một không gian sống thành một di sản truyền đời thực thụ.</p>
      
      ${getImgHtml('stunning infinity pool luxury villa sunset', 'Bể bơi vô cực - Tiện ích không thể thiếu của các dinh thự triệu đô')}
    `
  },
  2: {
    excerpt: "Du thuyền năm 2026 không chỉ là phương tiện di chuyển trên biển mà đã trở thành những resort di động xa hoa bậc nhất thế giới.",
    content: `
      <p class="magazine-dropcap">Thị trường siêu du thuyền năm 2026 đang chứng kiến sự bùng nổ chưa từng có của những công nghệ tiên tiến và thiết kế đột phá. Giới siêu giàu toàn cầu không chỉ mua du thuyền để khẳng định địa vị; họ đang thực sự đầu tư vào một lối sống tự do, không giới hạn trên những đại dương bao la, nơi họ có thể hoàn toàn tách biệt khỏi sự ồn ào của thế giới.</p>
      
      ${getImgHtml('futuristic mega yacht cruising ocean sunset', 'Siêu du thuyền thế hệ mới lướt sóng giữa đại dương bao la')}

      <p>Các thiết kế du thuyền mới nhất là sự giao thoa giữa hàng hải và hàng không vũ trụ. Tích hợp công nghệ xanh giảm phát thải, hệ thống đẩy hybrid tiên tiến không chỉ giúp con tàu vận hành êm ái hơn mà còn bảo vệ hệ sinh thái biển. Đi cùng với đó là nghệ thuật chế tác nội thất xa xỉ từ các thương hiệu thời trang đình đám như Armani, Fendi hay Hermes, biến mỗi khoang tàu thành một kiệt tác.</p>
      
      <div class="magazine-quote">Du thuyền không còn là phương tiện, mà là một "Resort nổi" mang đến tự do tuyệt đối trên mọi vùng biển.</div>
      
      <p>Những chiếc Mega Yacht hiện đại giờ đây sở hữu đầy đủ mọi tiện nghi vượt xa trí tưởng tượng. Từ bãi đỗ trực thăng cá nhân, rạp chiếu phim ngoài trời, sân tennis, đến các phòng thí nghiệm khám phá đại dương và tàu ngầm cá nhân. Chủ nhân có thể thưởng thức những bữa tối Michelin ngay giữa Thái Bình Dương, hoặc ngâm mình trong bể bơi đáy kính trong suốt ngắm nhìn rạn san hô bên dưới.</p>
      
      ${getImgHtml('luxury yacht master bedroom interior ocean view', 'Khoang ngủ Master Cabin sang trọng với tầm nhìn panorama')}
      
      <p>Tuy nhiên, sự xa xỉ thực sự của siêu du thuyền năm 2026 nằm ở đội ngũ thủy thủ đoàn (Crew). Tỷ lệ nhân viên phục vụ trên khách thường xuyên đạt mức 2:1 hoặc thậm chí 3:1. Đội ngũ này bao gồm từ đầu bếp hạng sao, chuyên gia rượu vang (sommelier), huấn luyện viên yoga cá nhân, đến các hướng dẫn viên lặn biển chuyên nghiệp, đảm bảo mọi nhu cầu dù là nhỏ nhất của chủ nhân đều được đáp ứng hoàn hảo.</p>
      
      <p>Tương lai của ngành công nghiệp du thuyền đang hướng đến sự kết hợp hoàn hảo giữa thiết kế táo bạo, tính bền vững với môi trường và những trải nghiệm siêu cá nhân hóa. Đó chính là đỉnh cao của lối sống thượng lưu hiện đại.</p>
      
      ${getImgHtml('gourmet dining setup on luxury yacht deck', 'Khu vực fine-dining ngay trên boong tàu ngập tràn nắng gió')}
    `
  },
  3: {
    excerpt: "Sự trỗi dậy của những chiếc Hypercar không chỉ phá vỡ giới hạn tốc độ mà còn định nghĩa lại nghệ thuật cơ khí đương đại.",
    content: `
      <p class="magazine-dropcap">Hypercar thế hệ mới là sự kết tinh hoàn hảo giữa kỹ thuật hàng không vũ trụ và đam mê tốc độ thuần túy. Với mức giá niêm yết lên tới hàng triệu đô la và số lượng sản xuất đếm trên đầu ngón tay, mỗi chiếc xe không chỉ là một cỗ máy, mà là một tác phẩm nghệ thuật cơ khí mang tính biểu tượng vĩnh cửu.</p>
      
      ${getImgHtml('futuristic hypercar speeding on coastal road', 'Sức mạnh vượt trội và thiết kế khí động học đỉnh cao')}

      <p>Năm 2026, cuộc đua giữa các nhà sản xuất không còn đơn thuần xoay quanh mã lực. Bugatti, Koenigsegg, hay Pagani đang tập trung vào tối ưu hóa tính khí động học chủ động, vật liệu siêu nhẹ và trải nghiệm lái được cá nhân hóa đến mức cực đoan. Sợi carbon đúc (forged carbon), hợp kim titan in 3D và các giải pháp hybrid hiệu năng cao đang thống trị, biến mỗi cú đạp ga thành một bản giao hưởng của sức mạnh và sự phấn khích tột độ.</p>
      
      <div class="magazine-quote">Sở hữu một chiếc Hypercar không phải là mua một phương tiện di chuyển, mà là mua một tấm vé bước vào lịch sử ngành ô tô.</div>
      
      <p>Bên cạnh yếu tố kỹ thuật, sự cá nhân hóa (Bespoke) là chìa khóa định hình phân khúc này. Khách hàng không bao giờ chọn màu sơn từ một bảng màu có sẵn. Họ yêu cầu các kỹ sư phát triển một màu sơn độc quyền, phối hợp với nội thất sử dụng các vật liệu quý hiếm như da đà điểu, nhôm nguyên khối chải xước, hay thậm chí là bụi kim cương pha trộn vào lớp sơn ngoại thất.</p>
      
      ${getImgHtml('close up hypercar steering wheel carbon fiber interior', 'Nội thất khoang lái được chế tác tinh xảo bằng sợi carbon và da cao cấp')}
      
      <p>Để sở hữu những siêu phẩm này, có tiền chưa chắc đã đủ. Các hãng xe áp dụng những quy định xét duyệt vô cùng khắt khe để chọn lọc khách hàng. Người mua thường phải chứng minh lịch sử sở hữu các dòng xe trước đó, tham gia vào câu lạc bộ độc quyền và ký các cam kết không bán lại trong một khoảng thời gian nhất định để chống lại nạn đầu cơ.</p>
      
      <p>Vượt lên trên mọi giới hạn, Hypercar đại diện cho tham vọng không mệt mỏi của con người trong việc chinh phục tốc độ và sự hoàn mỹ. Đó là những cỗ máy sẽ được ngắm nhìn và ngưỡng mộ qua hàng thế kỷ.</p>
      
      ${getImgHtml('hypercar engine bay close up intricate mechanical details', 'Trái tim của siêu xe: Cỗ máy cơ khí trị giá hàng triệu đô')}
    `
  },
  4: {
    excerpt: "Penthouse The View mang đến góc nhìn ngoạn mục và định nghĩa lại sự xa xỉ với những tiện ích đặc quyền ngay trên đỉnh thành phố.",
    content: `
      <p class="magazine-dropcap">Nằm ở vị trí đắc địa nhất, kiêu hãnh vươn mình giữa lòng đô thị phồn hoa, Penthouse The View là đỉnh cao thực sự của sự sang trọng và quyền uy. Tầm nhìn 360 độ không bị che khuất bao quát toàn cảnh thành phố rực rỡ ánh đèn, kết hợp cùng thiết kế thông tầng (duplex/triplex) mang đến một không gian sống vô tận giữa không trung.</p>
      
      ${getImgHtml('luxury penthouse interior living room city skyline view sunset', 'Phòng khách thông tầng với tầm nhìn panorama ôm trọn cảnh quan thành phố')}

      <p>Nội thất của The View được chăm chút tỉ mỉ đến từng mi-li-mét. Mỗi không gian là một buổi triển lãm thu nhỏ với các tác phẩm nghệ thuật đương đại, nội thất độc bản nhập khẩu từ Ý, và các hệ vách kính Low-E tràn viền tối đa hóa ánh sáng tự nhiên. Đây không chỉ là một không gian sống, mà là một "pháo đài bình yên" giữa bầu trời, nơi chủ nhân có thể hoàn toàn tách biệt khỏi sự náo nhiệt của phố thị.</p>
      
      <div class="magazine-quote">Sống tại Penthouse không chỉ là sở hữu không gian, mà là sở hữu cả một tầm nhìn bao quát thế giới bên dưới.</div>
      
      <p>Điểm nhấn làm nên đẳng cấp của Penthouse The View chính là hệ thống tiện ích đặc quyền (Private Amenities). Không cần phải chia sẻ với bất kỳ ai, chủ nhân sở hữu riêng một hồ bơi vô cực lơ lửng giữa lưng chừng trời, một khu vườn chân mây tĩnh lặng, hầm rượu vang kiểm soát nhiệt độ và phòng chiếu phim tiêu chuẩn rạp hát.</p>
      
      ${getImgHtml('penthouse private rooftop infinity pool night city view', 'Bể bơi vô cực riêng tư trên tầng thượng lộng gió')}
      
      <p>Bên cạnh đó, an ninh và sự riêng tư là ưu tiên tuyệt đối. Thang máy riêng với hệ thống nhận diện sinh trắc học đưa chủ nhân thẳng từ hầm đỗ xe siêu xe lên phòng khách. Đội ngũ quản gia (Butler) được đào tạo theo tiêu chuẩn Hoàng gia Anh luôn sẵn sàng phục vụ 24/7, từ việc chuẩn bị bữa sáng đến tổ chức những buổi tiệc xa hoa trên tầng thượng.</p>
      
      <p>Penthouse The View không chỉ là một bất động sản; nó là một tuyên ngôn vị thế. Nó dành cho những người đã lên tới đỉnh cao của sự nghiệp, và giờ đây, họ xứng đáng được tận hưởng cuộc sống ở vị trí cao nhất của thành phố.</p>
      
      ${getImgHtml('elegant master bedroom penthouse luxury minimalist', 'Phòng ngủ Master tối giản nhưng toát lên vẻ sang trọng quyền lực')}
    `
  },
  5: {
    excerpt: "Khi thời gian là tài sản quý giá nhất, Private Jet mở ra kỷ nguyên di chuyển linh hoạt, an toàn và riêng tư tuyệt đối.",
    content: `
      <p class="magazine-dropcap">Đối với giới siêu giàu, tài sản quý giá nhất không phải là tiền bạc, mà là thời gian. Sở hữu một chiếc chuyên cơ cá nhân (Private Jet) không còn chỉ là biểu tượng của sự phô trương; nó đã trở thành một công cụ tối ưu hóa hiệu suất làm việc và bảo vệ không gian riêng tư. Kỷ nguyên hàng không cá nhân hóa năm 2026 đang định hình lại cách thế giới di chuyển.</p>
      
      ${getImgHtml('luxurious private jet interior flying in the sky', 'Không gian cabin rộng rãi, tiện nghi của chuyên cơ cá nhân hiện đại')}

      <p>Các thế hệ máy bay phản lực thương gia mới nhất như Bombardier Global 8000 hay Gulfstream G800 sở hữu khả năng bay thẳng không dừng (non-stop) xuyên lục địa, vượt xa các dòng máy bay thương mại thông thường. Vận tốc tiệm cận ngưỡng siêu thanh cho phép các CEO sáng ăn sáng tại New York, chiều họp tại London và tối thưởng thức bữa tối tại Dubai mà không gặp bất kỳ trở ngại nào về lịch trình.</p>
      
      <div class="magazine-quote">Bầu trời không phải là giới hạn, đó là không gian làm việc và nghỉ ngơi tự do nhất của những nhà kiến tạo.</div>
      
      <p>Nội thất chuyên cơ được thiết kế bởi các kiến trúc sư danh tiếng, mang lại trải nghiệm như một khách sạn 5 sao lơ lửng trên mây. Cabin được chia thành các phân khu riêng biệt: phòng họp trực tuyến cách âm tuyệt đối với kết nối vệ tinh tốc độ cao, khu vực lounge giải trí, và phòng ngủ Master với phòng tắm đứng (shower) đầy đủ tiện nghi.</p>
      
      ${getImgHtml('business meeting inside private jet luxury cabin', 'Phòng họp trực tuyến chuẩn doanh nghiệp ngay trên bầu trời')}
      
      <p>Ngoài ra, yếu tố sức khỏe (Wellness) đang trở thành tiêu chuẩn mới. Áp suất cabin được điều chỉnh ở mức thấp để giảm thiểu triệu chứng jet lag. Hệ thống thanh lọc không khí y tế loại bỏ 99.9% vi khuẩn, cùng hệ thống ánh sáng sinh học mô phỏng chu kỳ mặt trời, đảm bảo hành khách luôn bước xuống máy bay với trạng thái minh mẫn và năng lượng tràn đầy nhất.</p>
      
      <p>Với khả năng cất hạ cánh tại hàng nghìn sân bay nhỏ lẻ mà các hãng hàng không lớn không thể tiếp cận, chuyên cơ cá nhân mang lại sự linh hoạt vô song. Đây không đơn thuần là phương tiện di chuyển, mà là một không gian sống, làm việc và thư giãn liền mạch không biên giới.</p>
      
      ${getImgHtml('elegant private jet exterior waiting on tarmac sunset', 'Sự chủ động tuyệt đối về lịch trình và thời gian bay')}
    `
  }
};

data.forEach(p => {
  if (articles[p.id]) {
    p.excerpt = articles[p.id].excerpt;
    p.content = '\n' + articles[p.id].content + '\n';
  }
});

fs.writeFileSync(file, JSON.stringify(data, null, 2));
console.log('Successfully updated Batch 1 (Articles 1-5).');
