# nicegui_layout_pattern_5.py
from nicegui import ui

with ui.splitter(value=20).classes('w-full h-screen') as splitter:
    with splitter.before:
        with ui.element('div').classes('w-full h-full bg-gray-100 p-4'):
            ui.label('List Area')

    with splitter.after:
        with ui.element('div').classes('w-full h-full p-4'):
            ui.label('Detail Area')

ui.run(reload=False)
