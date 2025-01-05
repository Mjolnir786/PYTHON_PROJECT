document.addEventListener('DOMContentLoaded', () => {
    const weatherInfo = document.querySelector('.weather-info');
    if (weatherInfo) {
        weatherInfo.style.transition = 'all 1s ease-in-out';
        weatherInfo.style.transform = 'translateY(20px)';
        setTimeout(() => {
            weatherInfo.style.transform = 'translateY(0)';
        }, 300);
    }
});
