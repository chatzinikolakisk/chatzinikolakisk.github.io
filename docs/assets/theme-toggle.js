// Theme toggle functionality
(function() {
  const THEME_KEY = 'nord-theme';
  const DARK = 'dark';
  const LIGHT = 'light';
  
  // Get saved theme or default to dark
  function getTheme() {
    return localStorage.getItem(THEME_KEY) || DARK;
  }
  
  // Save theme to localStorage
  function saveTheme(theme) {
    localStorage.setItem(THEME_KEY, theme);
  }
  
  // Apply theme to document
  function applyTheme(theme) {
    if (theme === LIGHT) {
      document.documentElement.setAttribute('data-theme', 'light');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    updateIconVisibility(theme);
  }
  
  // Toggle between themes
  function toggleTheme() {
    const currentTheme = getTheme();
    const newTheme = currentTheme === DARK ? LIGHT : DARK;
    saveTheme(newTheme);
    applyTheme(newTheme);
    updateToggleButton(newTheme);
  }
  
  // Update icon visibility
  function updateIconVisibility(theme) {
    const moonIcon = document.querySelector('.moon-icon');
    const sunIcon = document.querySelector('.sun-icon');
    
    if (moonIcon && sunIcon) {
      if (theme === LIGHT) {
          sunIcon.classList.remove('active');
          moonIcon.classList.add('active');
      } else {
          sunIcon.classList.add('active');
          moonIcon.classList.remove('active');
      }
    }
  }

  // Update toggle button appearance
  function updateToggleButton(theme) {
    const button = document.querySelector('.theme-toggle');
    if (button) {
      button.setAttribute('aria-label', `Switch to ${theme === DARK ? 'dark' : 'light'} theme`);
    }
  }
  
  // Initialize theme on page load
  function initTheme() {
    const savedTheme = getTheme();
    applyTheme(savedTheme);
    
    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
      updateToggleButton(savedTheme);
      
      // Add click listener to toggle button
      const toggleButton = document.querySelector('.theme-toggle');
      if (toggleButton) {
        toggleButton.addEventListener('click', toggleTheme);
      }
    });
  }
  
  // Initialize immediately
  initTheme();
})();