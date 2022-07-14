class AppStore:
    apps_list = list()

    def add_application(self, app):
        self.app = app
        self.apps_list.append(app)

    def remove_application(self, app):
        self.app = app
        self.apps_list.remove(app)
        return True

    def block_application(self, app):
        self.app = app
        app.blocked = True

    def total_apps(self):
        return len(self.apps_list)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


