/**
 * ==========================================================================
 * AI CONCIERGE CHATBOT ENGINE - HUỲNH HOÀNG THỊNH LUXURY PORTAL
 * Personality: Witty, Sophisticated, Humorous, Ultra-Luxurious & Knowledgeable
 * ==========================================================================
 */

(function () {
  'use strict';

  let postsData = [];

  // Knowledge Base Keywords & Pre-computed Highlights
  const LUXURY_KNOWLEDGE = {
    supercars: [
      { id: 107, name: 'Koenigsegg Jesko', price: '3,000,000 USD', desc: '1.600 mã lực, tốc độ tối đa lý thuyết 531 km/h - "Thần gió" Thụy Điển', img: 'assets/Posts/Koenigsegg_Jesko_2026/Koenigsegg_Jesko_20261_thumbnail.webp' },
      { id: 108, name: 'Bugatti Tourbillon (2026)', price: '4,100,000 USD', desc: 'Động cơ V16 Hybrid 1.800 mã lực, cụm đồng hồ cơ học Thụy Sĩ đỉnh cao', img: 'assets/Posts/Bugatti_tourbillon_2026/Bugatti Tourbillon (2026)1.jpg' },
      { id: 109, name: 'Ferrari LaFerrari', price: '3,500,000 USD', desc: 'Hypercar Hybrid V12 963 HP kiệt tác từ Maranello', img: 'assets/Posts/ferrari-laferrari/ferrari-laferrari-0f31e-c414325082026194653_1.jpg' },
      { id: 110, name: 'Lamborghini Revuelto', price: '600,000 USD', desc: 'Siêu bò V12 Hybrid thế hệ mới nhất 1.015 HP', img: 'assets/vehicles/lamborghini_revuelto.jpg' },
      { id: 111, name: 'Rolls-Royce Spectre', price: '450,000 USD', desc: 'Siêu sang thuần điện đầu tiên trong lịch sử Rolls-Royce', img: 'assets/Posts/Rolls_Royce_spectre/Thumbnail.webp' },
      { id: 112, name: 'Porsche 911 GT3 RS', price: '300,000 USD', desc: 'Vua đường đua khí động học 992', img: 'assets/vehicles/porsche_gt3_rs.jpg' },
      { id: 202, name: 'Louis Vuitton x Singer Porsche 911', price: '2,500,000 GBP', desc: 'Bespoke độc bản kết hợp giữa thời trang xa xỉ và cơ khí đỉnh cao', img: 'assets/Posts/911_LouisVuitton/Thumbnail.webp' }
    ],
    marketCars: [
      { id: 101, name: 'Land Rover Defender X', price: '4.390 Tỷ VNĐ', desc: 'Bản X đỉnh nhất, lướt 35k km, độ hơn 300tr phụ kiện zin', img: 'assets/Xe_dang_giao_dich/Land_rover/DefenderX/11DefenderX.jpg' },
      { id: 102, name: 'Maserati Grecale GT', price: '1.999 Tỷ VNĐ', desc: 'SUV thể thao Ý 300HP Mild Hybrid, âm thanh Sonus Faber', img: 'assets/Xe_dang_giao_dich/Maserarti/Grecale/Grecale-10.jpg' },
      { id: 103, name: 'BMW 735i M Sport (G70)', price: '3.690 Tỷ VNĐ', desc: 'Siêu lướt 8.100 km, đèn pha lê Swarovski, nội thất đỏ Amarone', img: 'assets/Xe_dang_giao_dich/BMW/BMW_735_MSP/BMW_735_MSP-10.jpg' }
    ],
    yachts: [
      { id: 122, name: 'Feadship 821 (Viva)', price: '350,000,000 USD', desc: 'Siêu du thuyền 119m chạy bằng Hydrogen đầu tiên thế giới', img: 'assets/Posts/Feadship_821_(Viva)_2026/Feadship_821_(Viva)_20261.webp' },
      { id: 120, name: 'Oceanco Bravo Eugenia', price: '250,000,000 USD', desc: 'Mega Yacht 109m sinh thái, rạp chiếu phim & bãi đỗ trực thăng', img: 'assets/Posts/Oceanco_Project_2026/Oceanco_Project_2026_thumbnail.jpg' },
      { id: 121, name: 'Lürssen Ahpo', price: '330,000,000 USD', desc: 'Cung điện nổi 115m xa hoa bậc nhất thế giới', img: 'assets/Posts/Lurssen_Ahpo/Lurssen_AhpoThumbnail.avif' },
      { id: 127, name: 'Sunseeker Ocean 182', price: '8,500,000 USD', desc: 'Du thuyền động cơ Anh Quốc với Enclosed Flybridge', img: 'assets/vehicles/sunseeker_ocean_182.jpg' },
      { id: 128, name: 'Riva 130 Bellissima', price: '22,000,000 USD', desc: 'Flybridge 40m nghệ thuật thủ công tinh hoa từ Ý', img: 'assets/Posts/Riva_130_Bellissima_2026/Riva_130_Bellissima_2026_00015_thumbnail.webp' },
      { id: 126, name: 'Azimut Grande 36M', price: '15,000,000 USD', desc: 'Du thuyền Ý đột phá với Semi-walkaround Upper Deck', img: 'assets/Posts/Azimut_Grande_36M_2026/Azimut_Grande_36M_2026_thumbnail.webp' }
    ],
    jets: [
      { id: 123, name: 'Gulfstream G700', price: '78,000,000 USD', desc: 'Chuyên cơ tốc độ Mach 0.925, tầm bay 7.500 hải lý', img: 'assets/Posts/Gulfstream_G700/Gulfstream_G700_22_thumbnail.jpg' },
      { id: 124, name: 'Bombardier Global 8000', price: '81,000,000 USD', desc: 'Chuyên cơ bay xa nhất thế giới (8.000 hải lý)', img: 'assets/Posts/Bombardier_8000_2026/Bombardier_8000_20266_thumbnail.jpg' },
      { id: 125, name: 'Dassault Falcon 10X', price: '75,000,000 USD', desc: 'Dinh thự bay cabin rộng nhất thế giới từ nước Pháp', img: 'assets/Posts/falcon-10x/falcon-10x15_thumbnail.jpg' }
    ],
    realEstate: [
      { id: 601, name: 'Saigon Farm Resort', price: 'Liên hệ Host Thịnh', desc: 'Resort sinh thái nghỉ dưỡng ven đô phong cách thượng lưu', img: 'assets/Saigon_Farm_Resort/Phoi_canh_tong_the/SFR_S01_Final_Fix.jpg' },
      { id: 1, name: 'Dinh Thự Ven Sông Sài Gòn', price: '120 - 350 Tỷ VNĐ', desc: 'Bất động sản vị trí kim cương có bến du thuyền riêng', img: 'assets/Index_asset/Ocean-Blue-35-Spoonbill-076-1.jpg' }
    ]
  };

  // Fetch posts.json on load (with dynamic timestamp to prevent stale cache)
  fetch('data/posts.json?t=' + new Date().getTime())
    .then(r => r.json())
    .then(data => { postsData = data; })
    .catch(() => {});

  // Build DOM Elements
  function initChatbotUI() {
    if (document.getElementById('aiChatTrigger')) return;

    // 1. Trigger Button
    const trigger = document.createElement('div');
    trigger.className = 'ai-chat-trigger';
    trigger.id = 'aiChatTrigger';
    trigger.innerHTML = `
      <div class="ai-trigger-avatar">
        <i class="fa-solid fa-sparkles"></i>
        <div class="ai-trigger-badge"></div>
      </div>
      <div class="ai-trigger-text">
        <span class="ai-trigger-label">AI Concierge</span>
        <span class="ai-trigger-title">Hỏi Trợ Lý AI</span>
      </div>
    `;

    // 2. Chat Window
    const chatWin = document.createElement('div');
    chatWin.className = 'ai-chat-window';
    chatWin.id = 'aiChatWindow';
    chatWin.innerHTML = `
      <div class="ai-chat-header">
        <div class="ai-header-info">
          <div class="ai-header-avatar">
            <i class="fa-solid fa-gem"></i>
          </div>
          <div>
            <h4 class="ai-header-title">Trợ Lý Giám Tuyển AI</h4>
            <span class="ai-header-status">Am hiểu siêu xe & tài sản xa xỉ</span>
          </div>
        </div>
        <button class="ai-chat-close" id="aiChatClose" aria-label="Đóng chat">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="ai-chat-body" id="aiChatBody">
        <div class="ai-msg bot">
          <div class="ai-msg-avatar"><i class="fa-solid fa-gem"></i></div>
          <div class="ai-msg-content">
            Kính chào Quý khách! Em là <strong>Trợ Lý Giám Tuyển AI</strong> của Host Huỳnh Hoàng Thịnh. ✨<br><br>
            Quý khách đang tìm kiếm cảm hứng về <strong>Siêu xe độc bản</strong>, <strong>Du thuyền triệu đô</strong>, <strong>Chuyên cơ cá nhân</strong> hay muốn chốt deal <strong>Bất động sản / Xe lướt</strong> hôm nay ạ? 😎
          </div>
        </div>
      </div>

      <div class="ai-quick-chips" id="aiQuickChips">
        <button class="ai-chip" data-query="Tư vấn siêu xe nào chạy nhanh nhất?">🏎️ Siêu xe khủng nhất?</button>
        <button class="ai-chip" data-query="Du thuyền Feadship 821 có gì đặc biệt?">🛥️ Du thuyền Feadship 821</button>
        <button class="ai-chip" data-query="Xe đang bán có con nào lướt đẹp dưới 5 tỷ không?">🚗 Xe lướt dưới 5 tỷ</button>
        <button class="ai-chip" data-query="Chuyên cơ nào bay xa nhất thế giới?">✈️ Chuyên cơ bay xa nhất</button>
        <button class="ai-chip" data-query="Tôi muốn liên hệ trực tiếp anh Huỳnh Hoàng Thịnh">📞 Nhắn Zalo Host Thịnh</button>
      </div>

      <div class="ai-chat-input-wrap">
        <input type="text" class="ai-chat-input" id="aiChatInput" placeholder="Hỏi em về siêu xe, du thuyền, giá bán..." autocomplete="off">
        <button class="ai-chat-send-btn" id="aiChatSend" aria-label="Gửi tin nhắn">
          <i class="fa-solid fa-paper-plane"></i>
        </button>
      </div>
    `;

    document.body.appendChild(trigger);
    document.body.appendChild(chatWin);

    // Event Listeners
    trigger.addEventListener('click', () => {
      chatWin.classList.toggle('active');
      if (chatWin.classList.contains('active')) {
        document.getElementById('aiChatInput').focus();
      }
    });

    document.getElementById('aiChatClose').addEventListener('click', () => {
      chatWin.classList.remove('active');
    });

    document.getElementById('aiChatSend').addEventListener('click', handleUserSend);
    document.getElementById('aiChatInput').addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        handleUserSend();
      }
    });

    // Delegate quick chips
    document.getElementById('aiQuickChips').addEventListener('click', (e) => {
      const chip = e.target.closest('.ai-chip');
      if (chip) {
        const query = chip.getAttribute('data-query');
        submitMessage(query);
      }
    });
  }

  function handleUserSend() {
    const input = document.getElementById('aiChatInput');
    const text = input.value.trim();
    if (!text) return;
    input.value = '';
    submitMessage(text);
  }

  function submitMessage(text) {
    appendUserMsg(text);
    showTypingIndicator();

    setTimeout(() => {
      removeTypingIndicator();
      const reply = generateSmartAnswer(text);
      appendBotMsg(reply.html);
    }, 600 + Math.random() * 400);
  }

  function appendUserMsg(text) {
    const body = document.getElementById('aiChatBody');
    const div = document.createElement('div');
    div.className = 'ai-msg user';
    div.innerHTML = `<div class="ai-msg-content">${escapeHTML(text)}</div>`;
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
  }

  function appendBotMsg(html) {
    const body = document.getElementById('aiChatBody');
    const div = document.createElement('div');
    div.className = 'ai-msg bot';
    div.innerHTML = `
      <div class="ai-msg-avatar"><i class="fa-solid fa-gem"></i></div>
      <div class="ai-msg-content">${html}</div>
    `;
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
  }

  function showTypingIndicator() {
    const body = document.getElementById('aiChatBody');
    const div = document.createElement('div');
    div.className = 'ai-msg bot';
    div.id = 'aiTypingIndicator';
    div.innerHTML = `
      <div class="ai-msg-avatar"><i class="fa-solid fa-gem"></i></div>
      <div class="ai-typing">
        <div class="ai-typing-dot"></div>
        <div class="ai-typing-dot"></div>
        <div class="ai-typing-dot"></div>
      </div>
    `;
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
  }

  function removeTypingIndicator() {
    const el = document.getElementById('aiTypingIndicator');
    if (el) el.remove();
  }

  function escapeHTML(str) {
    return str.replace(/[&<>'"]/g, 
      tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
    );
  }

  // Witty & Intelligent AI Response Generator
  function generateSmartAnswer(rawPrompt) {
    const q = rawPrompt.toLowerCase().trim();

    // 1. ZALO / CONTACT / GẶP ANH THỊNH
    if (q.includes('zalo') || q.includes('liên hệ') || q.includes('số điện thoại') || q.includes('hotline') || q.includes('gặp thịnh') || q.includes('anh thịnh') || q.includes('ceo')) {
      return {
        html: `Dạ để phục vụ Quý khách chuẩn vị VIP 1-1, bảo mật thông tin tuyệt đối, Quý khách có thể kết nối ngay với <strong>Host Huỳnh Hoàng Thịnh</strong> qua:<br><br>
        📞 <strong>Hotline / Zalo:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#c9a96e; font-weight:700;">0906060036</a><br><br>
        <a href="https://zalo.me/0906060036" target="_blank" style="display:inline-flex; align-items:center; gap:6px; background:#0068FF; color:#fff; padding:8px 16px; border-radius:20px; text-decoration:none; font-size:0.82rem; font-weight:600;">
          <i class="fa-solid fa-comment-dots"></i> Mở Zalo Nhắn Anh Thịnh Ngay
        </a>`
      };
    }

    // 2. FEADSHIP 821 / DU THUYỀN HYDRO
    if (q.includes('821') || q.includes('feadship') || q.includes('viva') || q.includes('hydro') || q.includes('du thuyền hydro')) {
      const item = LUXURY_KNOWLEDGE.yachts.find(y => y.id === 122);
      return {
        html: `🛥️ <strong>Feadship 821 (Viva) 2026</strong> là đỉnh cao lịch sử ngành hàng hải thế giới Quý khách ơi! Đây là siêu du thuyền dài <strong>119m</strong> đầu tiên trên thế giới vận hành bằng pin nhiên liệu <strong>Hydrogen (Phát thải 0%)</strong>.<br><br>
        Nó êm ái đến mức Quý khách có thể nghe tiếng sóng vỗ giữa đại dương mà không có một tiếng rung động cơ nào!
        ${createItemCardHTML(item)}`
      };
    }

    // 3. DU THUYỀN CHUNG (YACHTS)
    if (q.includes('du thuyền') || q.includes('yacht') || q.includes('oceanco') || q.includes('lurssen') || q.includes('riva') || q.includes('sunseeker') || q.includes('azimut')) {
      const topYacht = LUXURY_KNOWLEDGE.yachts[Math.floor(Math.random() * LUXURY_KNOWLEDGE.yachts.length)];
      return {
        html: `🌊 Nói về du thuyền thì gu của Quý khách thực sự ở tầng mây thứ 9 rồi! Trên website của anh Thịnh đang giám tuyển các siêu phẩm từ <strong>Feadship 821 (119m)</strong>, <strong>Lürssen Ahpo (115m)</strong> đến <strong>Riva 130 Bellissima (40m)</strong>.<br><br>
        Em xin gửi Quý khách chiêm ngưỡng ngay kiệt tác này:
        ${createItemCardHTML(topYacht)}`
      };
    }

    // 4. CHUYÊN CƠ / JETS
    if (q.includes('chuyên cơ') || q.includes('máy bay') || q.includes('jet') || q.includes('gulfstream') || q.includes('falcon') || q.includes('bombardier') || q.includes('g700') || q.includes('global 8000')) {
      const jet = LUXURY_KNOWLEDGE.jets[0]; // Gulfstream G700
      return {
        html: `✈️ Bước lên chuyên cơ là Quý khách đã bỏ lại mọi dòng người chờ đợi và check-in sau lưng rồi! Chiếc <strong>Gulfstream G700</strong> đạt vận tốc cận siêu thanh Mach 0.925 và tầm bay 7.500 hải lý — ăn sáng ở Sài Gòn, tối ăn tối ngắm tháp Eiffel tại Paris là chuyện trong tầm tay!
        ${createItemCardHTML(jet)}`
      };
    }

    // 5. LOUIS VUITTON PORSCHE SINGER
    if (q.includes('louis vuitton') || q.includes('singer') || q.includes('lv') || q.includes('porsche lv')) {
      const car = LUXURY_KNOWLEDGE.supercars.find(c => c.id === 202);
      return {
        html: `✨ Đây là thương vụ hợp tác lịch sử 172 năm của Louis Vuitton lần đầu tiên lên một chiếc Porsche 911 phục chế bởi Singer California! Họa tiết Monogram dập nổi trên da thuộc thủ công cùng khối động cơ Flat-6 450HP. Chiếc xe này không chỉ để chạy, mà để đưa vào bảo tàng gia tộc!
        ${createItemCardHTML(car)}`
      };
    }

    // 6. XE ĐANG BÁN / XE LƯỚT / DEFENDER X / MASERATI / BMW
    if (q.includes('xe đang bán') || q.includes('xe lướt') || q.includes('dưới 5 tỷ') || q.includes('defender') || q.includes('maserati') || q.includes('grecale') || q.includes('735i') || q.includes('bmw') || q.includes('giao dịch')) {
      let car = LUXURY_KNOWLEDGE.marketCars[0];
      if (q.includes('maserati') || q.includes('grecale') || q.includes('2 tỷ')) car = LUXURY_KNOWLEDGE.marketCars[1];
      if (q.includes('bmw') || q.includes('735')) car = LUXURY_KNOWLEDGE.marketCars[2];

      return {
        html: `🚗 Đội hình xe lướt chính chủ đang sẵn sàng giao dịch ngay hôm nay có 3 deal cực phẩm:<br>
        • <strong>Land Rover Defender 110 X:</strong> 4.390 Tỷ (Độ 300tr đồ chơi)<br>
        • <strong>Maserati Grecale GT 300HP:</strong> 1.999 Tỷ (Giá êm nhất phân khúc SUV Ý)<br>
        • <strong>BMW 735i M Sport G70:</strong> 3.690 Tỷ (Odo 8k km siêu lướt)<br><br>
        Em gửi Quý khách xem chi tiết chiếc này nhé:
        ${createItemCardHTML(car)}`
      };
    }

    // 7. SIÊU XE / HYPERCAR (JESKO, BUGATTI, FERRARI, REVUELTO...)
    if (q.includes('siêu xe') || q.includes('hypercar') || q.includes('jesko') || q.includes('bugatti') || q.includes('chiron') || q.includes('laferrari') || q.includes('revuelto') || q.includes('spectre') || q.includes('nhanh nhất')) {
      const topCar = LUXURY_KNOWLEDGE.supercars[0]; // Koenigsegg Jesko
      return {
        html: `🏎️ Nếu nói về tốc độ thuần khiết và phá vỡ mọi quy luật vật lý, <strong>Koenigsegg Jesko</strong> với 1.600 mã lực (531 km/h) chính là "quái vật" số 1 hành tinh hiện nay! Bên cạnh đó là <strong>Bugatti Chiron W16</strong> và <strong>Ferrari LaFerrari</strong>.<br><br>
        Mời Quý khách thưởng lãm tuyệt phẩm Thụy Điển:
        ${createItemCardHTML(topCar)}`
      };
    }

    // 8. BẤT ĐỘNG SẢN / RESORT / DINH THỰ / PENTHOUSE
    if (q.includes('bất động sản') || q.includes('nhà') || q.includes('biệt thự') || q.includes('dinh thự') || q.includes('resort') || q.includes('saigon farm') || q.includes('penthouse') || q.includes('thủ thiêm')) {
      const prop = LUXURY_KNOWLEDGE.realEstate[0];
      return {
        html: `🏰 Bất động sản trong bộ sưu tập của anh Thịnh luôn tuân theo tiêu chuẩn: <em>Vị trí kim cương, phong thủy sinh tài và không gian nghỉ dưỡng biệt lập</em>.<br><br>
        Đặc biệt dự án <strong>Saigon Farm Resort</strong> đang định hình phong cách sống sinh thái thượng lưu ven đô cho giới tinh hoa:
        ${createItemCardHTML(prop)}`
      };
    }

    // 9. DÍ DỎM / CHÉM GIÓ / KHEN / HỎI THĂM / CHÀO HỎI
    if (q.includes('chào') || q.includes('hello') || q.includes('hi') || q.includes('bạn là ai') || q.includes('ai tạo ra bạn')) {
      return {
        html: `Dạ em chào Quý khách! Em là Trợ Lý Giám Tuyển AI của Host Huỳnh Hoàng Thịnh — chuyên gia "bắt mạch" phong cách sống thượng lưu, định giá siêu xe và tìm kiếm những tài sản độc bản cho các Quý ông & Quý bà sành điệu. Hôm nay Quý khách muốn ngắm xe hay ngắm du thuyền giải tỏa căng thẳng ạ? 😄`
      };
    }

    if (q.includes('nghèo') || q.includes('không có tiền') || q.includes('tiền đâu mua') || q.includes('nhiều tiền thế') || q.includes('đắt quá')) {
      return {
        html: `Haha, người thành công luôn có lối đi riêng mà Quý khách! Người xưa có câu: <em>"Cứ ngắm siêu xe và du thuyền mỗi ngày, vũ trụ sẽ tự gửi năng lượng thịnh vượng đến tài khoản"</em>. 🥂<br><br>
        Cứ thưởng lãm cho đã mắt trước, biết đâu chiều nay trúng dự án lớn mai gọi anh Thịnh book luôn chiếc Gulfstream G700 thì sao ạ! 😎`
      };
    }

    if (q.includes('đẹp') || q.includes('xịn') || q.includes('hay quá') || q.includes('tuyệt vời') || q.includes('thông minh')) {
      return {
        html: `Dạ em cảm ơn lời khen tinh tế của Quý khách nhiều ạ! ✨ Được phục vụ những Quý khách có gu thưởng thức đỉnh cao như Quý khách chính là niềm vinh hạnh của cả em và anh Huỳnh Hoàng Thịnh.`
      };
    }

    // 10. TÌM KIẾM TRONG DATABASE POSTS.JSON THEO TỪ KHÓA
    if (postsData && postsData.length > 0) {
      const matched = postsData.find(p => 
        (p.title && p.title.toLowerCase().includes(q)) || 
        (p.excerpt && p.excerpt.toLowerCase().includes(q))
      );

      if (matched) {
        return {
          html: `Dạ em tìm thấy bài viết chuẩn xác đúng ý Quý khách đang quan tâm đây ạ:<br><br>
          <a class="ai-item-card" href="article.html?id=${matched.id}">
            <img src="${matched.image || 'assets/vehicles/koenigsegg_jesko.jpg'}" alt="${matched.title}">
            <div class="ai-item-card-body">
              <div class="ai-item-card-title">${matched.title}</div>
              <div class="ai-item-card-desc">${matched.excerpt ? matched.excerpt.substring(0, 100) + '...' : ''}</div>
              <span class="ai-item-card-btn">Đọc chi tiết bài viết &rarr;</span>
            </div>
          </a>`
        };
      }
    }

    // 11. DEFAULT LUXURY WITTY FALLBACK
    return {
      html: `Dạ câu hỏi này của Quý khách rất thú vị! Với tư cách là Trợ lý Giám Tuyển Xa Xỉ, em có thể hỗ trợ Quý khách tra cứu thông số chi tiết của hơn 30 mẫu <strong>Siêu xe độc bản</strong>, <strong>Du thuyền triệu đô</strong>, <strong>Chuyên cơ cá nhân</strong> hoặc kết nối xem xe/nhà trực tiếp cùng anh Huỳnh Hoàng Thịnh.<br><br>
      Quý khách muốn em gửi thông tin về mục nào trước ạ? ✨`
    };
  }

  function createItemCardHTML(item) {
    if (!item) return '';
    return `
      <a class="ai-item-card" href="article.html?id=${item.id}">
        <img src="${item.img}" alt="${item.name}">
        <div class="ai-item-card-body">
          <div class="ai-item-card-title">${item.name}</div>
          <div class="ai-item-card-desc">${item.desc} &bull; <strong style="color:#c9a96e;">${item.price}</strong></div>
          <span class="ai-item-card-btn">Xem chi tiết kiệt tác &rarr;</span>
        </div>
      </a>
    `;
  }

  // Initialize when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatbotUI);
  } else {
    initChatbotUI();
  }

})();
