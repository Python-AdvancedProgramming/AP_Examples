# nicegui_layout_pattern_1.py
# pkill -f nicegui => kills all nicegui processes
from nicegui import ui

with ui.column().classes('min-h-screen w-full items-center justify-center'):
    # .classes('items-center justify-center') centers the content both vertically and horizontally
    with ui.card().classes('w-full max-w-md p-6 shadow-lg'):
        # with maximum width 448px (max-w-md) = 28rem * 16px
        ui.label('Login').classes('text-2xl font-bold')
        with ui.column().classes('gap-4'):
            ui.input('Email')
            ui.input('Password', password=True)
            ui.button('Sign In').classes('w-full')

ui.run(reload=False)
