import config


class Module:

    def __init__(self, module_name):
        self.module_name = module_name

    def register(self, modules_dict):
        modules_dict[self.module_name] = self


class ModuleManager:

    def __init__(self):
        self.modules = dict()
        self.modules_list = list()

    def register_modules(self):

        if config.use_flair_enforcer:
            pass
