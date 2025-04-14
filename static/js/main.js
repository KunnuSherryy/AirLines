// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu');
    const nav = document.querySelector('nav');
    
    if (mobileMenuBtn && nav) {
        mobileMenuBtn.addEventListener('click', function() {
            nav.classList.toggle('active');
            if (nav.classList.contains('active')) {
                mobileMenuBtn.innerHTML = '<i class="fas fa-times"></i>';
            } else {
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!nav.contains(event.target) && !mobileMenuBtn.contains(event.target)) {
                nav.classList.remove('active');
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    }
    
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            // Close mobile menu if open
            if (nav) {
                nav.classList.remove('active');
                if (mobileMenuBtn) {
                    mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
                }
            }
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Initialize GSAP animations - only for main page
    // Only initialize if GSAP is loaded
    if (typeof gsap !== 'undefined') {
        // Register ScrollTrigger plugin
        if (typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);
        }
        
        // Hero section text animations
        gsap.from('.animate-text', {
            opacity: 0,
            y: 30,
            stagger: 0.3,
            duration: 1,
            ease: 'power3.out'
        });
        
        // Hero image animation
        gsap.from('.hero-image', {
            opacity: 0,
            x: 100,
            duration: 1.2,
            delay: 0.5,
            ease: 'power3.out'
        });
        
        // Features section animations
        gsap.from('.feature-card', {
            scrollTrigger: {
                trigger: '.features',
                start: 'top 80%'
            },
            opacity: 0,
            y: 50,
            stagger: 0.2,
            duration: 0.8,
            ease: 'power3.out'
        });
        
        // About section animations
        gsap.from('.about-content', {
            scrollTrigger: {
                trigger: '.about',
                start: 'top 80%'
            },
            opacity: 0,
            x: -50,
            duration: 0.8,
            ease: 'power3.out'
        });
        
        gsap.from('.about-image', {
            scrollTrigger: {
                trigger: '.about',
                start: 'top 80%'
            },
            opacity: 0,
            x: 50,
            duration: 0.8,
            ease: 'power3.out'
        });
        
        gsap.from('.stat-box', {
            scrollTrigger: {
                trigger: '.stats-container',
                start: 'top 90%'
            },
            opacity: 0,
            y: 30,
            stagger: 0.15,
            duration: 0.6,
            ease: 'power3.out'
        });
        
        // Team section animations
        gsap.from('.team-member', {
            scrollTrigger: {
                trigger: '.team',
                start: 'top 80%'
            },
            opacity: 0,
            y: 50,
            stagger: 0.2,
            duration: 0.8,
            ease: 'power3.out'
        });
        
        // Contact section animations
        gsap.from('.contact-form', {
            scrollTrigger: {
                trigger: '.contact',
                start: 'top 80%'
            },
            opacity: 0,
            x: -50,
            duration: 0.8,
            ease: 'power3.out'
        });
        
        gsap.from('.contact-info', {
            scrollTrigger: {
                trigger: '.contact',
                start: 'top 80%'
            },
            opacity: 0,
            x: 50,
            duration: 0.8,
            ease: 'power3.out'
        });
        
        // Header animation on scroll
        let lastScrollTop = 0;
        const header = document.querySelector('header');
        
        if (header) {
            window.addEventListener('scroll', function() {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                
                if (scrollTop > 100) {
                    header.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
                    header.style.background = 'rgba(255, 255, 255, 0.95)';
                } else {
                    header.style.boxShadow = 'none';
                    header.style.background = 'var(--white)';
                }
                
                lastScrollTop = scrollTop;
            });
        }
        
        // Highlight active menu item based on scroll position
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('nav ul li a');
        
        if (sections.length > 0 && navLinks.length > 0) {
            window.addEventListener('scroll', function() {
                let current = '';
                
                sections.forEach(section => {
                    const sectionTop = section.offsetTop;
                    const sectionHeight = section.clientHeight;
                    if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
                        current = section.getAttribute('id');
                    }
                });
                
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${current}`) {
                        link.classList.add('active');
                    }
                });
            });
        }
    }
});

// Preloader for main page
window.addEventListener('load', function() {
    // Check if preloader exists (only for main page and signup page)
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        setTimeout(function() {
            preloader.style.opacity = '0';
            setTimeout(function() {
                preloader.style.display = 'none';
            }, 500);
        }, 3000); // Show preloader for 3 seconds to match the animation duration
    }
}); 