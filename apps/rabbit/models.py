# import random
# import string
from collections import defaultdict
# from datetime import datetime, timedelta
from itertools import product
from pydoc import locate

# from dateutil import relativedelta as rd
from django.db import models
# from django.db.models import F
# from django.db.models import ObjectDoesNotExist
# from django.db.models import Sum, Min, Max, Case, Value, When, IntegerField, Avg
from django.contrib.auth.models import User

from qux.auth.models import Service
from qux.models import CoreModel, default_null_blank as dnb

class CalcScenario(CoreModel):
    """
    CalcScenarios model
    various parameter combinations of dragon for the study calculations
    """

    SLUG_PREFIX = "rabbit_scenario"

    slug = models.CharField(max_length=22, unique=True)
    name = models.CharField(max_length=64)
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="User",
    )
    is_public = models.BooleanField(default=False)
    price_per_run = models.DecimalField(decimal_places=3, max_digits=8, default="100")

    class Meta:
        verbose_name = "Rabbit Calculation Scenario"
        verbose_name_plural = "Rabbit Calculation Scenarios"
        unique_together = (
            "name",
            "user",
        )

    # add a list of params with their values
    # input dict => {param1: [value1, value2], param2: value2}
    def add_params(self, s_dict):
        c_dict = {}
        for k, v in s_dict.items():
            if not isinstance(v, list):
                v = [v]
            for i in v:
                c_dict["scenario"] = self
                c_dict[k] = i
                self.objects.update_or_create(**c_dict)
    
    def func_trial(self):
        return("Class Func")

    def enumerate_scenarios(self):
        custom_paramset = self.params.all()
        custom_param_list = list(custom_paramset.values_list("param", flat=True))

        service = Service.objects.get(name="dragon")
        service_params = service.get_preferences()

        params = defaultdict(list)
        for p in custom_paramset:
            params[p.param].append(p.value)
        expanded_params = list(
            dict(zip(params.keys(), values)) for values in product(*params.values())
        )

        results = []
        for x in expanded_params:
            items = {k: v for k, v in service_params.items()}
            for p in items:
                # overwrite p.value if value is defined in x
                if p["slug"] in custom_param_list:
                    f = locate(p["type"])
                    p["value"] = f(x[p["slug"]])
            results.append(items)

        return results


class CalcScenarioParam(CoreModel):
    """
    CalcScenarioParm model
    EVA model for all params in a scenario
    """

    scenario = models.ForeignKey(
        CalcScenario, on_delete=models.DO_NOTHING, related_name="params"
    )
    param = models.CharField(max_length=11)
    value = models.CharField(max_length=32, **dnb)

    class Meta:
        verbose_name = "Rabbit Calculation Scenario Params"
        verbose_name_plural = "Rabbit Calculation Scenario Params"
        unique_together = ("scenario", "param", "value")