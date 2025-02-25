class AuthRouter:
    route_app_labels = { "admin", "auth", "contenttypes", "sessions", "accounts" }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "accounts"
        return None


    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "accounts"
        return None


    def allow_relation(self, obj1, obj2, **hints):
        if( obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "accounts"
        return None




class Courses:
    router_app_labels = { "courses" }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "courses"
        return None


    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "courses"
        return None
    

    def allow_relation(self, obj1, obj2, **hints):
        if( obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None

    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "courses"
        return None



class Competitions:
    router_app_labels = { "competitions" }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "competitions"
        return None


    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "competitions"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if ( obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return "competitions"
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "competitions"
        return None





class Payments:
    router_app_labels = { "payments" }


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "payments"
        return None

    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "payments"
        return None


    def allow_relation(self, obj1, obj2, **hints):
        if( obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "payments"
        return None



