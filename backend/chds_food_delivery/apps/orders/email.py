from django.core.mail import send_mail,BadHeaderError
import os



def NotifyUserViaMail(subject,message,recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=os.getenv("EMAIL_HOST_USER"),
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except BadHeaderError:
        return 'Invalid header found.'
    except Exception as e:
        return f'An error occurred: {e}'
    return 'Email sent successfully!'