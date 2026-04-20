from django.core.management.base import BaseCommand
from store.models import Category

CATEGORIES = [
    "Dress (Women)", "Dress Materials", "Blouse Pieces", "Sarees",
    "Cosmetics", "Bangles", "Fancy Items (Chains, Necklaces, Bracelets)",
    "Hair Accessories", "Innerwears", "Others", "Kids Play Arena", "Kids Clothing",
]

class Command(BaseCommand):
    help = 'Seed default categories'

    def handle(self, *args, **kwargs):
        for name in CATEGORIES:
            obj, created = Category.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {name}'))
            else:
                self.stdout.write(f'Already exists: {name}')
        self.stdout.write(self.style.SUCCESS('Done seeding categories.'))
