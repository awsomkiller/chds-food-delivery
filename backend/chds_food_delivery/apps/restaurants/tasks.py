from celery import shared_task
from django.utils import timezone
from apps.restaurants.models import WorkingDays

current_date = timezone.now().date()


@shared_task(bind=True,max_retries=2)
def Update_ordering_status(self):
    try: 
        working_days = WorkingDays.objects.filter(date__lte=current_date, is_active=True)
        
        for working_day in working_days:
            working_day.is_active =False
            working_day.save() 
            
        return True
    except Exception as e:
        if self.request.retries == 2:
            return False
        print("Error:",e)
        self.retry(exc=e)
    
    