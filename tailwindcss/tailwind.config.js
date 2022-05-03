const plugin = require("tailwindcss/plugin")
const colors = require("tailwindcss/colors")
const defaultTheme = require('tailwindcss/defaultTheme')


module.exports = {
  mode: "JIT",
  content: ['../views/*.html'],
  theme: {
    screens: {
      'sm': '640px',
      'md': '768',
      'lg': '1024',
      'xl': '1280',
      ...defaultTheme.screens,
    },

    extend: {
      colors:{
        // "blue1": "#1DA1F2",
        "blue1": "#ff5c8a",
        // "blue2": "#2795D9",
        "blue2": "#ff5c8a",
        "blue": "#EFF9FF",
        "pinkish": "#C47AC0",
        "dark": "#657786",
        "light": "#AAB8C2",
        "lighter": "#E1E8ED",
        "lightest": "#F5F8FA",
      },
      height:{
        "large": "20rem",
        "font-2xs": "0.5rem",
        "max": "24rem"
      },
      margin:{
        '25.5rem': '25.5rem'
      }
    },
  },
  plugins: [],
}
