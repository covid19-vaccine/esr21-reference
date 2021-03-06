from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': ['esr21_subject.subjectvisit'], })

configs = {
    'esr21_subject.pregnancystatus': ['child_bearing_potential', ],
    'esr21_subject.pregnancytest': ['result', ],
    'esr21_subject.adverseevent': ['experienced_ae'],
    'esr21_subject.vaccinationdetails': ['adverse_event'],
    'esr21_subject.covid19symptomaticinfections': ['symptomatic_experiences',
                                                   'hospitalisation_visit'],
    'esr21_subject.covid19results': ['covid_result']
 }

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
