from mongoengine import Document, ListField, StringField, DateTimeField, IntField, FloatField

class Projects(Document):
    projectId = StringField(required=True, max_length=200, unique=True)
    abstract = StringField(required=False)
    approvalDate = DateTimeField()
    approvalFy = StringField(required=False)
    borrower = StringField(required=False)
    closingDate = DateTimeField(required=False)
    commitmentAmount = StringField(required=False)
    countryName = StringField(required=False)
    regionName = StringField(required=False)
    environmentalCategory = StringField(required=False)
    lastUpdateDate = DateTimeField()
    projectName= StringField(required=False)
    sectorId = IntField(min_value=0)
    status = StringField(required=False)
    teamLeader = ListField(required=False)
    sectors = ListField()
    implementingAgency = StringField()
    totalProjectCost = StringField(required=False)
    disbursedAmount = FloatField()
    loanAmount = FloatField()