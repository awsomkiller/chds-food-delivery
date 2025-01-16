from django.core.management.base import BaseCommand
from apps.translations.models import Module,Translation
import pandas as pd


class Command(BaseCommand):
    help_text ="load page languages"
    file_path = "apps/translations/data/chds translations.xlsx"
    
    def handle(self, *args, **options):
        df=pd.read_excel(self.file_path,engine="openpyxl")
        columns = df.columns
        for i, row in df.iterrows():
            try:
                instance ,_ = Module.objects.get_or_create(feature_name=row['featurecode'],feature_code=row['featurecode'])
                
                Translation.objects.create(
                    label=row['labelcode'],
                    language="en",
                    module=instance,
                    value=row['en translation']
                )
                Translation.objects.create(
                    label=row['labelcode'],
                    language="zh",
                    module=instance,
                    value=row['zh translation']
                )
                self.stdout.write(self.style.SUCCESS(f"Tranlation added successfully"))
            except Exception as e:
                 self.stdout.write(self.style.ERROR(f"Tranlation added failed"))
                
        