// Portfolio interactivity: navbar, mobile menu, scroll reveal, progress bar, skill bars.

document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.getElementById('navbar')
  const progressBar = document.getElementById('progress-bar')
  const menuToggle = document.getElementById('menu-toggle')
  const menuIcon = document.getElementById('menu-icon')
  const mobileMenu = document.getElementById('mobile-menu')

  const menuOpenSvg =
    '<svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/></svg>'
  const menuCloseSvg =
    '<svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>'

  // Sticky navbar background + scroll progress bar
  const onScroll = () => {
    const scrolled = window.scrollY > 20
    if (navbar) {
      navbar.classList.toggle('bg-navy-900/95', scrolled)
      navbar.classList.toggle('shadow-soft', scrolled)
      navbar.classList.toggle('backdrop-blur', scrolled)
    }
    if (progressBar) {
      const height = document.documentElement.scrollHeight - window.innerHeight
      const ratio = height > 0 ? window.scrollY / height : 0
      progressBar.style.transform = `scaleX(${ratio})`
    }
  }
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })

  // Mobile menu toggle
  let menuOpen = false
  const closeMenu = () => {
    menuOpen = false
    mobileMenu.classList.add('hidden')
    menuIcon.innerHTML = menuOpenSvg
    menuToggle.setAttribute('aria-expanded', 'false')
    document.body.style.overflow = ''
  }
  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      menuOpen = !menuOpen
      mobileMenu.classList.toggle('hidden', !menuOpen)
      menuIcon.innerHTML = menuOpen ? menuCloseSvg : menuOpenSvg
      menuToggle.setAttribute('aria-expanded', String(menuOpen))
      document.body.style.overflow = menuOpen ? 'hidden' : ''
    })
    document
      .querySelectorAll('.mobile-link')
      .forEach((link) => link.addEventListener('click', closeMenu))
  }

  // Scroll reveal via IntersectionObserver
  const revealEls = document.querySelectorAll('[data-reveal]')
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed')
            observer.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.15 },
    )
    revealEls.forEach((el) => observer.observe(el))
  } else {
    revealEls.forEach((el) => el.classList.add('revealed'))
  }

  // Animate skill bars when the skills section enters view
  const skillBars = document.querySelectorAll('.skill-bar')
  if (skillBars.length && 'IntersectionObserver' in window) {
    const skillObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const bar = entry.target
            bar.style.width = (bar.dataset.level || 0) + '%'
            skillObserver.unobserve(bar)
          }
        })
      },
      { threshold: 0.4 },
    )
    skillBars.forEach((bar) => skillObserver.observe(bar))
  } else {
    skillBars.forEach((bar) => {
      bar.style.width = (bar.dataset.level || 0) + '%'
    })
  }
})
