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

  // Hero Auto Slider Logic
  const heroSlides = document.querySelectorAll('#heroAutoSlider .hero-slide');
  let currentHeroIdx = 0;

  if (heroSlides.length > 0) {
    setInterval(() => {
      heroSlides[currentHeroIdx].classList.remove('active');
      currentHeroIdx = (currentHeroIdx + 1) % heroSlides.length;
      heroSlides[currentHeroIdx].classList.add('active');
    }, 10000); // 10 seconds
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

  // Fetch JSON and render Editorial Posts
  const editorialGrid = document.getElementById('editorial-grid');
  if (editorialGrid) {
    fetch('data/posts.json')
      .then(response => response.json())
      .then(posts => {
        editorialGrid.innerHTML = ''; // clear initial content
        posts.forEach(post => {
          const postHTML = `
            <div class="grid-card">
              <a href="article.html?id=${post.id}" style="display: block; text-decoration: none; color: inherit;">
                <div class="grid-img">
                   <img src="${post.image}" alt="${post.title}">
                </div>
                <h5 style="margin-bottom: 8px; line-height: 1.4;">${post.title}</h5>
              </a>
              <p style="font-weight: 400; font-size: 0.85rem; color: #555; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 12px;">
                ${post.excerpt}
              </p>
              <a href="article.html?id=${post.id}" class="editorial-btn">Đọc tiếp</a>
              <a href="https://zalo.me/0906060036" class="editorial-btn" style="background-color: #0068FF; color: white; border-color: #0068FF; margin-left: 8px;">
                Liên hệ CEO Thịnh (Ken) (0906060036)
              </a>
            </div>
          `;
          editorialGrid.insertAdjacentHTML('beforeend', postHTML);
        });
      })
      .catch(err => console.error("Error fetching posts:", err));
  }
});
