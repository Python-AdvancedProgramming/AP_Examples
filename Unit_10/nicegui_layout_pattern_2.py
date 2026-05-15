# nicegui_layout_pattern_2.py
from nicegui import ui

with ui.row().classes('w-full min-h-screen no-wrap'):
    with ui.column().classes('w-64 p-4 bg-gray-100'):
        ui.button('Dashboard')
        ui.button('Settings')

    with ui.column().classes('flex-grow p-6'):
        # flex-grow allows this column to take up the remaining space
        ui.label('Main Content')

ui.run(reload=False)
