from edc_reference import site_reference_configs
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'cancer_subject.baseriskassessmentsmoking': [
        'has_smoked', 'has_worked_mine', 'has_alcohol'],
    'cancer_subject.baseriskassessmentsmoking': [
        'has_smoked', 'has_worked_mine', 'has_alcohol'],
    'cancer_subject.bhhhivtest': ['has_hiv_result'],
    'cancer_subject.bhhwhoillness': ['had_who_illnesses'],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
