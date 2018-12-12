from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'cancer_subject.appointment': 'cancer_subject.subjectvisit'})

configs = {
    'cancer_subject.baseriskassessment': [
        'has_smoked', 'has_worked_mine', 'has_alcohol'],
    'cancer_subject.baselinehivhistory': ['has_hiv_result', 'had_who_illnesses'],
    'cancer_subject.oncologytreatmentplan': ['radiation_plan'],
    'cancer_subject.oncologytreatmentrecord': ['radiation_received'],
    'cancer_subject.symptomsandtesting': ['hiv_result', 'hiv_test_result']
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
