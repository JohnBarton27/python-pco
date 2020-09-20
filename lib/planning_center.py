import pypco


class PlanningCenter:

    _APP_ID = ""
    _SECRET = ""
    PCO = None

    @staticmethod
    def setup(app_id: str, secret: str):
        PlanningCenter._APP_ID = app_id
        PlanningCenter._SECRET = secret
        PlanningCenter.PCO = pypco.PCO(PlanningCenter._APP_ID, PlanningCenter._SECRET)
