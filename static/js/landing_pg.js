document.addEventListener('DOMContentLoaded', function() {
    // Initialize Lucide icons
    lucide.createIcons();
    
    // Scroll animation function
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });
    
    // Observe all staggered items
    document.querySelectorAll('.staggered-item').forEach(item => {
      observer.observe(item);
    });
    
    // Add visible class to hero elements on load
    setTimeout(() => {
      document.getElementById('hero-heading').classList.add('visible');
      setTimeout(() => {
        document.getElementById('hero-subheading').classList.add('visible');
        setTimeout(() => {
          document.getElementById('hero-button').classList.add('visible');
        }, 200);
      }, 100);
    }, 500);
    
    // Handle smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          window.scrollTo({
            top: target.offsetTop,
            behavior: 'smooth'
          });
        }
      });
    });
    
    // Add hover effect to destination cards
    document.querySelectorAll('.destination-card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        this.querySelector('img').style.transform = 'scale(1.05)';
      });
      
      card.addEventListener('mouseleave', function() {
        this.querySelector('img').style.transform = 'scale(1)';
      });
    });
    
    
    // Make features and destination headings animate when scrolled into view
    observer.observe(document.getElementById('features-heading'));
    observer.observe(document.getElementById('destinations-heading'));
  });
  