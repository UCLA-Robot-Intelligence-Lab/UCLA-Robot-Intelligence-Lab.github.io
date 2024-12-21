const body = document.body;
const btnTheme = document.querySelector('.fa-moon');

// Add or remove theme-related classes
const addThemeClass = (bodyClass, btnClass) => {
	body.classList.add(bodyClass);
	btnTheme.classList.add(btnClass);
};

// Set initial theme from localStorage
const getBodyTheme = localStorage.getItem('portfolio-theme');
const getBtnTheme = localStorage.getItem('portfolio-btn-theme');
addThemeClass(getBodyTheme, getBtnTheme);

// Check if current theme is light
const isLight = () => body.classList.contains('light');

// Set new theme and store it in localStorage
const setTheme = (bodyClass, btnClass) => {
	body.classList.remove(localStorage.getItem('portfolio-theme'));
	btnTheme.classList.remove(localStorage.getItem('portfolio-btn-theme'));
	addThemeClass(bodyClass, btnClass);
	localStorage.setItem('portfolio-theme', bodyClass);
	localStorage.setItem('portfolio-btn-theme', btnClass);
};

// Toggle between light and dark themes
const toggleTheme = () =>
	isLight() ? setTheme('dark', 'fa-sun') : setTheme('light', 'fa-moon');

btnTheme.addEventListener('click', toggleTheme);

// Scroll-to-top button visibility based on scroll position
const scrollUp = () => {
	const btnScrollTop = document.querySelector('.scroll-top');
	if (body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
		btnScrollTop.style.display = 'block';
	} else {
		btnScrollTop.style.display = 'none';
	}
};

document.addEventListener('scroll', scrollUp);


// Toggle

// Theme toggle logic
const toggle = document.getElementById("theme-toggle");

// Load theme from localStorage
if (localStorage.getItem("theme") === "light") {
	body.classList.add("light-mode");
	toggle.checked = true;
}

// Toggle theme and save to localStorage
toggle.addEventListener("change", () => {
	body.classList.toggle("light-mode");
	localStorage.setItem(
		"theme",
		body.classList.contains("light-mode") ? "light" : "dark"
	);
});