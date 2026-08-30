// ---- MOBILE MENU (prepended) ----
function closeMobileMenu() {
  var drawer = document.getElementById('mobileMenuDrawer');
  var overlay = document.getElementById('mobileMenuOverlay');
  if (drawer) drawer.classList.remove('open');
  if (overlay) overlay.classList.remove('open');
  document.body.style.overflow = '';
}
function openMobileMenu() {
  var drawer = document.getElementById('mobileMenuDrawer');
  var overlay = document.getElementById('mobileMenuOverlay');
  if (drawer) drawer.classList.add('open');
  if (overlay) overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}
// Main Application JS

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Trending Carousel Controls
  const track = document.getElementById('trendingTrack');
  const prevBtn = document.getElementById('trendPrevBtn');
  const nextBtn = document.getElementById('trendNextBtn');

  if (track && prevBtn && nextBtn) {
    const scrollAmount = 270;

    nextBtn.addEventListener('click', () => {
      track.parentElement.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });

    prevBtn.addEventListener('click', () => {
      track.parentElement.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });
  }

  // Initialize Podcast Audio Modal
  const podcastBtns = document.querySelectorAll('.podcast-listen-btn');
  const audioModal = document.getElementById('audioModal');
  const modalClose = document.getElementById('modalCloseBtn');
  const audioElem = document.getElementById('podcastAudio');
  const modalTitle = document.getElementById('audioModalTitle');
  const modalDesc = document.getElementById('audioModalDesc');
  const audioSource = document.getElementById('podcastAudioSource');

  if (podcastBtns.length > 0 && audioModal && modalClose) {
    podcastBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const title = btn.getAttribute('data-ep-title');
        const desc = btn.getAttribute('data-ep-desc');
        const src = btn.getAttribute('data-audio-src');
        
        if (modalTitle) modalTitle.textContent = title;
        if (modalDesc) modalDesc.textContent = desc;
        if (audioSource) {
          audioSource.src = src;
          if (audioElem) {
            audioElem.load(); // reload the audio source
          }
        }
        
        audioModal.classList.add('active');
        if (audioElem) audioElem.play().catch(() => {});
      });
    });

    modalClose.addEventListener('click', () => {
      audioModal.classList.remove('active');
      if (audioElem) audioElem.pause();
    });

    audioModal.addEventListener('click', (e) => {
      if (e.target === audioModal) {
        audioModal.classList.remove('active');
        if (audioElem) audioElem.pause();
      }
    });
  }

// Global Tab Activation Function
window.activateTab = function(tabId) {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  const navLinks = document.querySelectorAll('.nav-link');

  tabBtns.forEach(b => b.classList.toggle('active', b.getAttribute('data-tab') === tabId));
  tabContents.forEach(c => c.classList.toggle('active', c.id === tabId));
  navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('data-target') === tabId));

  const tabsSection = document.querySelector('.tabs-section');
  if (tabsSection) {
    tabsSection.scrollIntoView({ behavior: 'smooth' });
  }
};

  // Hero Auto Slider Logic
  const heroSlides = document.querySelectorAll('#heroAutoSlider .hero-slide');
  const heroPrevBtn = document.getElementById('heroPrevBtn');
  const heroNextBtn = document.getElementById('heroNextBtn');
  let currentHeroIdx = 0;
  let heroTimer = null;

  function showHeroSlide(index) {
    if (heroSlides.length === 0) return;
    heroSlides.forEach((slide, idx) => {
      slide.classList.toggle('active', idx === index);
    });
    currentHeroIdx = index;
  }

  function nextHeroSlide() {
    let nextIdx = (currentHeroIdx + 1) % heroSlides.length;
    showHeroSlide(nextIdx);
  }

  function prevHeroSlide() {
    let prevIdx = (currentHeroIdx - 1 + heroSlides.length) % heroSlides.length;
    showHeroSlide(prevIdx);
  }

  function resetHeroTimer() {
    if (heroTimer) clearInterval(heroTimer);
    if (heroSlides.length > 0) {
      heroTimer = setInterval(nextHeroSlide, 8000);
    }
  }

  if (heroSlides.length > 0) {
    resetHeroTimer();
  }

  if (heroNextBtn) {
    heroNextBtn.addEventListener('click', () => {
      nextHeroSlide();
      resetHeroTimer();
    });
  }

  if (heroPrevBtn) {
    heroPrevBtn.addEventListener('click', () => {
      prevHeroSlide();
      resetHeroTimer();
    });
  }

  // Tabs Switching Logic
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active classes
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      
      // Add active class to clicked
      btn.classList.add('active');
      const targetId = btn.getAttribute('data-tab');
      document.getElementById(targetId).classList.add('active');
    });
  });

  // Sub-tabs Switching Logic
  const subTabBtns = document.querySelectorAll('.sub-tab-btn');
  const subTabContents = document.querySelectorAll('.sub-tab-content');

  subTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const parentTab = btn.closest('.tab-content');
      const btnsInParent = parentTab.querySelectorAll('.sub-tab-btn');
      const contentsInParent = parentTab.querySelectorAll('.sub-tab-content');
      
      btnsInParent.forEach(b => b.classList.remove('active'));
      contentsInParent.forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      const targetId = btn.getAttribute('data-subtab');
      document.getElementById(targetId).classList.add('active');
    });
  });

  // Main Navigation Links Logic
  const navLinks = document.querySelectorAll('.nav-link');
  const tabsSection = document.querySelector('.tabs-section');
  
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      
      if (tabsSection) {
        tabsSection.scrollIntoView({ behavior: 'smooth' });
      }

      const targetTabId = link.getAttribute('data-target');
      if(targetTabId) {
        const targetTabBtn = document.querySelector(`.tab-btn[data-tab="${targetTabId}"]`);
        if(targetTabBtn) {
           targetTabBtn.click();
        }
      }
      
      navLinks.forEach(l => l.classList.remove('active'));
      link.classList.add('active');
    });
  });

  // Fetch JSON and render Editorial Posts with Category Filtering
  const editorialGrid = document.getElementById('editorial-grid');
  const filterBtns = document.querySelectorAll('.editorial-filter-btn');

  function getPostCategory(post) {
    const id = post.id;
    const title = (post.title || '').toLowerCase();
    
    if ((id >= 501 && id <= 530) || (id >= 101 && id <= 106) || [1, 4, 6, 9, 12, 15, 18, 19].includes(id) || title.includes('bất động sản') || title.includes('villa') || title.includes('dinh thự') || title.includes('penthouse') || title.includes('kiến trúc') || title.includes('hồ bơi') || title.includes('nội thất')) {
      return 'bds';
    }
    if ((id >= 601 && id <= 608) || (id >= 400 && id <= 415) || (id >= 107 && id <= 119) || [3, 7, 11, 14, 16, 202].includes(id) || title.includes('siêu xe') || title.includes('ferrari') || title.includes('porsche') || title.includes('bugatti') || title.includes('mclaren') || title.includes('koenigsegg') || title.includes('pagani') || title.includes('aston martin') || title.includes('lamborghini') || title.includes('bmw') || title.includes('mercedes') || title.includes('maserati') || title.includes('bentley') || title.includes('defender')) {
      return 'supercar';
    }
    if ((id >= 609 && id <= 617) || (id >= 120 && id <= 131) || [2, 5, 8, 10, 13, 17, 20].includes(id) || title.includes('du thuyền') || title.includes('chuyên cơ') || title.includes('gulfstream') || title.includes('bombardier') || title.includes('falcon') || title.includes('lürssen') || title.includes('sanlorenzo') || title.includes('benetti') || title.includes('riva') || title.includes('sunseeker') || title.includes('trực thăng') || title.includes('airbus') || title.includes('yacht') || title.includes('jet')) {
      return 'yacht-jet';
    }
    if ((id >= 618 && id <= 620) || (id >= 301 && id <= 304) || title.includes('patek') || title.includes('audemars') || title.includes('hermès') || title.includes('đồng hồ') || title.includes('hàng hiệu') || title.includes('xa xỉ') || title.includes('quiet luxury') || title.includes('thương hiệu')) {
      return 'luxury';
    }
    return 'bds';
  }

  function getCategoryLabel(cat) {
    switch (cat) {
      case 'bds': return 'BẤT ĐỘNG SẢN SIÊU SANG';
      case 'supercar': return 'SIÊU XE & HYPERCAR';
      case 'yacht-jet': return 'DU THUYỀN & CHUYÊN CƠ';
      case 'luxury': return 'ĐỒNG HỒ & HÀNG HIỆU';
      default: return 'TẠP CHÍ XA XỈ';
    }
  }

  if (editorialGrid) {
    fetch('data/posts.json?t=' + new Date().getTime())
      .then(response => response.json())
      .then(posts => {
        let currentFilter = 'all';

        function renderPosts(filter) {
          editorialGrid.innerHTML = '';
          const filtered = filter === 'all' ? posts : posts.filter(p => getPostCategory(p) === filter);
          
          filtered.forEach(post => {
            const cat = getPostCategory(post);
            const catLabel = getCategoryLabel(cat);
            const postHTML = `
              <div class="grid-card" data-category="${cat}">
                <a href="article.html?id=${post.id}" style="display: block; text-decoration: none; color: inherit;">
                  <div class="grid-img" style="position: relative;">
                    <img src="${post.image}" alt="${post.title}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
                    <span style="position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.8); color: #c9a96e; font-size: 0.65rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; letter-spacing: 0.05em; backdrop-filter: blur(4px);">
                      ${catLabel}
                    </span>
                  </div>
                  <div style="font-size: 0.72rem; color: #888; margin-bottom: 6px; font-weight: 600;">${post.date || '30 TH8 2026'}</div>
                  <h5 style="margin-bottom: 8px; line-height: 1.4; font-size: 0.98rem; font-weight: 700;">${post.title}</h5>
                </a>
                <p style="font-weight: 400; font-size: 0.84rem; color: #555; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 14px; line-height: 1.5;">
                  ${post.excerpt}
                </p>
                <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: auto;">
                  <a href="article.html?id=${post.id}" class="editorial-btn" style="flex: 1; text-align: center; margin-top: 0; padding: 8px 12px;">Đọc Chi Tiết</a>
                  <a href="https://zalo.me/0906060036" target="_blank" rel="noopener noreferrer" class="editorial-btn" style="background-color: #0068FF; color: white; border-color: #0068FF; margin-top: 0; padding: 8px 12px; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 4px;">
                    <i class="fa-solid fa-comment-dots"></i> Zalo CEO
                  </a>
                </div>
              </div>
            `;
            editorialGrid.insertAdjacentHTML('beforeend', postHTML);
          });
        }

        renderPosts('all');

        if (filterBtns.length > 0) {
          filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
              filterBtns.forEach(b => {
                b.classList.remove('active');
                b.style.background = '#1a1a1a';
                b.style.color = '#ccc';
                b.style.borderColor = '#333';
              });
              btn.classList.add('active');
              btn.style.background = '#c9a96e';
              btn.style.color = '#000';
              btn.style.borderColor = '#c9a96e';

              currentFilter = btn.getAttribute('data-filter');
              renderPosts(currentFilter);
            });
          });
        }
      })
      .catch(err => console.error("Error fetching posts:", err));
  }
});

// ---- MOBILE MENU INIT (added for responsive) ----
document.addEventListener('DOMContentLoaded', function() {
  // Show/hide hamburger based on viewport
  var mobileMenuBtn = document.getElementById('mobileMenuBtn');
  var mobileMenuClose = document.getElementById('mobileMenuClose');
  var mobileMenuOverlay = document.getElementById('mobileMenuOverlay');

  function updateHamburger() {
    if (mobileMenuBtn) {
      mobileMenuBtn.style.display = window.innerWidth <= 768 ? 'flex' : 'none';
    }
  }
  updateHamburger();
  window.addEventListener('resize', updateHamburger);

  if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobileMenu);
  if (mobileMenuClose) mobileMenuClose.addEventListener('click', closeMobileMenu);
  if (mobileMenuOverlay) mobileMenuOverlay.addEventListener('click', closeMobileMenu);

  // Mobile drawer links: switch tab + close + scroll
  document.querySelectorAll('.mobile-menu-links a[data-tab]').forEach(function(link) {
    link.addEventListener('click', function(e) {
      var tabId = link.getAttribute('data-tab');
      if (tabId) {
        document.querySelectorAll('.tab-btn').forEach(function(btn) {
          btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
        });
        document.querySelectorAll('.tab-content').forEach(function(tc) {
          tc.classList.toggle('active', tc.id === tabId);
        });
        var tabsSec = document.querySelector('.tabs-section');
        if (tabsSec) setTimeout(function() { tabsSec.scrollIntoView({behavior: 'smooth'}); }, 280);
      }
      closeMobileMenu();
    });
  });

  // Sticky header on scroll for desktop
  var header = document.querySelector('.main-header');
  window.addEventListener('scroll', function() {
    if (!header) return;
    if (window.innerWidth > 768) {
      if (window.scrollY > 80) {
        header.style.cssText = 'position:fixed;top:0;background:rgba(10,10,10,0.95);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);padding:12px 0;transition:all 0.3s ease;';
      } else {
        header.style.cssText = 'position:absolute;top:38px;background:linear-gradient(180deg,rgba(0,0,0,0.65) 0%,rgba(0,0,0,0) 100%);padding:20px 0;';
      }
    }
  });

  // Swipe gesture for hero slider on mobile
  var hero = document.getElementById('heroAutoSlider');
  if (hero) {
    var touchStartX = 0;
    hero.addEventListener('touchstart', function(e) { touchStartX = e.touches[0].clientX; }, {passive: true});
    hero.addEventListener('touchend', function(e) {
      var diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {
        var btn = diff > 0 ? document.getElementById('heroNextBtn') : document.getElementById('heroPrevBtn');
        if (btn) btn.click();
      }
    }, {passive: true});
  }
});
