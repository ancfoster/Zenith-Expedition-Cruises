/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
    './static/js/**/*.{html,js}',
    './cruise_manager/templates/cruise_manager/**/*.{html,js}'
  ],
  theme: {
    extend: {
      fontFamily: {
        admin: ['forma-djr-micro'],
        zenith_h: ['termina'],
        zenith_b: ['neue-haas-grotesk-display'],
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
        grey666: '#666666',
        grey_b_light: '#DADADA',
        field_inactive: '#f1f1f1',
        field_active_hover: '#fdfdfd',
        field_inactive_border: '#cdcdcd',
        admin_table_grey_top: '#F4F4F4',
        admin_table_border: '#DADADA',
        admin_table_grey1: '#F0F0F0',
        admin_table_grey2: '#E4E4E4',
        admin_form_tip: '#DEEBF1',
        main_border_grey: '#CDCDCD',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

