import importlib
import pkgutil


class PackageLoader:
    def load_package(self, package: str):
        package = importlib.import_module(package)

        for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
            full_name = f'{package.__name__}.{name}'
            importlib.import_module(full_name)

            if is_pkg:
                self.load_package(full_name)
