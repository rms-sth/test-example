from core.models import Person

from . import CustomBaseCommand


class Command(CustomBaseCommand):
    help = "Query person and position"

    def add_arguments(self, parser):
        parser.add_argument(
            "-p",
            "--person",
            type=str,
            help="Name of person.",
        )

    def handle(self, *args, **options):
        """
        @example:
            python manage.py query -p ramesh

        """
        name = options["person"]
        person = Person.objects.all()
        if name:
            person = Person.objects.filter(first_name__contains=name)

        person = person.first()
        print(f"Person: {person}")
        if person:
            print("Position: ")
            for position in person.positions.all():
                print(f"   -{position.position} => {position.company}")
