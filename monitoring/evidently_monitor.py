
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame({
    "temperature": [25, 26, 24, 25, 26, 24, 25, 26],
    "humidity": [60, 62, 61, 59, 60, 62, 61, 60]
})

current_data = pd.DataFrame({
    "temperature": [35, 36, 34, 35, 37, 34, 36, 35],
    "humidity": [75, 78, 76, 74, 77, 75, 78, 76]
})

report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("evidently_report.html")

print("Evidently monitoring completed.")
print("Report saved as evidently_report.html")
