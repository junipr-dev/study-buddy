/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#6B4FFF', // Synthwave purple-blue
        'primary-dark': '#4A2F9A', // Darker purple
        'primary-light': '#8B7FFF', // Lighter purple
        secondary: '#FF6EC7', // Synthwave pink
        'secondary-dark': '#E84AA8',
        background: '#0A0A0A',
        surface: '#1A1A1A',
        accent: '#00E6F6', // Cyan-blue
        success: '#B3FF00',
      },
      backgroundImage: {
        'gradient-primary': 'linear-gradient(135deg, #6B4FFF 0%, #4A2F9A 50%, #8B7FFF 100%)',
        'gradient-synthwave': 'linear-gradient(135deg, #6B4FFF 0%, #FF6EC7 100%)',
      },
      keyframes: {
        slideDown: {
          '0%': { opacity: '0', transform: 'translate(-50%, -100%)' },
          '100%': { opacity: '1', transform: 'translate(-50%, -50%)' },
        },
      },
      animation: {
        slideDown: 'slideDown 0.3s ease-out forwards',
      },
    },
  },
  plugins: [],
}
