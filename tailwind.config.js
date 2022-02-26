module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    screens: {
      'xs': {'min': '279px', 'max': '410px'},
      // => @media (min-width: 640px and max-width: 767px) { ... }

      'sm': {'min': '411px', 'max': '639px'},
      // => @media (min-width: 640px and max-width: 767px) { ... }

      'md': {'min': '640px', 'max': '767px'},
      // => @media (min-width: 768px and max-width: 991px) { ... }

      'tab': {'min': '820px', 'max': '1180px'},
      // => @media (min-width: 768px and max-width: 991px) { ... }


      'lg': {'min': '768px', 'max': '1023px'},
      // => @media (min-width: 768px and max-width: 1023px) { ... }

      'xl': {'min': '1024px', 'max': '1279px'},
      // => @media (min-width: 1024px and max-width: 1279px) { ... }

      '2xl': {'min': '1280px', 'max': '1535px'},
      // => @media (min-width: 1280px and max-width: 1535px) { ... }

      '3xl': {'min': '1536px'},
      // => @media (min-width: 1536px) { ... }
    },
    extend: {},
  },
  plugins: [],
}