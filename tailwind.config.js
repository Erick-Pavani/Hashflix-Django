/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    './filme/templates/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
