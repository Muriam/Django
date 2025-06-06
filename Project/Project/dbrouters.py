# для работы с несколькими БД
class SecondDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Hotels' and model.__name__ == 'SalesRecord':
            return 'second'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Hotels' and model.__name__ == 'SalesRecord':
            return 'second'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Hotels' and model_name == 'salesrecord':
            return db == 'second'
        return db == 'default'
