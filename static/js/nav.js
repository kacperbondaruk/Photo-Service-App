// Select the SVG Hamburger Icon and Navigation Links
const hamburgerIcon = document.querySelector('.ham');
const navLinks = document.querySelector('.nav-links');

// Add click event listener to toggle the menu
hamburgerIcon.addEventListener('click', () => {
    // Toggle 'active' class for SVG (for animation) and nav links (visibility)
    navLinks.classList.toggle('active');
});