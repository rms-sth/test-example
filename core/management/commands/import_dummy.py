import datetime

from core.models import Company, Person, PersonPositionInCompanyRelationship, Position

from . import CustomBaseCommand


class Command(CustomBaseCommand):
    help = "Import data"

    def import_ramesh(self):
        dob = datetime.datetime.utcnow().date() - datetime.timedelta(days=26 * 365)

        person_data = {
            "first_name": "Ramesh",
            "last_name": "Pradhan",
            "dob": dob,
        }
        person = Person.objects.create(**person_data)
        company1 = Company.objects.create(
            name="Chuchuro Firm", slug="chuchuro-firm", address="USA"
        )
        company2 = Company.objects.create(
            name="Code Himalaya", slug="code-himalaya", address="USA"
        )
        position = Position.objects.create(name="Team Lead", slug="team-lead")
        person_position1 = PersonPositionInCompanyRelationship.objects.create(
            person=person, position=position, company=company1
        )
        person_position2 = PersonPositionInCompanyRelationship.objects.create(
            person=person, position=position, company=company2
        )

        person.positions.add(person_position1, person_position2)

    def import_elon(self):
        dob = datetime.datetime.utcnow().date() - datetime.timedelta(days=46 * 365)
        person_data = {
            "first_name": "Elon",
            "last_name": "Musk",
            "dob": dob,
        }
        person = Person.objects.create(**person_data)
        company1 = Company.objects.create(name="Tesla", slug="tesla", address="USA")
        company2 = Company.objects.create(name="Space X", slug="space-x", address="USA")
        position = Position.objects.create(name="CEO", slug="ceo")
        person_position1 = PersonPositionInCompanyRelationship.objects.create(
            person=person, position=position, company=company1
        )
        person_position2 = PersonPositionInCompanyRelationship.objects.create(
            person=person, position=position, company=company2
        )

        person.positions.add(person_position1, person_position2)

    def handle(self, *args, **options):
        self.import_elon()
        self.import_ramesh()

        print("Imported successfully.")
