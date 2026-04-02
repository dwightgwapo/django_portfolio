/**
 * Portfolio Main JavaScript
 * Handles scroll animations, navigation, and interactive elements
 */

(function() {
    'use strict';

    // ============================================
    // DOM Ready Handler
    // ============================================
    document.addEventListener('DOMContentLoaded', function() {
        initScrollReveal();
        initNavbar();
        initScrollTop();
        initFAQ();
        initSmoothScroll();
        initSkillProgress();
    });

    // ============================================
    // Scroll Reveal Animation
    // ============================================
    function initScrollReveal() {
        const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
        
        if (!revealElements.length) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    // Optionally unobserve after animation
                    // observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        revealElements.forEach(el => {
            observer.observe(el);
        });
    }

    // ============================================
    // Navbar Scroll Effect
    // ============================================
    function initNavbar() {
        const navbar = document.getElementById('mainNav');
        if (!navbar) return;

        let lastScroll = 0;

        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;

            // Add/remove scrolled class
            if (currentScroll > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

            // Hide/show navbar on scroll direction (optional)
            if (currentScroll > lastScroll && currentScroll > 200) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }

            lastScroll = currentScroll;
        }, { passive: true });
    }

    // ============================================
    // Scroll to Top Button
    // ============================================
    function initScrollTop() {
        const scrollBtn = document.getElementById('scrollTop');
        if (!scrollBtn) return;

        // Show/hide button based on scroll position
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 500) {
                scrollBtn.classList.add('visible');
            } else {
                scrollBtn.classList.remove('visible');
            }
        }, { passive: true });

        // Smooth scroll to top on click
        scrollBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ============================================
    // FAQ Accordion
    // ============================================
    function initFAQ() {
        const faqItems = document.querySelectorAll('.faq-item');
        if (!faqItems.length) return;

        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            if (question) {
                question.addEventListener('click', () => {
                    // Close other items
                    faqItems.forEach(otherItem => {
                        if (otherItem !== item && otherItem.classList.contains('active')) {
                            otherItem.classList.remove('active');
                        }
                    });
                    // Toggle current item
                    item.classList.toggle('active');
                });
            }
        });
    }

    // ============================================
    // Smooth Scroll for Anchor Links
    // ============================================
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const headerOffset = 80;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    // ============================================
    // Skill Progress Animation
    // ============================================
    function initSkillProgress() {
        const progressBars = document.querySelectorAll('.skill-progress');
        if (!progressBars.length) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.5
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const progressBar = entry.target;
                    const targetWidth = progressBar.dataset.progress || '0%';
                    
                    // Animate the progress bar
                    setTimeout(() => {
                        progressBar.style.width = targetWidth;
                    }, 200);

                    observer.unobserve(progressBar);
                }
            });
        }, observerOptions);

        progressBars.forEach(bar => {
            observer.observe(bar);
        });
    }

    // ============================================
    // Parallax Effect for Hero Section
    // ============================================
    function initParallax() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;

        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * 0.3;
            
            if (rate < heroSection.offsetHeight) {
                heroSection.style.backgroundPositionY = `${rate}px`;
            }
        }, { passive: true });
    }

    // ============================================
    // Typing Effect (Optional for Hero)
    // ============================================
    function initTypewriter() {
        const typewriterElement = document.querySelector('.typewriter-text');
        if (!typewriterElement) return;

        const text = typewriterElement.dataset.text || typewriterElement.textContent;
        typewriterElement.textContent = '';
        
        let i = 0;
        const speed = 50; // typing speed in milliseconds

        function typeWriter() {
            if (i < text.length) {
                typewriterElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, speed);
            }
        }

        // Start typing after a short delay
        setTimeout(typeWriter, 500);
    }

    // ============================================
    // Counter Animation
    // ============================================
    function initCounters() {
        const counters = document.querySelectorAll('.counter');
        if (!counters.length) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.5
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.dataset.target) || 0;
                    const duration = 2000; // 2 seconds
                    const step = target / (duration / 16); // 60fps
                    let current = 0;

                    const updateCounter = () => {
                        current += step;
                        if (current < target) {
                            counter.textContent = Math.floor(current);
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target;
                        }
                    };

                    updateCounter();
                    observer.unobserve(counter);
                }
            });
        }, observerOptions);

        counters.forEach(counter => {
            observer.observe(counter);
        });
    }

    // ============================================
    // Card Tilt Effect (3D hover)
    // ============================================
    function initCardTilt() {
        const cards = document.querySelectorAll('.tilt-card');
        if (!cards.length) return;

        cards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
            });
        });
    }

    // ============================================
    // Image Lazy Loading
    // ============================================
    function initLazyLoading() {
        const lazyImages = document.querySelectorAll('img[data-src]');
        if (!lazyImages.length) return;

        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => {
            imageObserver.observe(img);
        });
    }

    // ============================================
    // Mobile Menu Close on Click
    // ============================================
    function initMobileMenu() {
        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
        const navbarCollapse = document.querySelector('.navbar-collapse');
        const navbarToggler = document.querySelector('.navbar-toggler');

        if (!navbarCollapse || !navbarToggler) return;

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }

    // ============================================
    // Form Validation Enhancement
    // ============================================
    function initFormValidation() {
        const forms = document.querySelectorAll('form.needs-validation');
        
        forms.forEach(form => {
            form.addEventListener('submit', (event) => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            });
        });
    }

    // ============================================
    // Initialize all on DOM ready
    // ============================================
    document.addEventListener('DOMContentLoaded', () => {
        initParallax();
        initTypewriter();
        initCounters();
        initCardTilt();
        initLazyLoading();
        initMobileMenu();
        initFormValidation();
    });

})();
