/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    fontFamily:{
      "my":"'Varela Round'",
      "title-font":"'Dancing Script',cursive"
    },
    extend: {},
  },
  plugins: [],
}