from abc import ABC

from car import Car


class SternmanEngine:
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on