from nicegui import ui

with ui.row().classes('w-full items-center gap-3'):
    # w-full       -> row spans the available width
    # items-center -> vertical align children in the middle (cross-axis)
    # gap-3        -> spacing between children

    ui.icon('menu')
    ui.label('Title').classes('text-lg font-semibold')

    # A common pattern: push items to the far right
    ui.space()  # Quasar spacer; expands to fill available space

    ui.button('Save')
    ui.button('Cancel').props('flat')

ui.separator()

with ui.column().classes('w-full gap-4'):
    # gap-4 -> vertical spacing between items
    ui.label('Profile').classes('text-xl font-bold')

    with ui.row().classes('gap-3 items-center'):
        ui.label('Name').classes('w-24 text-gray-600')
        ui.input().classes('flex-grow')  # flex-grow makes the input take remaining space

    with ui.row().classes('gap-3 items-center'):
        ui.label('Email').classes('w-24 text-gray-600')
        ui.input().classes('flex-grow')

ui.separator()

with ui.card().classes('w-full max-w-lg p-4'):
    # p-4 -> padding inside the card
    # max-w-lg -> cap width so it doesn't stretch too far on big screens

    with ui.card_section():
        ui.label('Settings').classes('text-lg font-semibold')

    with ui.card_section().classes('gap-3'):
        # card_section is just a sub-container with nice spacing defaults
        ui.switch('Enable feature')
        ui.select(['Low', 'Medium', 'High'], label='Quality')

    with ui.card_section().classes('flex justify-end gap-2'):
        # justify-end -> align buttons to the right
        ui.button('Reset').props('flat')
        ui.button('Save')

ui.separator()

with ui.grid(columns=1).classes('w-full gap-4 sm:grid-cols-2 lg:grid-cols-3'):
    for i in range(6):
        with ui.card().classes('p-4'):
            ui.label(f'Card {i}').classes('font-semibold')
            ui.label('Some description').classes('text-sm text-gray-600')

ui.separator()

with ui.tabs().classes('w-full') as tabs:
    general = ui.tab('General')
    advanced = ui.tab('Advanced')
    about = ui.tab('About')

with ui.tab_panels(tabs, value=general).classes('w-full'):

    with ui.tab_panel(general).classes('p-4'):
        ui.input('Project name')
        ui.switch('Enable notifications')

    with ui.tab_panel(advanced).classes('p-4'):
        ui.input('API Key')
        ui.checkbox('Verbose logging')

    with ui.tab_panel(about).classes('p-4'):
        ui.label('Version 1.2.3')

ui.run(reload=False)
