from django.db import models
import json

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chicken(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    egg_color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path) as f:
            data = json.load(f)

        chickens = []
        for chicken_data in data.get("chickens", []):
            breed_name = chicken_data.get("breed", "")
            category, _ = Category.objects.get_or_create(name=breed_name)

            chickens.append(
                Chicken(
                    name=chicken_data.get("name", ""),
                    breed=chicken_data.get("breed", ""),
                    egg_color=chicken_data.get("egg color", "")
                )
            )

        Chicken.objects.bulk_create(chickens)
