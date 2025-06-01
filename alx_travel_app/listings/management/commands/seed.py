from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database with sample listings...')
        for i in range(10):
            Listing.objects.create(
                title=f'Sample Listing {i+1}',
                description='A great place to stay!',
                price_per_night=random.randint(50, 500),
                location=random.choice(['New York', 'London', 'Paris', 'Nairobi', 'Tokyo'])
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
