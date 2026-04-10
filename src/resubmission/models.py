from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    DateTimeField,
    ListField,
    EmbeddedDocumentField,
    DynamicField,
)


class CoverageDetail(EmbeddedDocument):
    vip_level = StringField()
    overall_annual_limit = StringField()
    inpatient_outpatient_treatment = StringField()
    outpatient_deductible_mpn = StringField()
    outpatient_deductible_hospitals = StringField()
    outpatient_deductible_polyclinic = StringField()
    branded_medication_deductible = StringField()
    generic_medication_deductible = StringField()
    psychiatric = StringField()
    dental_general = StringField()
    dental_corrective = StringField()
    dental_emergency = StringField()
    optical = StringField()
    maternity = StringField()
    kidney_transplant = StringField()
    physiotherapy = StringField()
    dialysis = StringField()
    hearing_aids_audiometry = StringField()
    congenital = StringField()
    autism = StringField()
    checkup = StringField()
    vaccination = StringField()
    network = StringField()
    approval_preauthorization_notes = StringField()
    special_instructions = StringField()


class Policy(Document):
    policy_number = StringField(required=True, unique=True)
    company_name = StringField()
    policy_holder = StringField()
    effective_from = DateTimeField()
    effective_to = DateTimeField()
    coverage_details = ListField(EmbeddedDocumentField(CoverageDetail))

    meta = {"collection": "policies"}


class CaseCoverage(EmbeddedDocument):
    case_name = StringField()
    patient_share = StringField()
    max_patient_share = StringField()
    max_consultation_fee = StringField()
    approval_threshold = StringField()


class SubCoverage(EmbeddedDocument):
    sub_coverage_code = StringField()
    description = StringField()
    limit = StringField()
    approval_threshold = StringField()


class Benefit(EmbeddedDocument):
    benefit_code = StringField()
    description = StringField()
    limit = StringField()
    cases = ListField(EmbeddedDocumentField(CaseCoverage))
    sub_coverages = ListField(EmbeddedDocumentField(SubCoverage))


class PolicyClass(EmbeddedDocument):
    class_code = StringField()
    class_limit = StringField()
    room_type = StringField()
    room_limit = StringField()
    benefits = ListField(EmbeddedDocumentField(Benefit))


class Endorsement(EmbeddedDocument):
    meta = {"allow_inheritance": True}
    # Flexible fields — accepts any endorsement structure
    data = DynamicField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)


class NCCI_Policy(Document):
    provider_name = StringField()
    policy_number = StringField(required=True, unique=True)
    policy_status = StringField()
    policy_holder_name = StringField()
    policy_type = StringField()
    issue_date = DateTimeField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    last_update = DateTimeField()
    coverage = StringField()
    exclusion = StringField()
    comments = StringField()
    classes = ListField(EmbeddedDocumentField(PolicyClass))
    endorsements = ListField(EmbeddedDocumentField(Endorsement))
    additional_information = StringField()

    meta = {"collection": "ncci_policies"}
