import unicodedata
import subprocess
from guests.models import TunnelmoleURL
from django.core.management.base import BaseCommand


def remove_accent(text):
    """Remove acentos e normaliza o texto."""
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')


class NgrokSkipWarningMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['ngrok-skip-browser-warning'] = 'true'
        return response
    

class Command(BaseCommand):
    help = 'Updates the Tunnelmole URL'

    def handle(self, *args, **kwargs):
        # Command to get the current Tunnelmole URL
        result = subprocess.run(['tunnelmole', 'url'], capture_output=True, text=True)
        new_url = result.stdout.strip()

        # Update the URL in the database
        TunnelmoleURL.objects.create(url=new_url)
        self.stdout.write(self.style.SUCCESS(f'Successfully updated Tunnelmole URL to {new_url}'))