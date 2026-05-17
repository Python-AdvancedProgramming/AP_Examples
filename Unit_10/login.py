from nicegui import app, ui

# To go from Authentication (knowing who someone is) to
# Authorization (knowing what they can do), you typically use
# Roles or Permissions.

# 1. Credentials with assigned roles
USERS = {
    'admin': {'password': 'secret123', 'role': 'admin'},
    'staff': {'password': 'password123', 'role': 'editor'}
}


@ui.page('/admin')
def admin_page():
    # --- AUTHORIZATION CHECK ---
    user_data = app.storage.user
    if not user_data.get('authenticated', False):
        ui.navigate.to('/login')
        return

    # Check if the user has the 'admin' role
    if user_data.get('role') != 'admin':
        with ui.column().classes('absolute-center items-center'):
            ui.label('Access Denied: Admins Only').classes(
                'text-h4 text-negative')
            ui.button('Back to Home', on_click=lambda: ui.navigate.to('/'))
        return

    # Authorized Admin Content
    with ui.column().classes('absolute-center items-center'):
        ui.label(f"Welcome to the Admin Dashboard, {user_data['username']}!") \
            .classes('text-h4 text-primary')

        ui.button('Logout', on_click=lambda: (app.storage.user.clear(), ui.navigate.to('/login'))) \
            .props('outline')


@ui.page('/login')
def login_page():
    def try_login():
        user = USERS.get(username.value)
        if user and user['password'] == password.value:
            # Store both identity and role in the session cookie
            app.storage.user.update({
                'authenticated': True,
                'username': username.value,
                'role': user['role']
            })
            ui.navigate.to('/admin')
        else:
            ui.notify('Invalid username or password',
                      color='negative', position='top')

    with ui.card().classes('absolute-center shadow-2xl p-8 w-80'):
        ui.label('Login').classes('text-2xl font-bold mb-2')
        # on => Attach an event handler
        # keydown.enter => Trigger on Enter key press
        username = ui.input('Username').on(
            'keydown.enter', try_login).classes('w-full')
        password = ui.input('Password', password=True).on(
            'keydown.enter', try_login).classes('w-full')
        ui.button('Log in', on_click=try_login).classes('w-full mt-4')


@ui.page('/')
def index():
    # Since the user is not logged in yet, authenticated is missing/False, so they are redirected to /login
    if not app.storage.user.get('authenticated'):
        ui.navigate.to('/login')
    elif app.storage.user.get('role') == 'admin':
        ui.navigate.to('/admin')
    else:
        # Page for non-admin users
        with ui.column().classes('absolute-center items-center'):
            ui.label(
                f"Hello {app.storage.user.get('username')}, you are not an admin.")
            ui.button('Logout', on_click=lambda: (
                # clear makes => app.storage.user = {}, so authenticated becomes False again
                app.storage.user.clear(), ui.navigate.to('/login')))


ui.run(storage_secret='YOUR_SAFE_SECRET_HERE')
# storage_secret is internally used to secure data that NiceGUI stores between browser requests or sessions
