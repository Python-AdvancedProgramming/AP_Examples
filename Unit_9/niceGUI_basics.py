from nicegui import ui

# =============================================================================
# NICEGUI BASICS — LEARNING FROM SCRATCH
# =============================================================================

# =============================================================================
# 1. LABELS — Displaying Text
# =============================================================================
# ui.label() shows text on screen.
# .classes() changes the look using Tailwind CSS utility names.
# Think of it like: text-h4 = big, text-caption = small/gray.

ui.label('Hello, NiceGUI!')                            # plain text
ui.label('Big Title').classes('text-h4 text-primary')  # large + colored
ui.label('Small caption text').classes('text-caption') # small + muted

ui.separator()  # draws a horizontal line between sections


# =============================================================================
# 2. BUTTONS — Reacting to Clicks
# =============================================================================
# on_click= runs a function when the button is pressed.
# ui.notify() shows a small pop-up message (great for feedback).

ui.button('Click Me', on_click=lambda: ui.notify('Button was clicked!'))
ui.button('Download File', icon='download',
          on_click=lambda: ui.download(b'Hello, world!', 'hello.txt'))  # b = bytes literal for file content

ui.separator()


# =============================================================================
# 3. TEXT & NUMBER INPUTS
# =============================================================================
# ui.input()  → text box for typing strings
# ui.number() → numeric input with optional bounds

ui.input(label='Your Name', placeholder='e.g. Alice')
ui.number(label='Your Age', min=0, max=120, value=25)

ui.separator()


# =============================================================================
# 4. CHECKBOX, SWITCH, RADIO, TOGGLE
# =============================================================================
# All of these represent on/off or multiple-choice decisions.
#
# checkbox → classic tick box
# switch   → looks like a mobile toggle
# radio    → pick exactly one from a list
# toggle   → button-style choice from a list
# select   → dropdown list with single or multiple selection

ui.checkbox('I agree to the terms')
ui.switch('Enable notifications')
ui.radio(['Apple', 'Banana', 'Cherry'], value='Apple').props('inline')
ui.toggle(['Small', 'Medium', 'Large'], value='Medium')

ui.separator()


# =============================================================================
# 5. SLIDER & SELECT (DROPDOWN)
# =============================================================================
# slider → drag to pick a number between min and max
# select → dropdown to pick one option from a list

ui.slider(min=0, max=100, value=40)
ui.select(['Python', 'JavaScript', 'Rust'], label='Favorite Language', value='Python', multiple=True)

ui.separator()


# =============================================================================
# 6. MARKDOWN
# =============================================================================
# ui.markdown() renders formatted text.
# Useful for instructions, descriptions, or rich content.

ui.markdown('''
**Bold**, *italic*, and `inline code` all work here.

Shopping list:
- Apples
- Bread
- Coffee
''')

ui.separator()


# =============================================================================
# 7. DATA BINDING — Keeping Controls in Sync with State
# =============================================================================
# CONCEPT: Instead of manually reading every widget, we use a shared state
# dictionary. Controls "bind" to it — when one changes, others update too.
#
# .bind_value(state, 'key')
#   → Links a control's value to state['key'] in BOTH directions.
#     UI change  → state updates automatically.
#     State change → UI updates automatically.
#
# .bind_text_from(state, 'key', backward=fn)
#   → A label READS from state, but can't write back (read-only).
#     backward = is a function that formats the raw value for display.
#
# .bind_visibility_from(state, 'key')
#   → Shows or hides an element based on a True/False state value.
# =============================================================================

state = {
    'name': 'Alice',
    'score': 78,
    'show_warning': False,
}

ui.label('Binding Demo').classes('text-h5 text-primary')

# --- Example A: Two-way binding ---
# Both the input and the label below share state['name'].
# Type in the box → the greeting updates live.
# v = the current value of state['name']
ui.input(label='Enter your name').bind_value(state, 'name')
# backward: How to convert the raw state value → into what the UI should display
ui.label().bind_text_from(state, 'name', backward=lambda v: f'👋 Hello, {v}!')
ui.separator()

# --- Example B: Slider + live display ---
# The slider writes to state['score'] (two-way binding).
# The label reads from state['score'] and formats it for display (one-way binding).
# Precondition: state['score'] must always be a numeric value (int or float),
# otherwise the backward formatter will raise an error.
# v = the current value of state['score']
ui.slider(min=0, max=100).bind_value(state, 'score')
ui.label().bind_text_from(
    state, 'score',
    backward=lambda v: f'Score: {int(v)} / 100'
)
ui.separator()

# --- Example C: Show/hide with bind_visibility_from ---
# The switch controls state['show_warning'] (True/False).
# The warning label only appears when show_warning is True.
ui.switch('Show warning message').bind_value(state, 'show_warning')
ui.label('⚠️  Warning: This is a serious alert!') \
    .classes('text-red font-bold') \
    .bind_visibility_from(state, 'show_warning')


ui.run(reload=True)  # Start the app with auto-reload on code changes