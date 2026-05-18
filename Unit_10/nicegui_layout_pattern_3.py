# nicegui_layout_pattern_3.py
from nicegui import ui

with ui.column().classes('w-full max-w-none p-6 gap-6'):
    with ui.grid().classes('w-full grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4'):
        # w-full → full width
        # grid-cols-1 → mobile
        # sm:grid-cols-2 → small screens
        # lg:grid-cols-4 → large screens
        for i in range(8):
            with ui.card().classes('p-4'):
                ui.label(f'Card {i}')

ui.run(reload=False)
