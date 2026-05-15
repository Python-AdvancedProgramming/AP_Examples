# nicegui_layout_pattern_3.py
from nicegui import ui

with ui.column().classes('w-full p-6 gap-6'):
    with ui.grid(columns='1 sm:2 lg:4').classes('gap-4'):
        for i in range(8):
            with ui.card().classes('p-4'):
                ui.label(f'Card {i}')

ui.run(reload=False)
