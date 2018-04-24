from apistar.authentication import Auth


class IsLogin:
    def has_permission(self, auth: Auth):
        return auth.is_authenticated()


class IsAdmin:
    def has_permission(self, auth: Auth):
        return auth.is_authenticated() and auth.user.is_admin
