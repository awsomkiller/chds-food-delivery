from django.core.mail import EmailMultiAlternatives,BadHeaderError
import os



def NotifyUserViaMail(subject,message,recipient_list):
    try:
        email= EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=os.getenv("EMAIL_HOST_USER"),
            to=recipient_list,
    
        )
        email.send()
    except BadHeaderError:
        return 'Invalid header found.'
    except Exception as e:
        return f'An error occurred: {e}'
    return 'Email sent successfully!'