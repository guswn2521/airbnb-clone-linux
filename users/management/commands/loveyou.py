from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me he loves me."

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you.",
        )
        # return super().add_arguments(parser)

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(int(times)):
            self.stdout.write(self.style.WARNING("I love you"))
