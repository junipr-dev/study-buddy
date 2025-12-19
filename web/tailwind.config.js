/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#661FFF',
        secondary: '#00FFE0',
        background: '#0A0A0A',
        surface: '#1A1A1A',
        accent: '#FF2CF3',
        success: '#B3FF00',
      },
    },
  },
  plugins: [],
}
