/**
 * Google Analytics 4 (GA4) Centralized Integration
 * Dành cho website: huynhhoangthinh.com
 * 
 * HƯỚNG DẪN:
 * Khi bạn đã có mã Measurement ID thật từ Google Analytics (dạng G-XXXXXXXXXX),
 * chỉ cần dán vào biến GA_MEASUREMENT_ID dưới đây. Toàn bộ các trang sẽ tự động kích hoạt.
 */
(function () {
  // === ĐIỀN MÃ MEASUREMENT ID VÀO ĐÂY (VD: 'G-1234567890') ===
  const GA_MEASUREMENT_ID = 'G-0BJP6BZRF8';

  // Nếu chưa điền hoặc là mã placeholder thì không thực hiện gì (không gây lỗi console, không gửi request rác)
  if (
    !GA_MEASUREMENT_ID ||
    !GA_MEASUREMENT_ID.startsWith('G-') ||
    GA_MEASUREMENT_ID.includes('XXXXX')
  ) {
    return;
  }

  // 1. Tải thư viện gtag.js bất đồng bộ
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(GA_MEASUREMENT_ID)}`;
  document.head.appendChild(script);

  // 2. Khởi tạo dataLayer & cấu hình Google Analytics
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  gtag('js', new Date());
  gtag('config', GA_MEASUREMENT_ID, {
    send_page_view: true
  });
})();
