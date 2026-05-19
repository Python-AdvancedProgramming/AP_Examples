from nicegui import ui

ui.label('justify-center example')
with ui.row().classes('w-full justify-center bg-gray-200 p-4 gap-4'):
    ui.button('Button 1')
    ui.button('Button 2')
    ui.button('Button 3')

ui.separator()

ui.label('justify-between example')
with ui.row().classes('w-full justify-between bg-gray-200 p-4'):
    ui.button('Left')
    ui.button('Middle')
    ui.button('Right')

ui.run()