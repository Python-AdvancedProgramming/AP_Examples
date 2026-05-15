# nicegui_layout_pattern_4.py
from nicegui import ui

with ui.column().classes('w-full p-6 gap-6'):
    with ui.row().classes('justify-between items-center'):
        ui.label('Users')
        ui.button('Add User')
    with ui.card().classes('p-4'):
        ui.label('Content Area')

ui.run(reload=False)
