# from django.core.exceptions import ValidationError
# from .models import Pressure_Sensor
# from .constants import CONFIGURATION_SCHEMA
# from django import forms
# from jsoneditor.forms import JSONEditor
#
#
#
# class PressureSensorForm(forms.ModelForm):
#     configuration = forms.JSONField(
#         widget=JSONEditor(init_options={"mode": "code", "modes": ["code", "tree"]}),
#         required=False,
#     )
#
#
#     class Meta:
#         model = Pressure_Sensor
#         fields = "__all__"
#
#     def clean_configuration(self):
#         configuration = self.cleaned_data.get('configuration')
#
#         if not isinstance(configuration, dict):
#             raise ValidationError("Configuration must be a dictionary.")
#
#         # Validate alert_threshold
#         alert_threshold = configuration.get("alert_threshold")
#         if not isinstance(alert_threshold, dict):
#             raise ValidationError("'alert_threshold' must be a dictionary.")
#         for key in CONFIGURATION_SCHEMA["alert_threshold"]["required_keys"]:
#             if key not in alert_threshold:
#                 raise ValidationError(f"'alert_threshold' must include '{key}'.")
#
#         # Validate calibration
#         calibration = configuration.get("calibration")
#         if not isinstance(calibration, dict):
#             raise ValidationError("'calibration' must be a dictionary.")
#         for key in CONFIGURATION_SCHEMA["calibration"]["required_keys"]:
#             if key not in calibration:
#                 raise ValidationError(f"'calibration' must include '{key}'.")
#
#         return configuration
#
#     def clean(self):
#         super().clean()
#
#
#         return self.cleaned_data


from django import forms
from jsoneditor.forms import JSONEditor
from .models import Pressure_Sensor
from .constants import CONFIGURATION_SCHEMA


class PressureSensorForm(forms.ModelForm):
    class Meta:
        model = Pressure_Sensor
        fields = ['configuration', 'label', 'installation_date', 'latitude', 'longitude', 'serial_number']
        widgets = {
            'configuration': JSONEditor(
                attrs={
                    'mode': 'tree',  # Optional: sets the mode of the editor
                    'schema': CONFIGURATION_SCHEMA,
                }
            )
        }