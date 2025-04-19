class Benefits:
    def get_benefits(self):
        return ["Health Insurance", "Vacation Days"]

class ManagerBenefits(Benefits):
    def get_benefits(self):
        return super().get_benefits() + ["Stock Options"]

class DeveloperBenefits(Benefits):
    def get_benefits(self):
        return super().get_benefits() + ["Training Budget"]