import { writable } from 'svelte/store';
import { browser } from '$app/environment';

// Get initial theme from localStorage or default to 'light'
const userTheme = browser && localStorage.getItem('theme') || 'light';

// Create a writable store for the theme
export const theme = writable(userTheme);

// Function to toggle theme between light and dark
export function toggleTheme() {
  theme.update(currentTheme => {
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    if (browser) {
      // Save to localStorage
      localStorage.setItem('theme', newTheme);
      
      // Update document class for CSS
      document.documentElement.classList.toggle('dark-mode', newTheme === 'dark');
    }
    
    return newTheme;
  });
}

// Initialize the theme on client side
export function initTheme() {
  if (browser) {
    // Get the current theme value
    let currentTheme;
    theme.subscribe(value => {
      currentTheme = value;
    })();
    
    // Add class to document if theme is dark
    document.documentElement.classList.toggle('dark-mode', currentTheme === 'dark');
  }
}
