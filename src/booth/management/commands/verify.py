from django.core.management import BaseCommand,CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username',type=str)
        
        parser.add_argument('--all','-a',action='store_true')    
    def handle(self, *args, **options):
        username=options.get('username')
        
        user=User.objects.filter(username=username)
        if not options.get('all'):
            user=user.filter(is_active=True)
        if user:=user.first():
            self.stdout.write(self.style.SUCCESS(user.username))
        else:
            self.stdout.write(self.style.ERROR('User does not exist'))
