class Record:
    def __init__(self,ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr, start_date, end_date,
                 destination_en, destination_fr, airfare, other_transport, lodging, meal, other_expenses, total, additional_comment_en,
                 additional_comment_fr, owner_org, owner_org_title):
        self.ref_number = ref_number
        self.disclosure_group = disclosure_group
        self.title_en = title_en
        self.title_fr = title_fr
        self.name = name
        self.purpose_en = purpose_en
        self.purpose_fr = purpose_fr
        self.start_date = start_date
        self.end_date = end_date
        self.destination_en = destination_en
        self.destination_fr = destination_fr
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meal = meal
        self.other_expenses = other_expenses
        self.total = total
        self.additional_comment_en = additional_comment_en
        self.additional_comment_fr = additional_comment_fr
        self.owner_org = owner_org
        self.owner_org_title = owner_org_title