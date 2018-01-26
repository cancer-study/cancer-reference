from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': 'cancer_subject.subjectvisit'})

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
