/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './cruises/templates/cruises/**/*.{html,js}',
    './templates/**/*.{html,js}',
    './site_pages/templates/site_pages/**/*.{html,js}',
    './cruise_manager/templates/cruise_manager/**/*.{html,js}'
  ],
  theme: {
    extend: {
      fontFamily: {
        admin: ['forma-djr-micro']
      },
      colors: {
        admin_bar_bg: '#F5F5F5',
        admin_grey_bg: '#EFEFEF',
        admin_section_bg: '#FBFBFB',
        black111: '#111111',
        black222: '#222222',
        black333: '#333333',
        grey444: '#444444',
        grey555: '#555555',
        grey_b_light: '#DADADA',
        field_inactive: '#f1f1f1',
        field_active_hover: '#fdfdfd',
        field_inactive_border: '#cdcdcd',
      }
    },
  },
  plugins: [],
}

